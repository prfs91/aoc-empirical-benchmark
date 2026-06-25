# Fichamento Científico — Padrão SBC/AOC-UFPA

> **Arquivo:** `fichamento_CoordinatedEnergyManagement_Paul.md`
> **Gerado por:** Co-autor IA (Claude) — Disciplina de Arquitetura e Organização de Computadores
> **Instituição:** Faculdade de Engenharia de Computação — UFPA, Campus Tucuruí
> **Professor Orientador:** Prof. Dr. Iago Medeiros (iagomedeiros@ufpa.br)

---

## VEREDITO DE RELEVÂNCIA

> ✅ **O artigo SERÁ ÚTIL para o nosso projeto de AOC. SIM.**
>
> O artigo investiga gerenciamento coordenado de energia e frequência (DVFS) em
> processadores heterogêneos CPU-GPU integrados (APUs), cobrindo diretamente:
> Thermal Throttling, limites de TDP (Power Limits PL1/PL2), sensibilidade de
> frequência por workload, interferência de banda de memória compartilhada entre
> CPU e GPU, e a métrica ED² (Energy-Delay²) como proxy de eficiência energética.
> Todos esses fenômenos aparecem nos nossos dados de telemetria HWiNFO64
> (especialmente colunas de clock, temperatura, potência e limitadores de desempenho)
> e fundamentam a discussão arquitetural comparativa entre as Máquinas A, B, C e D.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA

### Referência Textual Padrão SBC (para `\begin{thebibliography}` no `main.tex`)

```
PAUL, I.; RAVI, V.; MANNE, S.; ARORA, M.; YALAMANCHILI, S. Coordinated Energy
Management in Heterogeneous Processors. In: INTERNATIONAL CONFERENCE FOR HIGH
PERFORMANCE COMPUTING, NETWORKING, STORAGE AND ANALYSIS (SC), 2013, Denver, CO,
USA. \textbf{Proceedings of SC'13}. New York: ACM, 2013. p. 1--11.
http://dx.doi.org/10.1145/2503210.2503227
```

### Código BibTeX Completo (para o arquivo `sbc-template.bib`)

```bibtex
@InProceedings{paul2013coordinated,
  author    = {Indrani Paul and Vignesh Ravi and Srilatha Manne
               and Manish Arora and Sudhakar Yalamanchili},
  title     = {Coordinated Energy Management in Heterogeneous Processors},
  booktitle = {Proceedings of the International Conference for High Performance
               Computing, Networking, Storage and Analysis ({SC}'13)},
  year      = {2013},
  address   = {Denver, {CO}, {USA}},
  publisher = {{ACM}},
  pages     = {1--11},
  doi       = {10.1145/2503210.2503227},
  note      = {Advanced Micro Devices ({AMD}) / Georgia Institute of Technology
               / University of California, San Diego}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

| Campo                    | Conteúdo                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------------|
| **Grau/Tipo**            | Artigo Completo de Conferência (Peer-Reviewed — ACM SC'13, Qualis A1)                     |
| **Instituição/Editora**  | Advanced Micro Devices (AMD) / Georgia Institute of Technology / UC San Diego / ACM        |
| **Autores**              | Indrani Paul; Vignesh Ravi; Srilatha Manne; Manish Arora; Sudhakar Yalamanchili            |
| **Palavras-Chave**       | Energy management; High-performance computing; DVFS; Heterogeneous processors; CPU-GPU     |
| **DOI**                  | 10.1145/2503210.2503227                                                                    |
| **Ano**                  | 2013                                                                                       |

### Resumo do Escopo Geral (em português)

O artigo propõe e avalia o **DynaCo** (*Dynamic Coordinated Energy Management*), um
algoritmo de gerenciamento dinâmico de energia para processadores heterogêneos integrados
CPU-GPU (APUs), com foco em aplicações de computação de alto desempenho (HPC). A contribuição
central é demonstrar que as decisões de DVFS (escalonamento dinâmico de tensão e frequência)
para CPU e GPU devem ser *coordenadas* — e não independentes — porque ambos os núcleos
compartilham recursos (controlador de memória, barramento DDR, orçamento térmico de pacote).
Os autores caracterizam empiricamente a sensibilidade de frequência de aplicações exascale,
constroem um modelo analítico preditivo e implementam o DynaCo em hardware real (AMD A-Series
APU — 100W TDP), alcançando até 30% de melhoria no produto ED² com menos de 2% de degradação
de desempenho médio.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO

---

### 3.1 — DVFS e Gerenciamento de Estados de Potência (P-States)

- **Conceito/Teoria:** Dynamic Voltage and Frequency Scaling (DVFS) — P-States de CPU e
  estados de frequência de GPU como mecanismo de controle de potência e temperatura.

- **Citação Direta (Ipsis Litteris):**
  > "P0 through P5 are software-visible DVFS states that are referred to as performance
  > states, or P-states, and are managed either by the OS through the Advanced Configuration
  > and Power Interface (ACPI) specification or by the hardware. Pb0 and Pb1 are called the
  > boost states and are visible only to, and managed by, the hardware." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  O escalonamento dinâmico de tensão e frequência (DVFS) é implementado nos processadores
  modernos por meio de estados de desempenho (P-states), que variam entre um estado de base
  (P0) e estados de menor consumo (P1 a P5). Adicionalmente, estados de *boost* (Pb0 e Pb1)
  são gerenciados exclusivamente pelo hardware para maximizar desempenho quando o orçamento
  térmico e de potência permite. O sistema operacional interage com esses estados por meio
  da especificação ACPI (Paul et al., 2013, p. 3).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre Gerenciamento
  de Frequência e Mecanismos de Throttling.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Relógios núcleo (avg) (MHz)` e `Relógios efetivos núcleo (avg) (MHz)`:
    evidenciam os diferentes P-states em execução durante o benchmark.
  - `maqX_rodada_YY.CSV` → `Relação do relógio do núcleo (avg) (x)` e `Core 0-3 Relação (x)`:
    indicam o multiplicador de clock em cada instante, mapeando diretamente os P-states.
  - `maqX_rodada_YY.CSV` → `Core VIDs (avg) (V)` e `Core 0-3 VID (V)`: confirmam a variação
    de tensão associada ao DVFS.
  - `maqX_rodada_YY.CSV` → `Modulação do relógio sob demanda (%)`: indica ativação de estados
    de clock reduzido por demanda.
  - `scores_maqX.txt` → colunas `Single_Core` e `Multi_Core`: refletem o impacto dos P-states
    no desempenho final medido pelo Geekbench 6.

---

### 3.2 — Thermal Throttling (Estrangulamento Térmico)

- **Conceito/Teoria:** Estrangulamento térmico — redução forçada de clock pela ultrapassagem
  de limites de temperatura de junção (TjMAX), causando variabilidade no desempenho.

- **Citação Direta (Ipsis Litteris):**
  > "Lower temperatures result in lower cooling costs, better energy efficiency, and better
  > heat management. [...] With DynaCo, peak die temperature is, on average, up to 2°C lower
  > across all the applications." (p. 10)

- **Citação Direta Complementar:**
  > "The BAPM algorithm sets power limits based on thermal constraints and greedily boosts the
  > power states to maximize use of the thermal capacity." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  O estrangulamento térmico (*thermal throttling*) ocorre quando o processador atinge o limite
  máximo de temperatura de junção (TjMAX), forçando a redução automática do clock para proteger
  o silício. Algoritmos como o BAPM (da AMD) monitoram continuamente estimativas de temperatura
  e potência, ajustando os limites de potência de cada componente (CPU e GPU) para maximizar
  o uso da capacidade térmica disponível sem ultrapassar os limites críticos. A redução de
  temperatura obtida por estratégias de escalonamento inteligente — como os 2°C reportados
  pelo DynaCo — tem impacto direto na estabilidade dos clocks e na reprodutibilidade dos
  resultados de benchmark (Paul et al., 2013, p. 3 e 10).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (definição de thermal throttling)
  e **Resultados e Discussão** (explicação do desvio padrão elevado em máquinas que sofreram
  throttling durante as 20 rodadas).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `CPU Inteira (°C)` e `Núcleo máximo (°C)`: temperatura do pacote
    e do núcleo mais quente — monitorar se alguma máquina atingiu TjMAX (~100°C para i5-8265U).
  - `maqX_rodada_YY.CSV` → `Core 0-3 (°C)` e `Distância do núcleo para TjMAX (avg) (°C)`:
    margem térmica restante por núcleo; valores próximos de zero indicam throttling iminente.
  - `maqX_rodada_YY.CSV` → `Estrangulamento térmico do núcleo (avg) (Yes/No)` e
    `Core 0-3 Estrangulamento térmico (Yes/No)`: **flags diretas de throttling** por núcleo.
  - `maqX_rodada_YY.CSV` → `Temperatura crítica do núcleo (avg) (Yes/No)`: confirmação de
    temperatura crítica atingida.
  - `maqX_rodada_YY.CSV` → `Regulagem térmica do pacote / anel (Yes/No)`: throttling de pacote.
  - `maqX_rodada_YY.CSV` → `IA: Package-Level RAPL/PBM PL1 (Yes/No)` e
    `IA: Package-Level RAPL/PBM PL2 PL3 (Yes/No)`: **flags de limitação por Power Limit**,
    análogas ao BAPM descrito pelos autores.
  - `scores_maqX.txt` → desvio padrão das colunas `Single_Core` e `Multi_Core` entre as 20
    rodadas: um σ elevado é evidência estatística de throttling intermitente.

---

### 3.3 — Orçamento Térmico de Pacote e TDP (Thermal Design Power)

- **Conceito/Teoria:** TDP como limite de projeto e sua influência nos algoritmos de
  gerenciamento de potência e alocação de frequência entre CPU e GPU.

- **Citação Direta (Ipsis Litteris):**
  > "We used the AMD A10-5800 desktop APU with 100W TDP as the baseline for all our
  > experiments and analysis. Base CPU frequency is 3.8GHz, with boost frequency up to
  > 4.2GHz." (p. 7)

- **Citação Direta Complementar:**
  > "The BAPM algorithm is optimized to maximize performance with a fair and balanced sharing
  > of power between on-chip entities. BAPM allocates power to each entity using a pre-set
  > static distribution weight that is derived using empirical analysis." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  O TDP (Thermal Design Power) define o envelope de dissipação de calor para o qual o sistema
  de resfriamento deve ser dimensionado. Em processadores heterogêneos, o orçamento de potência
  do pacote é compartilhado entre os núcleos de CPU e GPU, e algoritmos como o BAPM distribuem
  esse orçamento dinamicamente com base em pesos estáticos pré-calibrados por análise empírica.
  Quando a demanda agregada de CPU e GPU excede o TDP, o gerenciador de potência força a
  redução de frequência em um ou ambos os componentes (Paul et al., 2013, p. 3 e 7).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (caracterização do hardware — TDP de cada
  máquina) e **Resultados e Discussão** (análise dos limites de potência).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Potência total da CPU (W)`: consumo real do pacote CPU durante o
    benchmark — comparar com o TDP nominal de cada máquina.
  - `maqX_rodada_YY.CSV` → `Potência de núcleos IA (W)` e `Potência de núcleo GT (W)`:
    decomposição da potência entre núcleos de computação e gráficos integrados.
  - `maqX_rodada_YY.CSV` → `Limite de potência PL1 (Static) (W)`, `Limite de potência PL1
    (Dynamic) (W)`, `Limite de potência PL2 (Static) (W)`, `Limite de potência PL2 (Dynamic) (W)`:
    valores dos limites configurados — análogos aos P-states de potência do BAPM.
  - `maqX_rodada_YY.CSV` → `Limite de potência do núcleo excedido (avg) (Yes/No)` e
    `Core 0-3 Limite de potência excedido (Yes/No)`: **flags de violação de PL1/PL2**.
  - `maqX_rodada_YY.CSV` → `Potência total do sistema (W)`: consumo total do sistema,
    incluindo periféricos.
  - **Máquina D (Roberta):** i5-8265U com TDP de 15W (TDP-up: 25W) — processador mobile de
    baixo TDP, evidenciando envelope energético severamente restrito em comparação ao APU
    de 100W do artigo. Essa diferença de escala é um ponto de discussão rico.

---

### 3.4 — Interferência de Banda de Memória Compartilhada entre CPU e GPU

- **Conceito/Teoria:** Gargalo de memória por contenda entre CPU e GPU ao controlador DDR
  compartilhado — extensão do gargalo de Von Neumann para arquiteturas heterogêneas.

- **Citação Direta (Ipsis Litteris):**
  > "The memory hierarchy is a key determinant of performance, and the CPU and the GPU share
  > the Northbridge and memory controllers. The extent of interference at these points (which
  > is time-varying) has a significant impact on the effectiveness of DVFS for the CPU or the
  > GPU." (p. 3)

- **Citação Direta Complementar:**
  > "We observe that this kernel saturates the overall shared-memory bandwidth primarily due
  > to the high rate of memory references from the GPU. The CPU portion of memory demand,
  > which is captured by looking at last-level cache L2 miss rates, is relatively
  > insignificant." (p. 3-4)

- **Paráfrase (Citação Indireta Acadêmica):**
  Em arquiteturas heterogêneas integradas, a hierarquia de memória constitui o principal
  determinante de desempenho, pois CPU e GPU disputam acesso ao mesmo controlador de memória
  e ao barramento DDR compartilhado. Quando a GPU satura a banda disponível com acessos
  intensivos à memória principal, o aumento de frequência da CPU torna-se ineficaz — pois a
  CPU aguarda dados que o controlador não consegue fornecer na taxa necessária — e o incremento
  de clock apenas aumenta o consumo energético sem ganho de desempenho proporcional. Esse
  fenômeno representa uma manifestação do gargalo de Von Neumann em escala de chip (Paul
  et al., 2013, p. 3-4).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre Gargalo de
  Von Neumann e Hierarquia de Memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Relógio da memória (MHz)` e `Relação do relógio da memória (x)`:
    frequência operacional do barramento DDR — **Máquina D opera a 1333 MHz em Single Channel**,
    maximizando esse gargalo.
  - `maqX_rodada_YY.CSV` → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: vazão
    real do subsistema de memória/armazenamento durante o benchmark.
  - `maqX_rodada_YY.CSV` → `Carga da memória física (%)`: pressão sobre a RAM física.
  - `maqX_rodada_YY.CSV` → `Carga do controlador de memória GPU (%)`: contenda da GPU pelo
    controlador de memória — cruzar com `Taxa de leituras (MB/s)` e `Carga da memória física (%)`.
  - `maqX_rodada_YY.CSV` → `Uso de memória GPU (%)` e `GPU D3D Uso (avg) (%)`: utilização
    da memória pela GPU integrada (iGPU/MX130).
  - `maqX_rodada_YY.CSV` → `Relógio efetivo médio (MHz)`: clock efetivo da CPU — comparar
    com `Relógio da memória (MHz)` para identificar desproporção (CPU rápida, RAM lenta).
  - `maqX_rodada_YY.CSV` → Parâmetros de tempo de acesso à memória: `Tcas (T)`, `Trcd (T)`,
    `Trp (T)`, `Tras (T)`, `Trc (T)`, `Trfc (T)`: latências do barramento DDR.

---

### 3.5 — Sensibilidade de Frequência e Eficiência por Watt

- **Conceito/Teoria:** Sensibilidade de frequência como métrica de retorno de desempenho por
  incremento de clock — base para cálculo de eficiência Desempenho/Watt.

- **Citação Direta (Ipsis Litteris):**
  > "Frequency sensitivity is a time-varying function of the workload on a target processor.
  > In general, the frequency-performance function is unknown. Thus, the idea is to measure
  > the frequency sensitivity of an application periodically and determine whether it is
  > productive (efficient) to change the frequency." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  A sensibilidade de frequência quantifica o ganho de desempenho obtido por unidade de
  incremento de clock e varia dinamicamente ao longo da execução de um programa. Aplicações
  limitadas por memória (memory-bound) apresentam baixa sensibilidade de frequência da CPU —
  pois o gargalo está no barramento DDR e não nas unidades de execução — enquanto aplicações
  intensivas em computação (compute-bound) exibem alta sensibilidade. Essa distinção é
  fundamental para calcular a relação Desempenho por Watt: aumentar o clock de uma aplicação
  memory-bound eleva o consumo energético sem retorno proporcional de desempenho, reduzindo
  a eficiência energética (Paul et al., 2013, p. 3).

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** — subseção de Eficiência
  Energética e Desempenho por Watt.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqX.txt` → `Single_Core` e `Multi_Core`: numerador da razão Desempenho/Watt.
  - `maqX_rodada_YY.CSV` → `Potência total da CPU (W)`: denominador da razão Desempenho/Watt.
  - **Fórmula sugerida para o artigo:**
    `Desempenho por Watt = Score_Geekbench6 / Média(Potência total da CPU [W])`
  - `maqX_rodada_YY.CSV` → `Relógios efetivos núcleo (avg) (MHz)` vs. `scores_maqX.txt`:
    cruzamento para cálculo de IPC relativo entre máquinas.
  - `maqX_rodada_YY.CSV` → `Uso total da CPU (%)`: taxa de utilização — máquina compute-bound
    mostrará valores próximos de 100%; memory-bound mostrará subutilização com latências.
  - `maqX_rodada_YY.CSV` → `Core C0 Ocupação (avg) (%)` e `Core 0-3 T0/T1 C0 Ocupação (%)`:
    fração de tempo em que os núcleos estão em estado ativo (C0) — alta ocupação indica
    workload compute-bound; baixa ocupação sugere limitação de memória.

---

### 3.6 — ED² (Energy-Delay Squared) como Métrica de Eficiência Energética

- **Conceito/Teoria:** Produto Energia × Atraso² como figura de mérito para avaliar
  trade-offs entre eficiência energética e desempenho em HPC.

- **Citação Direta (Ipsis Litteris):**
  > "We report performance, power, and energy efficiency (energy-delay² product) for the two
  > variants of DynaCo algorithm. We picked ED² because it has been widely used in HPC
  > analysis and it captures the importance of both power and performance, the latter being
  > critical for HPC." (p. 8)

- **Paráfrase (Citação Indireta Acadêmica):**
  O produto energia-atraso ao quadrado (ED²) é amplamente adotado em análises de HPC por
  capturar simultaneamente a importância da eficiência energética e do desempenho: penaliza
  fortemente soluções que sacrificam desempenho em prol de economia de energia, equilibrando
  os dois objetivos. Em sistemas com restrições de TDP, otimizar o ED² é mais informativo
  do que otimizar energia ou desempenho isoladamente (Paul et al., 2013, p. 8).

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** — subseção de métricas de
  avaliação comparativa.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqX.txt` → `Single_Core` e `Multi_Core`: proxy de desempenho para cálculo do ED².
  - `maqX_rodada_YY.CSV` → `Potência total da CPU (W)` integrada ao longo do tempo de cada
    rodada: energia consumida = Potência × Tempo.
  - **Nota:** O tempo de execução do Geekbench 6 não é registrado diretamente nas colunas,
    mas pode ser inferido pelo número de amostras de cada CSV multiplicado pelo intervalo de
    amostragem do HWiNFO64.

---

### 3.7 — Comportamento de Fase e Variabilidade Temporal da Carga (Workload Phase Behavior)

- **Conceito/Teoria:** Variação temporal da carga de trabalho entre fases de alta e baixa
  utilização de CPU/GPU — causa de variabilidade nos resultados de benchmark.

- **Citação Direta (Ipsis Litteris):**
  > "Each application has phases that vary in their frequency sensitivity due to the type of
  > their activity rates and the degree of performance-coupling between CPU and GPU." (p. 4)

- **Citação Direta Complementar:**
  > "We attribute the relatively higher performance loss in miniMD to the impact of
  > variability in kernel phases shorter than our 10-ms sampling interval limitation." (p. 8)

- **Paráfrase (Citação Indireta Acadêmica):**
  Aplicações reais exibem comportamento de fase (*phase behavior*), alternando entre períodos
  de alta utilização de CPU, alta utilização de GPU, ou limitação por memória. Essa variação
  temporal da demanda computacional é uma das causas de variabilidade nos scores de benchmark:
  quando o intervalo de amostragem do monitor de telemetria é maior do que a duração de algumas
  fases, transições rápidas de carga não são capturadas, e os resultados apresentam ruído
  estatístico. Esse efeito é análogo ao que observamos nas 20 rodadas do Geekbench 6, onde
  o desvio padrão dos scores reflete a instabilidade de estados térmicos e de frequência
  ao longo das rodadas (Paul et al., 2013, p. 4 e 8).

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** — análise do desvio padrão
  amostral entre as 20 rodadas e sua interpretação arquitetural.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Uso total da CPU (%)` ao longo do tempo: evidencia as fases da
    aplicação dentro de cada rodada.
  - `maqX_rodada_YY.CSV` → `Carga do núcleo da GPU (%)`: fases de alto e baixo uso da GPU.
  - `maqX_rodada_YY.CSV` → `Relógios efetivos núcleo (avg) (MHz)`: variação do clock efetivo
    entre fases — queda brusca indica throttling ou entrada em estados C de baixa potência.
  - `scores_maqX.txt` → desvio padrão amostral entre as 20 linhas de `Single_Core` e
    `Multi_Core`: métrica estatística direta do efeito de variabilidade.

---

### 3.8 — Divergência de Controle e Impacto no Clock Efetivo da GPU

- **Conceito/Teoria:** Divergência de fluxo de controle em GPUs como causa de subutilização
  das unidades SIMD, afetando a relação entre clock nominal e clock efetivo.

- **Citação Direta (Ipsis Litteris):**
  > "GPUs are exceptional execution engines for data-parallel workloads with little control
  > divergence. However, performance efficiency degrades significantly with increasing control
  > divergence. [...] higher-frequency operation leads to faster re-convergence, and thus
  > shorter execution time." (p. 4)

- **Paráfrase (Citação Indireta Acadêmica):**
  As GPUs são otimizadas para cargas de trabalho data-paralelas com fluxo de controle
  uniforme. Quando há divergência de controle — isto é, diferentes threads de um mesmo
  *warp* seguem ramos distintos do código — as unidades SIMD serializam a execução, reduzindo
  a eficiência e produzindo um clock efetivo inferior ao clock nominal configurado. O
  monitoramento do clock efetivo da GPU revela essa subutilização em tempo real (Paul et al.,
  2013, p. 4).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre arquiteturas
  GPU integradas e paralelismo SIMD.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `GPU Clock (MHz)`: clock nominal configurado para a GPU.
  - `maqX_rodada_YY.CSV` → `Relógio efetivo da GPU (MHz)`: clock efetivo real — diferença
    entre nominal e efetivo indica subutilização por divergência ou limitação.
  - `maqX_rodada_YY.CSV` → `Carga do núcleo da GPU (%)` e `GPU D3D Uso (avg) (%)`:
    percentual de ocupação das unidades de execução.
  - `maqX_rodada_YY.CSV` → `GPU Computing (Compute_0) Uso (%)` e
    `GPU Computing (Compute_1) Uso (%)`: utilização dos motores de computação da GPU.

---

### 3.9 — Acoplamento de Desempenho CPU-GPU e Starving da GPU

- **Conceito/Teoria:** Dependência de desempenho entre CPU e GPU em arquiteturas integradas —
  redução excessiva do clock da CPU causa "fome" (starving) da GPU por dados.

- **Citação Direta (Ipsis Litteris):**
  > "For peak GPU utilization, the CPU must deliver data to the GPU at a certain rate;
  > otherwise, the GPU will starve, resulting in a reduction in overall performance." (p. 4)

- **Citação Direta Complementar:**
  > "The memory-bounded behavior of Neighbor makes it insensitive to CPU frequency with
  > minimal performance loss at the lower CPU DVFS state of P4. The GPU compute-intensive
  > nature of Force makes it less dependent on CPU frequency; however, decreasing CPU
  > frequency beyond P2 starts starving the GPU." (p. 5)

- **Paráfrase (Citação Indireta Acadêmica):**
  O acoplamento de desempenho entre CPU e GPU integradas impõe que o clock da CPU não pode
  ser reduzido indiscriminadamente durante fases de alta demanda da GPU. Se o processador
  principal reduzir sua frequência abaixo de um limiar crítico, o ritmo de fornecimento de
  dados e instruções de controle à GPU cai, levando à subutilização da GPU por escassez de
  trabalho disponível (*GPU starving*). Essa interdependência é especialmente relevante para
  a Máquina D (i5-8265U com GPU UHD 620 integrada), onde CPU e iGPU compartilham o mesmo
  pacote e a mesma memória RAM Single Channel (Paul et al., 2013, p. 4-5).

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão** — cruzamento entre uso de
  CPU e GPU durante o benchmark.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Uso total da CPU (%)` e `Carga do núcleo da GPU (%)`: cruzamento
    para identificar fases de CPU ativa fornecendo dados à GPU.
  - `maqX_rodada_YY.CSV` → `GPU GT Uso (%)` e `IGPU Potência (W)`: utilização e consumo da
    GPU integrada (iGPU) — relevante para Máquina D.
  - `maqX_rodada_YY.CSV` → `iGPU VID (V)`: tensão da GPU integrada durante operação.
  - `maqX_rodada_YY.CSV` → `Relógios efetivos núcleo (avg) (MHz)` vs. `Carga do núcleo da
    GPU (%)`: quando o clock efetivo cai e a GPU também cai, confirma o efeito de starving.

---

### 3.10 — Modelo Analítico de Regressão para Sensibilidade de Frequência

- **Conceito/Teoria:** Uso de regressão linear ponderada para modelar a relação entre métricas
  de hardware e sensibilidade de frequência — base metodológica para análise estatística.

- **Citação Direta (Ipsis Litteris):**
  > "We performed a correlation analysis between each performance counter/metric and the CPU
  > or GPU frequency sensitivity, measured as the ratio of the difference in execution times
  > to the corresponding differences in frequency. We computed the correlation coefficients
  > using linear regression." (p. 6)

- **Citação Direta Complementar:**
  > "The correlation coefficient using this combination of metrics improved to 0.97." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  A análise de correlação entre contadores de desempenho de hardware e a sensibilidade de
  frequência, realizada por meio de regressão linear, permite identificar quais métricas são
  preditores eficazes do comportamento do sistema sob variações de clock. Paul et al. (2013)
  alcançaram coeficiente de correlação de 0,97 combinando métricas de utilização de ALU
  ponderada pelo clock da GPU, utilização de memória agregada CPU-GPU, e UPC (*micro-operations
  per cycle*) ponderado pelo clock, demonstrando que a abordagem multivariada supera preditores
  univariados (p. 6).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificativa para o uso de média
  aritmética e desvio padrão amostral como instrumentos estatísticos, e **Resultados e
  Discussão** — correlação entre telemetria e scores de benchmark.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqX.txt` → variável dependente `Single_Core` ou `Multi_Core` em análise de
    correlação com colunas de telemetria.
  - `maqX_rodada_YY.CSV` → `Relógios efetivos núcleo (avg) (MHz)`: variável independente
    principal para correlação com scores.
  - `maqX_rodada_YY.CSV` → `Potência total da CPU (W)`: variável independente para
    correlação com scores e cálculo de eficiência.
  - **Script Python sugerido:** calcular coeficiente de Pearson entre a média por rodada de
    `Relógios efetivos núcleo (avg) (MHz)` e o `Single_Core` correspondente de
    `scores_maqX.txt`, para cada máquina separadamente.

---

> ## ATUALIZAÇÃO — NOVAS CITAÇÕES VINCULADAS À TABELA COMPLETA DE HARDWARE (6 MÁQUINAS)
>
> As subseções **3.11 a 3.16** abaixo foram acrescentadas após o recebimento da tabela
> comparativa completa (Máquinas A, B, C, D, E e F), substituindo o cenário anterior de
> "dados pendentes" para as Máquinas A, B e C, e introduzindo as Máquinas E e F (desktops).
> Cada subseção indica explicitamente **qual componente da tabela** ativa a citação e
> **como utilizá-la** na redação do artigo.

---

### 3.11 — TDP Elevado e Orçamento Térmico em Processadores Desktop de Alto Desempenho

- **Componente que ativa esta citação:** TDP Base da CPU — **Máquina E (65 W, Ryzen 5 5500)**
  e **Máquina F (125 W, i5-14600KF)**, em contraste direto com o TDP de 15 W das Máquinas
  B, C e D, e os 45 W da Máquina A.

- **Conceito/Teoria:** Escala de TDP como determinante do espaço de operação de DVFS — quanto
  maior o envelope térmico/energético, maior a margem para o algoritmo de gerenciamento de
  energia sustentar estados de boost sem throttling.

- **Citação Direta (Ipsis Litteris):**
  > "We used the AMD A10-5800 desktop APU with 100W TDP as the baseline for all our
  > experiments and analysis. Base CPU frequency is 3.8GHz, with boost frequency up to
  > 4.2GHz." (p. 7)

- **Citação Direta Complementar:**
  > "Although temperature tracks power and inversely tracks performance, it never reaches the
  > peak thermal limits. This means that the performance of the CUs and the GPU are not
  > constrained by temperature, and therefore they generally run at their maximum frequency."
  > (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  Processadores desktop com TDP elevado — como os 65 W do Ryzen 5 5500 (Máquina E) e,
  sobretudo, os 125 W do Core i5-14600KF (Máquina F) — dispõem de um envelope térmico
  significativamente maior do que processadores móveis de baixo consumo (15 W), análogo ao
  cenário de 100 W TDP descrito por Paul et al. (2013) como baseline experimental. Nesse
  regime, é esperado que o processador raramente atinja os limites térmicos críticos durante
  cargas de benchmark de curta duração, permanecendo a maior parte do tempo em estados de
  *boost* de frequência máxima, à semelhança do comportamento relatado pelos autores para a
  AMD A10-5800 (Paul et al., 2013, p. 3 e 7).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** (caracterização do hardware — contraste
  de TDP entre notebooks e desktops) e **Resultados e Discussão** (justificativa para a
  expectativa de menor incidência de throttling nas Máquinas E e F frente às Máquinas B, C e D).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqE_rodada_YY.CSV` e `maqF_rodada_YY.CSV` → `Potência total da CPU (W)`: comparar o
    consumo real sustentado contra os 65 W e 125 W nominais, respectivamente.
  - `maqE_rodada_YY.CSV` e `maqF_rodada_YY.CSV` → `Limite de potência PL1 (Static) (W)` e
    `Limite de potência PL2 (Static) (W)`: nos desktops, espera-se PL2 substancialmente acima
    do TDP base, refletindo maior margem de boost de curto prazo (especialmente no i5-14600KF).
  - `maqE_rodada_YY.CSV` e `maqF_rodada_YY.CSV` → `Estrangulamento térmico do núcleo (avg)
    (Yes/No)`: hipótese a validar — incidência esperada **menor** do que nas Máquinas B, C, D.
  - `scores_maqE.txt` e `scores_maqF.txt` → comparar desvio padrão de `Multi_Core` com o das
    Máquinas B/C/D: TDP maior tende a correlacionar com menor variabilidade entre rodadas.

---

### 3.12 — Dual Channel Real vs. Single Channel: Validação Empírica do Gargalo de Banda

- **Componente que ativa esta citação:** Topologia/Canais da RAM — **Máquinas A, B, E e F em
  Dual Channel** (DDR5 5200 MT/s, DDR4 2666 MHz, DDR4 não especificado e DDR4 3600 MHz,
  respectivamente) versus **Máquinas C e D em Single Channel** (DDR4 2400 MHz e DDR4 2400 MHz).

- **Conceito/Teoria:** Duplicação da banda agregada de memória em configuração Dual Channel,
  reduzindo a contenção de acesso e mitigando o gargalo de Von Neumann em cargas que dependem
  de throughput de memória.

- **Citação Direta (Ipsis Litteris):**
  > "The memory hierarchy is a key determinant of performance, and the CPU and the GPU share
  > the Northbridge and memory controllers. The extent of interference at these points (which
  > is time-varying) has a significant impact on the effectiveness of DVFS for the CPU or the
  > GPU." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  Diferentemente do cenário hipotético abordado na seção 3.4 (à época sem dados reais de
  Dual Channel no grupo), agora dispomos de comparação empírica direta: as Máquinas A, B, E
  e F operam em Dual Channel, dobrando o número de vias de acesso simultâneo ao controlador
  de memória em relação às Máquinas C e D (Single Channel). Segundo a lógica de compartilhamento
  de recursos descrita por Paul et al. (2013), a configuração Dual Channel amplia a banda
  agregada disponível, reduzindo a probabilidade de que o subsistema de memória se torne o
  fator limitante durante cargas de benchmark com pegada de memória elevada — efeito que deve
  se refletir em scores Multi-Core proporcionalmente mais altos e em menor variabilidade entre
  rodadas para as máquinas em Dual Channel (Paul et al., 2013, p. 3).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (já citada na seção 3.4 — aqui
  reforçada com dados reais) e **Resultados e Discussão** — comparação direta Single vs. Dual
  Channel com 4 máquinas de cada grupo, agora com poder estatístico muito maior do que o cenário
  preditivo original (apenas a Máquina D).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA/B/E/F_rodada_YY.CSV` → `Relógio da memória (MHz)` e `Taxa de leituras/gravações
    (MB/s)`: comparar diretamente contra `maqC/D_rodada_YY.CSV` para quantificar o ganho real
    de throughput em Dual Channel.
  - `scores_maqA/B/E/F.txt` vs. `scores_maqC/D.txt` → coluna `Multi_Core`: é a comparação
    central da seção — cargas multi-thread são mais sensíveis a banda de memória do que
    cargas single-thread.
  - `maqX_rodada_YY.CSV` → `Carga da memória física (%)`: cruzar com o tipo de canal para
    verificar se Single Channel acarreta picos de carga mais agudos sob a mesma tarefa.
  - **Nota estatística:** com 4 máquinas em Dual Channel (A, B, E, F) e 2 em Single Channel
    (C, D), o grupo já possui base suficiente para um teste estatístico comparativo (ex.:
    teste t para amostras independentes) entre as médias de `Multi_Core`, fortalecendo a
    seção de Resultados além da simples observação descritiva.

---

### 3.13 — GPU Dedicada com Maior Largura de Barramento PCIe (Acoplamento CPU-GPU Discreto)

- **Componente que ativa esta citação:** Interface de Barramento GPU — **Máquina A (RTX 4050
  Laptop, PCIe 4.0 x8)**, **Máquina E (RX 7600, PCIe 4.0 x8)** e **Máquina F (RTX 3050, PCIe
  4.0 x8)**, em contraste com a **Máquina D (MX130, PCIe 3.0 x4)**.

- **Conceito/Teoria:** Embora o artigo trate de GPU *integrada* (APU), o princípio de
  acoplamento de desempenho e de compartilhamento de largura de banda entre CPU e GPU se
  estende, por analogia, à interface PCIe que conecta a CPU a uma GPU dedicada — quanto maior
  a geração e o número de *lanes* PCIe, menor a limitação de tráfego de dados entre os
  componentes.

- **Citação Direta (Ipsis Litteris):**
  > "For peak GPU utilization, the CPU must deliver data to the GPU at a certain rate;
  > otherwise, the GPU will starve, resulting in a reduction in overall performance." (p. 4)

- **Paráfrase (Citação Indireta Acadêmica):**
  O princípio de que a CPU deve sustentar uma taxa mínima de fornecimento de dados para evitar
  a subutilização (*starving*) da GPU, descrito originalmente para GPUs integradas que
  compartilham o controlador de memória on-die, aplica-se também — com a devida ressalva
  arquitetural — ao tráfego entre CPU e GPU discreta via barramento PCIe. Uma interface PCIe
  4.0 x8 (Máquinas A, E e F) oferece o dobro da largura de banda teórica de uma interface PCIe
  3.0 x4 (Máquina D), reduzindo a probabilidade de que o próprio barramento se torne o
  estrangulador de desempenho em cargas que demandam transferência intensiva de dados entre
  CPU e GPU (Paul et al., 2013, p. 4).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — extensão do conceito de
  acoplamento CPU-GPU (originalmente da seção 3.9) para arquiteturas com GPU discreta —, com
  ressalva clara de que o artigo-fonte trata de GPU integrada e a extensão para PCIe é uma
  inferência analógica do grupo, não uma afirmação direta dos autores.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA/E/F_rodada_YY.CSV` → `Velocidade do link PCIe (GT/s)`: validar a geração/velocidade
    real negociada pelo link durante o benchmark.
  - `maqA/E/F_rodada_YY.CSV` → `Carga do barramento GPU (%)`: indicador direto de saturação do
    link PCIe.
  - `maqD_rodada_YY.CSV` → mesma coluna `Carga do barramento GPU (%)` para a MX130 (PCIe 3.0
    x4) — comparação direta da saturação relativa do barramento entre gerações distintas.
  - `maqX_rodada_YY.CSV` → `Receiver Errors`, `Replay Count`, `Correctable Error Count`
    (contadores PCI Express Error Counters): uso diagnóstico para verificar integridade do
    link, especialmente relevante caso haja diferença inesperada de desempenho não explicada
    por clock ou potência.
  - **Ressalva metodológica:** como o Geekbench 6 é majoritariamente um benchmark de CPU (os
    scores `Single_Core`/`Multi_Core` não exercitam a GPU dedicada), esta análise é mais
    relevante como **discussão teórica complementar** do que como evidência estatística direta
    extraída de `scores_maqX.txt`.

---

### 3.14 — Cache L3 e seu Papel na Mitigação do Gargalo de Memória (Escala Ampliada)

- **Componente que ativa esta citação:** Cache L3 Total — variação de **4 MB (Máquina C)** a
  **24 MB (Máquina F)**, passando por 6 MB (D), 12 MB (A e B) e 16 MB (E).

- **Conceito/Teoria:** A cache L3 atua como camada de amortecimento entre os núcleos de CPU e
  o controlador de memória, reduzindo o número de acessos que efetivamente chegam ao barramento
  DDR compartilhado — quanto maior a L3, menor a pressão sobre a banda de memória principal,
  fenômeno coerente com a discussão de interferência de banda do artigo-base.

- **Citação Direta (Ipsis Litteris):**
  > "The CPU portion of memory demand, which is captured by looking at last-level cache L2
  > miss rates, is relatively insignificant. Further (not shown), the CPU IPC of this kernel
  > is higher than a typical memory-bound application." (p. 3-4)

- **Paráfrase (Citação Indireta Acadêmica):**
  Paul et al. (2013) utilizam a taxa de *miss* na cache de último nível (LLC) como indicador
  da real demanda de memória principal imposta pela CPU, demonstrando que uma cache eficiente
  reduz substancialmente os acessos que extrapolam o chip. Por extensão, processadores com
  cache L3 maior — como os 24 MB do i5-14600KF (Máquina F) ou os 16 MB do Ryzen 5 5500
  (Máquina E) — tendem a reter um volume maior do *working set* da aplicação dentro do chip,
  reduzindo a frequência de acessos à DRAM e, consequentemente, amenizando o gargalo de Von
  Neumann mesmo em configurações de memória menos favoráveis. Já processadores com L3 reduzida,
  como os 4 MB do Ryzen 5 3500U (Máquina C), apresentam maior dependência da banda de memória
  externa para sustentar a taxa de acerto necessária (Paul et al., 2013, p. 3-4).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção de Hierarquia de
  Memória (reforça e amplia a seção 3.4, agora com 6 valores distintos de L3 para correlacionar).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqX.txt` → `Single_Core` e `Multi_Core` correlacionados com o tamanho nominal de
    L3 de cada máquina (4, 6, 12, 12, 16 e 24 MB) — análise de dispersão (scatter) com 6 pontos.
  - `maqX_rodada_YY.CSV` → `Carga da memória física (%)` e `Taxa de leituras (MB/s)`: máquinas
    com L3 menor (C: 4 MB) devem apresentar picos de tráfego de memória relativamente mais
    intensos sob a mesma carga de trabalho, na ausência de outros fatores confundidores
    (clock, canais de RAM).
  - **Ressalva estatística:** o HWiNFO64, conforme listado na estrutura de colunas do projeto,
    não expõe diretamente a taxa de *miss* da cache L3 (não há coluna equivalente a "LLC miss
    rate"). A validação desta citação no nosso conjunto de dados é, portanto, **indireta** —
    via cruzamento de tráfego de memória observado (`Taxa de leituras/gravações`) e não via
    medição direta de *cache misses*, o que deve ser explicitado como limitação metodológica
    na seção de Discussão.

---

### 3.15 — Litografia e Microarquitetura como Fatores de Eficiência Energética Intrínseca

- **Componente que ativa esta citação:** Microarquitetura/Litografia — variação de **14 nm
  (Whiskey Lake-U, Máquina D)** e **12 nm (Zen+, Máquina C)** até **Intel 7 (Raptor Lake,
  Máquinas A e F)** e **7 nm (Zen 3, Máquina E)**.

- **Conceito/Teoria:** A litografia do processo de fabricação influencia diretamente a
  potência dinâmica dissipada por ciclo de clock (proporcional a $C \cdot V^{2} \cdot f$),
  de modo que nós de fabricação mais avançados permitem maior frequência de operação dentro
  do mesmo envelope térmico — relação implícita na discussão de Paul et al. (2013) sobre como
  o BAPM ajusta tensão e frequência para maximizar o uso da capacidade térmica disponível.

- **Citação Direta (Ipsis Litteris):**
  > "Once BAPM has assigned power limits, each CU and GPU manages its own frequencies and
  > voltages to fit in the assigned limit (i.e., local to a unit, the hardware will employ
  > DVFS to keep the power dissipation in the assigned limit)." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  O mecanismo de DVFS descrito pelos autores ajusta tensão e frequência para que a potência
  dissipada permaneça dentro do limite atribuído a cada unidade. Como a potência dinâmica é
  proporcional ao quadrado da tensão de operação, processadores fabricados em nós litográficos
  mais avançados (como o Zen 3 de 7 nm da Máquina E) tendem a operar com tensões mais baixas
  para uma mesma frequência-alvo, dissipando menos potência por ciclo e, consequentemente,
  dispondo de maior margem térmica para sustentar estados de boost por períodos mais longos
  em comparação a processos mais antigos, como os 14 nm da Máquina D (Whiskey Lake-U) — um
  nó já distante da fronteira tecnológica vigente (Paul et al., 2013, p. 3).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção complementar sobre
  Escalonamento Tecnológico (*technology scaling*) e sua relação com DVFS, articulada com a
  seção 3.1 (DVFS e P-States).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqX_rodada_YY.CSV` → `Core VIDs (avg) (V)`: comparar a tensão média de operação entre
    máquinas de litografias distintas sob carga equivalente.
  - `maqX_rodada_YY.CSV` → `Relógios efetivos núcleo (avg) (MHz)` e `Potência total da CPU
    (W)`: calcular a potência dissipada por MHz efetivo (W/MHz) como proxy comparativo de
    eficiência por nó tecnológico.
  - **Ressalva teórica:** esta correlação é fortemente confundida por outras variáveis (TDP de
    projeto, número de núcleos, arquitetura P-core/E-core dos chips Raptor Lake). A citação
    deve ser usada como **pano de fundo conceitual**, não como prova isolada de causalidade
    direta entre nm e eficiência — o grupo deve frisar essa limitação na Discussão.

---

### 3.16 — Instruções Vetoriais Avançadas (AVX/VNNI) e Throughput em Benchmarks Multi-Core

- **Componente que ativa esta citação:** Instruções Avançadas (CPU) — presença de **Intel DL
  Boost (VNNI)** nas Máquinas A, B, D e F, ausente nas Máquinas C e E (que possuem apenas
  AVX/AVX2/FMA3, por serem CPUs AMD Zen+/Zen 3 nesta geração).

- **Conceito/Teoria:** Extensões de conjunto de instruções (ISA) que ampliam a largura de
  registradores SIMD ou adicionam instruções fundidas (*fused* multiply-add) elevam o número
  de operações de ponto flutuante por ciclo — conceito de paralelismo a nível de dados (DLP)
  complementar ao paralelismo a nível de instrução/thread discutido no artigo-base ao
  caracterizar unidades de execução SIMD em GPU.

- **Citação Direta (Ipsis Litteris):**
  > "The GPU consists of 384 AMD Radeon™ cores, each capable of one single-precision fused
  > multiply-add computation (FMAC) operation per cycle [...]. The GPU is organized as six
  > SIMD units, each containing 16 processing units that are each four-way VLIW." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora o trecho original descreva a organização SIMD/VLIW da GPU do APU estudado, o
  princípio de unidades de execução capazes de realizar operações fundidas de multiplicação-
  soma (*fused multiply-add*) por ciclo é diretamente análogo ao funcionamento das instruções
  AVX2/FMA3, presentes em todas as seis máquinas do grupo, e ao Intel DL Boost (VNNI),
  presente nas Máquinas A, B, D e F. Tais extensões aumentam o throughput aritmético por ciclo
  de clock sem necessariamente elevar a frequência de operação, constituindo uma forma de
  paralelismo a nível de dados que pode favorecer cargas vetorizáveis do Geekbench 6 nas
  máquinas que dispõem de VNNI, mesmo quando a frequência efetiva ou o TDP não diferem
  proporcionalmente (Paul et al., 2013, p. 2).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre Paralelismo a
  Nível de Instrução e Dados (complementando a seção já prevista sobre ILP/TLP no artigo
  principal).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqX.txt` → `Single_Core`: comparar máquinas com TDP e clock semelhantes mas
    presença/ausência de VNNI (ex.: Máquina D com VNNI vs. Máquina C sem VNNI, ambas com TDP
    de 15 W) para isolar o efeito da ISA.
  - `maqX_rodada_YY.CSV` → `Uso total da CPU (%)` e `Relógios efetivos núcleo (avg) (MHz)`:
    verificar se máquinas com VNNI atingem scores mais altos sem exigir maior utilização
    percentual ou clock mais elevado — evidência indireta de maior eficiência por instrução
    (IPC efetivo superior).
  - **Ressalva metodológica:** o Geekbench 6 inclui subtestes que exploram extensões vetoriais
    (ex.: cargas de Machine Learning), mas o HWiNFO64 não disponibiliza um contador direto de
    "instruções vetorizadas executadas". A validação permanece **qualitativa/comparativa**
    entre máquinas pareadas por TDP e arquitetura, não uma medição direta de utilização de
    VNNI.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 — Fórmula do Produto Energia-Atraso² (ED²)

Derivada da discussão metodológica do artigo (p. 8):

```latex
\begin{equation}
    ED^{2} = E \cdot T^{2} = \left( \bar{P} \cdot T \right) \cdot T^{2} = \bar{P} \cdot T^{3}
    \label{eq:ed2}
\end{equation}
```

Onde:
- $E$ = energia consumida (J)
- $T$ = tempo de execução (s)
- $\bar{P}$ = potência média durante a execução (W) — aproximável pela média da coluna
  `Potência total da CPU (W)` do HWiNFO64.

### 4.2 — Fórmula de Sensibilidade de Frequência (derivada do artigo, p. 6)

```latex
\begin{equation}
    S_{f} = \frac{\Delta T_{exec}}{\Delta f}
    \label{eq:freq_sensitivity}
\end{equation}
```

Onde:
- $S_{f}$ = sensibilidade de frequência
- $\Delta T_{exec}$ = diferença de tempo de execução entre dois estados de frequência
- $\Delta f$ = diferença de frequência entre os dois estados

**Adaptação para o nosso contexto:**

```latex
\begin{equation}
    S_{f,\text{maq}} = \frac{\Delta \text{Score}_{\text{Geekbench6}}}{\Delta \bar{f}_{\text{efetivo}}}
    \label{eq:freq_sensitivity_adapted}
\end{equation}
```

### 4.3 — Fórmula de Eficiência Desempenho por Watt (proposta para o artigo)

```latex
\begin{equation}
    \eta = \frac{\text{Score}_{\text{Geekbench6}}}{\bar{P}_{\text{CPU}}}
    \label{eq:perf_per_watt}
\end{equation}
```

Onde $\bar{P}_{\text{CPU}}$ é a média da coluna `Potência total da CPU (W)` ao longo da
rodada correspondente.

---

### 4.4 — Sugestão de Gráficos Python (Matplotlib) para o Artigo

**Gráfico 1 — Score Geekbench vs. Clock Efetivo Médio por Máquina:**
Barplot com duas séries (Single Core e Multi Core) por máquina, com hastes de erro (σ).
Eixo X secundário indicando `Relógios efetivos núcleo (avg) (MHz)` como linha sobreposta.

**Gráfico 2 — Temperatura Máxima e Ocorrências de Throttling por Máquina:**
Boxplot de `Núcleo máximo (°C)` para as 20 rodadas de cada máquina, com anotação do
número de amostragens onde `Estrangulamento térmico do núcleo (avg)` = "Yes".

**Gráfico 3 — Potência Total da CPU vs. Score (Eficiência Energética):**
Scatter plot com uma linha de tendência por máquina, mostrando a razão Score/Watt.
Referência direta ao conceito de Desempenho por Watt discutido por Paul et al. (2013).

**Gráfico 4 — Taxa de Leitura/Escrita de Memória ao Longo do Tempo (Máquina D):**
Série temporal de `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)` para uma rodada
representativa, evidenciando o gargalo do Single Channel DDR4 1333 MHz.

---

## 5. SUGESTÕES DE BUSCA BIBLIOGRÁFICA (Google Acadêmico)

Para identificar referências complementares de alto impacto, utilize as seguintes
strings de busca exatas:

### Em Inglês (Google Scholar)
1. `"thermal throttling" "benchmark" "CPU" "mobile processor" performance variability`
2. `DVFS "dynamic voltage frequency scaling" "integrated GPU" benchmark performance`
3. `"power limit" "PL1" "PL2" Intel processor thermal management`
4. `"memory bandwidth" "single channel" "dual channel" DDR4 CPU performance impact`
5. `"energy delay product" processor benchmark heterogeneous architecture`
6. `"Geekbench" CPU benchmark methodology validation reproducibility`
7. `"thermal throttling" laptop benchmark variability standard deviation`
8. `"performance per watt" mobile CPU integrated GPU benchmark comparison`
9. `"CPU-GPU shared memory" bandwidth bottleneck integrated processor`
10. `"Von Neumann bottleneck" memory bandwidth CPU performance benchmark`

### Em Português (Google Acadêmico / BDTD)
1. `"estrangulamento térmico" processador benchmark desempenho variabilidade`
2. `"gargalo de memória" "canal único" "dual channel" DDR4 desempenho processador`
3. `"eficiência energética" processador benchmark "desempenho por watt" comparativo`
4. `"hierarquia de memória" "cache" benchmark CPU desempenho arquitetura`
5. `"DVFS" "gerenciamento de energia" processador heterogêneo GPU integrada`
6. `benchmarking processadores "desvio padrão" variabilidade temperatura`

---

## 6. NOTA SOBRE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C)

> ⚠️ **NOTA EDITORIAL — Máquinas A, B e C:**
>
> As seções **3.4** (Interferência de Banda de Memória), **3.9** (Acoplamento CPU-GPU) e
> **4.4** (Gráfico 4 — Taxa de Leitura/Escrita) foram fichadas de forma preditiva para
> capturar o impacto de configurações de memória superiores (Dual Channel, frequências DDR4
> mais altas) e GPUs dedicadas com maior TDP. Os trechos teóricos mapeados — especialmente
> sobre saturação de banda de memória compartilhada e acoplamento CPU-GPU — só serão
> plenamente aproveitados na redação final **se as Máquinas A, B ou C apresentarem
> configuração Dual Channel ou GPU dedicada discreta com maior envelope de potência**.
> Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de
> forma preditiva e **só serão utilizados na redação final conforme as configurações reais de
> hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações,
> se necessário.**

---

## 6-BIS. ATUALIZAÇÃO DO STATUS PREDITIVO — TABELA COMPLETA RECEBIDA (6 MÁQUINAS)

> ✅ **NOTA EDITORIAL DE ATUALIZAÇÃO:**
>
> Com o recebimento da tabela comparativa completa de hardware (Máquinas A, B, C, D, E e F),
> a condição de pendência registrada na **Seção 6** foi **parcialmente superada**:
>
> - A seção **3.4** (Interferência de Banda de Memória) deixa de ser puramente preditiva: as
>   Máquinas A, B, E e F confirmam configuração **Dual Channel real**, permitindo a comparação
>   empírica desenvolvida na nova seção **3.12**.
> - A seção **3.9** (Acoplamento CPU-GPU / Starving) ganha uma extensão para GPU dedicada via
>   PCIe na nova seção **3.13**, cobrindo as Máquinas A, E e F (PCIe 4.0 x8) e mantendo a
>   Máquina D (PCIe 3.0 x4) como referência de barramento mais restrito.
> - A diretriz de **TDP elevado** prevista de forma genérica na Seção 3 do arquivo de
>   diretrizes do projeto agora é tratada com dados reais na nova seção **3.11** (Máquinas E
>   e F, 65 W e 125 W).
>
> **Pendências remanescentes:** os campos marcados com `[Preencher Gabinete]*`,
> `[Preencher MHz]*` (RAM da Máquina E) e `[Preencher Gen]*` (interface de disco da Máquina F)
> ainda não foram informados pelo grupo. As análises das seções 3.11 a 3.16 que dependem
> desses valores específicos (ex.: frequência exata da RAM da Máquina E, geração exata do SSD
> da Máquina F) devem ser tratadas como **estimativas a confirmar** até o preenchimento final
> desses campos pelo grupo.

---

*Fichamento concluído. Arquivo pronto para inclusão no repositório do Overleaf.*
*Referência BibTeX: `paul2013coordinated` — inserir no `sbc-template.bib` e citar com `\cite{paul2013coordinated}`.*
