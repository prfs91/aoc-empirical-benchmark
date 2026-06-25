# Geração padronizada de gráficos (Layout, cores e fontes do artigo)

# -*- coding: utf-8 -*-
"""
plotting_engine.py
================================================================================
Módulo de geração de gráficos no padrão visual exigido pelas diretrizes da
SBC (Sociedade Brasileira de Computação) para o artigo final:

    - Figuras em tons de cinza/preto e branco (sem cores saturadas).
    - Tipografia sans-serif (aproximação de Helvetica: usa-se
      'Liberation Sans'/'Arial' como substituto métrico, com fallback
      para DejaVu Sans caso nenhuma das duas esteja instalada - o
      LaTeX/SBC trata a tipografia da LEGENDA separadamente em
      Helvetica 10pt negrito; este módulo cuida apenas da aparência
      INTERNA do gráfico, como rótulos de eixo e barras).
    - Barras com hastes de erro representando o desvio padrão AMOSTRAL
      entre rodadas (não o erro padrão da média), para evidenciar a
      dispersão real observada experimentalmente.
    - Distinção entre categorias por tons de cinza + texturas (hachuras),
      garantindo legibilidade mesmo em impressão P&B (acessibilidade a
      daltonismo também é beneficiada).
    - Salvamento em alta resolução (300 DPI), pronto para
      \\includegraphics no Overleaf.

IMPORTANTE: este módulo gera apenas a FIGURA (gráfico). A legenda
formatada em Helvetica 10pt negrito (com a regra de centralizar legendas
curtas e justificar com recuo de 0,8cm legendas longas) deve ser escrita
diretamente no código-fonte LaTeX do artigo (\\caption{...}), pois esse
tipo de formatação de texto é responsabilidade do documento .tex, não da
imagem gerada em Python.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

try:
    from . import utils_utils as u
except ImportError:
    import utils_utils as u

logger = u.configurar_logger("aoc_pipeline.plots")

matplotlib.use("Agg")  # backend não interativo (seguro para scripts/CI); o
# Jupyter substitui isso automaticamente ao exibir a figura inline.

# Paleta de cinzas (do mais escuro ao mais claro) e hachuras associadas,
# para que cada "série"/máquina seja distinguível mesmo sem cor.
PALETA_CINZA = ["#1a1a1a", "#4d4d4d", "#808080", "#b3b3b3", "#d9d9d9", "#f0f0f0"]
HACHURAS = ["", "//", "xx", "..", "\\\\", "++"]


def configurar_estilo_sbc() -> None:
    """
    Ajusta os parâmetros globais (rcParams) do matplotlib para aproximar
    o padrão visual sóbrio exigido pela SBC: fonte sans-serif, sem
    grades fortes, eixos finos em preto, sem cores saturadas.

    Deve ser chamada UMA VEZ no início do notebook/script, antes de
    qualquer chamada às funções de plot deste módulo.
    """
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Liberation Sans", "Arial", "DejaVu Sans"],
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "axes.edgecolor": "#1a1a1a",
            "axes.linewidth": 0.8,
            "axes.grid": True,
            "grid.color": "#cccccc",
            "grid.linewidth": 0.5,
            "grid.alpha": 0.6,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.color": "#1a1a1a",
            "ytick.color": "#1a1a1a",
            "legend.frameon": False,
            "legend.fontsize": 10,
            "figure.dpi": 110,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )


def _salvar_figura(fig: plt.Figure, caminho_saida: Optional[Path]) -> Optional[Path]:
    """Salva a figura em disco (PNG, 300 DPI) se um caminho for fornecido."""
    if caminho_saida is None:
        return None
    caminho_saida = Path(caminho_saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    try:
        fig.savefig(caminho_saida)
        logger.info("Figura salva em: %s", caminho_saida)
    except (OSError, ValueError) as erro:
        logger.error("Falha ao salvar figura em '%s': %s", caminho_saida, erro)
        return None
    return caminho_saida


# ------------------------------------------------------------------------
# 1. GRÁFICO DE BARRAS COMPARATIVO ENTRE MÁQUINAS, COM ERRO (DESVIO PADRÃO)
# ------------------------------------------------------------------------

def grafico_barras_com_erro(
    categorias: Sequence[str],
    medias: Sequence[float],
    desvios: Sequence[float],
    titulo: str = "",
    ylabel: str = "",
    xlabel: str = "",
    caminho_saida: Optional[Path] = None,
    incluir_titulo: bool = True,
    formato_rotulo: str = "{:.1f}",
) -> plt.Figure:
    """
    Gera um gráfico de barras verticais comparando uma métrica entre
    várias máquinas/categorias, com hastes de erro representando o
    desvio padrão amostral calculado entre as rodadas.

    Parâmetros
    ----------
    categorias : sequência de rótulos do eixo X (ex.: nomes das máquinas).
    medias      : valores médios (altura das barras).
    desvios     : desvios padrão (tamanho da haste de erro); pode conter
                  NaN (ex.: máquina com apenas 1 rodada válida) - nesse
                  caso a haste daquela barra simplesmente não aparece.
    incluir_titulo : se False, omite o título interno (recomendado para a
                  versão final embutida no LaTeX, já que a legenda formal
                  fica a cargo do \\caption do artigo).

    Retorna
    -------
    matplotlib.figure.Figure
    """
    if len(categorias) != len(medias) or len(medias) != len(desvios):
        raise ValueError(
            "categorias, medias e desvios devem ter o mesmo tamanho "
            f"(recebido: {len(categorias)}, {len(medias)}, {len(desvios)})."
        )

    desvios_seguros = [0 if (d is None or (isinstance(d, float) and np.isnan(d))) else d for d in desvios]

    fig, ax = plt.subplots(figsize=(0.9 * max(4, len(categorias)) + 1.5, 4.2))

    posicoes = np.arange(len(categorias))
    cores = [PALETA_CINZA[i % len(PALETA_CINZA)] for i in range(len(categorias))]
    hachuras = [HACHURAS[i % len(HACHURAS)] for i in range(len(categorias))]

    barras = ax.bar(
        posicoes,
        medias,
        yerr=desvios_seguros,
        capsize=4,
        color=cores,
        edgecolor="#1a1a1a",
        linewidth=0.8,
        hatch=None,  # hachura aplicada individualmente abaixo
        error_kw={"elinewidth": 1.0, "ecolor": "#1a1a1a"},
    )
    for barra, hachura in zip(barras, hachuras):
        barra.set_hatch(hachura)

    for posicao, media in zip(posicoes, medias):
        if media is not None and not (isinstance(media, float) and np.isnan(media)):
            ax.text(
                posicao, media, formato_rotulo.format(media),
                ha="center", va="bottom", fontsize=9, color="#1a1a1a",
            )

    ax.set_xticks(posicoes)
    ax.set_xticklabels(categorias, rotation=0 if len(categorias) <= 6 else 30, ha="right" if len(categorias) > 6 else "center")
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    if incluir_titulo and titulo:
        ax.set_title(titulo)

    fig.tight_layout()
    _salvar_figura(fig, caminho_saida)
    return fig


# ------------------------------------------------------------------------
# 2. GRÁFICO DE DISPERSÃO (ex.: clock efetivo x score -> IPC relativo)
# ------------------------------------------------------------------------

def grafico_dispersao(
    x: Sequence[float],
    y: Sequence[float],
    rotulos: Optional[Sequence[str]] = None,
    titulo: str = "",
    xlabel: str = "",
    ylabel: str = "",
    caminho_saida: Optional[Path] = None,
    incluir_titulo: bool = True,
) -> plt.Figure:
    """
    Gera um gráfico de dispersão (scatter) em tons de cinza, útil para
    relacionar duas métricas contínuas (ex.: clock efetivo médio da
    rodada vs. score obtido na mesma rodada, para discutir eficiência por
    ciclo/IPC relativo).

    `rotulos`, se fornecido, anota cada ponto (ex.: nome da máquina ou
    número da rodada) - recomendado apenas para poucos pontos (<= 20),
    caso contrário a figura fica poluída.
    """
    fig, ax = plt.subplots(figsize=(5.5, 4.2))

    ax.scatter(
        x, y, s=60, color="#404040", edgecolor="#1a1a1a", linewidth=0.8, alpha=0.85,
        marker="o",
    )

    if rotulos is not None:
        for xi, yi, rotulo in zip(x, y, rotulos):
            if rotulo is None:
                continue
            ax.annotate(
                str(rotulo), (xi, yi), textcoords="offset points",
                xytext=(5, 4), fontsize=8, color="#333333",
            )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if incluir_titulo and titulo:
        ax.set_title(titulo)

    fig.tight_layout()
    _salvar_figura(fig, caminho_saida)
    return fig


# ------------------------------------------------------------------------
# 3. SÉRIE TEMPORAL DE UMA RODADA (ex.: clock/temperatura ao longo do tempo)
# ------------------------------------------------------------------------

def grafico_linha_temporal(
    serie_y: Sequence[float],
    eixo_x: Optional[Sequence] = None,
    titulo: str = "",
    xlabel: str = "Amostra (tempo)",
    ylabel: str = "",
    limiar_horizontal: Optional[float] = None,
    rotulo_limiar: str = "",
    caminho_saida: Optional[Path] = None,
    incluir_titulo: bool = True,
) -> plt.Figure:
    """
    Plota a evolução temporal de uma métrica dentro de UMA única rodada
    (ex.: temperatura da CPU amostra-a-amostra), útil para ilustrar
    visualmente o momento em que ocorre throttling térmico (quando o
    clock despenca após a temperatura cruzar um limiar).

    `limiar_horizontal`, se fornecido, desenha uma linha pontilhada de
    referência (ex.: TjMax ou o limite de potência PL1), facilitando a
    leitura do ponto em que a métrica o ultrapassa.
    """
    fig, ax = plt.subplots(figsize=(6.0, 3.6))

    eixo_x_final = eixo_x if eixo_x is not None else np.arange(len(serie_y))
    ax.plot(eixo_x_final, serie_y, color="#1a1a1a", linewidth=1.2)

    if limiar_horizontal is not None:
        ax.axhline(
            limiar_horizontal, color="#808080", linestyle="--", linewidth=1.0,
            label=rotulo_limiar or f"Limiar = {limiar_horizontal}",
        )
        ax.legend()

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if incluir_titulo and titulo:
        ax.set_title(titulo)

    fig.tight_layout()
    _salvar_figura(fig, caminho_saida)
    return fig


# ------------------------------------------------------------------------
# 4. BOXPLOT COMPARATIVO DE VARIABILIDADE ENTRE MÁQUINAS
# ------------------------------------------------------------------------

def grafico_boxplot_variabilidade(
    dados_por_categoria: dict,
    titulo: str = "",
    ylabel: str = "",
    caminho_saida: Optional[Path] = None,
    incluir_titulo: bool = True,
) -> plt.Figure:
    """
    Gera um boxplot comparando a distribuição de uma métrica (ex.: score
    Multi_Core das 20 rodadas) entre várias máquinas, evidenciando de
    forma visual a dispersão/outliers - complementar à barra com erro,
    pois mostra a distribuição completa, não apenas média ± desvio.

    Parâmetros
    ----------
    dados_por_categoria : dict[str, sequência de valores]
        Ex.: {'Máquina A': [1290, 1295, ...], 'Máquina B': [1200, 1350, ...]}
    """
    rotulos = list(dados_por_categoria.keys())
    valores = [
        [v for v in seq if v is not None and not (isinstance(v, float) and np.isnan(v))]
        for seq in dados_por_categoria.values()
    ]

    fig, ax = plt.subplots(figsize=(0.9 * max(4, len(rotulos)) + 1.5, 4.2))

    caixas = ax.boxplot(
        valores, labels=rotulos, patch_artist=True, showmeans=True,
        boxprops={"linewidth": 0.9, "edgecolor": "#1a1a1a"},
        medianprops={"color": "#1a1a1a", "linewidth": 1.4},
        whiskerprops={"color": "#1a1a1a"},
        capprops={"color": "#1a1a1a"},
        meanprops={"marker": "D", "markerfacecolor": "#1a1a1a", "markeredgecolor": "#1a1a1a", "markersize": 5},
        flierprops={"marker": "o", "markerfacecolor": "none", "markeredgecolor": "#1a1a1a", "markersize": 5},
    )
    for caixa, cor in zip(caixas["boxes"], PALETA_CINZA):
        caixa.set_facecolor(cor)

    ax.set_ylabel(ylabel)
    if incluir_titulo and titulo:
        ax.set_title(titulo)

    fig.tight_layout()
    _salvar_figura(fig, caminho_saida)
    return fig