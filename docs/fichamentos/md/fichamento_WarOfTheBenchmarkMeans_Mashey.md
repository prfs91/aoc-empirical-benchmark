# Fichamento Científico — `fichamento_WarOfTheBenchmarkMeans_Mashey.md`

> **Arquivo gerado por:** Sistema de Fichamento Científico — Projeto AOC / UFPA Tucuruí
> **Data de geração:** Junho de 2026
> **Veredito de Relevância:** ✅ **SIM — Alta aderência ao escopo do projeto.**
> O artigo é uma referência fundamental em **Estatística Experimental aplicada a Benchmarking**.
> Discute rigorosamente quando usar Média Aritmética (AM), Média Geométrica (GM), Média
> Harmônica (HM), Desvio Padrão, Skew, Kurtose, Intervalo de Confiança e distribuição
> lognormal de razões de desempenho — exatamente o instrumental matemático que sustenta
> a análise das 20 rodadas de Geekbench 6 (Single_Core/Multi_Core) e da telemetria HWiNFO64
> das nossas 4 máquinas. Não trata de CPU/GPU/RAM/Throttling diretamente, mas fornece a
> **base estatística obrigatória** para validar (ou refutar) o uso de médias e desvios-padrão
> simples na nossa Metodologia e Resultados.
>
> **Atualização (Junho/2026):** o parque experimental do grupo foi expandido para 6 máquinas
> (A, B, C, D, E, F), incorporando dois desktops montados (E e F) e detalhando integralmente
> as configurações de A, B e C. As Seções 3.10, 3.11 e 3.12 foram acrescentadas a este
> fichamento para conectar a teoria de Mashey (2004) à heterogeneidade real desse parque
> ampliado (TDP de 15 W a 125 W, núcleos híbridos P+E vs. homogêneos, e o tamanho reduzido
> da amostra de sistemas), sem alteração do conteúdo previamente fichado.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

MASHEY, J. R. War of the Benchmark Means: Time for a Truce. **ACM SIGARCH Computer Architecture News**, v. 32, n. 4, p. 1-14, set. 2004.

- **Código BibTeX Completo (.bib):**

```bibtex
@Article{mashey:04,
  author  = {John R. Mashey},
  title   = {War of the Benchmark Means: Time for a Truce},
  journal = {{ACM SIGARCH} Computer Architecture News},
  volume  = {32},
  number  = {4},
  pages   = {1--14},
  month   = {sep},
  year    = {2004},
  note    = {Techviser}
}
```

> ⚠️ **Nota editorial:** O artigo foi publicado como coluna/artigo técnico da *ACM SIGARCH
> Computer Architecture News* (não é um artigo de conferência com proceedings tradicional).
> O tipo `@Article` é o mais adequado para o `sbc-template.bib`. Citar no `main.tex` com
> `\cite{mashey:04}`.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo Técnico/Coluna de Periódico (ACM SIGARCH Computer Architecture News) — 14 páginas
- **Instituição/Editora:** ACM (Association for Computing Machinery) — SIGARCH; autor afiliado à empresa Techviser, ex-representante fundador da MIPS na SPEC
- **Palavras-Chave Originais:** Benchmarking, Geometric Mean, Lognormal Distribution
- **Resumo do Escopo Geral:**

O artigo resgata a "Guerra das Médias" (War of Means) entre Média Aritmética (AM), Geométrica (GM) e Harmônica (HM) na agregação de resultados de benchmark, mostrando que a controvérsia decorre de premissas estatísticas mal especificadas — confusão entre população, parâmetros, métodos de amostragem e estatísticas amostrais. Mashey argumenta que razões de desempenho relativo entre dois computadores não seguem, em geral, uma distribuição Normal (Gaussiana), mas sim uma distribuição **Log-Normal**, e que a GM é, matematicamente, a média retransformada (back-transformed) dessa distribução logarítmica. O autor introduz três categorias analíticas — **WCA** (Workload Characterization Analysis), **SERPOP** (Sample Estimation of Relative Performance Of Programs) e **WAW** (Workload Analysis with Weights) — e demonstra, com exemplos didáticos (VAX 8700, Hennessy & Patterson, Lilja, SPEC CINT2000/CFP2000), como calcular corretamente Média, Desvio Padrão, Skew (assimetria), Kurtose e Intervalos de Confiança a 95% sobre razões logarítmicas, retransformando os resultados para a escala original via função exponencial.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 A "Guerra das Médias" e a Identidade Matemática da Média Geométrica

- **Conceito/Teoria:** Média Geométrica (GM) como retransformação (back-transform) da média de uma distribuição log-normal — fundamento da escolha de qual média usar na agregação de scores de benchmark.

- **Citação Direta (Ipsis Litteris):**
> "The usual GM formula is rather unintuitive, and is often claimed to have no physical meaning. However, it is the back-transformed average of a lognormal distribution, as can be seen by the mathematical identity below." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
Conforme Mashey (2004), a fórmula usual da Média Geométrica é frequentemente considerada destituída de significado físico; entretanto, ela corresponde exatamente à média aritmética dos logaritmos dos valores, retransformada para a escala original por meio da função exponencial — propriedade que evidencia sua adequação estatística quando os dados seguem uma distribuição log-normal, como costuma ocorrer com razões de desempenho entre sistemas computacionais (p. 1).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (subseção de Métricas de Desempenho) e Metodologia (justificativa estatística para o tratamento dos scores Single-Core e Multi-Core).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: caso o grupo decida comparar **razões de desempenho entre máquinas** (ex.: Máquina A / Máquina D), em vez de apenas valores absolutos, a GM é a média estatisticamente correta para essas razões, não a AM.
  - Não há coluna de telemetria HWiNFO64 diretamente associada a este conceito, pois trata-se de fundamentação puramente estatística aplicada aos scores do Geekbench 6.

---

### 3.2 Distinção entre Tempo de Execução e Razões de Desempenho (Rij)

- **Conceito/Teoria:** Definição formal de razão de desempenho relativo entre sistemas — base matemática para comparar Tempo de Execução vs. Taxa de Transferência entre as 4 máquinas do projeto.

- **Citação Direta (Ipsis Litteris):**
> "Performance ratios are given as the ratio of Sj's performance to that of Sk's running program Pi with some specific input. Mathematically, any system could be chosen as the base, and k can be assumed to be 1 when omitted. Larger ratios imply higher speed. Rijk = Tik/Tij" (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
Mashey (2004) define formalmente a razão de desempenho relativo $R_{ijk}$ entre dois sistemas $S_j$ e $S_k$ executando um mesmo programa $P_i$ como a razão entre os tempos de execução $T_{ik}/T_{ij}$, estabelecendo que qualquer sistema pode ser adotado arbitrariamente como base de comparação, sem alterar a validade estatística da análise, desde que o tratamento matemático (escala logarítmica) seja consistente (p. 6).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — seção de Métricas de Desempenho (Tempo de Execução vs. Vazão).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: se o grupo comparar, por exemplo, Máquina A em relação à Máquina D (base), a razão Score(A)/Score(D) corresponde exatamente ao $R_{ijk}$ definido pelo autor.

---

### 3.3 Inconsistência da Média Aritmética sobre Razões (Problema da Base de Comparação)

- **Conceito/Teoria:** Demonstração de que a Média Aritmética aplicada a razões de desempenho produz resultados logicamente impossíveis (assimetria ao trocar a base de comparação).

- **Citação Direta (Ipsis Litteris):**
> "Rij (for j!=base) cannot, in general, be normally distributed, because it produces impossible results for both simple examples and real cases. Suppose S1 and S2 are systems whose performance is clearly equal, but making either the base causes the other to look 1.25X faster. This simply cannot be true, as meaningful statistics should not be changed just by labeling." (p. 8)

- **Paráfrase (Citação Indireta Acadêmica):**
O autor demonstra, por meio de exemplo numérico (Tabela 3), que ao se aplicar a Média Aritmética sobre razões de desempenho de sistemas equivalentes, a simples troca de qual sistema é usado como referência (base) altera artificialmente o resultado — um problema estatístico que não ocorre com a Média Geométrica, cuja simetria logarítmica preserva a coerência da comparação independentemente da base escolhida (Mashey, 2004, p. 8).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — ressalva metodológica sobre o uso de médias em comparações relativas entre as Máquinas A, B, C e D.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: relevante caso o grupo apresente tabelas de "Máquina X é Y vezes mais rápida que a Máquina Z" — recomenda-se citar esta ressalva para justificar o uso de Médias Aritméticas simples sobre os **scores absolutos** (não sobre razões), evitando a armadilha apontada pelo autor.

---

### 3.4 Desvio Padrão Amostral e Repetibilidade da Medição (Assunção A3)

- **Conceito/Teoria:** Repetibilidade de medição — pressuposto estatístico de que execuções repetidas do mesmo benchmark no mesmo sistema produzem uma distribuição de tempos com Desvio Padrão muito menor que a Média.

- **Citação Direta (Ipsis Litteris):**
> "A3: Measurement Repeatability — Assume that multiple executions of the same program with same input on same system yield a distribution of run-times with Standard Deviation << Mean, so that a Mean (or Median) is a good estimate of population mean." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
Mashey (2004) estabelece, como pressuposto fundamental (Assunção A3) de qualquer análise SERPOP, que execuções repetidas de um mesmo programa sob as mesmas condições devem produzir tempos de execução cujo desvio padrão seja consideravelmente menor que a média — condição que valida o uso da média (ou mediana) amostral como estimador confiável da performance real do sistema. Quando essa condição não se verifica, há indício de instabilidade na medição, frequentemente associada a fatores externos como variação térmica ou contenção de recursos (p. 6).

- **Onde Encaixar no Artigo LaTeX:** Metodologia (justificativa de 20 rodadas por máquina) e Resultados e Discussão (interpretação de desvios-padrão elevados).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core` (20 rodadas): cálculo direto do Desvio Padrão Amostral sobre as 20 repetições por máquina é o teste empírico desta assunção A3.
  - `maq*_rodada_*.CSV` → colunas `Estrangulamento térmico do núcleo (avg) (Yes/No)`, `CPU Inteira (°C)`, `Núcleo máximo (°C)`: quando o Desvio Padrão dos scores for elevado (violação de A3), estas colunas de telemetria devem ser cruzadas para verificar se a causa foi instabilidade térmica durante a rodada.

---

### 3.5 Skew (Assimetria) e Kurtose como Indicadores de Outliers/Instabilidade

- **Conceito/Teoria:** Interpretação arquitetural de Skew e Kurtose elevados como indícios de outliers, subpopulações distintas ou throttling térmico durante a coleta.

- **Citação Direta (Ipsis Litteris):**
> "Large Skew indicates the presence of one or more outliers that need to be examined carefully, or a mixture of samples whose means differ substantially, or in general, that the distribution is not normal, and hence one must be very careful in the interpretation of the Mean." (p. 7)

- **Paráfrase (Citação Indireta Acadêmica):**
Segundo o autor, valores elevados de Skew (assimetria estatística) sinalizam a presença de outliers que demandam investigação cuidadosa, ou a mistura de subpopulações com médias substancialmente diferentes dentro da mesma amostra — cenário em que a interpretação direta da média aritmética torna-se estatisticamente arriscada (Mashey, 2004, p. 7). De forma complementar, o autor associa Kurtose fortemente positiva à existência de elementos correlacionados na amostra, e Kurtose negativa a uma dispersão maior que a esperada em uma distribuição normal (p. 7).

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — ao explicar variações anômalas entre as 20 rodadas de uma mesma máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: cálculo de Skew/Kurtose sobre as 20 rodadas pode revelar rodadas-outlier (ex.: uma rodada anormalmente lenta).
  - `maq*_rodada_*.CSV` → colunas `Estrangulamento térmico do núcleo (avg) (Yes/No)`, `Limite de desempenho - Térmico (Yes/No)`, `IA: Package-Level RAPL/PBM PL1 (Yes/No)`: se uma rodada específica apresentar throttling térmico ativo, ela é candidata a outlier responsável pelo Skew elevado nos scores.

---

### 3.6 Intervalo de Confiança como Medida de Incerteza da Estimativa

- **Conceito/Teoria:** Necessidade de reportar Intervalo de Confiança (tipicamente 95%) junto à média amostral, pois a média é apenas um estimador, sujeito a incerteza que diminui com o aumento do tamanho da amostra.

- **Citação Direta (Ipsis Litteris):**
> "One would also want to compute the X% (commonly 95%) confidence interval, i.e., the interval that has X% chance of including the real population mean, as the sample mean, of course, is only an estimator." (p. 7)

- **Paráfrase (Citação Indireta Acadêmica):**
Mashey (2004) recomenda que toda média amostral seja acompanhada de um intervalo de confiança (comumente a 95%), uma vez que a média calculada a partir de uma amostra é apenas uma estimativa da verdadeira média populacional, sendo a precisão dessa estimativa diretamente relacionada ao tamanho da amostra coletada (p. 7).

- **Onde Encaixar no Artigo LaTeX:** Metodologia — ao justificar o uso de hastes de erro (desvio padrão) nos gráficos de barra, e Resultados e Discussão — ao interpretar a confiabilidade das médias de 20 rodadas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: as 20 rodadas por máquina formam a amostra sobre a qual se calculam Média, Desvio Padrão e, opcionalmente, Intervalo de Confiança a 95% (fundamenta estatisticamente as hastes de erro exigidas nos barplots do grupo).

---

### 3.7 Distribuição Log-Normal de Razões de Desempenho

- **Conceito/Teoria:** Razões de desempenho (relative performance ratios) tendem a seguir distribuição log-normal, e não Normal — fundamento teórico central do artigo, com aplicação direta à comparação entre as 4 máquinas do grupo.

- **Citação Direta (Ipsis Litteris):**
> "Normal distributions arise by aggregations of many additive effects, while lognormals arise from combinations of multiplicative effects, like clock rate differences, compiler optimizations, or memory system design differences." (p. 7)

- **Paráfrase (Citação Indireta Acadêmica):**
O autor explica que distribuições Normais emergem da agregação de efeitos aditivos, ao passo que distribuições Log-Normais resultam de combinações de efeitos multiplicativos — como diferenças de frequência de clock, otimizações de compilador ou variações no projeto do subsistema de memória (Mashey, 2004, p. 7). Essa observação é particularmente relevante para a comparação de desempenho entre arquiteturas heterogêneas, já que fatores de clock, cache e memória atuam de forma multiplicativa, e não aditiva, sobre o desempenho final.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — seção de Hierarquia de Memória e Paralelismo, ao discutir por que diferenças de clock, cache L3 e canal de memória (Single vs. Dual Channel) produzem efeitos multiplicativos, não aditivos, sobre o score final.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: se o grupo comparar razões de score entre máquinas com configurações de clock/cache distintas, espera-se um comportamento log-normal, não normal.
  - `maq*_rodada_*.CSV` → colunas `Relógios efetivos núcleo (avg) (MHz)`, `Relógio da memória (MHz)`: variáveis multiplicativas que, segundo a teoria do autor, geram a assimetria (skew) observada nas razões de desempenho entre máquinas com hardware distinto.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA:** Este conceito ganha maior relevância comparativa quando há heterogeneidade de hardware entre as máquinas (ex.: Dual Channel vs. Single Channel, ou diferentes litografias). Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.

---

### 3.8 SERPOP — Amostragem de Programas vs. Caracterização de Carga de Trabalho

- **Conceito/Teoria:** Distinção entre WCA (Workload Characterization Analysis), SERPOP (Sample Estimation of Relative Performance Of Programs) e WAW (Workload Analysis with Weights) — relevante para posicionar metodologicamente o uso do Geekbench 6 como benchmark sintético representativo, não como carga de trabalho real do usuário.

- **Citação Direta (Ipsis Litteris):**
> "A good SERPOP analysis constructs a multi-element benchmark suite that is a sample of some population of programs. It requires certain assumptions to be met regarding the sampling process, and it requires an appropriate model of the population's distribution." (p. 2-3)

- **Paráfrase (Citação Indireta Acadêmica):**
Mashey (2004) define a Estimação Amostral de Desempenho Relativo de Programas (SERPOP) como a construção de uma suíte de benchmarks que representa uma amostra de uma população maior de programas, exigindo o cumprimento de pressupostos sobre o processo de amostragem e um modelo adequado da distribuição da população para que se possa produzir estatísticas significativas (média, dispersão, intervalo de confiança e qualidade de ajuste) (p. 2-3).

- **Onde Encaixar no Artigo LaTeX:** Introdução e Metodologia — para posicionar epistemologicamente o Geekbench 6 como benchmark sintético do tipo SERPOP, distinto de uma análise WCA (que exigiria caracterização da carga de trabalho real do usuário).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Não há mapeamento direto de colunas; trata-se de fundamentação epistemológica sobre a natureza do instrumento de benchmarking (Geekbench 6) utilizado pelo grupo, justificando os limites de generalização dos resultados.

---

### 3.9 Crítica à Anonimidade de Benchmarks — Assunção A5 (Reconhecibilidade)

- **Conceito/Teoria:** Necessidade de identificação e reconhecibilidade dos programas/subtestes de um benchmark para garantir credibilidade científica dos resultados.

- **Citação Direta (Ipsis Litteris):**
> "A5: Programs should be 'recognizable' — In practice, credibility is improved if individual benchmarks are identified and recognizable. Even better, it may help some users select specific benchmarks for their own WAW analyses." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
O autor estabelece, como quinta assunção (A5) de uma análise SERPOP confiável, que os programas/subtestes que compõem o benchmark sejam identificáveis e reconhecíveis, o que aumenta a credibilidade científica dos resultados e permite que usuários selecionem subconjuntos relevantes para suas próprias análises de carga de trabalho ponderada (Mashey, 2004, p. 6).

- **Onde Encaixar no Artigo LaTeX:** Metodologia — ao apresentar o Geekbench 6 e justificar a transparência dos subtestes Single-Core e Multi-Core que compõem o score final.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: a separação explícita entre os dois subscores (em vez de um único score opaco) atende à recomendação A5 do autor, permitindo análises segmentadas por tipo de carga (mono-thread vs. multi-thread).

---

### 3.10 Heterogeneidade Extrema de TDP/Litografia como Gerador de Distribuição Log-Normal entre Sistemas (Máquinas B/D vs. E/F)

- **Conceito/Teoria:** Efeitos multiplicativos de hardware (litografia, TDP, geração de microarquitetura) como causa da assimetria (skew) observada na distribuição das razões de desempenho entre sistemas heterogêneos — aplicação direta da teoria de Mashey (Seção 3.7 deste fichamento) ao parque real de 6 máquinas do grupo.

- **Citação Direta (Ipsis Litteris):**
> "Normal distributions arise by aggregations of many additive effects, while lognormals arise from combinations of multiplicative effects, like clock rate differences, compiler optimizations, or memory system design differences." (p. 7)

- **Paráfrase (Citação Indireta Acadêmica):**
Como já discutido na Seção 3.7 deste fichamento, Mashey (2004) associa a origem de distribuições log-normais a efeitos multiplicativos de hardware — e essa condição se manifesta de forma particularmente acentuada no parque experimental do grupo, que reúne sistemas com TDP variando de 15 W (Máquinas B, C e D — notebooks ultrafinos) a 125 W (Máquina F — desktop com Intel Core i5-14600KF), uma razão de até 8,3 vezes no envelope térmico-energético declarado pelo fabricante. Tal disparidade, somada a diferenças de litografia (14 nm na Máquina D vs. Intel 7 nas Máquinas A e F) e de arquitetura de núcleos (híbrida P-core/E-core nas Máquinas A, B e F vs. núcleos homogêneos nas Máquinas C, D e E), constitui exatamente o cenário de "combinação de efeitos multiplicativos" descrito pelo autor, justificando a expectativa teórica de que as razões de desempenho entre essas máquinas sigam uma distribuição log-normal assimétrica, e não uma distribuição Normal simétrica (p. 7).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia/Eficiência Microarquitetural) e Resultados e Discussão — ao comparar razões de score entre o subgrupo de notebooks ultrafinos de baixo TDP (B, C, D) e o subgrupo de desktops/notebook gamer de alto TDP (A, E, F).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` (todas as 6 máquinas, colunas `Single_Core` e `Multi_Core`): ao calcular a razão Score(F)/Score(D) — desktop de 125 W vs. notebook de 15 W — espera-se um valor de razão muito mais distante de 1 do que entre, por exemplo, Score(B)/Score(D) (ambos 15 W), evidenciando empiricamente o efeito multiplicativo do TDP sobre o desempenho.
  - `maq*_rodada_*.CSV` → colunas `Potência total da CPU (W)`, `Relógios efetivos núcleo (avg) (MHz)`: permitem confirmar, rodada a rodada, se a máquina de maior TDP de fato sustenta um consumo e um clock proporcionalmente maiores, validando a causa arquitetural do efeito multiplicativo apontado por Mashey.

---

### 3.11 Subpopulações Distintas dentro da Amostra — Núcleos Híbridos (P+E) vs. Homogêneos como Fonte de Multimodalidade

- **Conceito/Teoria:** Natureza multimodal de uma distribuição de razões de desempenho como indício da existência de subpopulações distintas dentro da amostra — relacionado, no artigo, ao exemplo do VAX 8700, e aplicável à divisão arquitetural Híbrida (P-core + E-core) vs. Homogênea presente no parque de máquinas do grupo.

- **Citação Direta (Ipsis Litteris):**
> "On the other hand, the multi-modal nature of the distribution, with two peaks nearly a Standard Deviation apart, is a strong hint that there exist several distinct subpopulations, and that it would be wise to understand their nature." (p. 4)

- **Paráfrase (Citação Indireta Acadêmica):**
Mashey (2004) observa que uma distribuição multimodal de razões de desempenho — com picos de frequência separados por aproximadamente um desvio padrão — constitui forte indício da existência de subpopulações distintas dentro da amostra analisada, recomendando que sua natureza seja investigada e, se necessário, que a amostra seja segmentada em subamostras mais homogêneas (p. 4). No contexto do grupo, essa recomendação é diretamente aplicável à divisão entre processadores com arquitetura híbrida de núcleos (Máquinas A, B e F, com núcleos de Performance e Eficiência distintos) e processadores com núcleos homogêneos (Máquinas C, D e E), já que o comportamento de escalonamento de tarefas entre threads pode produzir distribuições de desempenho qualitativamente diferentes entre esses dois subgrupos.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Paralelismo a Nível de Instrução e Thread — Cores físicos vs. Threads lógicos) e Metodologia, ao justificar uma eventual segmentação das 6 máquinas em dois subgrupos de análise.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → coluna `Multi_Core`: é a métrica mais sensível à heterogeneidade de núcleos, pois depende diretamente de como o escalonador do Windows 11 distribui as 20 rodadas entre núcleos P e E (Máquinas A, B, F) versus núcleos uniformes (C, D, E).
  - `maq*_rodada_*.CSV` → colunas `Core 0 T0 Uso (%)` a `Core 3 T1 Uso (%)` e `Uso máximo de CPU / thread (%)`: permitem visualizar, rodada a rodada, se a carga foi distribuída de forma desigual entre núcleos (esperado em arquiteturas híbridas), o que sustentaria empiricamente a hipótese de subpopulação distinta.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA:** A telemetria HWiNFO64 listada no projeto contempla nominalmente 4 núcleos (Core 0 a Core 3), volume compatível com as Máquinas C e D (4 núcleos físicos), mas insuficiente para registrar individualmente os 8, 10 ou 14 núcleos das Máquinas A, B e F. Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C — e, agora, também E e F — forem preenchidas e os arquivos de telemetria correspondentes (com a quantidade real de núcleos monitorados) forem confirmados pelo grupo nas próximas interações, se necessário.

---

### 3.12 Amostra Pequena (n=6 Sistemas) e o Risco de Subdimensionamento Estatístico (Assunção A2)

- **Conceito/Teoria:** Recomendação de que amostras pequenas sejam evitadas em análises SERPOP, e que, quando inevitáveis, suas limitações de confiança estatística sejam explicitamente reconhecidas — diretamente aplicável ao fato de o grupo dispor de apenas 6 máquinas (sistemas), e não de 6 programas/benchmarks.

- **Citação Direta (Ipsis Litteris):**
> "A2: Small sample sizes should be avoided — One can learn something from even a handful of programs, if they are well-chosen. It is wonderful, but often expensive, to obtain a complete set of run-times for 30 different programs on multiple systems." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
O autor adverte, na Assunção A2, que amostras pequenas devem ser evitadas sempre que possível, embora reconheça que mesmo um pequeno número de elementos bem escolhidos já permita extrair informação útil, ainda que a obtenção de conjuntos completos de medições (idealmente 30 ou mais) seja onerosa na prática (Mashey, 2004, p. 6). Embora o autor trate originalmente do número de *programas* em uma suíte de benchmark, o mesmo princípio estatístico se aplica, por analogia, ao número de *sistemas* comparados: com apenas 6 máquinas na amostra do grupo, qualquer generalização sobre "notebooks ultrafinos" versus "desktops montados", por exemplo, deve ser apresentada com a devida ressalva de que se trata de um estudo de caso comparativo, e não de uma amostra estatisticamente representativa da população de computadores pessoais.

- **Onde Encaixar no Artigo LaTeX:** Metodologia (Limitações do Estudo) e Conclusão — ao delimitar o alcance das generalizações feitas a partir da comparação entre as Máquinas A, B, C, D, E e F.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt`: as 20 rodadas por máquina mitigam parcialmente o problema de pequena amostra **dentro** de cada máquina (robustez da média individual), mas não resolvem a limitação de uma amostra de apenas 6 máquinas **entre** sistemas — distinção que deve ser explicitada na seção de limitações do artigo.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmulas Matemáticas/Físicas em LaTeX Puro

**Média Geométrica e sua identidade log-normal (p. 1):**

```latex
GM = \overline{x_G} = \left( \prod_{i=1}^{n} x_i \right)^{\left(\frac{1}{n}\right)} = \exp\left( \frac{1}{n} \sum_{i=1}^{n} \ln(x_i) \right)
```

**Razão de desempenho relativo entre sistemas (p. 6):**

```latex
R_{ijk} = \frac{T_{ik}}{T_{ij}}
```

**Razão de desempenho a partir de métricas inversamente proporcionais ao tempo (p. 6), como scores de benchmark (Geekbench):**

```latex
R_{ijk} = \frac{X_{ij}}{X_{ik}}
```

**Média Aritmética dos logaritmos e retransformação (Mean = GM) (p. 8):**

```latex
\overline{x_A} = \frac{1}{n} \sum_{i=1}^{n} \log_{10} x_i
```
```latex
\text{Mean} = \exp(\overline{x_A}) = GM
```

**Propriedades de simetria da distribuição log-normal sob troca de base (p. 9):**

```latex
AM(\ln(R_{ijk})) = -AM(\ln(R_{ikj})) \quad \Rightarrow \quad GM(R_{ijk}) = \frac{1}{GM(R_{ikj})}
```
```latex
STDEV(\ln(R_{ijk})) = STDEV(\ln(R_{ikj}))
```
```latex
SKEW(\ln(R_{ijk})) = -SKEW(\ln(R_{ikj}))
```
```latex
KURTOSIS(\ln(R_{jk})) = KURTOSIS(\ln(R_{kj}))
```

**Propriedade transitiva da Média Geométrica entre sistemas relativos a uma base comum (p. 9):**

```latex
GM(R_{ijl}) = \frac{GM(R_{ijk})}{GM(R_{ilk})}
```

> ⚠️ **Nota:** As fórmulas de **Média Aritmética simples** e de **Desvio Padrão Amostral**
> exigidas pela diretriz geral do projeto (Seção 5 das instruções gerais) **não constam
> explicitamente no artigo de Mashey** com essa notação elementar — o autor assume que o
> leitor já conhece essas fórmulas clássicas (referenciando Jain [5] e Lilja [6] para a base
> teórica). Portanto, **a inclusão das fórmulas de AM e Desvio Padrão Amostral no `main.tex`
> deve ser feita citando Jain (1991) ou Lilja (2000)** — as referências bibliográficas
> primárias indicadas pelo próprio Mashey (2004, p. 6) — e não diretamente este artigo.
> Solicito ao grupo que confirme se desejam que eu localize essas referências (Jain, 1991;
> Lilja, 2000) para fichamento complementar, já que não foram anexadas ao projeto até o momento.

### 4.2 Sugestão de Gráficos/Tabelas Correspondentes

- **Tabela de Estatísticas Descritivas por Máquina:** seguindo o modelo das Tabelas 8 e 9 do artigo (p. 11), o grupo pode montar uma tabela no `main.tex` com colunas: Máquina | Mediana | Média Aritmética | Desvio Padrão | Skew | Kurtose — calculadas sobre as 20 rodadas de `Single_Core` e `Multi_Core` de cada arquivo `scores_maq*.txt`. Isso permite identificar, à semelhança do autor, se alguma máquina apresenta Skew/Kurtose anômalos (indício de outliers ou throttling).

- **Histograma de Frequência das Rodadas (Figura/Tabela 10 do artigo, p. 12):** o grupo pode gerar, em Matplotlib, um histograma de frequência dos 20 valores de `Single_Core` (e separadamente `Multi_Core`) por máquina, com bins definidos por Média ± k·Desvio Padrão, replicando a lógica visual do autor para verificar aderência a uma distribuição aproximadamente normal/log-normal nas 20 repetições.

- **Gráfico de Hastes de Erro (Error Bars) por Máquina:** barplot de Média de score (Single_Core e Multi_Core) por máquina, com hastes de erro = Desvio Padrão Amostral das 20 rodadas — aplicação direta da recomendação do autor (Seção 6.4, p. 7) de sempre acompanhar a média de uma medida de dispersão, em tons de cinza/preto e branco conforme padrão visual sóbrio da SBC.

- **Cruzamento com Telemetria (extensão proposta pelo grupo, não constante no artigo original):** para rodadas que se revelarem outliers (Skew elevado) na análise dos scores, sugere-se sobrepor, no texto da Discussão, os valores médios de `CPU Inteira (°C)` e `Estrangulamento térmico do núcleo (avg) (Yes/No)` extraídos do arquivo `.CSV` correspondente àquela rodada específica, conectando a teoria estatística de Mashey (outliers) à causa arquitetural real (throttling térmico).

---

*Fichamento concluído. Arquivo pronto para inclusão no repositório do projeto.*
*Referência BibTeX: `mashey:04` — inserir no `sbc-template.bib` e citar com `\cite{mashey:04}`.*
