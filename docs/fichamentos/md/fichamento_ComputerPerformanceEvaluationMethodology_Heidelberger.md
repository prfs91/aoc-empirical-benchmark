# Fichamento Científico — Padrão SBC/AOC-UFPA
**Arquivo:** `fichamento_ComputerPerformanceEvaluationMethodology_Heidelberger.md`
**Gerado por:** Claude (co-autor do projeto AOC — UFPA Campus Tucuruí)
**Data de geração:** 16 de junho de 2026

---

## ✅ VEREDITO DE RELEVÂNCIA

**O artigo SERÁ ÚTIL para o nosso projeto de AOC? SIM — ALTAMENTE RELEVANTE.**

Justificativa: O artigo de Heidelberger e Lavenberg (1984) é a referência seminal sobre metodologia de avaliação de desempenho computacional. Ele fundamenta diretamente: (1) o uso de **benchmarks sintéticos** (como o Geekbench 6) como instrumentos de medição controlada; (2) os **métodos estatísticos** para análise de dados empíricos, incluindo médias amostrais, variância, intervalos de confiança e o problema da autocorrelação entre rodadas repetidas — base teórica para justificar nosso uso de Desvio Padrão entre as 20 rodadas; (3) o conceito de **monitoramento híbrido de hardware e software** (o HWiNFO64 é exatamente um monitor híbrido no sentido dos autores); (4) a análise de **gargalos de subsistemas de I/O, CPU e memória**, núcleo da nossa discussão arquitetural comparativa. É uma referência com alta citabilidade, publicada em periódico IEEE de alto impacto, que confere rigor científico à metodologia do artigo.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC (para `\begin{thebibliography}` no `main.tex`):**

> HEIDELBERGER, P.; LAVENBERG, S. S. Computer Performance Evaluation Methodology. **IEEE Transactions on Computers**, v. C-33, n. 12, p. 1195–1220, dez. 1984.

- **Código BibTeX Completo (.bib) — para inserir no `sbc-template.bib`:**

```bibtex
@Article{heidelberger:84,
  author    = {Philip Heidelberger and Stephen S. Lavenberg},
  title     = {Computer Performance Evaluation Methodology},
  journal   = {{IEEE} Transactions on Computers},
  year      = {1984},
  volume    = {C-33},
  number    = {12},
  pages     = {1195--1220},
  month     = dec,
  doi       = {10.1109/TC.1984.1676408},
  issn      = {0018-9340},
  publisher = {{IEEE}},
  note      = {Invited Paper. Authorized licensed use limited to:
               {UNIVERSIDADE} {FEDERAL} {DO} {PARA}.}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo de Periódico Científico de Alto Impacto (Invited Paper)
- **Periódico/Editora:** IEEE Transactions on Computers — Vol. C-33, No. 12, Dezembro de 1984
- **Instituição dos Autores:** IBM T. J. Watson Research Center, Yorktown Heights, NY, EUA
- **Autores:**
  - Philip Heidelberger (Member, IEEE)
  - Stephen S. Lavenberg (Member, IEEE)
- **Palavras-Chave Originais (Index Terms):** *computer performance measurement; computer performance modeling; computer workload characterization; discrete event simulation; queueing networks*
- **Resumo do Escopo Geral:**
  O artigo faz um levantamento panorâmico dos principais métodos quantitativos usados na avaliação de desempenho computacional, com foco nos desenvolvimentos ocorridos após 1970. Os autores organizam o campo em três grandes áreas: (1) **medição de desempenho** (*performance measurement*), que trata da instrumentação real de sistemas em execução; (2) **modelagem analítica de desempenho** (*analytic performance modeling*), com foco em redes de filas (*queueing networks*) e algoritmos de forma produto; e (3) **modelagem por simulação** (*simulation performance modeling*), incluindo simulação dirigida por traço e simulação discreta estocástica. O trabalho enfatiza que a avaliação de desempenho é necessária em todo o ciclo de vida de um sistema computacional — desde o projeto até a operação e o planejamento de capacidade — e discute em profundidade os aspectos estatísticos, como o tratamento de autocorrelação nos dados, a geração de intervalos de confiança e o controle do comprimento das rodadas de simulação.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 — Avaliação Quantitativa de Desempenho e o Ciclo de Vida do Sistema

- **Conceito/Teoria:** Necessidade da avaliação quantitativa de desempenho ao longo de todo o ciclo de vida de um sistema computacional.

- **Citação Direta (Ipsis Litteris):**
  > "Performance is one of the key factors that needs to be taken into account in the design, development, configuration, and tuning of a computer system. Hence, the quantitative evaluation of computer performance is required during the entire life cycle of a system." (p. 1195)

- **Paráfrase (Citação Indireta Acadêmica):**
  O desempenho constitui um dos fatores centrais a ser considerado nas etapas de projeto, desenvolvimento, configuração e ajuste de qualquer sistema computacional; por conseguinte, a avaliação quantitativa de desempenho torna-se uma exigência que permeia integralmente o ciclo de vida do sistema \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Introdução** — justifica a importância do benchmarking sistemático e experimental que nosso grupo conduziu.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Esta afirmação é de natureza conceitual e metodológica; não mapeia diretamente para colunas de CSV.
  - Ela justifica a existência dos arquivos `scores_maqA.txt` a `scores_maqD.txt` (colunas `Single_Core` e `Multi_Core`) como registros quantitativos de desempenho ao longo de 20 rodadas repetidas.

---

### 3.2 — Benchmarks Sintéticos como Instrumento de Medição Controlada

- **Conceito/Teoria:** Uso de benchmarks sintéticos (cargas de trabalho executáveis artificiais) em ambientes controlados para medição de desempenho pelos fabricantes e pesquisadores.

- **Citação Direta (Ipsis Litteris):**
  > "Computer manufacturers typically measure performance in a controlled environment using benchmarks which may be real workloads or synthetic executable workloads." (p. 1196)

- **Paráfrase (Citação Indireta Acadêmica):**
  Fabricantes e pesquisadores tradicionalmente mensuram o desempenho computacional em ambientes controlados, recorrendo a benchmarks que podem ser cargas de trabalho reais ou cargas de trabalho executáveis de natureza sintética \cite{heidelberger:84}. O Geekbench 6, utilizado neste trabalho, classifica-se nesta última categoria: um benchmark sintético padronizado que submete o processador a tarefas de carga controlada e reproducível.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (seção sobre Benchmarks e Métricas de Desempenho) e **Metodologia** (justificativa da escolha do Geekbench 6).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Arquivos: `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqC.txt`, `scores_maqD.txt`
  - Colunas relevantes: `Single_Core` (score de núcleo único) e `Multi_Core` (score multinúcleo) — estes scores são os resultados diretos da carga sintética do Geekbench 6.

---

### 3.3 — Flutuação Aleatória nos Dados de Medição e o Problema da Variabilidade

- **Conceito/Teoria:** Natureza aleatória das medições de desempenho — mesmo rodadas repetidas em condições idênticas produzem resultados distintos devido a fatores incontroláveis.

- **Citação Direta (Ipsis Litteris):**
  > "Random fluctuations are often present in performance measurement data. [...] repetitions of a measurement session can yield nonidentical data due to factors that are uncontrollable or too difficult to control from session to session. Such data can also be considered to fluctuate randomly." (p. 1200)

- **Paráfrase (Citação Indireta Acadêmica):**
  Flutuações aleatórias são fenômeno recorrente nos dados de medição de desempenho computacional. Mesmo quando as sessões de medição são repetidas em condições nominalmente idênticas, os dados coletados tendem a apresentar variação entre si em razão de fatores difíceis ou impossíveis de controlar entre uma sessão e outra \cite{heidelberger:84}. Esta característica implica que qualquer estimativa derivada — como a média dos scores ou dos clocks — deve ser tratada como variável aleatória, e não como valor determinístico.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (seção de Análise Estatística) e **Resultados e Discussão** (justificativa para o uso do Desvio Padrão Amostral nas barras de erro dos gráficos).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Arquivos: `scores_maq*.txt` — colunas `Single_Core` e `Multi_Core` (as 20 rodadas por máquina evidenciam esta flutuação).
  - CSVs de telemetria: `maq*_rodada_*.CSV` — colunas:
    - `Relógios efetivos núcleo (avg) (MHz)` — variação de clock entre rodadas revela instabilidade de Turbo Boost.
    - `CPU Inteira (°C)` e `Núcleo máximo (°C)` — variação térmica é causa direta de flutuação de desempenho.
    - `Potência total da CPU (W)` — oscilação de potência reflete variação de carga e limites de TDP dinâmicos.
  - **Interpretação Arquitetural:** Um Desvio Padrão elevado nos scores da Máquina D (HD SATA + Single Channel + i5-8265U com TDP-up de 15W) seria coerente com esta teoria, pois o gargalo de armazenamento (HD SATA) varia o tempo de carregamento do benchmark, e a gestão de energia (PL1/PL2) introduz variações de clock que se manifestam como ruído estatístico nas 20 rodadas.

---

### 3.4 — Média Amostral como Estimador de Desempenho em Regime Estacionário

- **Conceito/Teoria:** Uso da média amostral como estimador pontual do desempenho em regime estacionário, com sua definição formal.

- **Citação Direta (Ipsis Litteris):**
  > "The usual estimate for μ is the sample average: $\hat{\mu} = (1/N) \sum_{n=1}^{N} X_n$." (p. 1214)

- **Paráfrase (Citação Indireta Acadêmica):**
  O estimador mais comum para a característica de desempenho em regime estacionário μ é a média aritmética amostral, definida como a soma das N observações dividida pelo total de amostras \cite{heidelberger:84}. Em nosso trabalho, esta fórmula foi aplicada sobre as 20 rodadas de cada máquina para calcular os scores médios e os valores médios de telemetria.

- **Fórmula LaTeX correspondente:**
  ```latex
  \begin{equation}
      \bar{X} = \hat{\mu} = \frac{1}{N} \sum_{n=1}^{N} X_n
      \label{eq:media_amostral}
  \end{equation}
  ```

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — seção de Análise Estatística, logo antes da fórmula do Desvio Padrão Amostral.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Aplicada sobre: `Single_Core` e `Multi_Core` dos arquivos `scores_maq*.txt` (N = 20 rodadas).
  - Aplicada também sobre todas as colunas críticas dos CSVs de telemetria ao longo da duração de cada rodada (média temporal por rodada → depois média das 20 rodadas).

---

### 3.5 — Variância de Observações Correlacionadas e o Fator de Expansão

- **Conceito/Teoria:** A variância de estimativas derivadas de sequências autocorrelacionadas é superior à variância de sequências independentes — o chamado "fator de expansão".

- **Citação Direta (Ipsis Litteris):**
  > "For large sample sizes, the correct expression for the variance of correlated observations is: $\sigma^2(\hat{\mu}) \approx (\sigma^2(X)/(N - N_0)) \left(\sum_{k=-\infty}^{\infty} \rho_k\right)$, where $\rho_k$ is the autocorrelation between $X_n$ and $X_{n+k}$." (p. 1214)

- **Paráfrase (Citação Indireta Acadêmica):**
  Quando as observações de uma sequência de medições não são independentes entre si — como ocorre em sistemas com inércia térmica, onde a temperatura de uma rodada afeta a seguinte —, a variância do estimador de desempenho é sistematicamente subestimada se calculada pelos métodos clássicos para amostras independentes. A expressão correta incorpora um fator de expansão dado pela soma da função de autocorrelação, que pode ser consideravelmente maior que a unidade \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — como nota técnica na seção de análise estatística, justificando por que as 20 rodadas foram executadas com o sistema em estado inicial controlado (temperatura ambiente) entre cada rodada, para minimizar a autocorrelação.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - CSVs de telemetria: coluna `CPU Inteira (°C)` e `Núcleo máximo (°C)` — se a temperatura no início de cada rodada não tiver sido resetada, as rodadas consecutivas serão autocorrelacionadas termicamente.
  - Coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)` — se houver throttling na rodada N, ele tende a persistir nas rodadas N+1 e N+2, gerando autocorrelação.
  - **Interpretação Arquitetural:** Para a Máquina D (notebook com dissipação de calor limitada), a autocorrelação térmica entre rodadas consecutivas é esperada, o que eleva o Desvio Padrão real além do estimado por métodos clássicos.

---

### 3.6 — Instrumentação por Software (Software Monitor) — Analogia com o HWiNFO64

- **Conceito/Teoria:** Monitores de software (*software monitors*) como instrumentos de coleta de dados de desempenho em sistemas reais, com seus trade-offs de overhead de intrusão.

- **Citação Direta (Ipsis Litteris):**
  > "Software probes are instructions added to the measured system (i.e., to the operating system or to application programs) to gather performance data. [...] Since the monitor's instructions run on the measured system and hence use system resources they alter, possibly significantly, the performance of the system." (p. 1197)

- **Paráfrase (Citação Indireta Acadêmica):**
  Monitores de software consistem em rotinas de coleta de dados inseridas no sistema operacional ou em programas de aplicação com o propósito de registrar parâmetros de desempenho em tempo real. Por executarem sobre o mesmo sistema que estão monitorando, esses monitores consomem recursos computacionais e podem, em maior ou menor grau, alterar o comportamento de desempenho que se pretende observar — fenômeno denominado interferência de intrusão (*measurement intrusion*) \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — subseção sobre ferramentas de telemetria, ao descrever o HWiNFO64 e justificar que sua interferência sobre o Geekbench é negligenciável por operar via polling do BIOS e não via interceptação de chamadas de sistema críticas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Todos os 80 arquivos CSV gerados pelo HWiNFO64 (`maq*_rodada_*.CSV`) são o produto direto de um monitor de software híbrido.
  - A frequência de amostragem do HWiNFO64 (configurada pelo grupo) determina a resolução temporal das colunas e o overhead gerado.

---

### 3.7 — Monitores Híbridos (Hardware + Software) — Maior Precisão e Flexibilidade

- **Conceito/Teoria:** Monitores híbridos combinam as vantagens de velocidade e precisão dos monitores de hardware com a flexibilidade e acesso a dados de software dos monitores de software.

- **Citação Direta (Ipsis Litteris):**
  > "It is possible to combine the advantages of hardware monitors (speed and accuracy) with those of software monitors (flexibility and easy access to software related data) by judiciously combining hardware and software probes in a so-called hybrid monitor." (p. 1197)

- **Paráfrase (Citação Indireta Acadêmica):**
  A combinação de sondas de hardware e de software em um mesmo instrumento de medição — denominado monitor híbrido — permite conciliar a precisão e a baixa latência dos monitores puramente baseados em hardware com a flexibilidade e o acesso a metadados de software característicos dos monitores de software \cite{heidelberger:84}. O HWiNFO64 opera neste paradigma: acessa registros de hardware (contadores de performance, sensores térmicos via BIOS/ACPI, interfaces SMBus) enquanto correlaciona esses dados com métricas do sistema operacional (uso de CPU por thread, estados C-states).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — descrição técnica do HWiNFO64 como instrumento de telemetria.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Exemplos de colunas acessadas via hardware (registros de CPU): `Core VIDs (avg) (V)`, `Relógios núcleo (avg) (MHz)`, `Temperaturas centrais (avg) (°C)`, `Potência total da CPU (W)`.
  - Exemplos de colunas acessadas via S.O. / interface de software: `Uso total da CPU (%)`, `Carga da memória física (%)`, `Atividade total (%)` (disco).

---

### 3.8 — Caracterização da Carga de Trabalho (*Workload Characterization*)

- **Conceito/Teoria:** A caracterização quantitativa da demanda por recursos de hardware e software de uma carga de trabalho é parte fundamental de qualquer estudo de avaliação de desempenho.

- **Citação Direta (Ipsis Litteris):**
  > "The performance of a system obviously depends heavily on the demand for hardware and (application and system) software resources of the workload being processed. Therefore, the quantitative characterization of the resource demands of workloads is an important part of computer performance evaluation studies." (p. 1198)

- **Paráfrase (Citação Indireta Acadêmica):**
  O desempenho de um sistema computacional é fortemente determinado pela demanda que a carga de trabalho exercício sobre os recursos de hardware e software disponíveis. Por esta razão, a caracterização quantitativa dos recursos demandados pela carga de trabalho constitui etapa indispensável em qualquer estudo sério de avaliação de desempenho \cite{heidelberger:84}. Em nosso experimento, o Geekbench 6 impõe uma carga de trabalho sintética padronizada, enquanto o HWiNFO64 quantifica a demanda real que essa carga gera sobre CPU, memória, GPU e armazenamento.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificativa para o uso conjunto do Geekbench 6 (carga) e do HWiNFO64 (telemetria de recursos).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Demanda de CPU: `Uso total da CPU (%)`, `Utilização total da CPU (%)`, `Core 0–3 T0/T1 Uso (%)`
  - Demanda de memória: `Carga da memória física (%)`, `Memória física utilizada (MB)`
  - Demanda de GPU: `Carga do núcleo da GPU (%)`, `Uso de memória GPU (%)`
  - Demanda de armazenamento: `Atividade total (%)`, `Taxa de leituras (MB/s)`, `Taxa de gravações (MB/s)`

---

### 3.9 — Gargalos de Subsistema de I/O e a Hierarquia de Memória

- **Conceito/Teoria:** O subsistema de I/O tornou-se fator dominante no desempenho global de sistemas computacionais, dado o gap crescente entre a velocidade dos processadores e o tempo de acesso dos dispositivos de armazenamento mecânicos.

- **Citação Direta (Ipsis Litteris):**
  > "Because of the vast difference between I/O access times and main memory access times, I/O subsystem performance has become a dominant factor affecting overall system performance. This is expected to continue in the future as processors and main memories become faster whereas access times for mechanically activated disks are not expected to decline much further." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  A enorme diferença entre os tempos de acesso de dispositivos de entrada/saída e os tempos de acesso à memória principal elevou o desempenho do subsistema de I/O à condição de fator dominante no desempenho global do sistema computacional. Esta assimetria tende a se acentuar na medida em que processadores e memórias continuam evoluindo em velocidade, ao passo que dispositivos de armazenamento baseados em mecanismos mecânicos — como discos rígidos — apresentam limites físicos severos de latência que dificilmente se reduzirão de forma expressiva \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Hierarquia de Memória e Gargalos Arquiteturais. Esta citação de 1984 é notável por já prever exatamente o problema que ainda distingue a Máquina D (HD SATA) das demais.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - CSVs de telemetria: `Taxa de leituras (MB/s)`, `Taxa de gravações (MB/s)`, `Atividade de leitura (%)`, `Atividade de gravação (%)`, `Atividade total (%)`, `Leia total (MB)`, `Gravar total (MB)`
  - **Interpretação Arquitetural (Máquina D):** O HD SATA de 1TB da Máquina D, com latência mecânica típica de 5–10 ms e largura de banda sequencial de ~100–150 MB/s, representa exatamente o gargalo que os autores descrevem. O carregamento do Geekbench 6 pelo HD gera picos de `Atividade total (%)` que podem impactar os primeiros segundos de cada rodada, contribuindo para maior Desvio Padrão nos scores.

---

### 3.10 — Modelos Analíticos para Planejamento de Capacidade e Identificação de Gargalos

- **Conceito/Teoria:** Modelos analíticos de desempenho são amplamente utilizados para identificar gargalos e estimar parâmetros sensíveis ao desempenho com acurácia aceitável para fins práticos.

- **Citação Direta (Ipsis Litteris):**
  > "It is generally thought that carefully constructed analytic models can provide estimates of average job throughputs and device utilizations to within 10 percent accuracy and estimates of average response time to within 30 percent accuracy." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  Modelos analíticos de desempenho criteriosamente construídos são capazes de fornecer estimativas de throughput médio e de utilização de dispositivos com precisão de até 10%, e estimativas de tempo médio de resposta com precisão de até 30%, sendo considerados instrumentos custo-efetivos para o planejamento de capacidade e a identificação de componentes limitantes de desempenho \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — contextualizando que os scores do Geekbench 6, enquanto métricas sintéticas, são proxies de throughput e tempo de resposta que se enquadram neste nível de acurácia analítica.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Os scores `Single_Core` e `Multi_Core` dos arquivos `scores_maq*.txt` são métricas de throughput e desempenho que se correlacionam com as estimativas analíticas mencionadas.

---

### 3.11 — Simulação Dirigida por Traço (*Trace Driven Simulation*) e o Desempenho de Cache

- **Conceito/Teoria:** A simulação dirigida por traço (*trace driven simulation*) é uma técnica que utiliza sequências de eventos reais capturadas de um sistema em execução para avaliar o impacto de diferentes configurações arquiteturais (como tamanhos de cache) sobre o desempenho.

- **Citação Direta (Ipsis Litteris):**
  > "In the design of storage hierarchies, trace driven simulation has been used to study the performance effects of paging algorithms, cache management algorithms, database buffering strategies [...]. An appropriate trace, or script, is obtained by measuring a system. [...] The key performance measure of interest in such studies is usually the cache miss ratio, the fraction of references not found in the cache." (p. 1213)

- **Paráfrase (Citação Indireta Acadêmica):**
  Na análise de hierarquias de armazenamento, a simulação dirigida por traço emprega sequências de referências de memória capturadas de sistemas reais para avaliar o desempenho de diferentes algoritmos de gerenciamento de cache e de paginação. A métrica central nestes estudos é a taxa de faltas de cache (*cache miss ratio*), que expressa a fração de referências à memória não encontradas no nível de cache analisado \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Hierarquia de Memória, ao discutir o papel do Cache L3 de 6 MB da Máquina D.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Embora o HWiNFO64 não exponha diretamente a taxa de faltas de cache nos CSVs, as colunas `Relógios efetivos núcleo (avg) (MHz)` e `Relação do relógio do núcleo (avg) (x)` refletem indiretamente a eficiência de cache: clocks efetivos abaixo do clock nominal indicam stalls de memória.
  - A coluna `Carga da memória física (%)` e `Memória física utilizada (MB)` refletem a pressão sobre a hierarquia de memória durante o benchmark.

  > ⚠️ **NOTA PREDITIVA (Máquinas A, B e C):** Se alguma das Máquinas A, B ou C possuir Cache L3 maior (ex.: 8 MB, 12 MB ou superior) ou memória em configuração Dual Channel (ex.: DDR4 2666 MHz, 2 × 4 GB), a teoria de simulação por traço prevê que a taxa de faltas de cache será menor, resultando em `Relógios efetivos` mais próximos do clock nominal (menos stalls) e scores `Multi_Core` proporcionalmente maiores. **Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.**

---

### 3.12 — Intervalo de Confiança e o Problema do Transiente Inicial

- **Conceito/Teoria:** O problema do transiente inicial (*initial transient problem*) — as primeiras observações de uma sequência de medições refletem o estado transiente do sistema, não o regime estacionário, e devem ser tratadas adequadamente.

- **Citação Direta (Ipsis Litteris):**
  > "The problem of nonstationarity is that for small n, E(X_n) ≠ μ [...]. The typical approach for dealing with this problem, which is also called the problem of the initial transient, is to determine an N₀ such that E(X_n) ≈ μ for n ≥ N₀, delete the observations before N₀, and then estimate μ." (p. 1214)

- **Paráfrase (Citação Indireta Acadêmica):**
  As primeiras observações de uma sequência de medições tendem a não representar o regime estacionário do sistema, pois o sistema ainda está em transição a partir de seu estado inicial. Este fenômeno, denominado problema do transiente inicial, recomenda que um período de aquecimento (*warm-up period*) seja identificado e as observações anteriores a ele sejam descartadas antes de calcular as estimativas de desempenho \cite{heidelberger:84}.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificando por que as rodadas do Geekbench 6 foram realizadas com o sistema já inicializado e estabilizado termicamente antes do início de cada rodada.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - CSVs de telemetria: `CPU Inteira (°C)` no início de cada arquivo `maq*_rodada_*.CSV` — permite verificar se a temperatura estava estabilizada (≈ temperatura ambiente) no início de cada rodada, garantindo que não houve transiente inicial significativo.
  - `Relógios efetivos núcleo (avg) (MHz)` — os primeiros segundos de cada CSV podem mostrar o transiente de ramp-up do Turbo Boost.

---

### 3.13 — Regressão e Delineamento Estatístico de Experimentos

- **Conceito/Teoria:** O delineamento estatístico de experimentos (*statistical design of experiments*) permite estimar os efeitos de múltiplos fatores controláveis sobre as respostas medidas, variando-os simultaneamente ao invés de um por vez.

- **Citação Direta (Ipsis Litteris):**
  > "Statistical design of experiments is used to design experiments whose purpose is to estimate the effects of multiple controllable factors on measured responses. [...] A key aspect of the designs is that the factors are varied simultaneously rather than one at a time in order to facilitate estimating the effects of interactions between the factors." (p. 1201)

- **Paráfrase (Citação Indireta Acadêmica):**
  O delineamento estatístico de experimentos tem por objetivo estimar o efeito de múltiplos fatores controláveis sobre as respostas medidas de um sistema, variando-os de forma simultânea — e não sequencial — a fim de permitir a identificação de efeitos de interação entre os fatores \cite{heidelberger:84}. Em nosso experimento, os quatro fatores principais são as configurações arquiteturais distintas das Máquinas A, B, C e D; a resposta medida é o score do Geekbench 6 (Single e Multi Core), correlacionado com as métricas de telemetria do HWiNFO64.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — seção de Planejamento Experimental.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Fatores arquiteturais (variáveis independentes): configurações de hardware das quatro máquinas (processador, RAM, armazenamento, GPU).
  - Respostas (variáveis dependentes): `Single_Core`, `Multi_Core` dos arquivos `.txt`; e as colunas críticas de telemetria dos CSVs (temperatura, clock efetivo, consumo de potência, utilização de CPU).

---

### 3.14 — Simulação por Eventos Discretos e Análise Estatística de Saídas

- **Conceito/Teoria:** A simulação estocástica por eventos discretos produz saídas aleatórias que requerem análise estatística rigorosa, incluindo a geração de intervalos de confiança, para que as conclusões sejam válidas.

- **Citação Direta (Ipsis Litteris):**
  > "Because simulation outputs are random, it is important to assess the amount of variability in estimates that is due purely to random sampling effects. In addition to assessing statistical accuracy, it is important to be able to adjust the length(s) of the simulation run(s) so as to obtain estimates of specified accuracy." (p. 1214)

- **Paráfrase (Citação Indireta Acadêmica):**
  Por serem aleatórias em sua natureza, as saídas de simulações — e por extensão, de experimentos de benchmarking com componente estocástico — exigem que a variabilidade atribuível ao processo de amostragem aleatória seja quantificada com rigor estatístico. A simples apresentação de estimativas pontuais sem a correspondente medida de dispersão constitui prática metodologicamente inadequada \cite{heidelberger:84}. Em nosso trabalho, o Desvio Padrão Amostral calculado sobre as 20 rodadas cumpre esta função, sendo representado como barra de erro nos gráficos de desempenho.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificativa formal para a inclusão das barras de erro (Desvio Padrão) nos gráficos comparativos de scores e telemetria.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Aplicado sobre: `Single_Core` e `Multi_Core` dos arquivos `scores_maq*.txt` (N = 20 por máquina).
  - Aplicado sobre as médias por rodada das colunas de telemetria críticas dos CSVs.

---

### 3.15 — Arquitetura Híbrida P-Core/E-Core e o Modelo de Múltiplos Tipos de Centro de Serviço

- **Conceito/Teoria:** O artigo discute redes de filas BCMP que permitem múltiplos tipos (ou *chains*) de tarefas com diferentes demandas de serviço — um paralelo conceitual direto às arquiteturas heterogêneas de núcleo Performance (P-core) e Efficiency (E-core), nas quais cada tipo de núcleo atende a uma classe distinta de carga de trabalho com taxas de serviço diferentes.

- **Citação Direta (Ipsis Litteris):**
  > "Baskett, Chandy, Muntz, and Palacios-Gomez [11] greatly extended the class of product form networks. Their generalization allowed for the following. 1) Multiple types, or chains, of jobs. Jobs in different chains can have different routing probabilities and different service demand distributions." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  A generalização das redes de filas de forma produto introduzida por Baskett, Chandy, Muntz e Palacios-Gomez permite a coexistência de múltiplos tipos de tarefas, cada qual com taxas de serviço e demandas de processamento distintas dentro do mesmo sistema \cite{heidelberger:84}. Esta abstração teórica é diretamente aplicável à descrição de microarquiteturas híbridas modernas, nas quais núcleos de desempenho (P-cores) e núcleos de eficiência (E-cores) operam como "centros de serviço" com taxas de atendimento (clock e IPC) distintas para a mesma carga de trabalho, exigindo do escalonador do sistema operacional uma política de roteamento de tarefas (*thread director*) análoga ao roteamento probabilístico entre centros descrito no modelo BCMP.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Paralelismo a Nível de Instrução e Thread, ao introduzir o conceito de núcleos heterogêneos.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - CSVs de telemetria: colunas `Core 0–3 T0/T1 Uso (%)` e `Core 0–3 T0/T1 Utilização (%)` — permitem observar a distribuição desigual de carga entre núcleos quando há heterogeneidade.
  - `Relógios núcleo (avg) (MHz)` por núcleo individual — evidencia clocks distintos entre núcleos P e E durante a mesma rodada.

- **Justificativa de Uso (Componente da Tabela):** Esta citação aplica-se diretamente às **Máquinas A (Intel Core i5-13420H, 4P+4E), B (Intel Core i5-1334U, 2P+8E) e F (Intel Core i5-14600KF, 6P+8E)**, todas com arquitetura híbrida Raptor Lake. Estas três máquinas constituem o conjunto ideal para uma discussão comparativa sobre escalonamento heterogêneo: a Máquina F, com 14 núcleos (6P+8E) e clock de boost de 5.3 GHz nos P-cores, deve apresentar o maior score `Multi_Core` do grupo, ao passo que a Máquina B, apesar de possuir 10 núcleos físicos, opera sob um TDP de apenas 15 W, o que — segundo a teoria de roteamento do BCMP — implica que o escalonador deverá direcionar preferencialmente a carga para os E-cores (mais eficientes energeticamente) em detrimento do throughput bruto.

---

### 3.16 — Velocidade de Clock, Litografia e o Modelo de Taxa de Serviço Variável (Queue-Length Dependent Rate)

- **Conceito/Teoria:** O artigo descreve centros de serviço com taxa de atendimento dependente do estado (*queue length dependent rate*), em que a taxa $\mu_i(n)$ varia conforme a carga instantânea do sistema — análogo direto ao comportamento do Turbo Boost/Precision Boost, em que o clock do processador aumenta ou diminui dinamicamente conforme a carga térmica e elétrica instantânea.

- **Citação Direta (Ipsis Litteris):**
  > "Let $\mu_i(n)$ be the service rate at center i when there are n jobs at center i." (p. 1204)

- **Paráfrase (Citação Indireta Acadêmica):**
  Em redes de filas mais gerais, a taxa de atendimento de um centro de serviço pode ser definida como uma função do número de tarefas presentes naquele centro, e não como uma constante fixa \cite{heidelberger:84}. Esta formulação de taxa de serviço dependente do estado encontra correspondência direta nos mecanismos modernos de *boost* dinâmico de frequência (Intel Turbo Boost, AMD Precision Boost), em que a "taxa de atendimento" do núcleo — isto é, seu clock efetivo — varia em função da carga de trabalho, da temperatura e do número de núcleos ativos simultaneamente.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Métricas de Desempenho e Clock de Processamento, ao explicar a diferença entre clock base e clock de boost.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `Relógios núcleo (avg) (MHz)`, `Relógios efetivos núcleo (avg) (MHz)` — capturam a variação dinâmica do clock conforme a carga.
  - `Core C0 Ocupação (avg) (%)` — taxa de ocupação ativa dos núcleos, análoga ao número de tarefas no centro de serviço.

- **Justificativa de Uso (Componente da Tabela):** Esta teoria sustenta a comparação entre as máquinas com maior razão Boost/Base, evidenciando o salto dinâmico de clock. Destacam-se: **Máquina B (Intel i5-1334U)**, com clock base de apenas 1.30 GHz e boost de 4.60 GHz (razão de 3.54×, a maior do grupo), evidenciando um sistema fortemente dependente do estado de boost para entregar desempenho, mas igualmente vulnerável a quedas de clock sob sustentação térmica prolongada (TDP de apenas 15 W); e a **Máquina F (Intel i5-14600KF)**, cujos P-cores atingem 5.3 GHz sob um TDP de 125 W, configurando o cenário com maior margem elétrica para sustentar o boost de forma contínua, devendo apresentar o menor Desvio Padrão relativo nos scores Multi-Core do grupo.

---

### 3.17 — Litografia, Densidade de Integração e a Eficiência Microarquitetural (Desempenho por Watt)

- **Conceito/Teoria:** A discussão dos autores sobre o ciclo de vida do sistema e a necessidade de avaliação contínua de desempenho conforme a tecnologia avança serve de base para abordar como diferentes processos de fabricação (litografias) impactam a eficiência energética e o desempenho por Watt entregue.

- **Citação Direta (Ipsis Litteris):**
  > "Distributed processing systems will become commonplace. [...] High levels of performance will be key. Performance needs to be designed into these systems, not only in determining the number of devices and their speeds, but also in designing operating system algorithms to dynamically manage the system." (p. 1212)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores argumentam que o desempenho de sistemas computacionais deve ser projetado de forma holística, considerando não apenas a velocidade nominal dos dispositivos, mas também os algoritmos de gerenciamento dinâmico que otimizam a operação do sistema \cite{heidelberger:84}. Esta perspectiva é diretamente aplicável à evolução das litografias de fabricação de semicondutores: processos mais avançados (como o Intel 7 de 7 nm-classe ou o TSMC N7 de 7 nm) permitem maior densidade de transistores por área, reduzindo a tensão necessária para operação e, consequentemente, elevando a eficiência energética — métrica capturada pela razão entre o score de desempenho e a potência total consumida.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Eficiência Microarquitetural (Desempenho por Watt) e **Resultados e Discussão** — comparação entre litografias.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `Potência total da CPU (W)` — usada no denominador do cálculo de Desempenho por Watt: $\text{Score} / \overline{P_{CPU}}$.
  - `Multi_Core` (dos arquivos `.txt`) — usado no numerador.

- **Justificativa de Uso (Componente da Tabela):** Esta análise é particularmente rica quando comparamos litografias distintas presentes no grupo: **Máquina C (AMD Ryzen 5 3500U, Zen+/12 nm)** representa o processo mais antigo e menos denso do conjunto; **Máquina E (AMD Ryzen 5 5500, Zen 3/7 nm)** representa um salto de duas gerações de litografia da AMD; e **Máquinas A, B e F (Intel Raptor Lake-H/P, "Intel 7")** representam o processo Intel mais refinado disponível no grupo. Espera-se, segundo a teoria de eficiência microarquitetural, que a Máquina E (7 nm, TDP 65 W, 6 núcleos) entregue um Desempenho por Watt superior à Máquina C (12 nm, TDP 15 W, mas IPC por núcleo inferior), demonstrando que a litografia mais avançada compensa o TDP nominal mais alto através de maior eficiência por instrução executada.

---

### 3.18 — Cache L3 como Mitigador do Gargalo de Von Neumann em Sistemas com Múltiplos Núcleos

- **Conceito/Teoria:** A discussão dos autores sobre a hierarquia de memória e o papel do cache como amortecedor entre a velocidade do processador e a velocidade da memória principal — diretamente relevante para avaliar como caches L3 de tamanhos distintos mitigam de forma desigual o gargalo de Von Neumann em sistemas multinúcleo.

- **Citação Direta (Ipsis Litteris):**
  > "Memory hierarchies have been constructed to mask this speed difference and I/O subsystems have been constructed to get the best possible performance out of the memory hierarchy." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  As hierarquias de memória foram concebidas precisamente para mascarar a disparidade de velocidade entre o processador e os níveis inferiores de armazenamento, e os subsistemas de entrada e saída são projetados de modo a extrair o melhor desempenho possível dessa hierarquia \cite{heidelberger:84}. Em arquiteturas multinúcleo modernas, o cache L3 compartilhado desempenha exatamente esta função de amortecimento entre os núcleos individuais e a memória principal, sendo tanto maior sua eficácia quanto maior for sua capacidade total e quanto mais núcleos compartilharem o mesmo espaço de cache.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Hierarquia de Memória, ampliando a discussão já fichada na seção 3.11 deste documento.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `Relógios efetivos núcleo (avg) (MHz)` confrontado com `Relógios núcleo (avg) (MHz)` — a proporção entre ambos indica a frequência de *stalls* por falta de dados em cache.
  - `Ring/LLC Relógio (MHz)` — clock do barramento em anel que interliga os núcleos ao cache L3 compartilhado (Intel); impacta diretamente a latência de acesso ao último nível de cache.

- **Justificativa de Uso (Componente da Tabela):** A tabela evidencia uma progressão clara de capacidades de Cache L3: **Máquina C (4 MB)** < **Máquina D (6 MB)** < **Máquinas A e B (12 MB)** < **Máquina E (16 MB)** < **Máquina F (24 MB)**. Esta progressão permite testar empiricamente a teoria de amortecimento de hierarquia de memória: espera-se que, ao normalizar pelo número de núcleos, a razão MB de Cache L3/núcleo seja o indicador mais relevante — a Máquina F (24 MB / 14 núcleos ≈ 1.71 MB/núcleo) e a Máquina C (4 MB / 4 núcleos = 1.0 MB/núcleo) tornam-se comparáveis nesta métrica normalizada, ainda que a Máquina F possua 6× mais cache em termos absolutos, permitindo uma discussão refinada sobre se o ganho de desempenho da Máquina F provém majoritariamente do cache absoluto ou da arquitetura/litografia superior.

---

### 3.19 — Largura de Banda do Barramento PCIe e o Gargalo de Comunicação Processador–GPU

- **Conceito/Teoria:** O artigo discute, no contexto do modelo de interconexão de memória para multiprocessadores (Goyal e Agerwala, citado pelos autores), a contenção por barramentos de transferência (*transfer buses*) entre módulos de memória compartilhada — modelo diretamente análogo à largura de banda do barramento PCIe que interconecta a CPU à GPU dedicada.

- **Citação Direta (Ipsis Litteris):**
  > "Contention occurs for both the modules of the shared memory and for transfer buses between the shared and local memories. [...] The purpose of the model is to determine the bus bandwidth required to support the processors at a reasonable performance level." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  Em arquiteturas com memória compartilhada distribuída, a contenção ocorre tanto no acesso aos módulos de memória quanto nos barramentos físicos responsáveis pela transferência de dados entre os níveis de memória; o objetivo de tais modelos é determinar a largura de banda mínima necessária para sustentar um nível de desempenho aceitável \cite{heidelberger:84}. Este princípio aplica-se diretamente à interface PCIe que conecta a CPU à GPU dedicada: gerações distintas do barramento (PCIe 3.0 versus PCIe 4.0) e larguras distintas de enlace (x4 versus x8) determinam a banda disponível para transferência de texturas, buffers e dados de computação entre a memória do sistema e a memória de vídeo, podendo constituir gargalo em cargas intensivas de GPU.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Gargalos de Arquitetura, como extensão da discussão sobre o gargalo de Von Neumann para o subsistema gráfico.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `Velocidade do link PCIe (GT/s)` — taxa de transferência efetiva do barramento.
  - `Carga do barramento GPU (%)` — utilização do barramento PCIe pela GPU.
  - `Memória dedicada D3D GPU (MB)` e `Memória dinâmica D3D GPU (MB)` — indicam se a GPU está recorrendo à memória do sistema via PCIe (sinal de gargalo de VRAM).

- **Justificativa de Uso (Componente da Tabela):** Esta teoria é diretamente aplicável às máquinas com GPU dedicada: **Máquina A (RTX 4050, PCIe 4.0 x8)**, **Máquina D (MX130, PCIe 3.0 x4)**, **Máquina E (RX 7600, PCIe 4.0 x8)** e **Máquina F (RTX 3050 8GB, PCIe 4.0 x8)**. A Máquina D apresenta a configuração de barramento mais restritiva do grupo (PCIe 3.0 x4, aproximadamente um quarto da banda teórica disponível na Máquina A), o que, segundo a teoria de contenção de barramento de transferência, deve ser considerado ao interpretar eventuais limitações de desempenho gráfico da MX130 — embora, dado o escopo do benchmark Geekbench 6 (predominantemente CPU-bound, com componente OpenCL/Vulkan limitado), o impacto prático desta restrição de barramento sobre os scores gerais deve ser discutido com cautela e delimitado ao sub-score de GPU Compute, se aplicável.

---

### 3.20 — Capacidade e Topologia de Memória RAM como Fator de Roteamento de Acesso (Multi-Channel)

- **Conceito/Teoria:** O artigo discute o número de módulos de memória e barramentos como parâmetros centrais do modelo de interconexão (Seção III-A.3, *Preliminary Design Aid*), nos quais o número de "rotas" físicas de acesso à memória determina o grau de paralelismo de acesso possível — fundamento teórico direto para a distinção entre topologias Single Channel e Dual Channel de memória RAM.

- **Citação Direta (Ipsis Litteris):**
  > "The system is parameterized by the numbers of processors, memory modules, and buses, the memory access and bus transfer times, and the page fault rate." (p. 1203)

- **Paráfrase (Citação Indireta Acadêmica):**
  Em modelos analíticos de subsistemas de memória, os parâmetros centrais que determinam o desempenho global incluem o número de módulos de memória disponíveis e o número de barramentos físicos de acesso \cite{heidelberger:84}. Por analogia direta, a topologia de canal único (*Single Channel*) restringe o acesso à memória RAM a um único barramento de 64 bits, ao passo que a topologia de canal duplo (*Dual Channel*) disponibiliza dois barramentos independentes operando em paralelo, dobrando teoricamente a largura de banda agregada de acesso à memória principal — fator crítico de mitigação do gargalo de Von Neumann.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — seção sobre Gargalos de Arquitetura (Impacto do Gargalo de Von Neumann), como complemento direto à discussão Single-Channel vs. Dual-Channel já prevista no escopo teórico do projeto.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `Relógio da memória (MHz)` e `Relação do relógio da memória (x)` — clock efetivo do barramento de memória.
  - `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)` (quando aplicável à RAM em sistemas com telemetria estendida) — proxy de banda agregada.
  - `Tcas (T)`, `Trcd (T)`, `Trp (T)`, `Tras (T)`, `Trc (T)`, `Trfc (T)` — temporizações (*timings*) da memória, que em conjunto com o clock determinam a latência efetiva de acesso.

- **Justificativa de Uso (Componente da Tabela):** A tabela apresenta uma divisão clara entre topologias: **Single Channel** — Máquina C (8 GB DDR4) e Máquina D (8 GB DDR4 2400 MHz); **Dual Channel** — Máquina A (1×8GB DDR5 5200 MT/s, *dual channel* nativo por chip), Máquina B (2×8GB DDR4 2666 MHz), Máquina E (2×8GB DDR4) e Máquina F (2×16GB DDR4 3600 MHz). Esta segmentação permite o teste direto da hipótese central do gargalo de Von Neumann proposta no escopo do projeto: comparando a Máquina D (Single Channel, 2400 MHz) com a Máquina B (Dual Channel, 2666 MHz), espera-se que a Máquina B apresente ganhos de desempenho Multi-Core superiores à razão simples de clocks (2666/2400 ≈ 1.11×), uma vez que o ganho de banda agregada por canal duplo (≈ 2×) tipicamente beneficia desproporcionalmente cargas de trabalho multithread que disputam acesso simultâneo à memória — fenômeno que o Geekbench 6 Multi-Core tende a evidenciar mais do que o Single-Core.

  > ⚠️ **NOTA PREDITIVA (Máquina C):** A tabela ainda não especifica a frequência exata da memória RAM da Máquina C (campo marcado como "[MHz]*" a ser preenchido). **Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme a frequência exata de RAM da Máquina C for preenchida pelo grupo nas próximas interações, se necessário.** O mesmo se aplica à frequência de RAM da Máquina E, também pendente de preenchimento.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 — Média Amostral (Estimador Pontual)

O artigo apresenta a fórmula formal da média amostral como estimador da característica de desempenho estacionária μ (p. 1214):

```latex
\begin{equation}
    \bar{X} = \hat{\mu} = \frac{1}{N} \sum_{n=1}^{N} X_n
    \label{eq:media_amostral}
\end{equation}
```

**Onde:** $N$ = número de rodadas (N = 20 em nosso experimento); $X_n$ = score ou métrica de telemetria da rodada $n$.

---

### 4.2 — Variância do Estimador com Correção para Correlação

O artigo apresenta a expressão da variância do estimador médio para sequências autocorrelacionadas (p. 1214):

```latex
\begin{equation}
    \sigma^2(\hat{\mu}) \approx \frac{\sigma^2(X)}{N - N_0}
    \left(\sum_{k=-\infty}^{\infty} \rho_k\right)
    \label{eq:variancia_corrigida}
\end{equation}
```

**Onde:** $\sigma^2(X)$ = variância de $X_n$; $N_0$ = observações descartadas do transiente inicial; $\rho_k$ = autocorrelação entre $X_n$ e $X_{n+k}$.

**Nota:** Em nossa análise, dado que as 20 rodadas foram executadas com resfriamento entre cada uma (minimizando autocorrelação térmica), simplificamos para o Desvio Padrão Amostral clássico:

```latex
\begin{equation}
    s = \sqrt{\frac{1}{N-1} \sum_{n=1}^{N} (X_n - \bar{X})^2}
    \label{eq:desvio_padrao_amostral}
\end{equation}
```

---

### 4.3 — Modelo Linear de Análise de Variância (ANOVA) para Dois Fatores

O artigo apresenta o modelo linear de dois fatores (p. 1201), aplicável à comparação inter-máquinas:

```latex
\begin{equation}
    y_{ij} = m + a_i + b_j + c_{ij} + \varepsilon_{ij}
    \label{eq:anova_dois_fatores}
\end{equation}
```

**Onde:** $m$ = média geral; $a_i$ = efeito principal do fator 1 (ex.: tipo de processador); $b_j$ = efeito principal do fator 2 (ex.: tipo de armazenamento); $c_{ij}$ = efeito de interação; $\varepsilon_{ij}$ = erro aleatório.

---

### 4.4 — Sugestão de Gráficos e Tabelas para o `main.tex`

**Baseado nas discussões do artigo sobre análise estatística de dados de desempenho:**

**Gráfico 1 — Barplot de Scores com Desvio Padrão (Matplotlib):**
```python
# Sugestão de implementação no script Python do projeto
import matplotlib.pyplot as plt
import numpy as np

maquinas = ['Máquina A', 'Máquina B', 'Máquina C', 'Máquina D']
medias_single = [...]  # Calculadas dos arquivos scores_maq*.txt
desvios_single = [...]  # Desvio padrão das 20 rodadas

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(maquinas))
bars = ax.bar(x, medias_single, yerr=desvios_single,
              capsize=5, color='gray', edgecolor='black',
              error_kw=dict(elinewidth=1.5, capthick=1.5))
ax.set_xlabel('Configuração de Hardware', fontsize=11)
ax.set_ylabel('Score Single-Core (Geekbench 6)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(maquinas)
ax.set_title('Comparativo de Scores Single-Core', fontsize=12)
plt.tight_layout()
plt.savefig('grafico_single_core.pdf', dpi=300, format='pdf')
```

**Tabela LaTeX sugerida — Média e Desvio Padrão dos Scores:**
```latex
\begin{table}[ht]
\caption{Médias e Desvios Padrão dos Scores do Geekbench~6 por Máquina
         (20 rodadas cada). Fonte: Dados da pesquisa (2026).}
\label{tab:scores_geekbench}
\centering
\begin{tabular}{lcccc}
\hline
\textbf{Máquina} & \textbf{SC Médio} & \textbf{SC DP} &
                   \textbf{MC Médio} & \textbf{MC DP} \\
\hline
Máquina A & --- & --- & --- & --- \\
Máquina B & --- & --- & --- & --- \\
Máquina C & --- & --- & --- & --- \\
Máquina D & --- & --- & --- & --- \\
\hline
\multicolumn{5}{l}{\small SC = Single-Core; MC = Multi-Core; DP = Desvio Padrão.}
\end{tabular}
\end{table}
```

---

## 5. SUGESTÕES DE BUSCA NO GOOGLE ACADÊMICO

Para encontrar artigos complementares que sustentem as discussões iniciadas a partir desta referência seminal, utilize as seguintes strings de busca:

**Em Inglês (alto impacto):**
1. `"benchmark" "synthetic workload" "CPU performance" "standard deviation" methodology`
2. `"hardware monitor" "software monitor" "performance measurement" telemetry CPU`
3. `"thermal throttling" "CPU benchmark" "measurement variability" statistical`
4. `"memory hierarchy" "cache miss ratio" "benchmark performance" multicore`
5. `"performance evaluation" "confidence interval" "benchmark repeatability"`
6. `"I/O bottleneck" "HDD vs SSD" "benchmark performance" "sequential access"`
7. `"workload characterization" "Geekbench" OR "SPEC CPU" "hardware telemetry"`
8. `"sample mean" "standard deviation" "performance benchmarking" "repeated measurements"`
9. `"Von Neumann bottleneck" "memory bandwidth" "single channel" "dual channel" performance`
10. `"TDP" "power limit" "CPU throttling" "benchmark score" variability`

**Em Português (para referências nacionais/SBC):**
1. `"avaliação de desempenho" "benchmark sintético" "metodologia experimental" processador`
2. `"estrangulamento térmico" "throttling" "desempenho CPU" "desvio padrão"`
3. `"gargalo de memória" "canal único" "canal duplo" "desempenho processador"`
4. `"hierarquia de memória" "cache" "desempenho benchmark" "arquitetura multicore"`
5. `"medição de desempenho" "telemetria" "hardware" "análise estatística" computador`

---

## 6. NOTAS EDITORIAIS FINAIS

> ⚠️ **DOI Verificado:** O DOI `10.1109/TC.1984.1676408` é o identificador padrão deste artigo no IEEE Xplore. A UFPA possui licença de acesso (conforme nota de copyright na última página do documento: "Authorized licensed use limited to: UNIVERSIDADE FEDERAL DO PARA"). O acesso pode ser realizado via Portal Periódicos CAPES.

> ⚠️ **Sobre a Antiguidade da Referência:** Embora publicado em 1984, este artigo é uma referência seminal e altamente citada que fundou as bases metodológicas da área. Sua utilização no artigo é adequada e confere autoridade histórica à metodologia adotada. Recomenda-se combiná-lo com referências mais recentes (especialmente os fichamentos já existentes no projeto) para demonstrar que a abordagem metodológica do grupo está alinhada tanto com os fundamentos clássicos quanto com o estado da arte contemporâneo.

> ⚠️ **Mapeamento de Hardware Pendente (Máquinas A, B e C):** As análises preditivas marcadas com "NOTA PREDITIVA" nas seções 3.11 e outras permanecerão em standby até que as especificações completas das Máquinas A, B e C sejam fornecidas pelo grupo. Uma vez disponíveis, as colunas mapeadas permitirão validar ou refutar empiricamente as teorias de gargalo e hierarquia de memória discutidas neste fichamento.

> ⚠️ **Atualização — Expansão do Grupo de Máquinas (A a F):** A partir da tabela de hardware completa recebida, o grupo de máquinas foi expandido de 4 (A, B, C, D) para 6 configurações (A, B, C, D, E, F), incluindo agora dois desktops montados (Máquinas E e F) ao lado dos notebooks já existentes. As seções 3.15 a 3.20 deste fichamento foram acrescentadas especificamente para cobrir os novos componentes revelados nesta tabela — arquitetura híbrida P-core/E-core, litografias distintas (12 nm, 14 nm, 7 nm, "Intel 7"), barramentos PCIe de GPU em diferentes gerações/larguras, e a ampliação do espectro de capacidades de Cache L3 (de 4 MB a 24 MB) e de topologias de RAM (Single Channel e Dual Channel, incluindo DDR5). Os campos ainda marcados com `[Preencher...]*` na tabela original (frequência de RAM da Máquina C e E; tipo de armazenamento e interface da Máquina C; geração do SSD da Máquina F; modelo de gabinete das Máquinas E e F) permanecem como lacunas que devem ser preenchidas pelo grupo antes da redação final, conforme já sinalizado nas notas preditivas correspondentes acima.
