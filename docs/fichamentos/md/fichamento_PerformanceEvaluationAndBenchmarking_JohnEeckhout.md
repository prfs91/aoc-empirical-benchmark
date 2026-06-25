# FICHAMENTO CIENTÍFICO COMPLETO
## Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí
## Arquivo: `fichamento_PerformanceEvaluationAndBenchmarking_JohnEeckhout.md`

---

> **VEREDITO DE RELEVÂNCIA:** ✅ **SIM — O documento é altamente útil e estruturalmente fundamental para o projeto de AOC.**
>
> Trata-se do livro de referência *Performance Evaluation and Benchmarking* (CRC Press/Taylor & Francis, 2006), organizado por Lizy Kurian John (University of Texas at Austin) e Lieven Eeckhout (Ghent University), com capítulos escritos por especialistas de instituições como Intel, IBM, North Carolina State University e UC San Diego. O conteúdo é o tratado mais completo e sistemático disponível sobre **metodologia de avaliação de desempenho**, cobrindo exatamente os pilares teóricos exigidos pelo nosso trabalho: (1) métricas de desempenho e formas de agregação (média aritmética, geométrica e harmônica) — Capítulo 4; (2) técnicas estatísticas para análise de desempenho computacional, incluindo desvio padrão, erro padrão e intervalos de confiança — Capítulo 5; (3) o conceito de IPC (*Instructions Per Cycle*) como métrica fundamental de desempenho microarquitetural, central à nossa discussão de "IPC Relativo" — Capítulo 6; (4) a justificativa teórica do porquê rodadas repetidas de um mesmo benchmark produzem variabilidade estatística, fundamentando diretamente o uso do Desvio Padrão Amostral sobre as 20 rodadas de cada máquina. O documento fornecido corresponde majoritariamente às páginas de prefácio, corpo de contribuidores, sumário, Capítulo 1 (Introdução e Visão Geral) — texto completo — e às referências bibliográficas dos Capítulos 2 a 13, além de um trecho técnico substancial do Capítulo 6 (Statistical Sampling for Processor and Cache Simulation), que veio digitalizado de forma mais completa que os demais. Por essa razão, o fichamento abaixo concentra-se nessas duas frentes: a Introdução (panorama conceitual de toda a obra) e o Capítulo 6 (conteúdo técnico extenso sobre erro amostral, desvio padrão e IPC), com registro também da estrutura bibliográfica dos capítulos restantes para indexação futura.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC (para `\begin{thebibliography}` no `main.tex`):**

> JOHN, L. K.; EECKHOUT, L. (Ed.). **Performance Evaluation and Benchmarking**. Boca Raton: CRC Press, Taylor & Francis Group, 2006. ISBN 0-8493-3622-8.

Para citação específica do Capítulo 1 (Introdução) e do Capítulo 6 (Amostragem Estatística), que constituem o núcleo do material analisado:

> JOHN, L. K.; EECKHOUT, L. Introduction and Overview. In: JOHN, L. K.; EECKHOUT, L. (Ed.). **Performance Evaluation and Benchmarking**. Boca Raton: CRC Press, 2006. cap. 1, p. 1–4.

> CONTE, T. M.; BRYAN, P. D. Statistical Sampling for Processor and Cache Simulation. In: JOHN, L. K.; EECKHOUT, L. (Ed.). **Performance Evaluation and Benchmarking**. Boca Raton: CRC Press, 2006. cap. 6, p. 117–150 (paginação aproximada).

- **Código BibTeX Completo (.bib) — para inserir no `sbc-template.bib`:**

```bibtex
@Book{john_eeckhout:06,
  author    = {Lizy Kurian John and Lieven Eeckhout},
  title     = {Performance Evaluation and Benchmarking},
  publisher = {{CRC} Press, Taylor {\&} Francis Group},
  year      = {2006},
  address   = {Boca Raton, {FL}},
  isbn      = {0-8493-3622-8},
  note      = {Inclui contribuições de David J. Lilja, Thomas M. Conte,
               Brad Calder, Chita Das, Brinkley Sprunt, Alex Mericas
               e Kishore Menezes.}
}

@InCollection{conte_bryan:06,
  author    = {Thomas M. Conte and Paul D. Bryan},
  title     = {Statistical Sampling for Processor and Cache Simulation},
  booktitle = {Performance Evaluation and Benchmarking},
  editor    = {Lizy Kurian John and Lieven Eeckhout},
  publisher = {{CRC} Press, Taylor {\&} Francis Group},
  year      = {2006},
  address   = {Boca Raton, {FL}},
  chapter   = {6}
}

@InCollection{john_eeckhout_intro:06,
  author    = {Lizy Kurian John and Lieven Eeckhout},
  title     = {Introduction and Overview},
  booktitle = {Performance Evaluation and Benchmarking},
  editor    = {Lizy Kurian John and Lieven Eeckhout},
  publisher = {{CRC} Press, Taylor {\&} Francis Group},
  year      = {2006},
  address   = {Boca Raton, {FL}},
  chapter   = {1},
  pages     = {1--4}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Livro acadêmico organizado (*edited book*), com capítulos de autoria múltipla — referência técnica de pós-graduação em Arquitetura de Computadores.
- **Instituição/Editora:** CRC Press, Taylor & Francis Group (Boca Raton, FL, EUA), 2006.
- **Organizadoras:** Lizy Kurian John (University of Texas at Austin) e Lieven Eeckhout (Ghent University, Bélgica).
- **Contribuidores dos capítulos:** David J. Lilja (Univ. Minnesota), Thomas M. Conte (NC State University), Brad Calder (UC San Diego), Chita Das (Penn State), Brinkley Sprunt (Bucknell University), Alex Mericas (IBM), Kishore Menezes (Intel), Joshua J. Yi (Freescale), Tim Sherwood (UCSB), Greg Hamerly (Baylor), Eun Jung Kim (Texas A&M), Ki Hwan Yum (UT San Antonio), Rumi Zahir e Susith Fernando (Intel), entre outros.
- **Palavras-Chave Originais (do registro catalográfico):** *Electronic digital computers — Evaluation*.
- **Resumo do Escopo Geral:**
  O livro consolida, em treze capítulos, o estado da arte (à época de 2006) em avaliação de desempenho e benchmarking de microprocessadores. Cobre desde a medição real em hardware (*performance measurement*) até a modelagem por simulação (simulação dirigida por traço, simulação estatística, SimPoint) e a modelagem analítica. Aborda explicitamente: técnicas de medição de desempenho e monitoramento de hardware; benchmarks padronizados (SPEC, TPC, SYSmark, SPLASH); métodos de agregação de métricas (médias aritmética, geométrica e harmônica); técnicas estatísticas rigorosas para tratar ruído experimental; amostragem estatística para reduzir o custo de simulação; e arquiteturas reais de monitoramento de desempenho em hardware (Pentium 4, POWER5, Itanium). A obra é dirigida tanto a estudantes de pós-graduação em Arquitetura de Computadores quanto a arquitetos de processadores na indústria.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 — A Complexidade da Avaliação de Desempenho em Microprocessadores Modernos

- **Conceito/Teoria:** Justificativa da necessidade de avaliação de desempenho diante da complexidade dos microprocessadores contemporâneos — paralelismo, pipelining, execução fora de ordem e grandes caches on-chip tornam a tarefa de avaliação um desafio de escala massiva.

- **Citação Direta (Ipsis Litteris):**
  > "State-of-the-art, high-performance microprocessors contain hundreds of millions of transistors and operate at frequencies close to 4 gigahertz (GHz). These processors are deeply pipelined, execute instructions in out-of-order, issue multiple instructions per cycle, employ significant amounts of speculation, and embrace large on-chip caches. [...] 1 second of program execution on these processors involves several billions of instructions, and analyzing 1 second of execution may involve dealing with hundreds of gigabytes of pieces of information." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  John e Eeckhout (2006) destacam que processadores de alto desempenho contemporâneos integram centenas de milhões de transistores, operam em frequências próximas a 4 GHz e empregam técnicas de pipelining profundo, execução fora de ordem, emissão múltipla de instruções por ciclo e especulação — recursos que tornam a avaliação de desempenho uma tarefa de escala computacional massiva, já que um único segundo de execução pode envolver bilhões de instruções e centenas de gigabytes de dados de análise \cite{john_eeckhout_intro:06}.

- **Onde Encaixar no Artigo LaTeX:** **Introdução** — justifica, em um nível conceitual elevado, por que a avaliação empírica de desempenho (mesmo em escala reduzida, como a do nosso experimento com 4 máquinas e Geekbench 6) é uma tarefa metodologicamente relevante e não trivial.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Esta afirmação é de natureza introdutória/conceitual; relaciona-se indiretamente com o volume de dados produzido pelos 80 arquivos `.CSV` de telemetria (20 rodadas × 4 máquinas, com amostragem segundo a segundo), que reproduzem em escala didática o problema de "lidar com centenas de gigabytes" mencionado pelos autores, ainda que em volume proporcionalmente menor.
  - Colunas `Relógios núcleo (avg) (MHz)` e `Relógios efetivos núcleo (avg) (MHz)` ilustram empiricamente as frequências de operação próximas (ou superiores, em boost) ao valor de referência de ~4 GHz citado pelos autores.

---

### 3.2 — Dualidade entre Simulação e Medição em Hardware Real

- **Conceito/Teoria:** Contraste metodológico entre avaliação por simulação (mais barata, mas lenta e potencialmente artificial) e avaliação por medição em hardware real/prototípico (mais precisa, porém dependente da existência do sistema físico).

- **Citação Direta (Ipsis Litteris):**
  > "Usually, early design exploration is accomplished by simulation models, because building hardware prototypes of state-of-the-art microprocessors is expensive and time consuming. However, simulators are orders of magnitude slower than real hardware and simulation results are artificially sanitized [...]. Performance measurement on a prototype will be more accurate; however, a prototype needs to be available. Performance measurement is also valuable after the actual product is built, in order to understand the performance of the actual system under real-world workloads and to identify modifications that could be incorporated in future designs." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores contrastam duas abordagens complementares de avaliação de desempenho: a simulação, empregada predominantemente nas fases iniciais de projeto por seu menor custo, mas sujeita a ser ordens de grandeza mais lenta que o hardware real e a incorporar simplificações artificiais; e a medição em hardware real, mais precisa, mas que depende da existência de um protótipo físico e que se torna especialmente valiosa após a fabricação do produto, permitindo observar seu comportamento sob cargas de trabalho reais \cite{john_eeckhout_intro:06}. O presente trabalho posiciona-se integralmente na segunda categoria: trata-se de medição empírica em hardware real e comercialmente disponível (as quatro máquinas A, B, C e D), e não de simulação.

- **Onde Encaixar no Artigo LaTeX:** **Introdução** e **Metodologia** — justifica teoricamente a escolha metodológica do grupo por medição direta em hardware físico via Geekbench 6 e HWiNFO64, em vez de simulação arquitetural.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Toda a base de dados do projeto (arquivos `scores_maq*.txt` e `maq*_rodada_*.CSV`) representa medição empírica direta em hardware real, não simulação — o que deve ser explicitamente declarado na seção de Metodologia como escolha epistemológica alinhada à categoria de "performance measurement" descrita pelos autores.

---

### 3.3 — O Problema de Resumir Desempenho com um Único Número e as Médias Estatísticas

- **Conceito/Teoria:** O desafio de sintetizar o desempenho de múltiplos benchmarks em um único número, e a necessidade de escolher corretamente entre média aritmética, média geométrica e média harmônica conforme a natureza da métrica (tempo de execução vs. taxa/vazão).

- **Citação Direta (Ipsis Litteris):**
  > "Another major issue in performance evaluation is the issue of representing performance with a single number. [...] The arithmetic mean, geometric mean, and harmonic mean are three ways of finding the central tendency of a group of numbers. However, it should be noted that each of these means should be used under appropriate circumstances. For example, the arithmetic mean can be used to find average execution time from a set of execution times; the harmonic mean can be used to find the central tendency of measures that are in the form of a rate, for example, throughput." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  John e Eeckhout (2006) discutem o problema metodológico de condensar o desempenho observado em múltiplos benchmarks em um único valor representativo, apontando que a média aritmética, a média geométrica e a média harmônica constituem três medidas distintas de tendência central, cada uma apropriada a um tipo específico de métrica: a média aritmética é adequada para tempos de execução, enquanto a média harmônica é a forma correta de agregar métricas expressas como taxa (*throughput*) \cite{john_eeckhout_intro:06}. Essa distinção é central à correta interpretação dos scores do Geekbench 6, que constituem índices sintéticos (não tempos de execução brutos nem taxas puras), exigindo cautela na escolha do método de agregação entre as 20 rodadas de cada máquina.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (seção de Métricas de Desempenho) — fundamenta diretamente a discussão pedida no escopo do trabalho sobre "Tempo de execução vs. Taxa de Transferência (Vazão), MIPS, FLOPS e Scores Sintéticos", e justifica metodologicamente a escolha da média aritmética como medida central adotada no projeto (uma vez que os scores Single-Core/Multi-Core do Geekbench 6 são tratados como observações repetidas de uma mesma métrica, não como agregação heterogênea de benchmarks distintos).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Arquivos `scores_maqA.txt` a `scores_maqD.txt`, colunas `Single_Core` e `Multi_Core`: a média aritmética simples sobre as 20 rodadas é a estatística central correta a ser reportada, já que cada rodada produz uma medida pontual e homogênea (não uma agregação de benchmarks distintos como nos suítes SPEC).
  - Recomenda-se, na seção de Metodologia, justificar explicitamente por que a média aritmética (e não a geométrica ou harmônica) foi escolhida, citando esta passagem.

---

### 3.4 — Estatística como Ferramenta Indispensável para Lidar com Ruído nas Medições Reais

- **Conceito/Teoria:** A necessidade do uso de métodos estatísticos tanto para medições reais (tratamento de ruído experimental) quanto para simulação (gerenciamento do volume de dados e identificação de tendências).

- **Citação Direta (Ipsis Litteris):**
  > "Irrespective of whether real system measurement or simulation based modeling is done, computer architects should use statistical methods to make correct conclusions. For real-system measurements, statistics are needed to deal with noisy data. The noisy data comes from noise in the system being measured or is due to the measurement tools themselves." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Independentemente de a avaliação ser conduzida por medição em sistema real ou por modelagem baseada em simulação, os autores defendem que arquitetos de computadores devem recorrer a métodos estatísticos para sustentar conclusões válidas; no caso específico de medições em sistemas reais, a estatística é necessária para tratar o ruído inerente aos dados, que pode originar-se tanto do próprio sistema medido quanto das ferramentas de instrumentação empregadas \cite{john_eeckhout_intro:06}. Esta afirmação fundamenta diretamente a necessidade de reportar o Desvio Padrão Amostral, e não apenas a média, em qualquer comparação de desempenho entre as máquinas A, B, C e D.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (seção de Análise Estatística) — justificativa teórica primária para o uso do desvio padrão sobre as 20 rodadas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Toda a base de dados de telemetria (`maq*_rodada_*.CSV`) está sujeita a ruído de medição proveniente tanto do hardware monitorado (variações de carga do S.O. Windows 11 em segundo plano, gerenciamento dinâmico de energia) quanto da própria ferramenta HWiNFO64 (latência de polling, granularidade de amostragem segundo a segundo).
  - Colunas como `Uso total da CPU (%)` e `Carga da memória física (%)` são particularmente suscetíveis a ruído de processos do sistema operacional concorrentes ao benchmark, reforçando a necessidade de reportar variabilidade (desvio padrão) e não apenas médias pontuais.

---

### 3.5 — Padrão Microestrutural de Estado: Onde o Estado Reside em um Processador

- **Conceito/Teoria:** Identificação das estruturas microarquitetônicas internas que armazenam "estado" e cuja perda compromete a precisão de simulações por amostragem — diretamente análogo aos componentes monitorados pelo HWiNFO64 em hardware real.

- **Citação Direta (Ipsis Litteris):**
  > "State in a processor is kept in a number of areas including: the scheduling queues, the reorder buffer, the functional unit pipelines, the branch handling target buffer (the BTB), instruction caches, data caches, load/store queues, and control transfer instruction queues." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conte e Bryan (2006) identificam que o estado interno de um processador superescalar está distribuído por múltiplas estruturas microarquitetônicas, incluindo filas de escalonamento, o *reorder buffer*, os pipelines das unidades funcionais, o *Branch Target Buffer* (BTB), as caches de instrução e de dados, e as filas de *load/store* \cite{conte_bryan:06}. Embora o contexto original trate de simulação por amostragem (onde a perda desse estado entre clusters de instruções introduz viés), o princípio é diretamente aplicável à interpretação da telemetria coletada em hardware real: cada uma dessas estruturas físicas corresponde a métricas observáveis pelo HWiNFO64, como o estado da cache (refletido indiretamente em latência) e a taxa de utilização dos núcleos.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (seção de Hierarquia de Memória e Paralelismo a Nível de Instrução) — conecta a discussão de cache L3 (6 MB da Máquina D) à arquitetura interna real do processador.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Core 0 Uso (%)` a `Core 3 T1 Uso (%)`: refletem a ocupação das unidades funcionais e filas de escalonamento mencionadas pelos autores.
  - `maqD_rodada_*.CSV` → `Relação do relógio do núcleo (avg) (x)` e `Uncore Relação (x)`: refletem o estado do domínio *uncore*, que inclui o cache L3 compartilhado (estrutura referida pelos autores como parte do estado persistente do processador).
  - **NOTA PREDITIVA:** Se as Máquinas A, B ou C possuírem maior número de núcleos físicos/threads do que a Máquina D (4C/8T), o número de colunas `Core N TX Uso (%)` populadas no CSV será proporcionalmente maior, permitindo uma análise mais granular do paralelismo a nível de thread.

---

### 3.6 — Desvio Padrão Amostral como Medida de Precisão para Simulações Repetidas (Equação 6.8)

- **Conceito/Teoria:** Definição formal do desvio padrão amostral para um desenho de amostragem em *clusters*, aplicada à dispersão da métrica IPC entre amostras (clusters) repetidas — formalismo diretamente transponível para o desvio padrão entre as 20 rodadas do Geekbench 6.

- **Citação Direta (Ipsis Litteris):**
  > "The standard deviation for a cluster sampling design is given by, $S_{IPC} = \sqrt{\dfrac{\sum_{i=1}^{N_{cluster}}(\mu_{IPC_i} - \mu_{IPC_{sample}})^2}{N_{cluster}-1}}$ where $\mu_{IPC_i}$ is the mean IPC for the ith cluster in the sample." (Cap. 6, Eq. 6.8)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conte e Bryan (2006) definem o desvio padrão de um desenho de amostragem em *clusters* como a raiz quadrada da soma dos quadrados das diferenças entre a média de cada cluster individual e a média geral da amostra, dividida pelo número de clusters menos um — formulação que corresponde exatamente ao desvio padrão amostral clássico aplicado, no caso dos autores, à métrica IPC de cada agrupamento de instruções \cite{conte_bryan:06}. No contexto do presente projeto, cada "cluster" do estudo original corresponde a uma "rodada" do Geekbench 6: assim, a mesma fórmula é aplicada substituindo $\mu_{IPC_i}$ pelo score (Single-Core ou Multi-Core) da i-ésima rodada e $N_{cluster}$ pelas 20 rodadas executadas por máquina.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (Análise Estatística) — esta é a fórmula central a ser citada e adaptada na seção que apresenta a equação de Desvio Padrão Amostral exigida pelo escopo do trabalho.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Arquivos `scores_maq*.txt`, colunas `Single_Core` e `Multi_Core`: aplicar a Equação 6.8 (adaptada) sobre as 20 observações de cada coluna, por máquina, para obter o desvio padrão amostral dos scores.
  - Arquivos `maq*_rodada_*.CSV`: a mesma lógica estatística pode ser aplicada às médias de telemetria por rodada (ex.: a média de `CPU Inteira (°C)` dentro de cada rodada, comparada entre as 20 rodadas), tratando cada rodada como um "cluster" estatístico análogo ao do artigo original.

---

### 3.7 — Erro Padrão Estimado e Intervalo de Confiança de 95% (Equações 6.9 e Discussão)

- **Conceito/Teoria:** Cálculo do erro padrão estimado a partir de uma única simulação (sem necessidade de repetição massiva) e construção do intervalo de confiança de 95% usando a propriedade da distribuição normal (fator 1,96).

- **Citação Direta (Ipsis Litteris):**
  > "Using the properties of the normal distribution, the 95% confidence interval is given by $\mu_{IPC_{sample}} \pm 1.96\, S_{IPC} / \sqrt{N_{cluster}}$ [...]. A confidence interval of 95% implies that 95 out of 100 sample estimates may be expected to fit into this interval." (Cap. 6, Eq. 6.9 e discussão)

- **Paráfrase (Citação Indireta Acadêmica):**
  Com base nas propriedades da distribuição normal, os autores estabelecem que o intervalo de confiança de 95% para a média amostral é dado pela média somada e subtraída de 1,96 vezes o erro padrão estimado (o desvio padrão dividido pela raiz do número de clusters), interpretando-se que, em 95 de cada 100 estimativas amostrais repetidas, o valor obtido recairia dentro desse intervalo \cite{conte_bryan:06}. Os autores destacam ainda que essa precisão pode ser obtida a partir de uma única simulação (ou, no nosso caso, de um único conjunto de 20 rodadas), sem necessidade de repetir todo o experimento múltiplas vezes — o que valida estatisticamente o desenho experimental adotado pelo grupo (20 rodadas únicas por máquina, e não múltiplos conjuntos de 20 rodadas).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (Análise Estatística) — pode ser citada como complemento opcional ao desvio padrão simples, caso o grupo decida reportar intervalos de confiança além da média ± desvio padrão.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Aplicável às colunas `Single_Core` e `Multi_Core` de `scores_maq*.txt`: permite, além do desvio padrão, calcular o intervalo de confiança de 95% da média de cada máquina, reforçando o rigor estatístico da comparação A vs. B vs. C vs. D.
  - **Observação prática:** com N=20 rodadas, recomenda-se cautela ao aplicar estritamente o fator 1,96 (válido para grandes amostras/distribuição normal assintótica); para N pequeno, a literatura estatística clássica recomenda o uso da distribuição t de Student. Esta é uma simplificação reconhecida pelos próprios autores do livro, que tratam o caso assintótico.

---

### 3.8 — Variabilidade entre Médias de Clusters como Explicação da Dificuldade de Amostragem (Homogeneidade)

- **Conceito/Teoria:** A precisão de um regime de amostragem depende diretamente da homogeneidade das médias entre os clusters — benchmarks (ou, por extensão, rodadas/máquinas) com alta variação entre clusters são intrinsecamente mais difíceis de amostrar com precisão.

- **Citação Direta (Ipsis Litteris):**
  > "Note that benchmarks with small variations among cluster means [...] are conducive to accurate sampling. Benchmarks [...] that exhibit high variation in the cluster means [...] are therefore difficult to sample. It is clear that the precision of a sampling regimen depends upon the homogeneity of the cluster means." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conte e Bryan (2006) observam que benchmarks cujas médias de cluster apresentam baixa variação favorecem uma amostragem precisa, ao passo que benchmarks com alta heterogeneidade entre as médias de cluster são, por natureza, mais difíceis de amostrar com confiabilidade; os autores concluem que a precisão de qualquer regime de amostragem está diretamente condicionada à homogeneidade dos valores médios entre as unidades amostrais \cite{conte_bryan:06}. Transposto ao contexto do projeto, este princípio implica que uma máquina cujas 20 rodadas produzem scores muito heterogêneos entre si (alto desvio padrão) representa, arquiteturalmente, um sistema cujo comportamento de desempenho é instável — provável indício de fatores como throttling térmico intermitente, gerenciamento dinâmico de energia agressivo, ou interferência de I/O (HD SATA) — e não meramente "ruído estatístico" sem causa identificável.

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** — fundamenta a interpretação arquitetural de um desvio padrão elevado em qualquer das quatro máquinas, conforme exigido nas diretrizes do projeto ("Sempre valide os dados estatísticos: explique o que um desvio padrão alto em uma das máquinas significa arquiteturalmente").

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Comparação direta entre o desvio padrão das colunas `Single_Core`/`Multi_Core` (de `scores_maq*.txt`) entre as quatro máquinas: a máquina com maior desvio padrão relativo deve ser investigada quanto à causa arquitetural via cruzamento com:
    - `Estrangulamento térmico do núcleo (avg) (Yes/No)` — eventos de throttling intermitente.
    - `IA: Package-Level RAPL/PBM PL1 (Yes/No)` — ativação do limite de potência sustentado.
    - `Taxa de leituras (MB/s)` / `Taxa de gravações (MB/s)` — possível gargalo de I/O (relevante no caso do HD SATA da Máquina D).
    - `Relógios efetivos núcleo (avg) (MHz)` — variabilidade de clock entre rodadas (Turbo Boost inconsistente).

---

### 3.9 — IPC (Instructions Per Cycle) como Métrica Padrão de Desempenho Superescalar

- **Conceito/Teoria:** Definição do IPC como a métrica-padrão para avaliação de processadores superescalares, e sua limitação fundamental: o IPC é, em última instância, limitado pela taxa de emissão (*issue rate*) do processador.

- **Citação Direta (Ipsis Litteris):**
  > "The standard performance metric for superscalar processors is the IPC, measured as the number of instructions retired per execution cycle. IPC is ultimately limited by the issue rate of the processor, because flow out of the processor cannot exceed the flow in." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conte e Bryan (2006) estabelecem o IPC — número médio de instruções retiradas (concluídas) por ciclo de execução — como a métrica-padrão de avaliação de desempenho em processadores superescalares, ressaltando que essa métrica é inerentemente limitada pela taxa de emissão de instruções do processador, já que o fluxo de saída (instruções retiradas) não pode superar o fluxo de entrada (instruções emitidas/buscadas) \cite{conte_bryan:06}. Esta definição fundamenta diretamente a discussão de "IPC Relativo" proposta no escopo do projeto, ainda que nosso experimento não meça o IPC diretamente (por ausência de contadores de desempenho de hardware/PMU expostos pelo HWiNFO64), mas sim grandezas substitutas, como a relação entre clock efetivo e score obtido.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (Métricas de Desempenho e Paralelismo a Nível de Instrução) — base conceitual para a discussão de Eficiência Microarquitetural proposta no escopo ("IPC Relativo: Relógios efetivos núcleo confrontados com o score final").

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)`: variável substituta (*proxy*) de desempenho microarquitetural, já que o IPC real não é diretamente exposto pelo HWiNFO64 sem leitura de contadores de desempenho de hardware (PMCs).
  - **Proposta de "IPC Relativo" para o artigo:** definir uma métrica derivada como $\text{IPC}_{rel} = \dfrac{\text{Score Multi-Core}}{\overline{\text{Relógio efetivo médio (MHz)}}}$, que aproxima — de forma indireta — quanto desempenho (score) é obtido por unidade de frequência, isolando parcialmente o ganho proveniente de melhorias microarquiteturais (IPC genuíno) do ganho proveniente puramente de maior clock.
  - **IMPORTANTE — Limitação a declarar no artigo:** deve-se deixar explícito que este "IPC Relativo" é uma aproximação heurística baseada em score/clock, e não o IPC real medido por contadores de hardware (*Performance Monitoring Counters*), tal como descrito formalmente neste capítulo do livro. Isso evita a invenção de uma métrica com rigor que os dados disponíveis não sustentam.

---

### 3.10 — A Robustez do Desenho de Amostragem Sem Necessidade de Simulação Completa (Conclusão Empírica do Capítulo 6)

- **Conceito/Teoria:** Demonstração de que o erro padrão estimado, calculado a partir de uma única amostra, é suficiente para validar a precisão de um experimento sem a necessidade de repetir o experimento completo (validação cruzada com a "verdade" da simulação completa).

- **Citação Direta (Ipsis Litteris):**
  > "Because the full-trace simulations are available in this study, it is possible to test whether sample design using standard error achieves accurate results. The estimates [...] show relative errors of less than 2% for most benchmarks [...]. The conclusion is that a robust sampling regimen can be designed without the need for full-trace simulations." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conte e Bryan (2006) demonstram, ao comparar suas estimativas amostrais com simulações completas de referência, que os erros relativos obtidos foram inferiores a 2% para a maioria dos benchmarks testados, concluindo que um regime de amostragem estatisticamente robusto pode ser projetado e validado sem a necessidade de uma simulação exaustiva e completa \cite{conte_bryan:06}. Essa conclusão reforça, por analogia metodológica, a validade de utilizar 20 rodadas (um número finito e gerenciável de amostras) por máquina como representativas do desempenho real e estável de cada sistema, desde que o erro padrão calculado seja suficientemente pequeno.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (justificativa do número de rodadas escolhido) — apoia teoricamente a decisão de realizar 20 rodadas por máquina, em vez de um número arbitrariamente maior, desde que o desvio padrão observado seja reportado como evidência de estabilidade estatística.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Arquivos `scores_maq*.txt`: o cálculo do erro padrão (desvio padrão dividido pela raiz de N=20) sobre `Single_Core` e `Multi_Core` permite reportar, para cada máquina, o grau de confiabilidade estatística do número de rodadas escolhido pelo grupo.

---

### 3.11 — Estrutura Conceitual dos Demais Capítulos (Referência para Indexação Futura)

Como o conteúdo fornecido do livro corresponde majoritariamente às listas de referências bibliográficas dos Capítulos 2 a 13 (sem o corpo textual completo desses capítulos), este item registra, de forma sintética e sem invenção de conteúdo, os temas estruturais de cada capítulo conforme o Sumário (p. 11–12) e as listas de referências fornecidas, para uso em buscas bibliográficas futuras e eventual aprofundamento:

| Capítulo | Tema | Autor(es) | Relevância potencial para o projeto |
|---|---|---|---|
| 2 | Performance Modeling and Measurement Techniques | Lizy Kurian John | Alta — técnicas de medição via hardware (análogo ao HWiNFO64) |
| 3 | Benchmarks | Lizy Kurian John | Alta — fundamenta a escolha do Geekbench 6 frente a SPEC, TPC, SYSmark |
| 4 | Aggregating Performance Metrics Over a Benchmark Suite | Lizy Kurian John | Alta — médias aritmética/geométrica/harmônica (citado na Seção 3.3 acima) |
| 5 | Statistical Techniques for Computer Performance Analysis | David J. Lilja; Joshua J. Yi | Altíssima — técnicas estatísticas de análise de desempenho |
| 6 | Statistical Sampling for Processor and Cache Simulation | Thomas M. Conte; Paul D. Bryan | Altíssima — fichado em profundidade nas Seções 3.5 a 3.10 acima |
| 7 | SimPoint: Picking Representative Samples to Guide Simulation | Brad Calder et al. | Baixa/Moderada — foco em simulação arquitetural, não medição real |
| 8 | Statistical Simulation | Lieven Eeckhout | Baixa/Moderada — foco em simulação, não medição em hardware real |
| 9 | Benchmark Selection | Lieven Eeckhout | Moderada — metodologia de seleção de cargas representativas |
| 10 | Introduction to Analytical Models | Eun Jung Kim; Ki Hwan Yum; Chita R. Das | Baixa — modelagem analítica, fora do escopo experimental do grupo |
| 11 | Performance Monitoring Hardware and the Pentium 4 Processor | Brinkley Sprunt | Alta — arquitetura de contadores de desempenho de hardware (PMU) |
| 12 | Performance Monitoring on the POWER5™ Microprocessor | Alex Mericas | Baixa — arquitetura IBM POWER5, não aplicável às máquinas Intel do grupo |
| 13 | Performance Monitoring on the Itanium® Processor Family | Rumi Zahir; Kishore Menezes; Susith Fernando | Baixa — arquitetura Itanium, obsoleta e não aplicável ao hardware do grupo |

> ⚠️ **Nota de transparência metodológica:** os Capítulos 2, 3, 5 e 11 (marcados como Alta/Altíssima relevância na tabela) possuem forte potencial de fornecer citações adicionais valiosas para o artigo, especialmente sobre benchmarks padronizados e contadores de desempenho de hardware. Contudo, **o PDF fornecido neste anexo contém apenas as listas de referências bibliográficas desses capítulos, não o corpo textual integral**. Caso o grupo deseje citações diretas (*ipsis litteris*) desses capítulos específicos — em especial do Capítulo 5 (Lilja e Yi, técnicas estatísticas) e do Capítulo 11 (Sprunt, monitoramento de hardware no Pentium 4) — será necessário fornecer o PDF completo desses capítulos para fichamento adicional, conforme a diretriz de não invenção de dados.

---

### 3.12 — ATUALIZAÇÃO (Nova Tabela de Hardware, 6 Máquinas): Núcleos Heterogêneos e Issue Rate como Limite Teórico do IPC

> **Contexto da atualização:** com a nova tabela de hardware fornecida, o grupo passou a documentar processadores de arquitetura **híbrida/heterogênea** (núcleos de performance — P-cores — e núcleos de eficiência — E-cores), presentes na Máquina A (i5-13420H, 4P+4E), na Máquina B (i5-1334U, 2P+8E) e na Máquina F (i5-14600KF, 6P+8E). Esse tipo de hardware não existia em 2006 (ano de publicação do livro), mas o **princípio teórico** estabelecido no Capítulo 6 sobre o limite fundamental do IPC — já fichado na Seção 3.9 deste documento — aplica-se diretamente a esse cenário, e por isso é revisitado aqui sob a nova luz fornecida pelos dados de hardware.

- **Conceito/Teoria:** O IPC de qualquer núcleo é, em última instância, limitado pela sua *issue rate* (taxa de emissão de instruções); em uma arquitetura heterogênea P-core/E-core, cada tipo de núcleo possui uma *issue rate* e uma microarquitetura distintas, de modo que o IPC agregado do processador passa a ser uma média ponderada entre subpopulações de núcleos com capacidades de emissão diferentes — e não um valor único e homogêneo, como implicitamente assumido nos processadores simétricos (SMP) estudados no Capítulo 6 do livro.

- **Citação Direta (Ipsis Litteris) — reaproveitada da Seção 3.9, agora aplicada ao novo contexto:**
  > "The standard performance metric for superscalar processors is the IPC, measured as the number of instructions retired per execution cycle. IPC is ultimately limited by the issue rate of the processor, because flow out of the processor cannot exceed the flow in." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conforme estabelecido por Conte e Bryan (2006), o IPC de um processador superescalar é fundamentalmente limitado por sua taxa de emissão de instruções \cite{conte_bryan:06}. Ao aplicar esse princípio a processadores com arquitetura híbrida — como o Intel Core i5-13420H (Raptor Lake-H, 4 núcleos de Performance + 4 núcleos de Eficiência) da Máquina A, o i5-1334U (Raptor Lake-P, 2P+8E) da Máquina B, e o i5-14600KF (Raptor Lake, 6P+8E) da Máquina F — torna-se necessário reconhecer que o "processador" não possui uma única *issue rate*, mas sim duas taxas distintas: uma mais alta e especulativa para os P-cores (otimizados para IPC de thread único) e outra mais conservadora para os E-cores (otimizados para eficiência energética por área de silício, com pipeline mais simples). Isso implica que o desempenho Multi-Core agregado do Geekbench 6 nessas três máquinas resulta da soma do trabalho de duas subpopulações de núcleos com limites de IPC teoricamente diferentes entre si, ao passo que nas Máquinas C, D e E (núcleos homogêneos: Zen+, Whiskey Lake-U e Zen 3, respectivamente) o IPC teórico é uniforme entre todos os núcleos físicos.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (subseção de Paralelismo a Nível de Instrução e Thread) — amplia a discussão de "Diferenças entre arquiteturas multicore (Cores físicos vs. Threads lógicos)" exigida no escopo, incorporando agora a dimensão adicional de heterogeneidade de núcleos (P-core vs. E-core), inexistente nas máquinas fichadas anteriormente (apenas a Máquina D estava consolidada até o fichamento anterior).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → colunas `Core 0 Relógio (MHz)` a `Core 3 Relógio (MHz)` (e, havendo colunas adicionais para núcleos extras conforme a topologia real exportada pelo HWiNFO64): permitem, em tese, observar relógios efetivos distintos entre P-cores e E-cores durante a carga do Geekbench 6.
  - `Core 0 T0 Uso (%)` a `Core 3 T1 Uso (%)`: a presença de **threads lógicos (T0/T1) apenas nos P-cores** (pois E-cores Intel não implementam Hyper-Threading) é um dado microarquitetural que deve ser observado nos CSVs das Máquinas A, B e F — diferentemente da Máquina D (i5-8265U), cujos 4 núcleos físicos são homogêneos e todos com Hyper-Threading (4C/8T uniformes).
  - **NOTA PREDITIVA:** A lista de colunas do HWiNFO64 fornecida no escopo do projeto foi originalmente mapeada para um processador de 4 núcleos homogêneos (padrão `Core 0` a `Core 3`). Para as Máquinas A (8 núcleos), B e F (10 e 14 núcleos, respectivamente), a exportação real do HWiNFO64 produzirá um número maior de colunas `Core N ...` (até `Core 7`, `Core 9` ou `Core 13`, conforme a máquina), e essas colunas adicionais ainda não constam na lista de colunas críticas definida no escopo do projeto. **Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware e os arquivos de telemetria efetivamente exportados das Máquinas A, B, C, E e F forem fornecidos/confirmados pelo grupo nas próximas interações.**

---

### 3.13 — ATUALIZAÇÃO (Nova Tabela de Hardware): TDP, Frequência de Boost e o Limite Físico da Equação de Potência

> **Contexto da atualização:** a nova tabela revela uma amplitude de TDP Base muito maior do que a observada anteriormente (apenas a Máquina D, com 15 W, estava documentada): de 15 W (Máquinas B, C e D) a 125 W (Máquina F, desktop). Essa variação de TDP, combinada com diferentes faixas de clock Base/Boost, é diretamente relacionável ao princípio da Seção 3.4 (estatística para tratar ruído) e, sobretudo, fundamenta uma extensão da discussão de throttling já presente no escopo do projeto, ainda que o livro não trate de TDP especificamente.

- **Conceito/Teoria:** A relação entre o envelope de potência (TDP) disponível a um processador e sua capacidade de sustentar o clock de Boost Máximo por períodos prolongados sob carga — processadores com TDP Base baixo (15 W, das Máquinas B, C e D) dependem de um orçamento de potência "turbo" transitório (análogo ao mecanismo de PL1/PL2 já fichado em fichamentos anteriores do projeto) para atingir picos de Boost de até 4,60 GHz (Máquina B), ao passo que processadores de TDP elevado (65 W e 125 W, Máquinas E e F) possuem maior margem física para sustentar frequências elevadas de forma mais estável ao longo de toda a execução do benchmark.

- **Citação Direta (Ipsis Litteris) — reaproveitada da Seção 3.4 (estatística para ruído), agora cruzada com os novos dados de TDP:**
  > "Irrespective of whether real system measurement or simulation based modeling is done, computer architects should use statistical methods to make correct conclusions. For real-system measurements, statistics are needed to deal with noisy data. The noisy data comes from noise in the system being measured or is due to the measurement tools themselves." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Como já fichado na Seção 3.4, John e Eeckhout (2006) sustentam que medições em sistemas reais exigem tratamento estatístico do ruído inerente ao próprio sistema medido \cite{john_eeckhout_intro:06}. A nova tabela de hardware evidencia uma fonte concreta e adicional desse ruído: processadores de TDP Base reduzido (15 W — Máquinas B, C e D) operam predominantemente em regime de *boost* transitório para atingir seus clocks máximos (até 4,60 GHz no caso da Máquina B, um salto de mais de 3,5× sobre o clock base de 1,30 GHz), o que torna o desempenho dessas máquinas mais sensível a variações térmicas e de gerenciamento de energia entre rodadas consecutivas do Geekbench 6 — e, portanto, estatisticamente mais ruidoso (maior desvio padrão esperado) — quando comparado a processadores de TDP elevado (65 W na Máquina E, 125 W na Máquina F), cujo clock de Boost (4,20 GHz e 5,30 GHz para os P-cores, respectivamente) dispõe de um envelope de potência nominal proporcionalmente mais generoso para ser sustentado.

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** (seção de Termodinâmica e Estrangulamento) — fornece a base comparativa entre máquinas de TDP muito distinto (15 W vs. 125 W) para interpretar diferenças no desvio padrão dos scores e na incidência de eventos de throttling.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` (todas as seis máquinas) → colunas `Single_Core` e `Multi_Core`: comparar o desvio padrão amostral (Equação \ref{eq:desvio_padrao_amostral_geral}, já fichada na Seção 4.1) entre o grupo de TDP baixo (B, C, D — 15 W) e o grupo de TDP alto (E — 65 W, F — 125 W; A, notebook gamer, em posição intermediária com 45 W).
  - `maq*_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)`: verificar empiricamente se as máquinas de TDP baixo (B, C, D) apresentam maior queda percentual entre o clock de Boost nominal da Tabela de Hardware e o clock efetivo médio realmente sustentado durante as 20 rodadas — evidência direta de throttling por limite de potência (PL1).
  - `maq*_rodada_*.CSV` → `Potência total da CPU (W)`: validar se a potência média sustentada por cada máquina se aproxima do TDP Base declarado (15/45/65/125 W) ou se há ultrapassagem sustentada característica de PL2 prolongado.
  - **NOTA PREDITIVA:** Esta comparação cruzada entre TDP declarado (Tabela de Hardware) e potência/clock efetivamente sustentado (telemetria HWiNFO64) **só poderá ser executada de fato após a consolidação dos 80+ arquivos de telemetria das Máquinas A, B, C, E e F**, pois até o momento apenas a Máquina D possui dados de telemetria integralmente confirmados pelo grupo conforme os fichamentos anteriores do projeto.

---

### 3.14 — ATUALIZAÇÃO (Nova Tabela de Hardware): Cache L3 — Amplitude de 4 MB a 24 MB e o Estado Persistente do Domínio *Uncore*

> **Contexto da atualização:** a Seção 3.5 deste fichamento já havia citado a passagem do livro sobre as estruturas internas de estado (incluindo caches) referenciando apenas a Máquina D (Cache L3 de 6 MB). A nova tabela revela uma amplitude muito maior de Cache L3 entre as seis máquinas — de 4 MB (Máquina C, AMD Ryzen 5 3500U) a 24 MB (Máquina F, Intel i5-14600KF) —, o que justifica uma extensão direta dessa mesma citação, sem repeti-la integralmente, apenas cruzando-a com os novos dados.

- **Conceito/Teoria:** O cache L3 (compartilhado entre núcleos, parte do domínio *uncore*) é uma das estruturas de estado persistente identificadas no Capítulo 6 do livro; seu tamanho determina a capacidade do processador de reter dados de trabalho sem recorrer à memória principal (RAM), influenciando diretamente a frequência de acessos ao subsistema de memória durante cargas de trabalho intensivas como o Geekbench 6.

- **Citação Direta (Ipsis Litteris) — já citada integralmente na Seção 3.5, reaproveitada por cruzamento com os novos dados de Cache L3:**
  > "State in a processor is kept in a number of areas including: the scheduling queues, the reorder buffer, the functional unit pipelines, the branch handling target buffer (the BTB), instruction caches, data caches, load/store queues, and control transfer instruction queues." (Cap. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Como já fichado na Seção 3.5, Conte e Bryan (2006) incluem as caches de instrução e de dados entre as estruturas que retêm o estado microarquitetural do processador \cite{conte_bryan:06}. Com a nova tabela de hardware, esse princípio passa a poder ser comparado em uma amplitude de seis configurações de Cache L3 muito mais ampla: 4 MB (Máquina C — AMD Ryzen 5 3500U, Zen+), 6 MB (Máquina D — Intel i5-8265U, Whiskey Lake-U), 12 MB (Máquinas A e B — Intel Raptor Lake-H/P), 16 MB (Máquina E — AMD Ryzen 5 5500, Zen 3) e 24 MB (Máquina F — Intel i5-14600KF, Raptor Lake desktop). Quanto maior a capacidade do cache L3, maior a probabilidade de que o conjunto de trabalho (*working set*) do benchmark Geekbench 6 permaneça contido nessa estrutura sem extravasar para a hierarquia de memória principal — o que, por extensão da teoria de hierarquia de memória, tende a reduzir a frequência relativa de acessos à RAM e, consequentemente, a sensibilidade do desempenho final às limitações de banda da memória principal (tema já discutido nos fichamentos do projeto sobre o gargalo de Von Neumann).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (seção de Hierarquia de Memória) — amplia a Tabela de Hardware comparativa do `main.tex` ao oferecer uma base teórica para classificar as seis máquinas em função da capacidade de Cache L3, antes de cruzar com os resultados de desempenho.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` (todas as seis máquinas) → coluna `Uncore Relação (x)`: representa o multiplicador de clock do domínio uncore (que inclui o cache L3 e o *Ring/LLC*), permitindo comparar indiretamente a "velocidade" de acesso ao cache entre as seis configurações.
  - `maq*_rodada_*.CSV` → coluna `Ring/LLC Relógio (MHz)`: frequência do anel de interconexão que liga os núcleos ao Cache L3 (Last Level Cache); processadores com L3 maior (Máquina F, 24 MB) tendem a apresentar relação distinta entre este clock e o desempenho observado, em comparação com processadores de L3 menor (Máquina C, 4 MB).
  - **NOTA PREDITIVA:** A correlação efetiva entre tamanho de Cache L3 e estabilidade/magnitude do score Multi-Core só poderá ser quantificada quando os arquivos `scores_maq*.txt` e `maq*_rodada_*.CSV` das Máquinas A, B, C, E e F estiverem consolidados, conforme a diretriz de não antecipação de resultados empíricos ainda não coletados.

---

### 3.15 — ATUALIZAÇÃO (Nova Tabela de Hardware): RAM Single-Channel vs. Dual-Channel — Ampliação do Conjunto Comparativo do Gargalo de Von Neumann

> **Contexto da atualização:** anteriormente, apenas a Máquina D (Single Channel, 8 GB DDR4 1333 MHz, conforme as diretrizes de fichamento) estava consolidada para a discussão do gargalo de Von Neumann. A nova tabela revela que esse cenário de Single Channel **não é exclusivo da Máquina D**: a Máquina C (ASUS VivoBook X515DA, AMD Ryzen 5 3500U) também opera em Single Channel (1×8GB DDR4 2400 MHz), enquanto as Máquinas A, B, E e F operam em Dual Channel. Isso transforma a discussão de gargalo de memória de um caso isolado (apenas D) para uma **comparação experimental real entre dois grupos** (Single-Channel: C e D; Dual-Channel: A, B, E e F), fortalecendo substancialmente o valor científico da análise.

- **Conceito/Teoria:** A topologia de canais de memória (Single-Channel vs. Dual-Channel) determina a largura de banda teórica disponível para o subsistema de memória; em configuração Dual-Channel, dois módulos de RAM operam em paralelo, efetivamente dobrando a banda de transferência teórica em relação a uma configuração Single-Channel de especificação equivalente — um princípio que, embora não tratado explicitamente no recorte do livro fornecido (que se concentra em cache e não em DRAM externa), decorre diretamente do mesmo arcabouço teórico de hierarquia de memória e gargalo de Von Neumann já discutido nos fichamentos anteriores do projeto.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (Tabela de Hardware Comparativa) e **Resultados e Discussão** (seção de Gargalos de Arquitetura) — permite reorganizar a comparação de desempenho não apenas por máquina individual, mas por **agrupamento de topologia de memória**: {Máquina C, Máquina D} vs. {Máquina A, Máquina B, Máquina E, Máquina F}.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqC.txt` e `scores_maqD.txt` (grupo Single-Channel) vs. `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqE.txt`, `scores_maqF.txt` (grupo Dual-Channel) → coluna `Multi_Core`: a métrica multi-núcleo é a mais sensível à largura de banda de memória, pois mais núcleos competem simultaneamente pelo barramento de memória compartilhado.
  - `maqC_rodada_*.CSV` e `maqD_rodada_*.CSV` → coluna `Relógio da memória (MHz)`: deve ser comparada não isoladamente, mas em conjunto com a topologia de canais, já que dois módulos a uma mesma frequência nominal em Dual-Channel entregam o dobro da banda teórica de um único módulo na mesma frequência em Single-Channel.
  - `maq*_rodada_*.CSV` (todas) → colunas `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: embora estas colunas no escopo do projeto refiram-se primariamente ao armazenamento (disco), uma eventual correlação com `Carga da memória física (%)` pode ajudar a identificar se a máquina está gargalada por I/O de disco ou por banda de RAM durante a execução do benchmark.
  - **Reforço metodológico importante:** como agora existem **dois grupos** de máquinas em Single-Channel (C e D) com microarquiteturas de fabricantes diferentes (AMD Zen+ vs. Intel Whiskey Lake-U), o grupo deve tomar cuidado redobrado ao atribuir uma eventual queda de desempenho exclusivamente à topologia de memória — é necessário controlar (ou ao menos discutir explicitamente) o efeito confundidor da arquitetura de núcleo em si (IPC nativo de Zen+ vs. de Skylake-derivado), evitando generalizações causais não sustentadas apenas por dois pontos de dados.

---

### 3.16 — ATUALIZAÇÃO (Nova Tabela de Hardware): GPU Dedicada, Interface PCIe e o Papel do Barramento de E/S no Gargalo de Von Neumann Estendido

> **Contexto da atualização:** a tabela anterior não trazia informações sobre GPU dedicada nem sobre a interface de barramento PCIe. A nova tabela revela que três das seis máquinas possuem GPU dedicada (Máquina A — RTX 4050 Laptop via PCIe 4.0 x8; Máquina D — MX130 via PCIe 3.0 x4; Máquina E — RX 7600 via PCIe 4.0 x8; Máquina F — RTX 3050 via PCIe 4.0 x8), com gerações e larguras de barramento distintas.

- **Conceito/Teoria:** O barramento PCIe que conecta a GPU dedicada ao restante do sistema constitui uma extensão do mesmo princípio do gargalo de Von Neumann (compartilhamento de um canal único de comunicação entre unidades de processamento e memória/periféricos): tanto a *geração* do PCIe (3.0 vs. 4.0, que dobra a taxa de transferência por linha) quanto o *número de linhas* (x4 vs. x8) determinam a banda teórica disponível para a GPU comunicar-se com o restante do sistema.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (extensão da seção de Gargalos de Arquitetura) — embora o Geekbench 6 em sua componente CPU não exercite intensamente a GPU, esta tabela é relevante caso o grupo decida (ou já tenha decidido, conforme dados do projeto) incluir testes de GPU Compute do Geekbench 6 na análise.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqD_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` (máquinas com GPU dedicada) → colunas `Velocidade do link PCIe (GT/s)`, `Carga do núcleo da GPU (%)`, `GPU Clock (MHz)` e `Uso de memória GPU (%)`: permitem observar se a GPU dedicada é solicitada em algum momento durante a execução do Geekbench 6 (mesmo que o teste principal do projeto seja a componente CPU).
  - Comparação específica Máquina A (PCIe 4.0 x8) vs. Máquina D (PCIe 3.0 x4): caso o grupo eventualmente analise testes de GPU, esta é a comparação de maior contraste de barramento disponível no dataset, e deve ser tratada com a devida cautela interpretativa (a Máquina A possui também uma GPU de classe de desempenho muito superior à MX130 da Máquina D, de modo que qualquer diferença observada não pode ser atribuída isoladamente ao barramento PCIe).
  - **NOTA PREDITIVA:** Como o escopo de telemetria definido pelo grupo prioriza primariamente as colunas de CPU (clock, temperatura, potência, uso) e a base do Geekbench 6 documentada (`scores_maq*.txt`) registra apenas `Single_Core` e `Multi_Core` — sem coluna explícita de score de GPU Compute —, esta seção permanece **fichada de forma preditiva** e só será incorporada à redação final caso o grupo confirme a existência de dados de benchmark de GPU (Geekbench 6 GPU Compute/OpenCL/Vulkan) a serem analisados, o que não foi declarado até o momento na estrutura de dados do projeto.

---

### 3.17 — ATUALIZAÇÃO (Nova Tabela de Hardware): Armazenamento — Ampliação do Espectro de NVMe Gen3/Gen4 e o Caso Isolado do HDD SATA

> **Contexto da atualização:** nos fichamentos anteriores do projeto, a discussão de "HD SATA vs. SSD NVMe" baseava-se exclusivamente no contraste entre a Máquina D (HDD SATA, único caso) e uma generalização teórica sobre SSDs NVMe. A nova tabela revela que **todas as outras cinco máquinas** possuem armazenamento em estado sólido, mas com gerações de interface distintas: PCIe Gen 3.0 x4 (Máquinas B e C) e PCIe Gen 4.0 x4 (Máquina A), além de configurações com dois SSDs NVMe M.2 em paralelo (Máquina F) e uma configuração híbrida SATA SSD + HDD (Máquina E).

- **Conceito/Teoria:** Dentro da hierarquia de memória, o subsistema de armazenamento secundário constitui o nível mais lento e mais distante da CPU; a diferença de geração de interface PCIe (Gen 3.0 vs. Gen 4.0, que dobra a taxa de transferência teórica por linha, de aproximadamente 8 GT/s para 16 GT/s) determina o teto de desempenho sequencial do SSD, fator que pode influenciar etapas do benchmark Geekbench 6 que dependam de carregamento de dados a partir do disco (por exemplo, na inicialização do aplicativo e no carregamento dos subtestes), ainda que a fase de medição propriamente dita do benchmark seja majoritariamente limitada por CPU e memória, não por disco.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (seção de Hierarquia de Memória, subseção de Armazenamento) — amplia a Tabela de Hardware Comparativa do `main.tex`, permitindo uma classificação mais granular das seis máquinas por nível de desempenho de armazenamento: HDD SATA (D, isolado) < SSD SATA híbrido (E) < SSD NVMe PCIe 3.0 (B, C) < SSD NVMe PCIe 4.0 (A, e presumivelmente F, a confirmar).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` (todas as seis máquinas) → colunas `Taxa de leituras (MB/s)`, `Taxa de gravações (MB/s)`, `Temperatura do disco (°C)`: permitem quantificar empiricamente a diferença de desempenho de armazenamento entre as seis configurações, validando (ou refutando) a hipótese teórica de hierarquia apresentada acima.
  - **Caso de maior interesse experimental — Máquina D (HDD SATA, 5400 RPM):** dentre as seis máquinas, é a única com armazenamento mecânico (HDD), o que a torna o caso de controle mais relevante para evidenciar o impacto do gargalo de I/O nos tempos de carregamento e, possivelmente, na variabilidade (desvio padrão) das 20 rodadas — hipótese já registrada nos fichamentos anteriores do projeto e agora reforçada por comparação direta com cinco outras máquinas inteiramente baseadas em memória de estado sólido.
  - **NOTA PREDITIVA:** A coluna `Interface / Taxa do Disco` da Máquina F está marcada como "[Preencher Gen]*" na tabela de hardware fornecida — ou seja, a geração exata do PCIe dos dois SSDs NVMe M.2 dessa máquina ainda não foi informada pelo grupo. Da mesma forma, o gabinete e a memória RAM (MHz) da Máquina E constam como "[Preencher Gabinete]*" e "[MHz]*", respectivamente, e o gabinete da Máquina F também está pendente. **Estes três campos pendentes devem ser preenchidos pelo grupo antes da redação final da Metodologia, pois a Tabela de Hardware Comparativa em LaTeX exigida pelas diretrizes do projeto não deve conter lacunas no documento final.**

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 — Desvio Padrão Amostral para Desenho de Amostragem em Clusters (Equação 6.8 do livro)

```latex
\begin{equation}
    S_{IPC} = \sqrt{\frac{\sum_{i=1}^{N_{cluster}} \left(\mu_{IPC_i} - \mu_{IPC_{sample}}\right)^2}{N_{cluster} - 1}}
    \label{eq:desvio_padrao_cluster}
\end{equation}
```

**Onde:** $\mu_{IPC_i}$ = média da métrica (IPC, ou, por adaptação, score) no $i$-ésimo cluster/rodada; $\mu_{IPC_{sample}}$ = média geral da amostra; $N_{cluster}$ = número total de clusters/rodadas (N = 20 no presente experimento).

**Adaptação direta para o nosso contexto (Desvio Padrão Amostral dos scores):**

```latex
\begin{equation}
    s = \sqrt{\frac{1}{N-1}\sum_{n=1}^{N}\left(X_n - \overline{X}\right)^2}
    \label{eq:desvio_padrao_amostral_geral}
\end{equation}
```

**Onde:** $N = 20$ (número de rodadas); $X_n$ = score (Single-Core ou Multi-Core) ou valor de telemetria da rodada $n$; $\overline{X}$ = média aritmética amostral.

### 4.2 — Erro Padrão Estimado e Intervalo de Confiança de 95% (Equação 6.9 e discussão do livro)

```latex
\begin{equation}
    \text{IC}_{95\%} = \overline{X} \pm 1{,}96 \cdot \frac{s}{\sqrt{N}}
    \label{eq:intervalo_confianca}
\end{equation}
```

**Onde:** $\overline{X}$ = média amostral; $s$ = desvio padrão amostral (Equação \ref{eq:desvio_padrao_amostral_geral}); $N$ = número de rodadas.

> **Nota de rigor estatístico:** para $N=20$, a literatura estatística clássica recomenda substituir o valor crítico $1{,}96$ (válido assintoticamente, $N \to \infty$, distribuição normal padrão) pelo valor crítico da distribuição $t$ de Student com $N-1=19$ graus de liberdade ($t_{0{,}975;19} \approx 2{,}093$), o que produz um intervalo de confiança ligeiramente mais conservador (mais largo). Esta ressalva deve ser explicitada no artigo caso o grupo opte por reportar intervalos de confiança, evitando uma aplicação tecnicamente imprecisa da equação do livro para amostras pequenas.

### 4.3 — Definição de IPC (Instructions Per Cycle)

O livro não apresenta uma fórmula numerada explícita para o IPC no trecho fornecido, mas a definição textual ("number of instructions retired per execution cycle") permite a formalização padrão da literatura de arquitetura de computadores:

```latex
\begin{equation}
    \text{IPC} = \frac{N_{instrucoes\_retiradas}}{N_{ciclos\_execucao}}
    \label{eq:ipc_definicao}
\end{equation}
```

**Métrica derivada proposta para o artigo ("IPC Relativo"), com base na limitação de dados disponíveis (sem PMCs/contadores de hardware):**

```latex
\begin{equation}
    \text{IPC}_{rel} = \frac{\text{Score}_{Multi\text{-}Core}}{\overline{f}_{efetiva}}
    \label{eq:ipc_relativo}
\end{equation}
```

**Onde:** $\overline{f}_{efetiva}$ = média da coluna `Relógios efetivos núcleo (avg) (MHz)` durante a execução do benchmark. Esta é uma métrica heurística proposta pelo grupo, não uma fórmula extraída diretamente do livro, e deve ser apresentada como tal no artigo.

### 4.4 — Sugestão de Gráficos e Tabelas Correspondentes

**Gráfico 1 — Barplot de Desvio Padrão dos Scores por Máquina (validação da homogeneidade entre rodadas, Seção 3.8):**

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

maquinas = ['Máquina A', 'Máquina B', 'Máquina C', 'Máquina D']
medias_mc = []
desvios_mc = []

for m in ['A', 'B', 'C', 'D']:
    df = pd.read_csv(f'scores_maq{m}.txt', sep=';')
    medias_mc.append(df['Multi_Core'].mean())
    desvios_mc.append(df['Multi_Core'].std(ddof=1))  # ddof=1 -> desvio padrão amostral

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(maquinas))
ax.bar(x, medias_mc, yerr=desvios_mc, capsize=5, color='0.6',
       edgecolor='black', error_kw=dict(elinewidth=1.3, capthick=1.3))
ax.set_xlabel('Máquina', fontsize=11)
ax.set_ylabel('Score Multi-Core (Geekbench 6)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(maquinas)
ax.set_title('Média e Desvio Padrão Amostral — Score Multi-Core (N=20)', fontsize=11)
plt.tight_layout()
plt.savefig('fig_desvio_padrao_multicore.pdf', dpi=300, format='pdf')
```

**Tabela LaTeX — IPC Relativo (heurístico) por máquina:**

```latex
\begin{table}[ht]
\caption{IPC Relativo heurístico (Score Multi-Core / Relógio efetivo médio)
         por máquina. Fonte: Dados da pesquisa (2026).}
\label{tab:ipc_relativo}
\centering
\begin{tabular}{lccc}
\hline
\textbf{Máquina} & \textbf{Score MC Médio} &
\textbf{Relógio Efetivo Médio (MHz)} & \textbf{IPC$_{rel}$} \\
\hline
Máquina A & --- & --- & --- \\
Máquina B & --- & --- & --- \\
Máquina C & --- & --- & --- \\
Máquina D & --- & --- & --- \\
\hline
\multicolumn{4}{l}{\small MC = Multi-Core; IPC$_{rel}$ = métrica heurística proposta} \\
\multicolumn{4}{l}{\small (Equação~\ref{eq:ipc_relativo}), não medida por PMCs de hardware.}
\end{tabular}
\end{table}
```

---

## 5. SUGESTÕES DE BUSCA NO GOOGLE ACADÊMICO

**Para complementar/encontrar os capítulos não fornecidos integralmente (2, 3, 5, 11), em inglês:**
1. `"Performance Evaluation and Benchmarking" John Eeckhout CRC Press 2006`
2. `Lilja Yi "statistical techniques" "computer performance analysis" chapter`
3. `Sprunt "performance monitoring hardware" "Pentium 4 processor"`
4. `John "aggregating performance metrics" "benchmark suite" arithmetic geometric harmonic mean`
5. `Conte Bryan "statistical sampling" "processor and cache simulation"`

**Para embasar diretamente os conceitos fichados (médias, IPC, amostragem), em inglês:**
6. `"arithmetic mean" "geometric mean" "harmonic mean" computer performance benchmark`
7. `"instructions per cycle" IPC superscalar processor performance metric`
8. `"confidence interval" "standard error" benchmark sample size computer architecture`
9. `"cluster sampling" processor simulation standard deviation IPC`
10. `Smith "characterizing computer performance with a single number" 1988`

**Em português (para referências nacionais/SBC):**
1. `"avaliação de desempenho" computador "média aritmética" "média geométrica" benchmark`
2. `"instruções por ciclo" IPC desempenho processador superescalar`
3. `"intervalo de confiança" "erro padrão" desempenho computacional amostragem`
4. `"metodologia de avaliação de desempenho" arquitetura de computadores benchmark`
5. `"monitoramento de desempenho" hardware contadores processador`

---

### 5.1 — ATUALIZAÇÃO (Nova Tabela de Hardware): Strings de Busca Adicionais para os Novos Componentes Mapeados nas Seções 3.12 a 3.17

**Em inglês — núcleos híbridos P-core/E-core (Seção 3.12):**
1. `"hybrid architecture" "performance cores" "efficiency cores" IPC benchmark Intel`
2. `Intel "Alder Lake" OR "Raptor Lake" "heterogeneous cores" performance analysis`
3. `"big.LITTLE" OR "P-core E-core" scheduling thread performance benchmark`
4. `"Thread Director" Intel hybrid core scheduling performance`

**Em inglês — TDP e sustentação de Boost Clock (Seção 3.13):**
5. `"TDP" "boost clock" "sustained frequency" laptop processor benchmark`
6. `"power budget" "turbo boost" duration thermal CPU benchmark variability`

**Em inglês — Cache L3 e domínio uncore (Seção 3.14):**
7. `"L3 cache size" "last level cache" benchmark performance comparison processor`
8. `"uncore frequency" "ring bus" cache latency processor performance`

**Em inglês — Single/Dual Channel memory (Seção 3.15):**
9. `"single channel" "dual channel" memory bandwidth CPU benchmark performance`
10. `DDR4 "memory bandwidth" multicore performance scaling benchmark`

**Em inglês — PCIe e GPU (Seção 3.16):**
11. `"PCIe 3.0" "PCIe 4.0" bandwidth GPU performance comparison benchmark`
12. `PCIe lanes "x4" "x8" GPU bottleneck gaming performance`

**Em inglês — SSD NVMe Gen3/Gen4 e HDD (Seção 3.17):**
13. `"NVMe" "PCIe Gen3" "PCIe Gen4" SSD sequential read write benchmark`
14. `HDD vs SSD "boot time" "application load time" benchmark comparison`

**Em português:**
15. `"núcleos heterogêneos" "P-core" "E-core" desempenho processador Intel`
16. `"canal único" "canal duplo" memória RAM desempenho benchmark multicore`
17. `"PCIe Gen3" "PCIe Gen4" largura de banda GPU desempenho`
18. `SSD NVMe HDD SATA "tempo de carregamento" desempenho comparação`
19. `cache L3 "última camada" desempenho processador multicore`

---

## 6. NOTAS EDITORIAIS FINAIS

> ⚠️ **Sobre a completude do documento fornecido:** O PDF anexado corresponde a um *preview* (pré-visualização) do livro disponibilizado pela Taylor & Francis/CRC Press, contendo a capa, ficha catalográfica, prefácio, biografias dos editores e contribuidores, sumário completo, o texto integral do Capítulo 1 (Introdução e Visão Geral), as referências bibliográficas dos Capítulos 2 a 13, e um trecho técnico substancialmente mais extenso do Capítulo 6 (Statistical Sampling for Processor and Cache Simulation), incluindo figuras, tabelas e equações originais. O fichamento acima respeita rigorosamente esse recorte, sem inventar conteúdo dos capítulos cujo corpo textual não foi fornecido (notadamente os Capítulos 2, 3, 4 — citado apenas via Cap. 1 —, 5, 7 a 13).

> ⚠️ **Sobre a antiguidade da obra:** Publicado em 2006, o livro antecede arquiteturas modernas como as estudadas no projeto (Intel Whiskey Lake/i5-8265U, Windows 11). Os processadores citados nos exemplos do Capítulo 6 (MIPS R10000, SimpleScalar) e nos capítulos de monitoramento de hardware (Pentium 4, POWER5, Itanium) são tecnologicamente superados. Ainda assim, os **fundamentos estatísticos e metodológicos** (desvio padrão amostral, erro padrão, intervalo de confiança, definição de IPC, agregação de métricas) permanecem integralmente válidos e constituem a base teórica de toda a literatura posterior em avaliação de desempenho — devendo ser citados como referência metodológica clássica, complementada por referências mais recentes (já fichadas no projeto) para os aspectos específicos de hardware contemporâneo (DVFS, RAPL, throttling térmico).

> ⚠️ **Mapeamento de Hardware Pendente (Máquinas A, B e C):** Nenhuma das discussões fichadas acima depende de especificações de hardware ainda não fornecidas, pois o conteúdo do livro é predominantemente metodológico e estatístico (aplicável a qualquer máquina). Contudo, a tabela comparativa de "IPC Relativo" (Seção 4.4) e a análise de homogeneidade entre rodadas (Seção 3.8) só poderão ser preenchidas com valores reais e comparados entre as quatro máquinas após a consolidação completa dos dados de telemetria das Máquinas A, B e C, conforme já registrado nos fichamentos anteriores do projeto.

> ⚠️ **NOTA DE ATUALIZAÇÃO (Nova Tabela de Hardware — 6 Máquinas):** Esta revisão do fichamento incorporou as Seções 3.12 a 3.17 e a Subseção 5.1, acrescentadas em resposta ao fornecimento da tabela de hardware ampliada e completa do grupo (Máquinas A, B, C, D, E e F), substituindo o cenário anterior em que apenas a Máquina D possuía especificação integral. As novas seções cruzam os conceitos já estabelecidos no livro (limite de IPC pela *issue rate*, estado persistente em estruturas de cache, necessidade de tratamento estatístico do ruído de medição) com os seguintes componentes inéditos no fichamento original: (a) núcleos heterogêneos P-core/E-core (Máquinas A, B e F); (b) amplitude de TDP de 15 W a 125 W; (c) amplitude de Cache L3 de 4 MB a 24 MB; (d) um segundo caso de topologia Single-Channel (Máquina C), que transforma a discussão de gargalo de memória de um caso isolado (apenas D) em uma comparação real entre dois grupos; (e) presença de GPU dedicada com interfaces PCIe de gerações distintas (3.0 x4 e 4.0 x8); e (f) ampliação do espectro de armazenamento, com SSDs NVMe de PCIe Gen 3.0 e Gen 4.0, uma configuração híbrida SATA+HDD (Máquina E) e dois SSDs NVMe em paralelo (Máquina F). **Nenhum conteúdo, citação, paráfrase, fórmula ou seção pré-existente neste arquivo foi alterado, removido ou renumerado nesta atualização** — todas as adições foram inseridas como novas subseções (3.12–3.17, 5.1) e como o presente parágrafo, preservando integralmente a estrutura e o conteúdo anteriormente aprovados pelo grupo.
>
> Permanecem pendentes de preenchimento pelo grupo, conforme identificado na Seção 3.17: (i) o modelo de gabinete das Máquinas E e F; (ii) a frequência (MHz) da RAM da Máquina E; (iii) a geração da interface PCIe dos SSDs NVMe da Máquina F. Estes três campos devem ser completados antes da finalização da Tabela de Hardware Comparativa no `main.tex`.
