# FICHAMENTO CIENTÍFICO COMPLETO
## Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí
## Arquivo: `fichamento_CompleteSystemPowerEstimation_Bircher.md`

---

> **VEREDITO DE RELEVÂNCIA:** ✅ **SIM — O documento é altamente útil para o projeto de AOC.**
>
> O artigo de Bircher e John (2012) é um dos trabalhos seminais sobre estimativa de potência em
> sistemas computacionais completos a partir de contadores de desempenho do processador (*performance
> counters*). Ele fundamenta diretamente a relação entre métricas de desempenho (clock, taxa de
> instruções, utilização) e consumo energético, além de discutir explicitamente a interação entre
> CPU, memória, chipset, disco e GPU — exatamente os subsistemas monitorados pelo nosso HWiNFO64.
> O artigo também trata de gerenciamento dinâmico de tensão e frequência (DVFS), *clock gating*,
> estados de energia ociosa (C-states) e a relação entre temperatura, tensão e potência de fuga
> (*leakage power*), todos diretamente mapeáveis às colunas de telemetria coletadas (`Potência total
> da CPU (W)`, `Core VIDs (avg) (V)`, `CPU Inteira (°C)`, `Package C2/C3/C6/C7 Ocupação (%)`, entre
> outras). É uma referência de altíssimo impacto (IEEE Transactions on Computers) para sustentar a
> discussão de Eficiência Microarquitetural (Desempenho por Watt) proposta no escopo do nosso artigo.
> Com o detalhamento completo de hardware das seis máquinas do grupo (A a F), este fichamento foi
> atualizado para incluir comparações específicas de litografia, TDP, núcleos heterogêneos, conjuntos
> de instruções vetoriais, topologia de memória e barramento PCIe (Seções 3.13 a 3.19).

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  BIRCHER, W. Lloyd; JOHN, Lizy K. Complete System Power Estimation Using Processor Performance Events. **IEEE Transactions on Computers**, v. 61, n. 4, p. 563–577, abr. 2012.

- **Código BibTeX Completo (.bib):**

```bibtex
@Article{bircher:12,
  author  = {W. Lloyd Bircher and Lizy K. John},
  title   = {Complete System Power Estimation Using Processor Performance
             Events},
  journal = {{IEEE} Transactions on Computers},
  year    = {2012},
  volume  = {61},
  number  = {4},
  pages   = {563--577},
  month   = apr,
  doi     = {10.1109/TC.2011.47},
  note    = {Publicado eletronicamente em 10~fev.~2010. W.~L.~Bircher:
             Advanced Micro Devices ({AMD}), Austin, TX. L.~K.~John:
             Department of Electrical and Computer Engineering,
             University of Texas at Austin.}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo de Periódico Internacional (IEEE Transactions on Computers — periódico de
  altíssimo impacto na área de Arquitetura de Computadores)
- **Instituição/Editora:** IEEE Computer Society — autores vinculados à Advanced Micro Devices (AMD)
  e à University of Texas at Austin
- **Ano:** 2012 (recebido em mar. 2010; publicado online em fev. 2010; impresso em abr. 2012)
- **Financiamento:** US National Science Foundation (NSF, grant 0429806), IBM e AMD
- **Palavras-Chave Originais:** Energy-aware systems; evaluation; measurement; modeling; power
  management.
- **Resumo do Escopo Geral:**
  O artigo propõe o uso de contadores de desempenho do microprocessador (*performance counters*)
  para a medição online do consumo de potência de um sistema computacional completo, explorando o
  chamado efeito *trickle-down* (efeito cascata) dos eventos de desempenho. Os autores demonstram que
  eventos bem conhecidos no processador — como *cache misses* e transações DMA — podem ser usados
  para estimar o consumo de potência de subsistemas externos ao microprocessador, como memória,
  chipset, disco, I/O e GPU. Os modelos de potência são desenvolvidos e validados empiricamente em
  duas plataformas distintas (um servidor quad-socket Intel Pentium IV Xeon e um desktop AMD
  dual-core com GPU integrada), utilizando cargas de trabalho científicas, comerciais e de
  produtividade (SPEC CPU2000, SPEC CPU2006, SPECjbb, DBT-2, SYSMark2007 e 3DMark06). Os modelos
  resultantes atingem erro médio inferior a 9% por subsistema, permitindo estimar o consumo total de
  energia sem a necessidade de sensores físicos de potência dedicados.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 Efeito *Trickle-Down* (Cascata) dos Eventos de Desempenho

- **Conceito/Teoria:** Eventos de desempenho locais ao processador (cache misses, acessos DMA,
  transações no barramento de memória) propagam-se ("trickle-down") para os demais subsistemas do
  computador, permitindo que um único conjunto de contadores no processador seja usado para estimar
  o consumo de potência de todo o sistema.

- **Citação Direta (Ipsis Litteris):**
  > "Trickle-down power modeling [6] provides an accurate representation of complete-system power
  > consumption using a simple methodology. The approach relies on the broad visibility of
  > system-level events to the processor. This allows accurate, performance counter-based models to
  > be created using events local to the processor." (p. 563)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) demonstram que a modelagem de potência por efeito cascata (*trickle-down*)
  permite representar com precisão o consumo energético de um sistema computacional completo a
  partir de uma metodologia simples, fundamentada na visibilidade ampla que o processador possui
  sobre eventos ocorridos em nível de sistema. Dessa forma, modelos confiáveis baseados em contadores
  de desempenho podem ser construídos utilizando exclusivamente eventos locais ao processador, sem
  exigir sensores dedicados em cada subsistema.

- **Onde Encaixar no Artigo LaTeX:** Introdução (justificativa metodológica) e Fundamentação Teórica
  — subseção de Consumo Energético e Eficiência Microarquitetural.

- **Mapeamento de Colunas e Arquivos de Teste:**
  Este conceito sustenta teoricamente o uso conjunto, em nossa metodologia, das colunas de
  telemetria centradas no processador para inferir o comportamento de subsistemas inteiros:
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`, `Potência de núcleos IA (W)`, `Potência total
    de DRAM (W)`, `Potência do System Agent (W)`: medidas que, na prática, derivam de contadores
    internos de desempenho (RAPL) — exatamente o tipo de abordagem "sem sensores externos" defendida
    pelos autores.
  - `maqD_rodada_*.CSV` → `Uso total da CPU (%)`, `Relógios efetivos núcleo (avg) (MHz)`: eventos de
    atividade do processador que, segundo a teoria do *trickle-down*, correlacionam-se com o consumo
    de outros subsistemas (memória, disco).

---

### 3.2 Modelo Linear de Potência da CPU em Função de Ciclos Ociosos e Operações Buscadas

- **Conceito/Teoria:** A potência consumida pela CPU pode ser modelada como função linear do
  percentual de tempo ativo (não ocioso) e da taxa de microoperações buscadas por ciclo, evidenciando
  a relação direta entre atividade de pipeline e dissipação de potência dinâmica.

- **Citação Direta (Ipsis Litteris):**
  > "Given that the Pentium IV can fetch three instructions/cycle, the model predicts range of power
  > consumption from 9.25 to 48.6 W. The form of the model is given as follows: $9.3 + 26.5 \times
  > Active\% + 4.3 \times \frac{Fetched\mu ops}{Cycle}$." (p. 568)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) propõem um modelo linear no qual a potência do processador é decomposta em
  um termo de potência estática (consumida mesmo em estado ocioso), um termo proporcional ao
  percentual de tempo em que o processador está ativo (`Active%`) e um termo proporcional à taxa de
  microoperações buscadas por ciclo de clock. Essa formulação evidencia que, mesmo com o processador
  ocioso, há um piso de consumo energético — o que reforça a importância de mecanismos como
  *clock gating* para a redução do consumo em períodos de baixa utilização.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Consumo Energético e Limites
  de Projeto; pode também sustentar a discussão de Resultados sobre a relação entre `Uso total da
  CPU (%)` e `Potência total da CPU (W)`.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Uso total da CPU (%)` (proxy direto para `Active%` do modelo original).
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`: variável dependente equivalente à potência
    modelada pelos autores.
  - `scores_maqD.txt` → colunas `Single_Core`/`Multi_Core`: podem ser cruzadas com a média de
    `Potência total da CPU (W)` para estimar a métrica de Desempenho por Watt, análoga em espírito ao
    uso da taxa de operações buscadas por ciclo como preditor de potência.

---

### 3.3 *Clock Gating* e Redução de Potência em Estado Ocioso

- **Conceito/Teoria:** *Clock gating* é uma técnica de gerenciamento de energia em que o sinal de
  clock é desligado (gateado) para partes do processador que estão ociosas, reduzindo
  significativamente a potência dinâmica consumida sem desligar o circuito.

- **Citação Direta (Ipsis Litteris):**
  > "When the Pentium IV processor is idle, it saves power by gating the clock signal to portions of
  > itself. Idle phases of execution are 'detected' by the processor through the use of the HLT
  > (halt) instruction. [...] This has a significant effect on power consumption by reducing
  > processor idle power from 36 W to 9 W." (p. 566)

- **Paráfrase (Citação Indireta Acadêmica):**
  Conforme descrito por Bircher e John (2012), o processador economiza energia em fases ociosas por
  meio do *clock gating*, técnica acionada quando o sistema operacional executa a instrução de
  parada (HLT) durante períodos de inatividade do escalonador. Os autores quantificam empiricamente
  esse efeito, demonstrando uma redução de aproximadamente 75% na potência ociosa do processador (de
  36 W para 9 W) graças exclusivamente ao desligamento do sinal de clock em unidades não utilizadas.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Termodinâmica e Arquitetura
  / Consumo Energético.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Package C2 Ocupação (%)`, `Package C3 Ocupação (%)`, `Package C6
    Ocupação (%)`, `Package C7 Ocupação (%)`, `Package C8 Ocupação (%)`: colunas que registram a
    ocupação de estados de baixo consumo (C-states), conceitualmente equivalentes ao mecanismo de
    *clock gating* (e *power gating*) descrito pelos autores.
  - `maqD_rodada_*.CSV` → `Core C0 Ocupação (avg) (%)`, `Core C3 Ocupação (avg) (%)`, `Core C7
    Ocupação (avg) (%)`: ocupação por núcleo, permitindo identificar quanto tempo cada núcleo
    permanece em estado ativo (C0) versus estados de economia de energia durante o benchmark.
  - `maqD_rodada_*.CSV` → `Relógios núcleo (avg) (MHz)` próximo de zero ou reduzido em rodadas/
    intervalos específicos pode ser indício indireto de *clock gating* ativo.

---

### 3.4 Cache Misses como Preditor de Potência da Memória (Hierarquia de Memória)

- **Conceito/Teoria:** Faltas na última camada de cache (L3) geram, necessariamente, acessos à
  memória principal (DRAM), de modo que a taxa de *misses* por ciclo é um preditor da potência
  consumida pelo subsistema de memória — desde que o modelo seja válido apenas em faixas moderadas de
  utilização.

- **Citação Direta (Ipsis Litteris):**
  > "A miss in the first-level cache will necessarily generate traffic in higher level caches and or
  > the memory subsystem. [...] Since the number of main memory accesses is directly proportional to
  > the number of L3 misses, it is possible to approximate the number of accesses using only L3
  > misses." (p. 564, 566)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) explicam que uma falta de cache nos níveis inferiores da hierarquia
  necessariamente gera tráfego nos níveis superiores ou na própria memória principal. Por
  consequência, o número de faltas na cache de último nível (L3, no caso estudado) é proporcional ao
  número de acessos à memória DRAM, permitindo aproximar a atividade — e, portanto, a potência —
  do subsistema de memória apenas a partir da taxa de *misses* na L3. Os autores ressaltam, contudo,
  que esse modelo simples falha sob utilização extremamente alta de memória, quando eventos de
  *prefetch* de hardware não capturados pela contagem de *misses* tornam-se relevantes.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  (Cache L3) e Gargalo de Von Neumann.

- **Mapeamento de Colunas e Arquivos de Teste:**
  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA:** O HWiNFO64 coletado pelo nosso grupo não expõe diretamente
  > contadores de *cache misses* por ciclo (métrica disponível apenas via ferramentas como
  > Intel VTune ou `perf`). Este conceito é fichado de forma teórica e qualitativa, servindo de
  > fundamentação indireta. Caso instrumentação adicional seja disponibilizada futuramente para
  > as Máquinas A, B ou C, este mapeamento deverá ser revisitado.
  - Indiretamente, a Cache L3 de 6 MB da Máquina D (i5-8265U) e seu impacto podem ser discutidos
    qualitativamente ao lado de `Relógio da memória (MHz)`, `Taxa de leituras (MB/s)` e `Taxa de
    gravações (MB/s)` (`maqD_rodada_*.CSV`), como proxies observáveis de atividade do subsistema de
    memória, ainda que sem o contador exato de *L3 misses* usado pelos autores.

---

### 3.5 Modelo Quadrático de Potência de Memória via Transações de Barramento (Acessos DMA)

- **Conceito/Teoria:** Em cenários de alta utilização de memória, é necessário incluir não apenas os
  acessos gerados pelo processador, mas também transações DMA originadas por outros agentes (como o
  próprio controlador de memória), resultando em um modelo quadrático mais robusto.

- **Citação Direta (Ipsis Litteris):**
  > "Changing the model to include memory accesses generated by the microprocessors and DMA events
  > resulted in a model that remains valid for all observed bus utilization rates. [...] The model
  > yields an average error rate of 2.2 percent." (p. 569)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores demonstram que, para cargas de trabalho de altíssima intensidade de memória (como o
  benchmark *mcf* do SPEC CPU2000), um modelo baseado apenas em *misses* de cache subestima
  sistematicamente a potência real, pois transações geradas por acesso direto à memória (DMA),
  originadas por dispositivos de I/O e não diretamente pelo processador, também consomem potência
  relevante no barramento de memória. Ao incorporar o total de transações de barramento — somando
  acessos do processador e DMA — o modelo quadrático resultante atinge erro médio de apenas 2,2%.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — Gargalo de Von Neumann (Barramento de
  Memória); Resultados e Discussão, ao justificar limitações de modelos lineares simples.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: representam a
    intensidade de tráfego no subsistema de armazenamento/memória, conceitualmente análogas ao papel
    das transações de barramento no modelo dos autores.
  - `maqD_rodada_*.CSV` → `Relógio da memória (MHz)`, `Relação do relógio da memória (x)`: parâmetros
    de configuração do canal de memória (1333 MHz Single Channel na Máquina D) que delimitam a
    largura de banda disponível, sustentando a discussão sobre o gargalo de Von Neumann em
    comparação com configurações Dual-Channel ou clocks de RAM superiores.

---

### 3.6 DVFS (*Dynamic Voltage and Frequency Scaling*) e sua Relação Exponencial com a Potência

- **Conceito/Teoria:** O escalonamento dinâmico de tensão e frequência (DVFS) permite que o
  processador opere em diferentes combinações de tensão/frequência para economizar energia, sendo
  que a potência dinâmica varia com o quadrado da tensão (V²) e a potência de fuga (*leakage*) varia
  com o cubo da tensão (V³).

- **Citação Direta (Ipsis Litteris):**
  > "Due to the application of DVFS the processor may operate at a range of discrete voltages in
  > order to save power. Changes in voltage have a significant impact on power consumption due to
  > the exponential relationship between voltage and dynamic power ($V^2$) and the cubic relationship
  > between voltage and leakage power ($V^3$)." (p. 571)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) explicam que o DVFS permite a operação do processador em diferentes níveis
  discretos de tensão e frequência conforme a demanda de desempenho, e que pequenas variações de
  tensão têm impacto desproporcionalmente grande no consumo, dado que a potência dinâmica escala
  quadraticamente e a potência de fuga (relevante em processos de fabricação modernos) escala
  cubicamente com a tensão de operação. Por isso, modelos de potência completos para sistemas com
  gerenciamento agressivo de energia, como notebooks, precisam necessariamente incluir tensão e
  frequência como variáveis explícitas, e não apenas métricas de atividade do *pipeline*.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Eficiência Microarquitetural
  (Desempenho por Watt) e Consumo Energético; também sustenta a discussão sobre por que a Máquina D
  (notebook com TDP de 15W) apresenta variação de potência distinta de um desktop.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Core VIDs (avg) (V)`, `Core 0 VID (V)` a `Core 3 VID (V)`: tensão
    requisitada pelos núcleos, variável central do modelo de potência V²/V³ descrito pelos autores.
  - `maqD_rodada_*.CSV` → `Relógios núcleo (avg) (MHz)`, `Relação do relógio do núcleo (avg) (x)`:
    frequência operante, par complementar à tensão no mecanismo de DVFS do Intel SpeedStep/Turbo
    Boost presente no i5-8265U.
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)` cruzada com `Core VIDs (avg) (V)` permite
    visualizar empiricamente a relação não linear entre tensão e potência prevista pela teoria.

---

### 3.7 Temperatura, Potência de Fuga (*Leakage Power*) e Throttling Térmico

- **Conceito/Teoria:** Em altas tensões necessárias para operação em frequências multi-GHz, a
  potência de fuga (*leakage*) torna-se um componente relevante do consumo total, e como a fuga tem
  forte dependência da temperatura, o monitoramento térmico é essencial para a precisão dos modelos
  de potência — fundamentando também o mecanismo de *thermal throttling*.

- **Citação Direta (Ipsis Litteris):**
  > "At the high voltages required for multi-GHz operation, leakage power becomes a major component
  > of power consumption. Also, at idle when dynamic power is nearly eliminated due to clock gating
  > leakage power can be the dominant contributor. Since temperature has a strong relation to leakage
  > power it is necessary to account for this effect by measuring temperature." (p. 571)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores destacam que, em operação a altas tensões — necessária para sustentar frequências da
  ordem de gigahertz —, a potência de fuga passa a representar uma fração significativa do consumo
  total do processador, podendo inclusive dominar o consumo total durante períodos ociosos, quando a
  potência dinâmica é quase eliminada pelo *clock gating*. Como a potência de fuga é fortemente
  dependente da temperatura de junção do chip, os modelos de potência precisos exigem o monitoramento
  direto da temperatura via sensores on-die, evidenciando a relação intrínseca entre arquitetura
  térmica e consumo energético — base teórica do fenômeno de estrangulamento térmico (*thermal
  throttling*), no qual o sistema reduz deliberadamente o clock para conter o aumento de temperatura
  e, por consequência, da potência de fuga.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Termodinâmica e
  Estrangulamento (Thermal Throttling); Resultados e Discussão, ao explicar variações de desempenho
  associadas a temperatura elevada.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `CPU Inteira (°C)`, `Núcleo máximo (°C)`, `Core 0 (°C)` a `Core 3 (°C)`:
    temperatura instantânea, variável central da teoria de potência de fuga.
  - `maqD_rodada_*.CSV` → `Estrangulamento térmico do núcleo (avg) (Yes/No)`, `Core 0 Estrangulamento
    térmico (Yes/No)` a `Core 3 Estrangulamento térmico (Yes/No)`: registro direto da ativação do
    mecanismo de *thermal throttling* previsto pela teoria.
  - `maqD_rodada_*.CSV` → `Distância do núcleo para TjMAX (avg) (°C)`: proximidade do limiar crítico
    de temperatura, relevante para avaliar o risco de ativação da proteção térmica.
  - `maqD_rodada_*.CSV` → `IA: Limite térmico médio em execução (RATL) (Yes/No)`, `IA: PROCHOT
    (Yes/No)`: razões específicas de limitação térmica reportadas pelo Intel RAPL, diretamente
    relacionadas ao mecanismo descrito pelos autores.

---

### 3.8 Estados de Energia Ociosa de Memória (Self-Refresh e Precharge Power Down)

- **Conceito/Teoria:** O subsistema de memória DRAM opera em três modos com diferentes níveis de
  consumo — ativo, *precharge power down* e *self-refresh* —, sendo a transição entre eles controlada
  pelo controlador de memória conforme a duração das fases de inatividade.

- **Citação Direta (Ipsis Litteris):**
  > "This variation is caused by the three modes of operation: self-refresh, precharge power down,
  > and active. Self-refresh represents the lowest power state in which DRAM contents are maintained
  > by on-chip refresh logic. [...] Precharge power down is a higher-power, lower-latency alternative
  > which provides power savings for short idle phases." (p. 575)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) descrevem que a variabilidade do consumo de potência da memória DRAM decorre
  da alternância entre três estados operacionais: o modo ativo, de maior consumo; o modo de
  *precharge power down*, que oferece economia moderada para períodos curtos de ociosidade com baixa
  latência de reativação; e o modo de auto-atualização (*self-refresh*), de menor consumo possível,
  reservado a períodos longos de inatividade do sistema, no qual o conteúdo da memória é preservado
  exclusivamente por lógica de refresh interna ao próprio chip. Essa hierarquia de estados de energia
  é análoga aos C-states do processador, mas aplicada ao subsistema de memória.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória e
  Gargalo de Von Neumann; também relevante para discutir diferenças de RAM Single-Channel vs.
  Dual-Channel sob o aspecto de gerenciamento de energia.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Carga da memória física (%)`, `Memória física utilizada (MB)`: indicam
    indiretamente o quão ativa está a memória, podendo ser cruzadas qualitativamente com períodos de
    baixa atividade do benchmark (idle entre rodadas) para inferir momentos de possível entrada em
    estados de economia.
  - `maqD_rodada_*.CSV` → `Potência total de DRAM (W)`: medida agregada de potência da memória,
    variável de saída diretamente análoga à modelada pelos autores (equações 8 e 9 do artigo
    original, baseadas em `DCTAccess` e `LinkActivepercent`).
  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA:** O HWiNFO64 não expõe diretamente o percentual de tempo em
  > cada estado de energia da DRAM (self-refresh/precharge), de modo que esta correlação permanece
  > qualitativa até que instrumentação adicional seja eventualmente disponibilizada para as Máquinas
  > A, B ou C.

---

### 3.9 Comportamento Bimodal de Potência da GPU e Modelo Baseado em Clocks Não-Gateados

- **Conceito/Teoria:** Em GPUs com gerenciamento agressivo de energia ociosa, o consumo de potência
  tende a ser bimodal — próximo do mínimo quando ociosa (clock gateado) e próximo do máximo quando
  ativa —, permitindo modelos de potência simples baseados apenas na fração de tempo com clocks não
  gateados.

- **Citação Direta (Ipsis Litteris):**
  > "This subsystem has a unique bimodal power consumption. In all cases, GPU power is either near
  > the maximum or minimum levels. [...] This unique behavior leads to the creation of a simple power
  > model. [...] Therefore, it is sufficient to create a power model using only the ratio of time
  > spent with clocks gated." (p. 573–574)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores observam que a GPU integrada estudada (AMD RS780) apresenta um padrão de consumo
  fortemente bimodal: a potência permanece próxima do nível mínimo durante períodos ociosos — graças
  ao *clock gating* agressivo — e salta para próximo do nível máximo durante cargas gráficas
  intensas, sem estados intermediários relevantes. Esse comportamento permite construir um modelo de
  potência simples e de baixo erro (inferior a 1,7%) utilizando exclusivamente a proporção de tempo
  em que os clocks da GPU permanecem ativos (não gateados), sem necessidade de métricas adicionais de
  carga de trabalho gráfica.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Desempenho e Clock de
  Processamento (GPU) e Eficiência Microarquitetural; Resultados e Discussão, ao analisar a GPU
  integrada/discreta da Máquina D durante os testes do Geekbench 6 (que pode utilizar aceleração
  gráfica em alguns subtestes).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `GPU Clock (MHz)`, `Relógio efetivo da GPU (MHz)`: equivalentes diretos ao
    "*nongated clocks*" utilizado no modelo de potência da GPU dos autores.
  - `maqD_rodada_*.CSV` → `Carga do núcleo da GPU (%)`, `GPU D3D Uso (avg) (%)`: indicadores de
    atividade da GPU (Intel UHD 620 e/ou NVIDIA MX130 na Máquina D) que podem evidenciar o
    comportamento bimodal descrito, caso o Geekbench 6 acione testes de Computação/OpenCL ou Vulkan.
  - `maqD_rodada_*.CSV` → `Potência das linhas GPU (avg) (W)`, `GPU Core (NVVDD) Saida de Energia (W)`:
    variável de saída (potência) a ser confrontada com o clock da GPU para validar empiricamente o
    padrão bimodal.

---

### 3.10 Influência da Tecnologia de Processo (Litografia) na Redução de Potência

- **Conceito/Teoria:** A redução do nó de litografia de fabricação (de 130 nm para 45 nm, no exemplo
  do artigo) contribui, junto a outros fatores como DVFS e gerenciamento de energia ociosa, para
  reduções de potência de uma ordem de grandeza entre gerações de processadores.

- **Citação Direta (Ipsis Litteris):**
  > "Not surprisingly, the desktop processor's average power is an order of magnitude less than the
  > server processor. This is largely influenced by process (130 nM in server versus 45 nM in
  > desktop), DVFS (desktop-only) and idle power management." (p. 573)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) atribuem a redução de uma ordem de grandeza no consumo médio de potência
  entre a plataforma servidor (Pentium IV Xeon, processo de 130 nm) e a plataforma desktop (AMD
  dual-core, processo de 45 nm) à combinação de três fatores: o avanço do processo de fabricação
  (litografia menor), a presença de DVFS exclusivamente na plataforma desktop e um gerenciamento de
  energia ociosa mais agressivo. Esse resultado evidencia como a evolução da tecnologia de
  fabricação de semicondutores é, isoladamente, um fator relevante de eficiência energética,
  independentemente das otimizações de software ou arquitetura.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Eficiência Microarquitetural;
  Introdução, ao contextualizar a evolução tecnológica dos processadores estudados.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Diretamente relevante à comparação de hardware na Tabela de especificações: a Máquina D utiliza
    processo de **14 nm** (Intel Whiskey Lake-U), o que, segundo a teoria discutida, tende a produzir
    menor potência de fuga e maior eficiência energética relativa em comparação a processos mais
    antigos das Máquinas A, B ou C (a depender de suas especificações).
  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA:** Este trecho teórico e seu respectivo mapeamento foram fichados
  > de forma preditiva e só serão utilizados na redação final conforme as configurações reais de
  > litografia das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se
  > necessário.
  - `scores_maq*.txt` → cruzamento de `Single_Core`/`Multi_Core` com `Potência total da CPU (W)`
    médias de cada máquina permite uma discussão empírica de Desempenho por Watt influenciada pela
    litografia de cada processador.

---

### 3.11 Métrica de Erro Percentual Médio para Validação de Modelos (Equação de Erro)

- **Conceito/Teoria:** A validação de modelos preditivos de potência é realizada por meio do cálculo
  do erro percentual médio absoluto entre os valores modelados e medidos, amostra a amostra.

- **Citação Direta (Ipsis Litteris):**
  > "The average for each combination of workload and subsystem model is calculated using equation
  > (6)." — Equação: $AverageError = \frac{\sum_{i=1}^{NumSamples} \frac{|Modeled_i - Measured_i|}
  > {Measured_i}}{NumSamples} \times 100\%$ (p. 569)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores definem a métrica de validação de seus modelos como o erro percentual absoluto médio,
  calculado pela diferença absoluta entre o valor modelado e o valor efetivamente medido em cada
  amostra, normalizada pelo valor medido e expressa em percentual, sendo então tirada a média sobre
  todas as amostras da carga de trabalho. Essa métrica de erro relativo é especialmente adequada
  para comparar a precisão de modelos preditivos quando as grandezas medidas variam em escalas
  distintas entre subsistemas (ex.: I/O de baixa variação versus CPU de alta variação).

- **Onde Encaixar no Artigo LaTeX:** Metodologia — subseção de Análise Estatística, como métrica
  complementar (ou alternativa) ao desvio padrão amostral, especialmente se o grupo decidir comparar
  scores do Geekbench 6 com alguma estimativa teórica de desempenho esperado.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - Aplicável conceitualmente à comparação entre o desempenho *esperado* teoricamente (com base em
    clock e cache) e o desempenho *medido* nos arquivos `scores_maq*.txt` (colunas `Single_Core` e
    `Multi_Core`), caso o grupo opte por propor um modelo preditivo simplificado de desempenho.

---

### 3.12 Fórmulas de Média Aritmética e Desvio Padrão Amostral (Validação Estatística)

- **Conceito/Teoria:** O artigo emprega sistematicamente a média e o desvio padrão das medições de
  potência por subsistema (Tabelas 2, 3, 8 e 9 do artigo original) como ferramentas estatísticas
  básicas para caracterizar tanto o nível médio de consumo quanto sua variabilidade entre cargas de
  trabalho.

- **Citação Direta (Ipsis Litteris):**
  > "the average power in Watts for the considered workloads are given in Table 2. Also, workload
  > variation is presented in Table 3 as the standard deviation of the power values in Watts." (p.
  > 567)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) caracterizam o comportamento energético de cada subsistema por meio de duas
  estatísticas complementares: a potência média, que resume o nível típico de consumo durante a
  execução de uma carga de trabalho, e o desvio padrão, que quantifica a variabilidade desse consumo
  ao longo da execução — sendo o desvio padrão elevado um indicativo direto de cargas de trabalho com
  fases de atividade fortemente heterogêneas (ex.: alternância entre fases de alta e baixa
  utilização), enquanto o desvio padrão baixo caracteriza subsistemas com comportamento de potência
  praticamente constante (como o chipset do servidor estudado).

- **Onde Encaixar no Artigo LaTeX:** Metodologia — subseção de Análise Estatística (justificativa
  direta para o uso de média e desvio padrão amostral nas 20 rodadas de cada máquina).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqC.txt`, `scores_maqD.txt` → colunas
    `Single_Core` e `Multi_Core`: aplicação direta de média e desvio padrão amostral sobre as 20
    rodadas de cada máquina.
  - `maq*_rodada_*.CSV` → qualquer coluna numérica de telemetria (`CPU Inteira (°C)`, `Potência total
    da CPU (W)`, `Relógios efetivos núcleo (avg) (MHz)`) pode ser agregada por média e desvio padrão
    intra-rodada e, posteriormente, entre as 20 rodadas de cada máquina, replicando exatamente a
    metodologia estatística empregada pelos autores nas Tabelas 2, 3, 8 e 9 do artigo original.

---

### 3.13 Influência da Litografia (Processo de Fabricação) sobre Potência de Fuga — Aplicação às Seis Máquinas

- **Conceito/Teoria:** Reforçando o conceito já fichado na Seção 3.10, a comparação agora é possível
  de forma quantitativa e direta entre as seis máquinas do grupo, já que dispomos da litografia de
  fabricação de cada processador: Intel 7 (10 nm classe aprimorada) nas Máquinas A, B e F; 14 nm na
  Máquina D; 12 nm (GlobalFoundries) na Máquina C; e 7 nm (TSMC) na Máquina E.

- **Citação Direta (Ipsis Litteris):**
  > "Not surprisingly, the desktop processor's average power is an order of magnitude less than the
  > server processor. This is largely influenced by process (130 nM in server versus 45 nM in
  > desktop), DVFS (desktop-only) and idle power management." (p. 573)

- **Paráfrase (Citação Indireta Acadêmica):**
  Como descrito por Bircher e John (2012), processos de fabricação mais avançados (menor litografia)
  reduzem substancialmente a potência de fuga e, por consequência, o consumo total do processador para
  um mesmo nível de atividade. Aplicando esse princípio ao nosso conjunto de seis máquinas, espera-se
  que a Máquina E (Ryzen 5 5500, Zen 3, processo de 7 nm da TSMC) apresente a maior eficiência
  energética relativa entre os processadores de desktop, enquanto a Máquina D (i5-8265U, Whiskey
  Lake-U, 14 nm Intel) — por usar o processo mais antigo do conjunto — tende a exibir maior potência
  de fuga relativa, especialmente sob carga sustentada, mesmo operando em frequências e TDP nominal
  mais baixos que as demais.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Eficiência Microarquitetural;
  Resultados e Discussão, ao comparar `Potência total da CPU (W)` entre as seis máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → `Potência total da CPU (W)`,
    `CPU Inteira (°C)`: processadores fabricados em Intel 7 (equivalente a ~10 nm aprimorado),
    esperando-se potência de fuga intermediária entre a Máquina D (14 nm) e a Máquina E (7 nm TSMC).
  - `maqC_rodada_*.CSV` → processo de 12 nm (GlobalFoundries, Zen+); espera-se eficiência energética
    intermediária entre a Máquina D (14 nm Intel, mais antiga) e processos mais modernos.
  - `maqE_rodada_*.CSV` → processo de 7 nm (TSMC, Zen 3); segundo a teoria, deve apresentar a menor
    potência de fuga relativa por núcleo entre todos os processadores de desktop do grupo.
  - `scores_maq*.txt` (`Single_Core`/`Multi_Core`) cruzados com a média de `Potência total da CPU
    (W)` de cada máquina permitem testar empiricamente, com os seis pontos de dados, se a hipótese de
    melhoria de eficiência por litografia (3.10 e 3.13) se confirma na métrica de Desempenho por Watt
    (Equação 12, Seção 4.1 deste fichamento).

- **Justificativa de Uso:** Esta citação deve ser usada na Discussão de Resultados como base teórica
  para explicar diferenças de Desempenho por Watt entre as seis máquinas que não decorrem apenas do
  número de núcleos ou do clock, mas também do processo de fabricação do silício.

---

### 3.14 TDP como Limite de Projeto e sua Relação com a Magnitude da Potência Sustentada

- **Conceito/Teoria:** O TDP (*Thermal Design Power*) declarado pelo fabricante define o orçamento de
  potência ao qual o sistema de resfriamento foi projetado para atender, sendo o principal parâmetro
  que distingue, segundo a lógica de Bircher e John (2012), processadores otimizados para eficiência
  energética dos otimizados para desempenho bruto.

- **Citação Direta (Ipsis Litteris):**
  > "The target desktop system, described in Table 6, is optimized for power efficiency rather than
  > performance. This leads to greater variation in power consumption compared to a server since
  > power management features reduce power greatly during low utilization." (p. 571)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) associam diretamente o orçamento de potência de projeto (TDP) à filosofia de
  projeto do processador: sistemas otimizados para eficiência energética (TDP baixo) tendem a exibir
  maior variação relativa de potência entre os estados ocioso e ativo, pois dependem fortemente de
  gerenciamento dinâmico para permanecer dentro do envelope térmico. Em contraste, processadores
  projetados para desempenho bruto (TDP elevado) mantêm potência sustentada mais próxima do limite de
  projeto mesmo sob utilização moderada. Esse contraste é diretamente aplicável ao conjunto das seis
  máquinas do nosso grupo, que abrange um intervalo de TDP de 15 W (Máquinas B, C e D) a 125 W
  (Máquina F), permitindo testar empiricamente a hipótese dos autores em um espectro mais amplo do que
  o par servidor/desktop original do artigo.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — Tabela de hardware comparativo (coluna de TDP);
  Resultados e Discussão — análise comparativa de variabilidade de potência entre máquinas de TDP
  baixo (notebooks ultrafinos) e alto (desktops/notebook gamer).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqB_rodada_*.CSV`, `maqC_rodada_*.CSV`, `maqD_rodada_*.CSV` (TDP 15 W) → `Potência total da
    CPU (W)`: espera-se, segundo a teoria, maior desvio padrão relativo (proporcionalmente ao valor
    médio) ao longo das 20 rodadas, refletindo a maior dependência de gerenciamento dinâmico agressivo.
  - `maqA_rodada_*.CSV` (TDP 45 W, notebook gamer) → potência intermediária esperada, com possível
    ativação mais frequente de `Limite de potência PL1 (Dynamic) (W)` e `Limite de potência PL2
    (Dynamic) (W)` em cargas sustentadas do Geekbench 6 Multi-Core.
  - `maqE_rodada_*.CSV` (TDP 65 W) e `maqF_rodada_*.CSV` (TDP 125 W) → desktops com maior orçamento
    térmico; espera-se menor variabilidade relativa de `Potência total da CPU (W)` e menor incidência
    de `IA: Package-Level RAPL/PBM PL1 (Yes/No)` ativado, por possuírem maior margem de dissipação.
  - `scores_maqA.txt` a `scores_maqF.txt` → colunas `Single_Core`/`Multi_Core` cruzadas com o TDP
    nominal de cada máquina permitem visualizar a relação (não necessariamente linear) entre orçamento
    de potência declarado e desempenho bruto obtido.

- **Justificativa de Uso:** Citação central para a subseção de Consumo Energético e Limites de
  Projeto, pois fundamenta teoricamente por que comparar diretamente os scores absolutos entre
  máquinas de TDP tão distintos (15 W a 125 W) é metodologicamente incompleto sem normalizar pela
  métrica de Desempenho por Watt.

---

### 3.15 Núcleos Heterogêneos (P-Cores/E-Cores) e Implicações para o Modelo de *Fetched Ops*

- **Conceito/Teoria:** O modelo de potência de Bircher e John (2012) é fundamentado na contagem de
  microoperações buscadas por ciclo (*fetched ops*) como proxy de atividade do *pipeline* — métrica
  originalmente concebida para núcleos homogêneos, mas que requer reinterpretação em arquiteturas
  híbridas com núcleos de desempenho (P-cores) e de eficiência (E-cores), como as presentes nas
  Máquinas A, B e F.

- **Citação Direta (Ipsis Litteris):**
  > "Fetched ops—Microoperations fetched. [...] Using ops normalizes the metric to give
  > representative counts independent of instruction mix. Also, by considering fetched rather than
  > retired ops, the metric is more directly related to power consumption." (p. 566)

- **Paráfrase (Citação Indireta Acadêmica):**
  Os autores justificam o uso de microoperações buscadas (e não apenas retiradas) como métrica de
  atividade porque ela captura também o trabalho especulativo descartado, sendo mais diretamente
  relacionada ao consumo de potência real do que contagens de instruções completadas. Em arquiteturas
  heterogêneas como as das Máquinas A (Raptor Lake-H, 4P+4E), B (Raptor Lake-P, 2P+8E) e F (Raptor
  Lake, 6P+8E), essa métrica de atividade por ciclo precisa necessariamente ser decomposta por tipo de
  núcleo, já que P-cores e E-cores possuem larguras de *pipeline*, frequências e eficiências energéticas
  por operação substancialmente distintas — um P-core tipicamente busca mais operações por ciclo a um
  custo de potência por operação maior, ao passo que um E-core prioriza eficiência energética em
  detrimento de taxa de busca.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível de
  Instrução e Thread (Cores Físicos vs. Threads Lógicos); Resultados e Discussão, ao explicar por que
  o ganho de desempenho Multi-Core das Máquinas A, B e F não escala linearmente com o número total de
  núcleos reportado.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV` (8 Cores: 4P+4E/12T) → colunas `Core 0 T0/T1 Uso (%)` a `Core 3 T0/T1 Uso (%)`:
    o HWiNFO64 expõe apenas 4 núcleos monitorados simultaneamente por *thread* (T0/T1) no nosso
    template de colunas; ao processar os CSVs desta máquina, deve-se identificar explicitamente quais
    dos núcleos físicos correspondem a P-cores e quais a E-cores para uma interpretação correta da
    carga de trabalho.
  - `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → mesma lógica de heterogeneidade aplicada, com proporções
    de E-cores ainda maiores (8 E-cores em ambos os casos), reforçando a necessidade de segmentar a
    análise de `Relógios efetivos núcleo (avg) (MHz)` por tipo de núcleo, e não apenas pela média
    agregada de todos os núcleos.
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqF.txt` → coluna `Multi_Core`: o ganho de
    desempenho multi-thread nessas três máquinas deve ser interpretado à luz da heterogeneidade de
    núcleos, e não diretamente comparado ao Multi-Core das Máquinas C, D e E (núcleos homogêneos) sem
    essa ressalva metodológica.

- **Justificativa de Uso:** Esta paráfrase deve introduzir, na Fundamentação Teórica, a ressalva
  metodológica de que a contagem simples de "núcleos" e "threads" relatada na tabela de hardware é
  insuficiente para explicar o desempenho Multi-Core nas arquiteturas híbridas Raptor Lake, sendo
  necessário qualificar teoricamente essa heterogeneidade antes de comparar scores brutos.

---

### 3.16 Conjuntos de Instruções Vetoriais (AVX2/VNNI) como Fator de Throughput e Potência

- **Conceito/Teoria:** Embora o artigo original não trate de extensões vetoriais especificamente, o
  princípio geral discutido pelos autores — de que instruções de maior intensidade computacional por
  ciclo (no caso deles, operações de ponto flutuante) consomem proporcionalmente mais potência do que
  instruções inteiras simples — se generaliza para as instruções vetoriais largas (AVX2, e
  particularmente o conjunto Intel DL Boost/VNNI presente nas Máquinas A, B, D e F).

- **Citação Direta (Ipsis Litteris):**
  > "FP ops retired—Floating point microoperations retired. This metric is used to account for the
  > difference in power consumption between floating point and integer instructions. Assuming equal
  > throughput, floating point instructions have significantly higher average power." (p. 572)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) demonstram que, para uma mesma taxa de throughput, instruções de ponto
  flutuante consomem significativamente mais potência do que instruções inteiras equivalentes, devido
  à maior atividade das unidades funcionais envolvidas (FPU/SIMD). Esse princípio é diretamente
  extensível à comparação entre as instruções vetoriais disponíveis nas seis máquinas do grupo: as
  Máquinas A, B, D e F dispõem de Intel DL Boost (VNNI), conjunto de instruções vetoriais voltado à
  aceleração de operações de inteiros de baixa precisão para inferência de IA, enquanto a Máquina E
  está limitada a FMA3/AVX2 convencional, sem aceleração VNNI dedicada. Espera-se que cargas de
  trabalho do Geekbench 6 que explorem essas extensões (subtestes de processamento de imagem e
  *machine learning*) produzam picos de potência proporcionalmente mais elevados nas máquinas com
  suporte a VNNI durante a execução desses subtestes específicos, em relação a uma carga de trabalho
  puramente escalar/inteira de mesma duração.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível de
  Instrução (extensões SIMD/vetoriais); Resultados e Discussão, ao analisar picos de
  `Potência de núcleos IA (W)` durante subtestes específicos do Geekbench 6.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqD_rodada_*.CSV`, `maqF_rodada_*.CSV` →
    `Potência de núcleos IA (W)`, `Core 0 T0/T1 Uso (%)` a `Core 3 T0/T1 Uso (%)`: máquinas com
    Intel DL Boost (VNNI); picos momentâneos de potência por núcleo são esperados durante subtestes de
    *machine learning*/processamento de imagem do Geekbench 6, coerentes com a teoria de maior consumo
    de instruções vetoriais largas.
  - `maqE_rodada_*.CSV` → mesma análise, porém sem suporte a VNNI (apenas FMA3/AVX2); útil como
    "caso de controle" para comparação do incremento de potência atribuível especificamente à
    aceleração vetorial dedicada nas demais máquinas.
  - `maqC_rodada_*.CSV` → Ryzen 5 3500U (Zen+) com FMA3/AVX2/BMI2, sem VNNI; comparável à Máquina E
    sob esse aspecto, ainda que em microarquitetura e litografia distintas.

- **Justificativa de Uso:** Esta citação fundamenta teoricamente por que diferenças no conjunto de
  instruções suportado (e não apenas clock ou número de núcleos) podem produzir variações na relação
  entre desempenho e potência observada nos diferentes subtestes do Geekbench 6, justificando uma
  eventual discussão granular por subteste na seção de Resultados, caso o grupo opte por essa
  abordagem mais detalhada.

---

### 3.17 Topologia de Canais de Memória (Single vs. Dual Channel) e o Gargalo de Von Neumann

- **Conceito/Teoria:** O artigo discute a influência do tráfego de barramento de memória (BusTrans) e
  da taxa de transações DCT (DRAM Controller) sobre a potência e, implicitamente, sobre a capacidade de
  throughput do subsistema de memória — fundamento direto para comparar configurações Single-Channel
  e Dual-Channel entre as seis máquinas do grupo.

- **Citação Direta (Ipsis Litteris):**
  > "DCTAccesses—$DCTPageHits + DCTPageMisses + DCTPageConflicts$. DCT (DRAM Controller) Access
  > accounts for all memory traffic flowing out of the two on-die memory controllers, destined for
  > system DRAM." (p. 572)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) definem a métrica de acessos ao controlador de memória (DCTAccess) como a
  soma de acertos, faltas e conflitos de página em *ambos* os canais do controlador integrado de
  memória, evidenciando — mesmo sem o explicitarem como objetivo central do artigo — que a presença de
  múltiplos canais de memória operando simultaneamente (Dual-Channel) amplia a capacidade total de
  tráfego que pode ser atendida por ciclo, em comparação a uma configuração de canal único
  (Single-Channel), na qual todo o tráfego de memória do processador deve necessariamente ser
  serializado por um único controlador. Essa distinção topológica está diretamente refletida no
  conjunto de seis máquinas do grupo: as Máquinas C e D operam em Single-Channel (1×8GB), enquanto as
  Máquinas A, B, E e F operam em Dual-Channel, devendo, segundo a teoria do gargalo de Von Neumann,
  apresentar maior largura de banda efetiva de memória e, por consequência, menor penalidade de
  desempenho em cargas de trabalho com forte dependência de acesso à memória principal.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Gargalo de Von Neumann
  (Barramento de Memória), comparando explicitamente Single-Channel vs. Dual-Channel; Resultados e
  Discussão — análise comparativa de desempenho Multi-Core normalizado pelo número de núcleos entre as
  máquinas Single- e Dual-Channel.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqC_rodada_*.CSV`, `maqD_rodada_*.CSV` (Single-Channel) → `Taxa de leituras (MB/s)`, `Taxa de
    gravações (MB/s)`, `Relógio da memória (MHz)`: espera-se, segundo a teoria, throughput de memória
    proporcionalmente menor (em relação à capacidade nominal do clock de RAM) do que nas máquinas
    Dual-Channel, evidenciando o estrangulamento do barramento único.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV`
    (Dual-Channel) → mesmas colunas (`Taxa de leituras (MB/s)`, `Taxa de gravações (MB/s)`, `Relógio
    da memória (MHz)`); espera-se throughput proporcionalmente mais próximo da capacidade teórica
    máxima de banda, por dispor de dois canais operando em paralelo.
  - `scores_maqC.txt`, `scores_maqD.txt` (Single-Channel) versus `scores_maqA.txt`,
    `scores_maqB.txt`, `scores_maqE.txt`, `scores_maqF.txt` (Dual-Channel) → coluna `Multi_Core`:
    cargas de trabalho multi-thread tendem a ser mais sensíveis à largura de banda de memória
    disponível, de modo que a razão Multi_Core/Single_Core pode evidenciar empiricamente a penalidade
    do Single-Channel, especialmente entre máquinas de núcleo/thread count semelhante (ex.: Máquina C,
    4C/8T Single-Channel, vs. uma futura comparação normalizada com máquinas Dual-Channel de
    contagem de núcleos próxima).

- **Justificativa de Uso:** Esta é a citação central para sustentar, com base em literatura de alto
  impacto (IEEE TC), a comparação Single-Channel vs. Dual-Channel já prevista no escopo teórico do
  nosso artigo (Seção 5 das diretrizes gerais do projeto), agora aplicável de forma efetiva, já que o
  grupo passou a dispor de pelo menos duas máquinas em cada topologia de canal.

---

### 3.18 Velocidade de Armazenamento (HD SATA vs. SSD NVMe/PCIe) e o Modelo de Potência de Disco

- **Conceito/Teoria:** O artigo demonstra que a distância física e lógica do disco em relação ao
  processador, combinada às diferenças de tecnologia de armazenamento, produz modelos de potência e
  desempenho fundamentalmente distintos — base teórica direta para comparar o HDD SATA da Máquina D
  com os SSDs NVMe das demais cinco máquinas do grupo.

- **Citação Direta (Ipsis Litteris):**
  > "The modeling of disk power at the level of the microprocessor presents two major challenges:
  > large distance from CPU to disk and little variation in disk power consumption. [...] The various
  > hardware and software structures that are intended to reduce the average access time to the
  > distant disk by the processor make power modeling difficult." (p. 569)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) identificam o disco como o subsistema mais distante do processador em termos
  de tempo de acesso, exigindo estruturas intermediárias (caches de disco, filas de I/O) que dificultam
  tanto a modelagem de potência quanto a previsibilidade de latência. Essa "distância" arquitetural se
  manifesta de forma marcadamente diferente entre tecnologias de armazenamento: discos magnéticos
  (HDD), como o Western Digital Blue 5400 RPM da Máquina D, dependem de movimentação mecânica do
  cabeçote e rotação do prato, impondo latências de acesso ordens de magnitude maiores do que SSDs
  baseados em memória flash. As demais cinco máquinas do grupo utilizam exclusivamente SSDs NVMe (ou,
  no caso da Máquina E, um SSD SATA auxiliar), conectados via barramento PCIe — Gen 3.0 x4 (Máquinas
  B e C) ou Gen 4.0 x4 (Máquina A) — eliminando a limitação mecânica e reduzindo drasticamente o tempo
  de carregamento de dados para os testes de benchmark, com impacto direto na reprodutibilidade e
  variabilidade dos tempos de inicialização e carregamento de cada rodada do Geekbench 6.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  (velocidade de armazenamento, HD SATA vs. SSD NVMe); Resultados e Discussão — análise da
  variabilidade (desvio padrão) das rodadas da Máquina D em comparação às demais.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` (HDD SATA III, 5400 RPM) → `Taxa de leituras (MB/s)`, `Taxa de gravações
    (MB/s)`, `Temperatura do disco (°C)`, `Atividade de leitura (%)`, `Atividade de gravação (%)`:
    espera-se throughput sequencial e aleatório substancialmente inferior, com maior variabilidade
    entre rodadas devido à latência mecânica de busca (*seek time*).
  - `maqA_rodada_*.CSV` (SSD NVMe PCIe Gen 4.0 x4), `maqB_rodada_*.CSV` e `maqC_rodada_*.CSV` (SSD
    NVMe PCIe Gen 3.0 x4), `maqF_rodada_*.CSV` (2× SSD NVMe M.2) → mesmas colunas; espera-se throughput
    ordens de magnitude superior e desvio padrão proporcionalmente menor entre rodadas, por ausência de
    componentes mecânicos.
  - `maqE_rodada_*.CSV` (SSD SATA 120GB + HD 1TB) → caso intermediário relevante: a Máquina E possui
    SSD SATA (sem interface NVMe/PCIe) somado a um HDD secundário, permitindo uma terceira categoria de
    comparação (SSD SATA vs. SSD NVMe vs. HDD) dentro do próprio conjunto de dados do grupo.
  - `scores_maqD.txt` (coluna `Single_Core`/`Multi_Core`) → o desvio padrão amostral das 20 rodadas da
    Máquina D deve ser comparado estatisticamente ao das demais máquinas para verificar se a maior
    variabilidade de tempo de carregamento do HDD se reflete em maior dispersão também no score final
    do benchmark, e não apenas nos tempos de I/O brutos.

- **Justificativa de Uso:** Esta citação amplia, com uma terceira categoria de armazenamento (SSD
  SATA, presente na Máquina E), a comparação binária HD SATA vs. SSD NVMe já prevista no escopo
  teórico do projeto, permitindo uma discussão mais granular sobre a hierarquia de armazenamento na
  seção de Resultados.

---

### 3.19 Barramento PCIe da GPU Dedicada (Largura/Geração) como Extensão do Gargalo de Von Neumann

- **Conceito/Teoria:** Embora o artigo de Bircher e John (2012) trate de uma GPU integrada conectada
  internamente ao mesmo die do processador (sem barramento PCIe externo), o princípio geral de que a
  largura de banda de interconexão entre processador e subsistema gráfico impõe um limite físico ao
  tráfego de dados — análogo ao barramento de memória (FSB/BusTrans) discutido pelos autores — permite
  fundamentar teoricamente a comparação entre as diferentes gerações e larguras de barramento PCIe das
  GPUs dedicadas presentes nas Máquinas A, D, E e F.

- **Citação Direta (Ipsis Litteris):**
  > "All transactions that enter/exit the processor must pass through this bus. Intel calls this the
  > Front Side Bus (FSB)." (p. 566)

- **Paráfrase (Citação Indireta Acadêmica):**
  Bircher e John (2012) destacam que todo tráfego de entrada e saída do processador necessariamente
  atravessa um barramento físico de capacidade finita, sendo este um ponto de estrangulamento
  potencial para qualquer subsistema conectado externamente — princípio diretamente análogo ao
  barramento PCIe que interliga a GPU dedicada ao restante do sistema nas Máquinas A (PCIe 4.0 x8),
  D (PCIe 3.0 x4), E (PCIe 4.0 x8) e F (PCIe 4.0 x8). A Máquina D, com sua GPU NVIDIA GeForce MX130
  conectada via PCIe 3.0 x4 — geração e largura inferiores às demais —, está sujeita a uma capacidade
  de transferência teórica substancialmente menor do que a RTX 4050 (Máquina A) ou a RX 7600
  (Máquina E), ambas em PCIe 4.0 x8, o que pode constituir um gargalo adicional em cargas de trabalho
  que dependam de transferência intensiva de dados entre CPU e GPU (ex.: subtestes de *computer
  vision*/*machine learning* do Geekbench 6 que utilizem aceleração via OpenCL/Vulkan).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Gargalo de Von Neumann
  (extensão ao barramento de interconexão CPU-GPU); Resultados e Discussão — análise de subtestes do
  Geekbench 6 que utilizem aceleração gráfica, comparando as quatro máquinas com GPU dedicada.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` (PCIe 3.0 x4) → `Velocidade do link PCIe (GT/s)`, `Carga do barramento
    GPU (%)`, `Taxa de leituras (MB/s)`/`Taxa de gravações (MB/s)` da GPU: espera-se menor velocidade
    de link reportada e potencial saturação do barramento em cargas intensas de transferência
    CPU↔GPU, em comparação às demais máquinas com GPU dedicada.
  - `maqA_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` (PCIe 4.0 x8) → mesmas colunas;
    espera-se maior velocidade de link e menor probabilidade de saturação do barramento, dada a maior
    largura (x8) e geração (Gen 4.0) do barramento PCIe.
  - `maqB_rodada_*.CSV`, `maqC_rodada_*.CSV` → não aplicável a este conceito específico, pois ambas as
    máquinas não possuem GPU dedicada (N/A na interface de barramento GPU), dependendo exclusivamente
    da GPU integrada (Intel Iris Xe e AMD Radeon Vega 8, respectivamente).

- **Justificativa de Uso:** Esta citação fundamenta teoricamente, por analogia direta ao barramento de
  memória do processador (FSB) discutido pelo artigo, a comparação entre gerações distintas de PCIe
  presentes no parque de máquinas do grupo, ampliando a discussão de gargalo de Von Neumann da
  hierarquia de memória para a hierarquia de interconexão gráfica — um ponto de discussão adicional e
  diferenciado para a seção de Resultados.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmulas Matemáticas/Físicas em LaTeX Puro (Transcritas do Artigo Original)

**Modelo de Potência da CPU (Servidor Pentium IV) — Equação (1), p. 568:**
```latex
\begin{equation}
P_{CPU} = 9.3 + 26.5 \times Active\% + 4.3 \times \frac{Fetched\mu ops}{Cycle}
\label{eq:potencia_cpu_pentium}
\end{equation}
```

**Modelo Quadrático de Potência de Memória via L3 Misses — Equação (2), p. 568:**
```latex
\begin{equation}
P_{MEM} = 28 + \frac{L3LoadMiss}{Cycle} \times \left(\frac{L3LoadMiss}{Cycle}\right)^2 \times 7.7
\label{eq:potencia_mem_l3miss}
\end{equation}
```

**Modelo Quadrático de Potência de Memória via Transações de Barramento — Equação (3), p. 569:**
```latex
\begin{equation}
P_{MEM} = 29.2 - \frac{BusTrans}{MCycle} \times 50 \times 10^{-4} + \left(\frac{BusTrans}{MCycle}\right)^2 \times 813 \times 10^{-8}
\label{eq:potencia_mem_bustrans}
\end{equation}
```

**Equação Geral de Erro Percentual Médio — Equação (6), p. 569:**
```latex
\begin{equation}
AverageError = \frac{\sum_{i=1}^{NumSamples} \frac{|Modeled_i - Measured_i|}{Measured_i}}{NumSamples} \times 100\%
\label{eq:erro_medio}
\end{equation}
```

**Modelo de Potência da GPU via Clocks Não-Gateados (Plataforma Desktop AMD) — Equação (7), p. 574:**
```latex
\begin{equation}
P_{GPU} = 0.0068 \times \left(\frac{NonGatedClocks}{Sec}\right) / 10^6 + 0.847
\label{eq:potencia_gpu}
\end{equation}
```

**Modelo de Potência de Memória (Plataforma Desktop AMD) — Equação (8), p. 575:**
```latex
\begin{equation}
P_{MEM} = 4 \times 10^{-8} \times \frac{DCTAccess}{Sec} + 0.743 \times LinkActive\% + 0.24
\label{eq:potencia_mem_amd}
\end{equation}
```

**Fórmulas de Análise Estatística para o Nosso Artigo (Necessárias na Metodologia):**

Média Aritmética:
```latex
\begin{equation}
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\label{eq:media}
\end{equation}
```

Desvio Padrão Amostral:
```latex
\begin{equation}
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
\label{eq:desvpad}
\end{equation}
```

Onde $x_i$ representa a medição (score do Geekbench 6 ou variável de telemetria do HWiNFO64) da
$i$-ésima rodada e $n = 20$ é o número total de rodadas por máquina.

**Desempenho por Watt (métrica derivada, proposta para o nosso artigo, inspirada na razão entre
desempenho e potência discutida implicitamente pelos autores ao longo de toda a Seção 3.8 e 4.4):**
```latex
\begin{equation}
DPW = \frac{Score_{Geekbench}}{\overline{P}_{CPU}}
\label{eq:desempenho_por_watt}
\end{equation}
```
Onde $\overline{P}_{CPU}$ é a média amostral da coluna `Potência total da CPU (W)` ao longo das 20
rodadas de uma mesma máquina.

---

### 4.2 Sugestão de Gráficos e Tabelas Correspondentes

**Gráfico 1 — Dispersão Potência vs. Clock Efetivo (validação da relação V²/V³ e DVFS):**
Inspirado nas Figuras 2, 3 e 5 do artigo original (traços de potência modelada vs. medida ao longo
do tempo), sugere-se um gráfico de linha duplo-eixo (tempo no eixo X; `Potência total da CPU (W)` e
`Relógios efetivos núcleo (avg) (MHz)` em eixos Y distintos) para uma rodada representativa da
Máquina D, evidenciando a correlação entre aumento de clock (DVFS/Turbo Boost) e aumento de potência.

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('maqD_rodada_01.CSV', sep=';', decimal=',')
fig, ax1 = plt.subplots(figsize=(9, 5))

ax1.plot(df.index, df['Potência total da CPU (W)'], color='black', linewidth=1.0, label='Potência (W)')
ax1.set_xlabel('Tempo (amostras, 1/s)', fontsize=11)
ax1.set_ylabel('Potência total da CPU (W)', fontsize=11)

ax2 = ax1.twinx()
ax2.plot(df.index, df['Relógios efetivos núcleo (avg) (MHz)'], color='gray', linestyle='--', linewidth=1.0, label='Clock Efetivo (MHz)')
ax2.set_ylabel('Relógios efetivos núcleo (avg) (MHz)', fontsize=11)

fig.legend(loc='upper center', ncol=2)
plt.title('Relação entre Potência e Clock Efetivo — Máquina D (Rodada 01)', fontsize=12)
plt.tight_layout()
plt.savefig('fig_potencia_clock_maqD.pdf', dpi=300)
```

**Gráfico 2 — Barplot de Desempenho por Watt (Geekbench Multi-Core / Potência Média da CPU):**
Barplot comparando as 4 máquinas, com a métrica derivada $DPW = Score_{MultiCore} / \overline{P}_{CPU}$,
com hastes de erro propagadas a partir do desvio padrão amostral de ambas as grandezas (propagação de
incerteza). Visualmente em tons de cinza, conforme padrão SBC.

**Gráfico 3 — Boxplot/Barplot de Ocupação de C-States por Máquina:**
Inspirado na discussão de *clock gating* e estados ociosos (Seção 3.3 deste fichamento), sugere-se um
gráfico de barras empilhadas com a ocupação média de `Package C2/C3/C6/C7/C8 Ocupação (%)` por
máquina, evidenciando diferenças de agressividade de gerenciamento de energia entre arquiteturas.

**Tabela LaTeX — Resumo dos Modelos de Potência do Artigo de Bircher e John (2012), para uso na
Fundamentação Teórica:**
```latex
\begin{table}[ht]
\centering
\caption{Erro médio dos modelos de potência por subsistema (Bircher e John, 2012)}
\label{tab:erro_bircher}
\begin{tabular}{lcc}
\hline
\textbf{Subsistema} & \textbf{Erro Médio — Servidor (\%)} & \textbf{Erro Médio — Desktop (\%)} \\
\hline
CPU                  & $>$6,0  & 1,63 \\
Memória              & $\approx$9,0 & 5,27 \\
Chipset              & --      & 3,34 \\
GPU                  & --      & 0,79 \\
Disco                & --      & 6,62 \\
\hline
\end{tabular}

\vspace{0.2cm}
{\footnotesize Fonte: Adaptado de Bircher e John (2012, Tabelas 4, 5 e 11).}
\end{table}
```

---

## 5. KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

**Para embasar a seção de Consumo Energético e Modelagem de Potência:**
- `"performance counters" power estimation processor`
- `"trickle-down" power modeling complete system`
- `CPU power model performance events regression`
- `"contadores de desempenho" estimativa de potência processador`
- `RAPL "running average power limit" power estimation accuracy`

**Para embasar a seção de DVFS e Gerenciamento Dinâmico de Energia:**
- `dynamic voltage frequency scaling DVFS power consumption CPU`
- `"clock gating" idle power processor energy saving`
- `"escalonamento dinâmico de tensão e frequência" processador`
- `Intel SpeedStep Turbo Boost power management mobile`

**Para embasar a seção de Termodinâmica, Leakage Power e Throttling:**
- `leakage power temperature dependence CMOS processor`
- `"thermal throttling" frequency reduction CPU temperature`
- `static power dynamic power CMOS voltage relationship`
- `"potência de fuga" temperatura processador CMOS`

**Para embasar a seção de Hierarquia de Memória e Estados de Energia da DRAM:**
- `DRAM power states self-refresh precharge power down`
- `"memory power management" DDR SDRAM idle states`
- `cache misses memory power correlation performance counters`
- `"estados de energia" memória DRAM self-refresh precharge`

**Para embasar a seção de Eficiência Microarquitetural (Desempenho por Watt):**
- `"performance per watt" microprocessor energy efficiency`
- `energy efficiency benchmark CPU GPU comparison`
- `"desempenho por watt" eficiência energética CPU benchmark`
- `process technology node power efficiency processor generations`

**Para embasar a seção de Núcleos Heterogêneos (P-cores/E-cores) e Conjuntos de Instruções:**
- `hybrid architecture "performance cores" "efficiency cores" power`
- `heterogeneous multicore P-core E-core scheduling performance`
- `"arquitetura híbrida" núcleos de desempenho eficiência processador`
- `AVX2 VNNI vector instructions power consumption CPU`
- `Intel Deep Learning Boost VNNI inference power efficiency`

**Para embasar a seção de Topologia de Memória e Barramento de Interconexão (Gargalo de Von Neumann estendido):**
- `single channel dual channel RAM bandwidth benchmark impact`
- `"largura de banda de memória" canal único canal duplo desempenho`
- `PCIe generation bandwidth GPU bottleneck benchmark`
- `"PCIe 3.0" "PCIe 4.0" GPU bandwidth comparison performance`
- `NVMe SSD vs SATA HDD storage benchmark loading time`

---

> **⚠️ NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
>
> Diversos conceitos fichados acima — especialmente os referentes a DVFS (Seção 3.6), comportamento
> bimodal de potência de GPU (Seção 3.9), impacto da litografia (Seção 3.10) e estados de energia da
> DRAM (Seção 3.8) — foram fichados de forma teórica geral, aplicável a qualquer arquitetura x86
> moderna, mas seu mapeamento quantitativo específico para as Máquinas A, B e C depende das
> especificações de hardware ainda não fornecidas pelo grupo (litografia do processador, presença de
> GPU dedicada, configuração de canal de memória). Este mapeamento de colunas e sua interpretação
> **só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A,
> B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.**

---

> **🔄 ADITIVO DE ATUALIZAÇÃO — TABELA DE HARDWARE COMPLETA RECEBIDA (MÁQUINAS A, B, C, E e F):**
>
> Com o recebimento da tabela completa de especificações de hardware do grupo, as especificações das
> Máquinas A (Raony), B (Leandro), C (Cinara), E (Nauan) e F (Nicolas) — anteriormente pendentes —
> foram incorporadas a este fichamento nas novas Seções 3.13 a 3.19, que tratam respectivamente de:
> litografia/processo de fabricação (3.13), TDP como limite de projeto (3.14), núcleos heterogêneos
> P-core/E-core (3.15), instruções vetoriais AVX2/VNNI (3.16), topologia de memória Single/Dual
> Channel (3.17), velocidade de armazenamento HD SATA vs. SSD NVMe/SATA (3.18) e barramento PCIe da
> GPU dedicada (3.19).
>
> A nota de abstração preditiva original (acima) permanece válida apenas para os pontos remanescentes
> ainda não preenchidos na tabela do grupo, a saber: (i) o modelo comercial do gabinete das Máquinas E
> e F; (ii) a frequência exata da RAM DDR4 da Máquina E (`[MHz]*`); e (iii) a geração da interface do
> disco da Máquina F (`[Preencher Gen]*`). Os mapeamentos de colunas associados a esses três campos
> específicos devem ser tratados como provisórios até o devido preenchimento pelo grupo.
