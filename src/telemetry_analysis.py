# Processamento pesado dos 80 logs do HWiNFO

# -*- coding: utf-8 -*-
"""
telemetry_analysis.py
================================================================================
Módulo de análise da TELEMETRIA DE HARDWARE (HWiNFO64), correspondente aos
arquivos .csv/.CSV coletados durante cada rodada do benchmark.

Cada arquivo .csv representa o log COMPLETO de uma rodada (várias amostras
no tempo, ex.: uma linha por segundo durante a execução do Geekbench),
contendo até ~250 colunas de sensores. Este módulo:

    1. Carrega cada CSV de forma tolerante a "sujeira" comum em exports do
       HWiNFO64: separador ';' ou ',', decimal brasileiro (vírgula),
       encoding Latin-1, colunas duplicadas, valores ausentes ('-', 'N/A').
    2. Seleciona apenas as COLUNAS CRÍTICAS definidas pelo grupo (clock,
       uso de CPU/GPU, temperatura, potência, throttling, memória) -
       processar as ~250 colunas originais para todas as análises seria
       desnecessário e tornaria o pipeline lento.
    3. Agrega cada rodada (que tem N amostras no tempo) em UMA única linha
       de resumo por rodada (ex.: clock médio da rodada, temperatura
       máxima atingida na rodada, % de tempo em throttling), permitindo
       comparar rodada-a-rodada e cruzar com os scores do benchmark.
    4. Consolida as rodadas de uma máquina (até 20) em uma tabela única e
       calcula estatísticas (média, desvio padrão amostral) ao nível de
       MÁQUINA.

Fundamentação teórica:
    - Hierarquia de memória e gargalo de Von Neumann: colunas de clock de
      memória e taxa de leitura/gravação são usadas para discutir o
      impacto do barramento de memória no desempenho (Hennessy e
      Patterson, 2018; Patterson e Hennessy, 2014).
    - Thermal Throttling: a coluna booleana de "Estrangulamento térmico"
      é usada para quantificar o percentual de tempo em que o sistema
      operacional/firmware reduziu o clock para proteção térmica,
      fenômeno bem documentado na literatura de gerenciamento térmico de
      processadores (ex.: Castilhos et al.; Lee et al., "Thermal
      Challenges and Opportunities in 3D Stacked CPUs").

Boas práticas aplicadas:
    - Toda leitura de CSV é protegida por try/except específico, com
      fallback de engine/encoding/separador.
    - Colunas ausentes (sensor não suportado por determinada placa-mãe
      ou GPU) jamais derrubam o pipeline: ficam como NaN com aviso único.
    - Tipagem numérica é sempre validada/coagida antes de qualquer cálculo
      estatístico.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

try:
    from . import utils_utils as u
except ImportError:
    import utils_utils as u

logger = u.configurar_logger("aoc_pipeline.telemetria")

NUMERO_RODADAS_ESPERADO = 20

# ------------------------------------------------------------------------
# 1. MAPA DE COLUNAS CRÍTICAS (nome interno em português -> nome original
#    da coluna exportada pelo HWiNFO64, exatamente como fornecido pelo
#    grupo na especificação do projeto).
#
#    Usar um "nome interno" curto evita que o restante do código fique
#    cheio de strings longas/acentuadas repetidas, e centraliza num único
#    lugar qualquer ajuste futuro de nome de coluna do HWiNFO64.
# ------------------------------------------------------------------------
"""
COLUNAS_CRITICAS = {
    # --- Desempenho e clock ---
    "clock_nucleo_mhz": "Relógios núcleo (avg) (MHz)",
    "clock_efetivo_nucleo_mhz": "Relógios efetivos núcleo (avg) (MHz)",
    "clock_gpu_mhz": "GPU Clock (MHz)",
    # --- Carga de trabalho / utilização ---
    "uso_cpu_pct": "Uso total da CPU (%)",
    "carga_nucleo_gpu_pct": "Carga do núcleo da GPU (%)",
    "carga_memoria_fisica_pct": "Carga da memória física (%)",
    "uso_memoria_gpu_pct": "Uso de memória GPU (%)",
    # --- Termodinâmica / throttling ---
    "temp_cpu_c": "CPU Inteira (°C)",
    "temp_nucleo_max_c": "Núcleo máximo (°C)",
    "temp_gpu_c": "GPU Temperatura (°C)",
    "throttling_termico_nucleo": "Estrangulamento térmico do núcleo (avg) (Yes/No)",
    "limite_termico_gpu_c": "Limite térmico da GPU (°C)",
    # --- Potência / limites de projeto ---
    "potencia_cpu_w": "Potência total da CPU (W)",
    "potencia_linhas_gpu_w": "Potência das linhas GPU (avg) (W)",
    "limite_pl1_atingido": "IA: Package-Level RAPL/PBM PL1 (Yes/No)",
    "limite_desempenho_termico": "Limite de desempenho - Térmico (Yes/No)",
    # --- Subsistema de memória / armazenamento ---
    "clock_memoria_mhz": "Relógio da memória (MHz)",
    "taxa_leitura_mb_s": "Taxa de leituras (MB/s)",
    "taxa_gravacao_mb_s": "Taxa de gravações (MB/s)",
}
"""

COLUNAS_CRITICAS = {
    # --- Desempenho e clock ---
    "clock_nucleo_mhz": ["Relógios núcleo (avg) [MHz]", "Relógios núcleo (avg) (MHz)"],
    "clock_efetivo_nucleo_mhz": ["Relógios efetivos núcleo (avg) [MHz]", "Relógios efetivos núcleo (avg) (MHz)"],
    "clock_gpu_mhz": ["GPU Clock [MHz]", "GPU Clock (MHz)"],
    
    # --- Carga de trabalho / utilização ---
    "uso_cpu_pct": ["Uso total da CPU [%]", "Uso total da CPU (%)"],
    "carga_nucleo_gpu_pct": ["Uso total da GPU [%]", "Carga do núcleo da GPU (%)"],
    "carga_memoria_fisica_pct": ["Carga da memória física [%]", "Carga da memória física (%)"],
    "uso_memoria_gpu_pct": ["Uso de memória GPU [%]", "Uso de memória GPU (%)"],
    
    # --- Termodinâmica / throttling ---
    "temp_cpu_c": ["CPU Inteira [°C]", "CPU Inteira (°C)"],
    "temp_nucleo_max_c": ["Núcleo máximo [°C]", "Núcleo máximo (°C)"],
    "temp_gpu_c": ["GPU Core Temperatura [°C]", "GPU Temperatura [°C]", "GPU Temperatura (°C)"],
    "throttling_termico_nucleo": ["Estrangulamento térmico do núcleo (avg) [Yes/No]", "Estrangulamento térmico do núcleo (avg) (Yes/No)"],
    "limite_termico_gpu_c": ["Limite térmico da GPU [°C]", "Limite térmico da GPU (°C)"],
    
    # --- Potência / limites de projeto ---
    "potencia_cpu_w": ["Potência total da CPU [W]", "Potência total da CPU (W)"],
    "potencia_linhas_gpu_w": ["Potência das linhas GPU (avg) [W]", "Potência das linhas GPU (avg) (W)", "IGPU Potência [W]"],
    "limite_pl1_atingido": ["IA: Package-Level RAPL/PBM PL1 [Yes/No]", "IA: Package-Level RAPL/PBM PL1 (Yes/No)", "Package-Level RAPL/PBM PL1 [Yes/No]"],
    "limite_desempenho_termico": ["IA: Limite térmico médio em execução (RATL) [Yes/No]", "Limite de desempenho - Térmico (Yes/No)", "RING: Limite térmico médio em execução (RATL) [Yes/No]"],
    
    # --- Subsistema de memória / armazenamento ---
    "clock_memoria_mhz": ["Relógio da memória [MHz]", "Relógio da memória (MHz)"],
    "taxa_leitura_mb_s": ["Taxa de leituras [MB/s]", "Taxa de leituras (MB/s)"],
    "taxa_gravacao_mb_s": ["Taxa de gravações [MB/s]", "Taxa de gravações (MB/s)"],
}


# Colunas que representam indicadores categóricos "Yes/No" (serão
# convertidas para booleano, NÃO numérico).
COLUNAS_BOOLEANAS_INTERNAS = {
    "throttling_termico_nucleo",
    "limite_pl1_atingido",
    "limite_desempenho_termico",
}

VALORES_AUSENTES_HWINFO = ["-", "N/A", "NA", "n/a", "", " "]


# ------------------------------------------------------------------------
# 2. CARREGAMENTO TOLERANTE DE UM ARQUIVO CSV DE TELEMETRIA
# ------------------------------------------------------------------------

def _tentar_leitura_csv(caminho_csv: Path, separador: str, encoding: str) -> pd.DataFrame:
    """Tentativa única de leitura (uso interno por `carregar_csv_telemetria`)."""
    return pd.read_csv(
        caminho_csv,
        sep=separador,
        encoding=encoding,
        na_values=VALORES_AUSENTES_HWINFO,
        low_memory=False,
        on_bad_lines="skip",
    )


def carregar_csv_telemetria(caminho_csv: Path) -> pd.DataFrame:
    """
    Carrega um arquivo CSV de telemetria do HWiNFO64 de forma tolerante a
    variações comuns de exportação:

        - Separador ',' (padrão internacional) OU ';' (locale BR, comum
          quando o Excel/HWiNFO está configurado em português).
        - Encoding UTF-8 OU Latin-1 (cp1252), já que o HWiNFO64 no
          Windows BR frequentemente grava em Latin-1.
        - Decimal '.' ou ',' (detectado/convertido posteriormente por
          `_limpar_colunas_numericas`, pois o separador de campo e o
          separador decimal podem ser inconsistentes entre arquivos).

    Estratégia: tenta as combinações mais prováveis em ordem; usa como
    critério de sucesso o fato de o DataFrame resultante ter mais de 1
    coluna (se o separador estiver errado, o pandas lê tudo como uma
    única coluna gigante).

    Lança
    -----
    ValueError
        Se nenhuma combinação de separador/encoding produzir um
        DataFrame com mais de 1 coluna (arquivo corrompido/ilegível).
    """
    caminho_csv = Path(caminho_csv)
    if not caminho_csv.is_file():
        raise FileNotFoundError(f"Arquivo de telemetria não encontrado: {caminho_csv}")

    tentativas = [
        (",", "utf-8"),
        (";", "utf-8"),
        (",", "latin-1"),
        (";", "latin-1"),
    ]

    ultimo_erro: Optional[Exception] = None
    for separador, encoding in tentativas:
        try:
            df = _tentar_leitura_csv(caminho_csv, separador, encoding)
        except (UnicodeDecodeError, pd.errors.ParserError, OSError) as erro:
            ultimo_erro = erro
            continue

        if df.shape[1] > 1:
            df.columns = [u.normalizar_nome_coluna(c) for c in df.columns]
            return df

    raise ValueError(
        f"Não foi possível interpretar '{caminho_csv.name}' com nenhuma "
        f"combinação conhecida de separador/encoding. Último erro: {ultimo_erro}"
    )


# ------------------------------------------------------------------------
# 3. LIMPEZA E SELEÇÃO DAS COLUNAS CRÍTICAS
# ------------------------------------------------------------------------

def selecionar_colunas_criticas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Localiza, dentro do DataFrame bruto (com até ~250 colunas), as colunas
    críticas definidas em `COLUNAS_CRITICAS` e retorna um novo DataFrame
    apenas com elas, já renomeadas para os nomes internos em português.

    Colunas não encontradas (sensor ausente naquela máquina/rodada) são
    criadas como NaN, com um único aviso agregado ao final (evita "spam"
    de log quando o mesmo sensor falta em todas as 20 rodadas).
    """
    dados_selecionados = {}
    colunas_nao_encontradas = []

    for nome_interno, opcoes_nome_original in COLUNAS_CRITICAS.items():
        # Se for uma string simples, converte em lista para o loop funcionar
        if isinstance(opcoes_nome_original, str):
            opcoes_nome_original = [opcoes_nome_original]

        coluna_real = None
        # Varre a lista de nomes possíveis até achar a coluna real do CSV
        for nome_original in opcoes_nome_original:
            coluna_real = u.encontrar_coluna(df, nome_original)
            if coluna_real is not None:
                break

        if coluna_real is None:
            # Opção Profissional: Cria uma coluna cheia de NaN com o mesmo tamanho (index) do DataFrame original
            dados_selecionados[nome_interno] = pd.Series(np.nan, index=df.index)
            colunas_nao_encontradas.append(nome_interno)
        else:
            dados_selecionados[nome_interno] = df[coluna_real]

    if colunas_nao_encontradas:
        logger.debug(
            "Colunas críticas não encontradas neste arquivo: %s",
            colunas_nao_encontradas,
        )

    # Verifica se TODAS as colunas falharam (se o tamanho das não encontradas é igual ao total planejado)
    if len(colunas_nao_encontradas) == len(COLUNAS_CRITICAS):
        return pd.DataFrame()

    # Remove os colchetes [] para tratar o dicionário como colunas (séries), mantendo as múltiplas linhas do arquivo temporal
    return pd.DataFrame(dados_selecionados)

    """
    # Se nenhuma coluna crítica foi extraída, retorna um DataFrame vazio de forma segura
    if not dados_selecionados:
        return pd.DataFrame()

    # Cria o DataFrame tratando o dicionário como uma linha (registro)
    return pd.DataFrame([dados_selecionados])
    """


def limpar_dataframe_telemetria(df_critico: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica a limpeza/tipagem final sobre o DataFrame já reduzido às
    colunas críticas:

        - Colunas numéricas: conversão tolerante a decimal BR (vírgula).
        - Colunas booleanas (Yes/No): conversão para True/False/NaN.
        - Linhas 100% vazias (todas as colunas críticas ausentes naquela
          amostra) são descartadas, pois não agregam informação e
          distorceriam médias por contagem (NaN é ignorado por
          .mean()/.std(), mas linhas totalmente vazias indicam problema
          de log e merecem ser removidas explicitamente).
    """
    df_limpo = df_critico.copy()

    for nome_interno in df_limpo.columns:
        if nome_interno in COLUNAS_BOOLEANAS_INTERNAS:
            df_limpo[nome_interno] = u.converter_sim_nao_para_booleano(df_limpo[nome_interno])
        else:
            df_limpo[nome_interno] = u.converter_decimal_brasileiro_para_float(
                df_limpo[nome_interno]
            )

    linhas_vazias = df_limpo.isna().all(axis=1)
    if linhas_vazias.any():
        logger.debug(
            "%d linha(s) totalmente vazias removidas durante a limpeza.",
            int(linhas_vazias.sum()),
        )
        df_limpo = df_limpo[~linhas_vazias].reset_index(drop=True)

    return df_limpo


# ------------------------------------------------------------------------
# 4. AGREGAÇÃO DE UMA RODADA (série temporal -> 1 linha de resumo)
# ------------------------------------------------------------------------

def agregar_rodada(df_limpo: pd.DataFrame, numero_rodada: Optional[int] = None) -> dict:
    """
    Reduz a série temporal de UMA rodada (várias amostras no tempo) a um
    único dicionário de métricas-resumo, que serão depois empilhadas para
    formar a tabela "1 linha por rodada" de uma máquina.

    Métricas calculadas por coluna numérica: média e máximo (o máximo é
    especialmente relevante para temperatura: o que importa
    arquiteturalmente é o pico térmico atingido, não apenas a média).
    Para colunas booleanas (throttling/limites), calcula-se o percentual
    de amostras em que a condição esteve ativa (True), que funciona como
    uma "fração de tempo em throttling" dentro da rodada.

    Retorna
    -------
    dict
        Pronto para ser usado como uma linha de um DataFrame (via
        pd.DataFrame(lista_de_dicts)).
    """
    resumo: dict = {"rodada": numero_rodada}

    for coluna in df_limpo.columns:
        serie = df_limpo[coluna]

        if coluna in COLUNAS_BOOLEANAS_INTERNAS:
            valores_validos = serie.dropna()
            if len(valores_validos) == 0:
                resumo[f"{coluna}_pct_tempo"] = np.nan
            else:
                resumo[f"{coluna}_pct_tempo"] = round(
                    100 * valores_validos.mean(), 2
                )  # média de booleanos = proporção de True
            continue

        valores_validos = serie.dropna()
        if len(valores_validos) == 0:
            resumo[f"{coluna}_media"] = np.nan
            resumo[f"{coluna}_max"] = np.nan
        else:
            resumo[f"{coluna}_media"] = round(valores_validos.mean(), 3)
            resumo[f"{coluna}_max"] = round(valores_validos.max(), 3)

    return resumo


# ------------------------------------------------------------------------
# 5. CONSOLIDAÇÃO DE TODAS AS RODADAS DE UMA MÁQUINA
# ------------------------------------------------------------------------

def consolidar_telemetria_maquina(relatorio_maquina) -> pd.DataFrame:
    """
    Processa TODOS os arquivos .csv disponíveis de uma máquina (pode ser
    menos que 20, caso a coleta ainda esteja incompleta) e retorna uma
    tabela com 1 linha por rodada processada com sucesso.

    Parâmetros
    ----------
    relatorio_maquina : utils_utils.RelatorioMaquina

    Retorna
    -------
    pd.DataFrame
        1 linha por rodada, colunas = métricas-resumo agregadas
        (ver `agregar_rodada`). DataFrame vazio se nenhum CSV pôde ser
        processado.
    """
    linhas_resumo = []

    for caminho_csv in relatorio_maquina.arquivos_csv:
        numero_rodada = u.extrair_numero_rodada(caminho_csv)
        try:
            df_bruto = carregar_csv_telemetria(caminho_csv)
        except (FileNotFoundError, ValueError) as erro:
            logger.error(
                "Falha ao carregar '%s' (rodada %s): %s",
                caminho_csv.name, numero_rodada, erro,
            )
            continue

        df_critico = selecionar_colunas_criticas(df_bruto)
        df_limpo = limpar_dataframe_telemetria(df_critico)

        print(f"\n--- DEBUG: {caminho_csv.name} ---")
        print(f"Linhas antes da limpeza (df_critico): {len(df_critico)}")
        print(f"Colunas encontradas: {list(df_critico.columns)}")
        if not df_critico.empty:
            print("Amostra dos dados antes da limpeza:")
            print(df_critico.head(2))
        print(f"Linhas após a limpeza (df_limpo): {len(df_limpo)}")
        print("-" * 40)

        if df_limpo.empty:
            logger.warning(
                "'%s': após limpeza, nenhuma amostra válida restante; "
                "rodada ignorada.", caminho_csv.name,
            )
            continue

        resumo = agregar_rodada(df_limpo, numero_rodada=numero_rodada)
        resumo["arquivo_origem"] = caminho_csv.name
        linhas_resumo.append(resumo)

    if not linhas_resumo:
        logger.warning(
            "Máquina '%s': nenhuma rodada de telemetria pôde ser "
            "processada.", relatorio_maquina.nome_maquina,
        )
        return pd.DataFrame()

    df_consolidado = pd.DataFrame(linhas_resumo)
    if "rodada" in df_consolidado.columns:
        df_consolidado = df_consolidado.sort_values("rodada", na_position="last").reset_index(drop=True)

    if len(df_consolidado) != NUMERO_RODADAS_ESPERADO:
        logger.warning(
            "Máquina '%s': %d rodada(s) de telemetria consolidada(s), "
            "esperado %d. Prosseguindo com os dados disponíveis.",
            relatorio_maquina.nome_maquina, len(df_consolidado),
            NUMERO_RODADAS_ESPERADO,
        )

    return df_consolidado


def consolidar_telemetria_todas_maquinas(relatorios: dict) -> dict:
    """
    Aplica `consolidar_telemetria_maquina` a todas as máquinas presentes
    em `relatorios` (saída de utils_utils.verificar_estrutura_diretorios).

    Retorna
    -------
    dict[str, pd.DataFrame]
        Uma tabela "1 linha por rodada" para cada máquina (chave = nome
        da pasta, ex.: 'machine_a').
    """
    tabelas_por_maquina = {}
    for nome_maquina, relatorio in sorted(relatorios.items()):
        if relatorio.total_csv == 0:
            logger.warning(
                "Máquina '%s' sem arquivos CSV de telemetria; ignorada.",
                nome_maquina,
            )
            continue
        tabelas_por_maquina[nome_maquina] = consolidar_telemetria_maquina(relatorio)

    return tabelas_por_maquina


# ------------------------------------------------------------------------
# 6. ESTATÍSTICAS AO NÍVEL DE MÁQUINA (entre rodadas)
# ------------------------------------------------------------------------

def calcular_estatisticas_telemetria(df_consolidado: pd.DataFrame) -> pd.DataFrame:
    """
    A partir da tabela "1 linha por rodada" de uma máquina, calcula
    média e desvio padrão amostral (ddof=1) ENTRE as 20 (ou menos)
    rodadas, para cada métrica numérica.

    Esta é a tabela "de uma máquina" que entra nos gráficos de barra com
    erro (eixo Y = média da métrica, haste de erro = desvio padrão entre
    rodadas) e nas tabelas comparativas do artigo.
    """
    colunas_numericas = df_consolidado.select_dtypes(include=[np.number]).columns
    colunas_numericas = [c for c in colunas_numericas if c != "rodada"]

    linhas = []
    for coluna in colunas_numericas:
        valores = df_consolidado[coluna].dropna()
        n = len(valores)
        if n == 0:
            continue
        media = valores.mean()
        desvio = valores.std(ddof=1) if n > 1 else np.nan
        linhas.append(
            {
                "metrica": coluna,
                "media": round(media, 3),
                "desvio_padrao": round(desvio, 3) if pd.notna(desvio) else np.nan,
                "coef_variacao_pct": (
                    u.coeficiente_de_variacao(media, desvio) if pd.notna(desvio) else np.nan
                ),
                "n_rodadas": n,
            }
        )

    return pd.DataFrame(linhas).set_index("metrica") if linhas else pd.DataFrame()


def calcular_percentual_throttling(df_consolidado: pd.DataFrame) -> Optional[float]:
    """
    Calcula o percentual médio de tempo em throttling térmico do núcleo,
    considerando todas as rodadas disponíveis da máquina (média das
    proporções por rodada, calculadas em `agregar_rodada`).

    Retorna None se a coluna não estiver disponível.
    """
    coluna = "throttling_termico_nucleo_pct_tempo"
    if coluna not in df_consolidado.columns:
        return None
    valores = df_consolidado[coluna].dropna()
    if valores.empty:
        return None
    return round(valores.mean(), 2)