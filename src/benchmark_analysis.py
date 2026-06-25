# Processamento das 20 rodadas do Geekbench de cada máquina

# -*- coding: utf-8 -*-
"""
benchmark_analysis.py
================================================================================
Módulo de análise dos resultados de BENCHMARK SINTÉTICO (Geekbench 6).

Cada máquina possui 1 arquivo .txt com 20 rodadas (linhas), no formato:

    Rodada;Single_Core;Multi_Core
    01;1291;2881
    02;1295;2890
    ...

Este módulo é responsável por:
    1. Carregar e validar esse arquivo .txt (carregar_scores_maquina).
    2. Calcular estatísticas descritivas clássicas de Arquitetura de
       Computadores aplicadas a desempenho: média aritmética, desvio
       padrão amostral, coeficiente de variação, mínimo e máximo
       (calcular_estatisticas_benchmark).
    3. Consolidar os resultados de todas as máquinas em uma única tabela
       comparativa (consolidar_benchmark_todas_maquinas), pronta para
       exportação a uma Tabela no padrão SBC.
    4. Cruzar os scores com a potência média (telemetria) para estimar
       Desempenho por Watt (calcular_desempenho_por_watt) - métrica de
       eficiência microarquitetural pedida pelo professor.

Fundamentação teórica (a ser citada no texto do artigo, não apenas no
código): a métrica "Score" do Geekbench é um índice sintético de
desempenho (não é MIPS nem FLOPS puro), mas correlaciona-se com a
Taxa de Transferência de instruções executada pela CPU em uma carga de
trabalho padronizada (Hennessy e Patterson, 2018 - "Computer
Architecture: A Quantitative Approach"). A análise estatística por
rodada (média e desvio padrão amostral) segue a metodologia clássica de
avaliação de desempenho descrita por Hennessy/Patterson e por
Heidelberger e Lavenberg (1984) para sistemas com variabilidade
intrínseca de medição.

Boas práticas aplicadas:
    - Nenhuma estatística é calculada sobre uma lista vazia (checagens
      defensivas) - retorna NaN com aviso em vez de lançar exceção.
    - O número esperado de rodadas é 20, mas o módulo aceita qualquer
      quantidade > 0 (dado parcial), emitindo apenas um alerta.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

try:
    # Quando importado como parte do pacote 'src'
    from . import utils_utils as u
except ImportError:
    # Quando importado/executado diretamente (ex.: dentro do notebook)
    import utils_utils as u

logger = u.configurar_logger("aoc_pipeline.benchmark")

NUMERO_RODADAS_ESPERADO = 20
COLUNAS_ESPERADAS_TXT = ["Rodada", "Single_Core", "Multi_Core"]


# ------------------------------------------------------------------------
# 1. CARREGAMENTO DO ARQUIVO DE SCORES (.txt)
# ------------------------------------------------------------------------

def carregar_scores_maquina(caminho_txt: Path) -> pd.DataFrame:
    """
    Lê o arquivo .txt de scores do Geekbench 6 de uma máquina.

    Formato esperado (separador ';', cabeçalho na primeira linha):
        Rodada;Single_Core;Multi_Core
        01;1291;2881

    Tratamento de erros:
        - Arquivo inexistente -> levanta FileNotFoundError (erro grave,
          pois sem o .txt não há dados de desempenho para a máquina).
        - Colunas com nomes diferentes do esperado -> tenta renomear por
          posição, mas registra aviso.
        - Linhas mal formatadas (ex.: número de colunas errado) -> são
          descartadas silenciosamente pelo parser do pandas
          (on_bad_lines='warn'), e o motivo fica registrado no log.
        - Valores não numéricos em Single_Core/Multi_Core -> convertidos
          para NaN (não interrompem o carregamento das demais linhas).

    Retorna
    -------
    pd.DataFrame
        Colunas: Rodada (str, ex. '01'), Single_Core (float), Multi_Core (float).
    """
    caminho_txt = Path(caminho_txt)
    if not caminho_txt.is_file():
        raise FileNotFoundError(f"Arquivo de scores não encontrado: {caminho_txt}")

    try:
        df = pd.read_csv(
            caminho_txt,
            sep=";",
            dtype={"Rodada": str},
            encoding="utf-8",
            on_bad_lines="warn",
        )
    except UnicodeDecodeError:
        # Fallback para encoding Latin-1, comum em arquivos exportados no Windows BR
        logger.warning(
            "Falha ao decodificar '%s' como UTF-8; tentando Latin-1.", caminho_txt.name
        )
        df = pd.read_csv(
            caminho_txt,
            sep=";",
            dtype={"Rodada": str},
            encoding="latin-1",
            on_bad_lines="warn",
        )

    df.columns = [u.normalizar_nome_coluna(c) for c in df.columns]

    colunas_faltantes = set(COLUNAS_ESPERADAS_TXT) - set(df.columns)
    if colunas_faltantes:
        logger.warning(
            "'%s': colunas esperadas não encontradas (%s). Colunas presentes: %s",
            caminho_txt.name, colunas_faltantes, list(df.columns),
        )

    # Garante tipo numérico em Single_Core/Multi_Core, mesmo que vierem como texto
    for coluna in ("Single_Core", "Multi_Core"):
        if coluna in df.columns:
            df[coluna] = u.converter_decimal_brasileiro_para_float(df[coluna])

    linhas_invalidas = df[["Single_Core", "Multi_Core"]].isna().all(axis=1) if (
        "Single_Core" in df.columns and "Multi_Core" in df.columns
    ) else pd.Series(False, index=df.index)
    if linhas_invalidas.any():
        logger.warning(
            "'%s': %d linha(s) sem nenhum score numérico válido foram descartadas.",
            caminho_txt.name, int(linhas_invalidas.sum()),
        )
        df = df[~linhas_invalidas].reset_index(drop=True)

    if len(df) == 0:
        logger.error("'%s': nenhuma rodada válida foi carregada.", caminho_txt.name)
    elif len(df) != NUMERO_RODADAS_ESPERADO:
        logger.warning(
            "'%s': %d rodada(s) carregada(s), esperado %d. "
            "A análise seguirá apenas com as rodadas disponíveis.",
            caminho_txt.name, len(df), NUMERO_RODADAS_ESPERADO,
        )

    return df


# ------------------------------------------------------------------------
# 2. ESTATÍSTICA DESCRITIVA DO BENCHMARK
# ------------------------------------------------------------------------

def calcular_estatisticas_benchmark(df_scores: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula estatísticas descritivas (média, desvio padrão AMOSTRAL,
    coeficiente de variação, mínimo, máximo e nº de rodadas válidas) para
    as colunas Single_Core e Multi_Core.

    Fórmulas de referência (a transcrever no artigo em LaTeX):

        Média aritmética:
            \\bar{x} = \\frac{1}{n} \\sum_{i=1}^{n} x_i

        Desvio padrão amostral (n-1 no denominador, correção de Bessel,
        adequado pois trabalhamos com uma AMOSTRA de rodadas, não a
        população completa de execuções possíveis):
            s = \\sqrt{ \\frac{1}{n-1} \\sum_{i=1}^{n} (x_i - \\bar{x})^2 }

    Parâmetros
    ----------
    df_scores : pd.DataFrame
        Saída de `carregar_scores_maquina`.

    Retorna
    -------
    pd.DataFrame
        Índice = ['Single_Core', 'Multi_Core'], colunas =
        ['media', 'desvio_padrao', 'coef_variacao_pct', 'minimo', 'maximo', 'n_rodadas'].
    """
    resultados = {}
    for coluna in ("Single_Core", "Multi_Core"):
        if coluna not in df_scores.columns:
            logger.warning("Coluna '%s' ausente; estatísticas não calculadas.", coluna)
            continue

        valores = df_scores[coluna].dropna()
        n = len(valores)

        if n == 0:
            resultados[coluna] = {
                "media": np.nan, "desvio_padrao": np.nan,
                "coef_variacao_pct": np.nan, "minimo": np.nan,
                "maximo": np.nan, "n_rodadas": 0,
            }
            continue

        media = valores.mean()
        # ddof=1 -> desvio padrão AMOSTRAL (divide por n-1), consistente
        # com a fórmula apresentada no artigo. Se n==1, pandas retorna NaN
        # (não há variabilidade estimável com uma única observação).
        desvio = valores.std(ddof=1) if n > 1 else np.nan

        resultados[coluna] = {
            "media": round(media, 2),
            "desvio_padrao": round(desvio, 2) if pd.notna(desvio) else np.nan,
            "coef_variacao_pct": u.coeficiente_de_variacao(media, desvio) if pd.notna(desvio) else np.nan,
            "minimo": valores.min(),
            "maximo": valores.max(),
            "n_rodadas": n,
        }

    return pd.DataFrame(resultados).T


# ------------------------------------------------------------------------
# 3. CONSOLIDAÇÃO ENTRE MÁQUINAS
# ------------------------------------------------------------------------

def consolidar_benchmark_todas_maquinas(
    relatorios: dict, mapa_nomes_exibicao: Optional[dict] = None
) -> dict:
    """
    Para cada máquina presente em `relatorios` (saída de
    utils_utils.verificar_estrutura_diretorios), carrega o respectivo .txt
    (se existir) e calcula as estatísticas de benchmark.

    Parâmetros
    ----------
    relatorios : dict[str, RelatorioMaquina]
    mapa_nomes_exibicao : dict, opcional
        Mapeia o nome da pasta (ex.: 'machine_a') para um nome de exibição
        mais descritivo (ex.: 'Máquina A - Notebook Dell Inspiron').

    Retorna
    -------
    dict com as chaves:
        'tabelas_individuais' : dict[str, pd.DataFrame] (uma por máquina)
        'scores_brutos'       : dict[str, pd.DataFrame] (rodadas brutas, p/ outros módulos)
        'comparativo'         : pd.DataFrame (uma linha por máquina, formato wide)
    """
    mapa_nomes_exibicao = mapa_nomes_exibicao or {}
    tabelas_individuais = {}
    scores_brutos = {}
    linhas_comparativo = []

    for nome_maquina, relatorio in sorted(relatorios.items()):
        if relatorio.total_txt == 0:
            logger.warning(
                "Máquina '%s' sem arquivo .txt de scores; ignorada na "
                "consolidação de benchmark.", nome_maquina,
            )
            continue

        # Usa o primeiro .txt encontrado (deveria haver só 1, por construção)
        caminho_txt = relatorio.arquivos_txt[0]
        try:
            df_scores = carregar_scores_maquina(caminho_txt)
        except (FileNotFoundError, pd.errors.ParserError, ValueError) as erro:
            logger.error("Erro ao carregar scores de '%s': %s", nome_maquina, erro)
            continue

        if df_scores.empty:
            continue

        scores_brutos[nome_maquina] = df_scores
        estatisticas = calcular_estatisticas_benchmark(df_scores)
        tabelas_individuais[nome_maquina] = estatisticas

        nome_exibicao = mapa_nomes_exibicao.get(nome_maquina, nome_maquina)
        linha = {"maquina": nome_exibicao, "pasta": nome_maquina}
        for metrica in estatisticas.index:
            for stat_nome, stat_valor in estatisticas.loc[metrica].items():
                linha[f"{metrica}_{stat_nome}"] = stat_valor
        linhas_comparativo.append(linha)

    comparativo = pd.DataFrame(linhas_comparativo)
    return {
        "tabelas_individuais": tabelas_individuais,
        "scores_brutos": scores_brutos,
        "comparativo": comparativo,
    }


# ------------------------------------------------------------------------
# 4. EFICIÊNCIA MICROARQUITETURAL: DESEMPENHO POR WATT
# ------------------------------------------------------------------------

def calcular_desempenho_por_watt(
    score_medio: float, potencia_media_watts: float
) -> Optional[float]:
    """
    Calcula a eficiência energética como Score / Potência média (W),
    métrica de "desempenho por Watt" amplamente utilizada na literatura
    de avaliação de microarquiteturas (ex.: relatórios SPECpower,
    Hennessy e Patterson 2018, cap. 1).

    Quanto maior o valor, mais "trabalho" (score sintético) a CPU produz
    por unidade de energia consumida - métrica especialmente relevante em
    comparações onde uma das máquinas sofre throttling térmico (reduz
    clock para limitar potência, sacrificando desempenho).

    Retorna None se a potência for None, zero ou NaN (evita divisão
    indefinida/poluir o gráfico com infinito).
    """
    if potencia_media_watts is None or pd.isna(potencia_media_watts) or potencia_media_watts == 0:
        logger.warning(
            "Potência média inválida (%s); Desempenho/Watt não calculado.",
            potencia_media_watts,
        )
        return None
    if score_medio is None or pd.isna(score_medio):
        return None
    return round(score_medio / potencia_media_watts, 3)


def calcular_ipc_relativo(
    score_medio: float, clock_efetivo_medio_mhz: float
) -> Optional[float]:
    """
    Calcula um indicador de "eficiência por ciclo de clock":

        IPC_relativo = Score / Clock_efetivo_medio (MHz)

    IMPORTANTE (rigor científico): este NÃO é o IPC (Instructions Per
    Cycle) real da microarquitetura, pois o Score do Geekbench é um
    índice sintético ponderado de múltiplas cargas de trabalho, não uma
    contagem direta de instruções executadas. Trata-se de uma métrica
    PROXY de eficiência por ciclo, útil apenas para comparação relativa
    ENTRE as máquinas deste estudo (mesma metodologia de medição), não
    para comparação com valores de IPC publicados na literatura.
    Esta limitação deve ser explicitada na seção de Resultados/Discussão
    do artigo, citando a documentação metodológica do Geekbench e
    Hennessy e Patterson (2018) sobre a diferença entre métricas
    sintéticas (scores) e métricas arquiteturais diretas (IPC, CPI).

    Retorna None se o clock for inválido (None, NaN ou zero).
    """
    if (
        clock_efetivo_medio_mhz is None
        or pd.isna(clock_efetivo_medio_mhz)
        or clock_efetivo_medio_mhz == 0
    ):
        return None
    if score_medio is None or pd.isna(score_medio):
        return None
    return round(score_medio / clock_efetivo_medio_mhz, 4)