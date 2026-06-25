# -*- coding: utf-8 -*-
"""
utils_utils.py
================================================================================
Módulo de utilidades compartilhadas do projeto de Benchmarking Empírico
(Arquitetura e Organização de Computadores - UFPA/Tucuruí).

Responsabilidades deste módulo:
    1. Centralizar caminhos (paths) do projeto (data/raw, data/processed, results).
    2. Verificar a integridade/completude da estrutura de dados coletados
       (cada pasta "machine_x" deveria ter, no máximo, 1 arquivo .txt de
       scores + 20 arquivos .csv de telemetria = 21 arquivos no total).
    3. Oferecer funções de limpeza/normalização de dados (decimal BR -> US,
       Yes/No -> booleano, normalização de nomes de colunas) reaproveitadas
       por benchmark_analysis.py e telemetry_analysis.py.
    4. Configurar logging padronizado para todo o pipeline.

Convenções adotadas no projeto:
    - Cada máquina possui uma pasta própria em data/raw/ (ex.: machine_a).
    - Dentro de cada pasta de máquina:
        * 1 arquivo .txt  -> resultados do Geekbench 6 (scores por rodada).
        * até 20 arquivos .csv/.CSV -> telemetria do HWiNFO64 (1 por rodada).
    - O pipeline deve funcionar mesmo com dados PARCIAIS (nem todas as
      rodadas/máquinas precisam estar completas), mas nunca deve aceitar
      MAIS do que 1 .txt e 20 .csv por máquina (acima disso é tratado como
      inconsistência da coleta e deve gerar um alerta).

Boas práticas aplicadas:
    - Funções pequenas, com responsabilidade única e docstrings.
    - Tratamento de exceções específico (nunca "except: pass" silencioso).
    - Logging em vez de "print" para facilitar depuração futura.
    - Nomes de variáveis/funções em português, por orientação do professor.
"""

from __future__ import annotations

import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pandas as pd

# ------------------------------------------------------------------------
# 1. CONSTANTES E CONFIGURAÇÃO DE CAMINHOS
# ------------------------------------------------------------------------

# Limites da coleta empírica definidos pelo grupo: 20 rodadas de telemetria
# (CSV) + 1 arquivo consolidado de scores (TXT) por máquina.
NUMERO_MAXIMO_CSV_POR_MAQUINA = 20
NUMERO_MAXIMO_TXT_POR_MAQUINA = 1
NUMERO_MAXIMO_ARQUIVOS_POR_MAQUINA = (
    NUMERO_MAXIMO_CSV_POR_MAQUINA + NUMERO_MAXIMO_TXT_POR_MAQUINA
)  # = 21


def localizar_raiz_projeto(arquivo_referencia: Optional[str] = None) -> Path:
    """
    Localiza a raiz do projeto (pasta que contém 'data', 'src', 'results').

    A busca sobe diretórios a partir de `arquivo_referencia` (ou do diretório
    de trabalho atual, se None) até encontrar uma pasta que contenha 'data'
    e 'src'. Isso evita caminhos absolutos "hardcoded" que quebram quando o
    repositório é clonado em outra máquina (ex.: notebook x scripts).

    Parâmetros
    ----------
    arquivo_referencia : str, opcional
        Caminho de referência (normalmente `__file__` de quem chamou).

    Retorna
    -------
    Path
        Caminho absoluto da raiz do projeto.

    Lança
    -----
    FileNotFoundError
        Se a raiz não puder ser determinada automaticamente.
    """
    if arquivo_referencia is not None:
        ponto_partida = Path(arquivo_referencia).resolve().parent
    else:
        ponto_partida = Path.cwd().resolve()

    candidato = ponto_partida
    for _ in range(6):  # limite de subidas para evitar loop infinito
        if (candidato / "data").is_dir() and (candidato / "src").is_dir():
            return candidato
        if candidato.parent == candidato:
            break
        candidato = candidato.parent

    # Fallback: assume que a raiz é o diretório pai de "src" (caso típico
    # de execução de um script dentro de src/).
    if ponto_partida.name == "src":
        return ponto_partida.parent

    raise FileNotFoundError(
        "Não foi possível localizar a raiz do projeto automaticamente. "
        "Verifique se a estrutura contém as pastas 'data' e 'src', ou "
        "informe manualmente o caminho via parâmetro 'raiz_projeto'."
    )


@dataclass
class CaminhosProjeto:
    """Agrupa todos os caminhos relevantes do projeto em um único objeto."""

    raiz: Path
    dados_raw: Path = field(init=False)
    dados_processed: Path = field(init=False)
    resultados: Path = field(init=False)
    resultados_figuras: Path = field(init=False)
    resultados_tabelas: Path = field(init=False)

    def __post_init__(self) -> None:
        self.dados_raw = self.raiz / "data" / "raw"
        self.dados_processed = self.raiz / "data" / "processed"
        self.resultados = self.raiz / "results"
        self.resultados_figuras = self.resultados / "figures"
        self.resultados_tabelas = self.resultados / "tables"

    def garantir_pastas_saida(self) -> None:
        """Cria as pastas de saída (processed/results) e subpastas de figuras se não existirem."""
        pastas_base = (
            self.dados_processed,
            self.resultados,
            self.resultados_figuras,
            self.resultados_tabelas,
        )
        for pasta in pastas_base:
            pasta.mkdir(parents=True, exist_ok=True)
            
        (self.resultados_figuras / "final_plots").mkdir(parents=True, exist_ok=True)
        (self.resultados_figuras / "raw_plots").mkdir(parents=True, exist_ok=True)


def obter_caminhos(raiz_projeto: Optional[str] = None) -> CaminhosProjeto:
    """Função de conveniência para obter um objeto CaminhosProjeto pronto."""
    raiz = Path(raiz_projeto) if raiz_projeto else localizar_raiz_projeto()
    caminhos = CaminhosProjeto(raiz=raiz)
    caminhos.garantir_pastas_saida()
    return caminhos


# ------------------------------------------------------------------------
# 2. LOGGING PADRONIZADO
# ------------------------------------------------------------------------

def configurar_logger(nome: str = "aoc_pipeline", nivel: int = logging.INFO) -> logging.Logger:
    """
    Configura (ou reaproveita) um logger padronizado para todo o pipeline.

    Evita duplicar handlers quando a função é chamada múltiplas vezes
    (comportamento comum em notebooks Jupyter, que reexecutam células).
    """
    logger_local = logging.getLogger(nome)
    logger_local.setLevel(nivel)

    if not logger_local.handlers:
        manipulador = logging.StreamHandler(sys.stdout)
        formato = logging.Formatter(
            "[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
        )
        manipulador.setFormatter(formato)
        logger_local.addHandler(manipulador)
        logger_local.propagate = False

    return logger_local


logger = configurar_logger()


# ------------------------------------------------------------------------
# 3. VERIFICAÇÃO DE ESTRUTURA E COMPLETUDE DOS DADOS COLETADOS
# ------------------------------------------------------------------------

@dataclass
class RelatorioMaquina:
    """Resultado da verificação de uma única pasta de máquina."""

    nome_maquina: str
    caminho: Path
    arquivos_txt: list = field(default_factory=list)
    arquivos_csv: list = field(default_factory=list)
    alertas: list = field(default_factory=list)

    @property
    def total_csv(self) -> int:
        return len(self.arquivos_csv)

    @property
    def total_txt(self) -> int:
        return len(self.arquivos_txt)

    @property
    def total_arquivos(self) -> int:
        return self.total_csv + self.total_txt

    @property
    def completa(self) -> bool:
        """Verdadeiro somente se atingir o máximo esperado (20 csv + 1 txt)."""
        return (
            self.total_csv == NUMERO_MAXIMO_CSV_POR_MAQUINA
            and self.total_txt == NUMERO_MAXIMO_TXT_POR_MAQUINA
        )

    @property
    def percentual_completude(self) -> float:
        return round(100 * self.total_arquivos / NUMERO_MAXIMO_ARQUIVOS_POR_MAQUINA, 1)


def listar_arquivos_maquina(pasta_maquina: Path) -> RelatorioMaquina:
    """
    Varre uma pasta de máquina (ex.: data/raw/machine_a) e classifica os
    arquivos encontrados em .txt (scores) e .csv/.CSV (telemetria),
    gerando alertas para qualquer inconsistência com o padrão esperado
    (no máximo 1 txt e 20 csv).

    A comparação de extensão é case-insensitive (".CSV" e ".csv" são
    tratados da mesma forma), pois o HWiNFO64 no Windows costuma salvar
    com extensão em maiúsculas.
    """
    nome_maquina = pasta_maquina.name
    relatorio = RelatorioMaquina(nome_maquina=nome_maquina, caminho=pasta_maquina)

    if not pasta_maquina.is_dir():
        relatorio.alertas.append(f"Pasta inexistente: {pasta_maquina}")
        return relatorio

    for item in sorted(pasta_maquina.iterdir()):
        if not item.is_file():
            continue
        extensao = item.suffix.lower()
        if extensao == ".csv":
            relatorio.arquivos_csv.append(item)
        elif extensao == ".txt":
            relatorio.arquivos_txt.append(item)
        # Outros tipos de arquivo (ex.: .DS_Store, .gitkeep) são ignorados
        # silenciosamente, pois não fazem parte dos dados experimentais.

    # --- Validações de limite (a coleta NUNCA deve exceder 21 arquivos) ---
    if relatorio.total_csv > NUMERO_MAXIMO_CSV_POR_MAQUINA:
        relatorio.alertas.append(
            f"Excesso de arquivos CSV: encontrados {relatorio.total_csv}, "
            f"esperado no máximo {NUMERO_MAXIMO_CSV_POR_MAQUINA}. Verifique "
            f"se há rodadas duplicadas ou arquivos de outra máquina na pasta."
        )
    if relatorio.total_txt > NUMERO_MAXIMO_TXT_POR_MAQUINA:
        relatorio.alertas.append(
            f"Excesso de arquivos TXT: encontrados {relatorio.total_txt}, "
            f"esperado no máximo {NUMERO_MAXIMO_TXT_POR_MAQUINA}."
        )
    if relatorio.total_txt == 0:
        relatorio.alertas.append(
            "Nenhum arquivo .txt de scores (Geekbench) encontrado nesta máquina."
        )
    if relatorio.total_csv == 0:
        relatorio.alertas.append(
            "Nenhum arquivo .csv de telemetria (HWiNFO64) encontrado nesta máquina."
        )
    if 0 < relatorio.total_csv < NUMERO_MAXIMO_CSV_POR_MAQUINA:
        faltantes = NUMERO_MAXIMO_CSV_POR_MAQUINA - relatorio.total_csv
        relatorio.alertas.append(
            f"Dados parciais: faltam {faltantes} arquivo(s) CSV de telemetria "
            f"(encontrados {relatorio.total_csv}/{NUMERO_MAXIMO_CSV_POR_MAQUINA}). "
            f"A análise prosseguirá apenas com as rodadas disponíveis."
        )

    return relatorio


def verificar_estrutura_diretorios(
    caminhos: CaminhosProjeto, padrao_pasta_maquina: str = "machine_*"
):
    """
    Percorre data/raw/ procurando por todas as pastas de máquina (padrão
    "machine_*", ex.: machine_a, machine_b, ...) e retorna um relatório de
    completude para cada uma (dict[nome_da_pasta] -> RelatorioMaquina).

    Esta função é deliberadamente genérica quanto à quantidade de máquinas:
    o grupo iniciou com 4 (A-D) mas a pasta de dados já contempla outras
    (E, F, ...) que serão preenchidas posteriormente. O código não deve
    assumir um número fixo de máquinas.
    """
    if not caminhos.dados_raw.is_dir():
        raise FileNotFoundError(
            f"Diretório de dados brutos não encontrado: {caminhos.dados_raw}"
        )

    pastas_maquina = sorted(caminhos.dados_raw.glob(padrao_pasta_maquina))

    if not pastas_maquina:
        logger.warning(
            "Nenhuma pasta de máquina encontrada em %s com o padrão '%s'.",
            caminhos.dados_raw,
            padrao_pasta_maquina,
        )

    relatorios = {}
    for pasta in pastas_maquina:
        if not pasta.is_dir():
            continue
        relatorios[pasta.name] = listar_arquivos_maquina(pasta)

    return relatorios


def exibir_relatorio_completude(relatorios: dict) -> pd.DataFrame:
    """
    Imprime (via logger) um resumo legível da completude de cada máquina e
    devolve os mesmos dados como DataFrame, útil para inspeção no notebook
    ou exportação para uma tabela LaTeX no relatório final.
    """
    linhas = []
    for nome, rel in sorted(relatorios.items()):
        status = "OK (completa)" if rel.completa else "INCOMPLETA/ATENÇÃO"
        logger.info(
            "%-12s | TXT: %d/%d | CSV: %2d/%2d | Completude: %5.1f%% | %s",
            nome,
            rel.total_txt,
            NUMERO_MAXIMO_TXT_POR_MAQUINA,
            rel.total_csv,
            NUMERO_MAXIMO_CSV_POR_MAQUINA,
            rel.percentual_completude,
            status,
        )
        for alerta in rel.alertas:
            logger.warning("  -> [%s] %s", nome, alerta)

        linhas.append(
            {
                "maquina": nome,
                "arquivos_txt": rel.total_txt,
                "arquivos_csv": rel.total_csv,
                "total_arquivos": rel.total_arquivos,
                "percentual_completude": rel.percentual_completude,
                "completa": rel.completa,
                "qtd_alertas": len(rel.alertas),
            }
        )

    return pd.DataFrame(linhas)


# ------------------------------------------------------------------------
# 4. FUNÇÕES DE LIMPEZA E NORMALIZAÇÃO DE DADOS
# ------------------------------------------------------------------------

def normalizar_nome_coluna(nome: str) -> str:
    """
    Remove espaços extras nas bordas e colapsa múltiplos espaços internos.
    Não traduz nem renomeia semanticamente a coluna - apenas higieniza o
    texto para tornar a busca/comparação de nomes mais confiável (arquivos
    HWiNFO64 por vezes trazem espaços duplicados ou caracteres invisíveis).
    """
    if not isinstance(nome, str):
        return nome
    nome = nome.replace("\ufeff", "")  # remove BOM (UTF-8 com marca de ordem de bytes)
    nome = re.sub(r"\s+", " ", nome).strip()
    return nome


def converter_decimal_brasileiro_para_float(serie: pd.Series) -> pd.Series:
    """
    Converte uma coluna que pode estar em formato numérico americano
    ("1234.56") ou brasileiro ("1234,56") para float, de forma tolerante.

    Estratégia:
        1. Se já for numérica, retorna como está (apenas garante float).
        2. Se for texto, remove separador de milhar '.' SOMENTE quando
           houver vírgula decimal explícita (ex.: "1.234,56" -> "1234.56"),
           depois troca ',' por '.'.
        3. Valores não conversíveis (ex.: "-", "N/A", strings vazias)
           tornam-se NaN (pd.to_numeric com errors='coerce'), em vez de
           interromper o pipeline com exceção.
    """
    if pd.api.types.is_numeric_dtype(serie):
        return serie.astype(float)

    serie_texto = serie.astype(str).str.strip()

    contem_virgula_decimal = serie_texto.str.contains(r",\d", regex=True, na=False)

    def _normalizar(valor: str, tem_virgula: bool) -> str:
        if tem_virgula:
            valor = valor.replace(".", "")  # separador de milhar
            valor = valor.replace(",", ".")  # separador decimal -> ponto
        return valor

    serie_normalizada = pd.Series(
        [
            _normalizar(v, tem_virgula)
            for v, tem_virgula in zip(serie_texto, contem_virgula_decimal)
        ],
        index=serie.index,
    )

    return pd.to_numeric(serie_normalizada, errors="coerce")


def converter_sim_nao_para_booleano(serie: pd.Series) -> pd.Series:
    """
    Converte colunas categóricas do tipo "Yes"/"No" (ou "Sim"/"Não") do
    HWiNFO64 para booleano (True/False). Valores não reconhecidos (NaN,
    strings inesperadas) tornam-se NaN, preservando a informação de dado
    ausente em vez de assumir um valor padrão arbitrário.
    """
    mapa = {
        "yes": True, "y": True, "sim": True, "true": True, "1": True,
        "no": False, "n": False, "não": False, "nao": False,
        "false": False, "0": False,
    }
    serie_texto = serie.astype(str).str.strip().str.lower()
    return serie_texto.map(mapa)


def detectar_colunas_booleanas_yes_no(colunas) -> list:
    """Identifica, por convenção de nome, quais colunas são do tipo Yes/No."""
    return [c for c in colunas if "(yes/no)" in str(c).lower()]


def coeficiente_de_variacao(media: float, desvio_padrao: float):
    """
    Calcula o Coeficiente de Variação percentual: CV(%) = (desvio / média) * 100.

    É uma medida adimensional de dispersão relativa, útil para comparar a
    estabilidade de máquinas com médias muito diferentes entre si (ex.:
    comparar a variabilidade de clock entre processadores com frequências
    base distintas). Retorna None se a média for zero ou NaN, evitando
    ZeroDivisionError.
    """
    if media == 0 or pd.isna(media):
        return None
    return round(100 * desvio_padrao / media, 2)


# ------------------------------------------------------------------------
# 5. BUSCA TOLERANTE DE COLUNAS (HWiNFO pode duplicar/renomear sensores)
# ------------------------------------------------------------------------

def encontrar_coluna(df: pd.DataFrame, nome_alvo: str):
    """
    Localiza, dentro de um DataFrame, o nome real de uma coluna que
    corresponde a `nome_alvo`, mesmo que o pandas tenha sufixado nomes
    duplicados (ex.: "CPU Inteira (°C)" e "CPU Inteira (°C).1", quando o
    HWiNFO64 exporta o mesmo sensor em duas seções do log).

    Estratégia de busca, em ordem de prioridade:
        1. Correspondência exata.
        2. Correspondência exata ignorando maiúsculas/minúsculas e espaços.
        3. Primeira coluna cujo nome comece com `nome_alvo` seguido de
           sufixo numérico do pandas (".1", ".2", ...).

    Retorna None (e não lança exceção) se nenhuma correspondência for
    encontrada - a ausência de uma coluna específica não deve interromper
    todo o pipeline, apenas aquela métrica fica indisponível.
    """
    if nome_alvo in df.columns:
        return nome_alvo

    alvo_normalizado = normalizar_nome_coluna(nome_alvo).lower()
    for coluna in df.columns:
        if normalizar_nome_coluna(str(coluna)).lower() == alvo_normalizado:
            return coluna

    padrao_duplicata = re.compile(rf"^{re.escape(nome_alvo)}\.\d+$")
    for coluna in df.columns:
        if padrao_duplicata.match(str(coluna)):
            return coluna

    return None


# ------------------------------------------------------------------------
# 6. EXTRAÇÃO DO IDENTIFICADOR DE RODADA A PARTIR DO NOME DO ARQUIVO
# ------------------------------------------------------------------------

def extrair_numero_rodada(caminho_arquivo: Path):
    """
    Extrai o número da rodada a partir do nome do arquivo de telemetria,
    buscando o último grupo de dígitos presente (robusto a padrões como
    'maqA_rodada_01.CSV', 'machine_a_run_1.csv', 'rodada01.csv', etc.).

    Retorna None se nenhum dígito for encontrado no nome do arquivo.
    """
    nome = caminho_arquivo.stem  # nome sem extensão
    numeros = re.findall(r"(\d+)", nome)
    if not numeros:
        return None
    return int(numeros[-1])