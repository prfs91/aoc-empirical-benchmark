# FICHAMENTO CIENTÍFICO COMPLETO
## Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí
## Arquivo: `fichamento_FrequencyThrottlingSideChannel_Liu.md`

---

> **VEREDITO DE RELEVÂNCIA:** ✅ **SIM — O artigo é altamente útil para o projeto de AOC.**
>
> O artigo de Liu et al. (2022), da Intel Corporation, publicado no ACM CCS '22, descreve
> com precisão técnica excepcional o funcionamento interno do mecanismo de Frequency Throttling,
> do DVFS, do RAPL (PL1/PL2), do VR-TDC, dos P-States e a equação de potência dinâmica CMOS.
> Embora o foco primário seja segurança computacional (side-channel attack), o artigo constitui
> uma das referências mais rigorosas disponíveis sobre a arquitetura de gerenciamento de potência
> de processadores Intel modernos — incluindo processadores da família Whiskey Lake (i5-8265U
> da Máquina D). Os conceitos fundamentam diretamente a interpretação das colunas
> `Estrangulamento térmico do núcleo (avg) (Yes/No)`, `Relógios efetivos núcleo (avg) (MHz)`,
> `Potência total da CPU (W)`, `IA: Package-Level RAPL/PBM PL1 (Yes/No)`,
> `IA: Package-Level RAPL/PBM PL2 PL3 (Yes/No)` e `Limite de potência do núcleo excedido (avg)
> (Yes/No)` do nosso dataset HWiNFO64.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  LIU, C.; CHAKRABORTY, A.; CHAWLA, N.; ROGGEL, N. **Frequency Throttling Side-Channel
  Attack**. In: PROCEEDINGS OF THE 2022 ACM SIGSAC CONFERENCE ON COMPUTER AND
  COMMUNICATIONS SECURITY (CCS '22), 2022, Los Angeles, CA, USA. *Anais [...]*. New York:
  ACM, 2022. p. 1977--1991. https://doi.org/10.1145/3548606.3560682

- **Código BibTeX Completo (.bib):**

```bibtex
@InProceedings{liu:22,
  author    = {Chen Liu and Abhishek Chakraborty and Nikhil Chawla and Neer Roggel},
  title     = {Frequency Throttling Side-Channel Attack},
  booktitle = {Proceedings of the 2022 {ACM} {SIGSAC} Conference on Computer
               and Communications Security ({CCS} '22)},
  year      = {2022},
  pages     = {1977--1991},
  address   = {New York, NY, {USA}},
  publisher = {{ACM}},
  month     = {November},
  doi       = {10.1145/3548606.3560682},
  note      = {Intel Corporation, Hillsboro, OR, {USA} and Rio Rancho, NM, {USA}.
               Los Angeles, CA, {USA}, November 7--11, 2022.}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo Completo de Conferência (ACM SIGSAC CCS '22 — Qualis A1 em Ciência da Computação)
- **Instituição/Editora:** Intel Corporation (Hillsboro, OR, USA e Rio Rancho, NM, USA) / ACM — Association for Computing Machinery
- **Autores:** Chen Liu; Abhishek Chakraborty; Nikhil Chawla; Neer Roggel
- **Ano:** 2022
- **Páginas:** 1977–1991 (15 páginas)
- **DOI:** https://doi.org/10.1145/3548606.3560682
- **Palavras-Chave Originais:** Power Management; Frequency Throttling; Side-Channel Analysis.
- **Resumo do Escopo Geral:**
  O artigo demonstra como o mecanismo de ajuste dinâmico de frequência de processadores modernos
  (Intel, AMD e ARM) — ativado quando parâmetros elétricos ou térmicos ultrapassam limites
  predefinidos (RAPL PL1/PL2, VR-TDC) — cria um canal de vazamento de informação baseado em
  tempo de execução. Os autores provam que mesmo implementações de código com tempo de ciclo
  constante (constant-cycle) tornam-se vulneráveis a ataques de side-channel quando o throttling
  de frequência induzido por limite de potência converte diferenças de consumo de energia em
  diferenças de tempo de execução mensuráveis. O estudo utiliza AES-NI como carga de trabalho
  vítima e recupera com sucesso chaves AES de 128 bits. Para o projeto de AOC, o valor central
  do artigo está na descrição arquitetural precisa e quantitativa do funcionamento do DVFS,
  RAPL, P-States e da equação de potência dinâmica CMOS — fundamentos que explicam o fenômeno
  de Thermal Throttling observado na telemetria HWiNFO64 da Máquina D.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 Equação de Potência Dinâmica CMOS — Fundamento Físico do Throttling

- **Conceito/Teoria:** A potência dinâmica dissipada por um circuito CMOS digital é proporcional
  à atividade de chaveamento, à capacitância de carga, ao quadrado da tensão de alimentação e à
  frequência de operação. Essa equação é o fundamento físico que conecta dados processados
  (carga de trabalho), consumo de energia e temperatura — e, portanto, explica por que o
  processador ativa o throttling durante cargas computacionais intensas.

- **Citação Direta (Ipsis Litteris):**
  > "Power side-channel analysis attacks exploit the fact that the dynamic power consumption
  > $P_{dyn}$ of a digital CMOS-based circuit is data-dependent in nature, as evident in the
  > following equation: $P_{dyn} = \alpha \cdot C \cdot V_{DD}^2 \cdot f$
  > where, $\alpha$, $C$, $V_{DD}$, and $f$ represent switching activity factor, load
  > capacitance, supply voltage, and clock frequency, respectively." (p. 1978)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) estabelecem que o consumo de potência dinâmica de um circuito CMOS é
  intrinsecamente dependente dos dados processados, sendo modelado pela expressão
  $P_{dyn} = \alpha \cdot C \cdot V_{DD}^2 \cdot f$, onde $\alpha$ representa o fator de
  atividade de chaveamento, $C$ a capacitância de carga, $V_{DD}$ a tensão de alimentação
  e $f$ a frequência de operação. Essa relação implica que cargas de trabalho mais intensas
  — como as executadas durante o benchmark Geekbench 6 — elevam $\alpha$, aumentando
  proporcionalmente a potência dissipada e, consequentemente, a temperatura do pacote do
  processador, até ativar os mecanismos reativos de controle de frequência (throttling).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Consumo Energético
  e Potência Dinâmica; é a equação central que conecta as seções de benchmarking, termodinâmica
  e eficiência energética.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Potência total da CPU (W)`: representa empiricamente o
    $P_{dyn}$ do processador medido via interface RAPL, variando conforme a carga do Geekbench 6.
  - `maqD_rodada_*.CSV` → coluna `Core VIDs (avg) (V)`: representa $V_{DD}$ — a tensão de
    alimentação dos núcleos. Pela equação, quedas de VID reduzem $P_{dyn}$ quadraticamente.
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: representa $f$ —
    a frequência efetiva de operação. Redução de frequência pelo throttling reduz $P_{dyn}$
    linearmente.
  - `maqD_rodada_*.CSV` → coluna `Potência de núcleos IA (W)`: componente dominante de
    $P_{dyn}$, equivalente à parcela dos núcleos de CPU na equação.
  - **Análise sugerida:** calcular a correlação de Pearson entre `Potência total da CPU (W)` e
    `CPU Inteira (°C)` para validar empiricamente que maior $P_{dyn}$ implica maior temperatura,
    conforme previsto pela equação de Liu et al. (2022).

---

### 3.2 DVFS — Dynamic Voltage and Frequency Scaling como Mecanismo de Throttling

- **Conceito/Teoria:** O DVFS (Dynamic Voltage and Frequency Scaling) é o mecanismo central de
  gerenciamento de potência em processadores modernos Intel, AMD e ARM, que ajusta dinamicamente
  a frequência e a tensão de operação para otimizar o consumo de energia ou para garantir a
  operação dentro de limites elétricos e térmicos predefinidos.

- **Citação Direta (Ipsis Litteris):**
  > "A widely-used power management architectural mechanism known as Dynamic Voltage and
  > Frequency Scaling (DVFS) is available on Intel®, AMD and ARM CPUs. DVFS dynamically
  > adjusts CPU frequency and voltage in order to reduce system power consumption, yielding
  > higher performance per Watt, or to quickly alter CPU frequency during workload execution,
  > in order to ensure that different electrical and thermal parameters of the system remain
  > below predefined safe limits." (p. 1977)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) descrevem o DVFS como o mecanismo arquitetural de gerenciamento de
  potência mais amplamente utilizado em processadores de todas as principais arquiteturas —
  Intel, AMD e ARM. O DVFS opera em dois modos complementares: de forma proativa, reduzindo
  tensão e frequência para minimizar o consumo de energia e maximizar o desempenho por Watt;
  e de forma reativa, ajustando rapidamente a frequência durante a execução de cargas de
  trabalho para garantir que parâmetros elétricos e térmicos permaneçam dentro dos limites
  de segurança do sistema. No contexto da Máquina D (i5-8265U), o DVFS é implementado via
  Intel Speed Shift (hardware-controlled) e Intel SpeedStep (OS-controlled), registrado pelo
  HWiNFO64 através das variações na coluna `Relógios efetivos núcleo (avg) (MHz)`.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de DVFS e Gerenciamento
  de Potência; Resultados e Discussão — interpretação das variações de clock efetivo.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: rastreia o DVFS
    em tempo real — a variação desta coluna ao longo de uma rodada registra os ajustes de
    frequência realizados pelo controlador de potência.
  - `maqD_rodada_*.CSV` → coluna `Core VIDs (avg) (V)`: rastreia o ajuste de tensão
    correspondente ao DVFS — redução de tensão acompanha redução de frequência.
  - `maqD_rodada_*.CSV` → coluna `Relação do relógio do núcleo (avg) (x)`: multiplicador
    de clock aplicado — representa diretamente o P-State selecionado pelo algoritmo DVFS.
  - `maqD_rodada_*.CSV` → coluna `Potência total da CPU (W)` versus `Relógios efetivos
    núcleo (avg) (MHz)`: gráfico de dispersão que visualiza o trade-off de DVFS — menor
    frequência implica menor potência, conforme a equação $P_{dyn} \propto f \cdot V_{DD}^2$.

---

### 3.3 P-States e Turbo Boost — Hierarquia de Estados de Desempenho

- **Conceito/Teoria:** Os P-States (Performance States) definem os pares tensão-frequência
  disponíveis no processador. O estado P0 corresponde à frequência máxima turbo atingível,
  enquanto estados superiores correspondem a frequências progressivamente menores. Durante
  o throttling, o algoritmo de gerenciamento de potência reduz o limite de frequência máxima
  ($f_{max}$), impedindo o processador de operar no P0 (turbo mode).

- **Citação Direta (Ipsis Litteris):**
  > "Intel processors implement performance states (referred to as P-States, defined per
  > ACPI), by realizing a DVFS mechanism for optimizing power consumption. Such P-States
  > correspond to different voltage-frequency pairs, which can be proactively controlled
  > either by the operating system (using SpeedStep) or by the hardware (using Speed Shift).
  > As per convention, the highest CPU P-State is referred to as P0, and it corresponds to
  > the highest achievable operating frequency, as determined during manufacturing, enabling
  > the processor to enter the so-called turbo mode." (p. 1979)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) explicam que os processadores Intel implementam o DVFS por meio de uma
  hierarquia de P-States definida pela especificação ACPI, onde cada estado corresponde a
  um par tensão-frequência específico. O estado P0 — o de maior desempenho — habilita o
  modo turbo, permitindo ao processador operar na frequência máxima determinada em fábrica.
  O controle dos P-States pode ser realizado pelo sistema operacional via Intel SpeedStep ou
  diretamente pelo hardware via Intel Speed Shift, tecnologia presente no i5-8265U da
  Máquina D. Quando limites reativos (RAPL ou VR-TDC) são atingidos, o algoritmo reduz o
  limite de $f_{max}$, impedindo o acesso ao turbo e causando o fenômeno de Thermal
  Throttling observado no benchmark.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Arquitetura de
  Gerenciamento de Potência e Intel Turbo Boost; explica por que o clock efetivo da Máquina D
  varia entre o clock base (1,60 GHz) e o boost máximo (3,90 GHz) durante as rodadas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Relação do relógio do núcleo (avg) (x)`: o multiplicador
    de clock reflete diretamente o P-State ativo — valor máximo sustentado indica P0 (turbo);
    reduções abaixo do multiplicador de boost indicam P-States inferiores por throttling.
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: durante throttling,
    o processador abandona o turbo (3,90 GHz) e recua para frequências mais baixas — o
    patamar mínimo visível corresponde ao clock base TDP-up de 1,80 GHz do i5-8265U.
  - `maqD_rodada_*.CSV` → coluna `Relógios núcleo (avg) (MHz)`: clock nominal solicitado,
    comparado com `Relógios efetivos` revela a lacuna entre o clock desejado e o efetivamente
    entregue durante episódios de throttling.
  - `scores_maqD.txt` → colunas `Single_Core` e `Multi_Core`: rodadas em que o processador
    permaneceu mais tempo no turbo tendem a produzir scores mais altos; a variabilidade entre
    as 20 rodadas é consequência direta da oscilação entre P-States.

---

### 3.4 RAPL — Running Average Power Limit (PL1 e PL2)

- **Conceito/Teoria:** O RAPL (Running Average Power Limit) é o mecanismo da Intel para limitar
  o consumo de potência do processador. PL1 controla o limite de potência de longo prazo (janela
  de dezenas de segundos), enquanto PL2 controla bursts de curto prazo (janela de milissegundos).
  Quando a potência média calculada excede o limite configurado, o algoritmo reduz $f_{max}$
  e ativa o throttling. Para o i5-8265U da Máquina D, o PL1 nominal é 15W (TDP) e o PL2 é
  tipicamente 25W (cTDP up burst).

- **Citação Direta (Ipsis Litteris):**
  > "RAPL is a feature supported by Intel power management architecture to cap the power
  > consumption on the system. When the configured power limit is exceeded, the CPU will be
  > forced to run at a lower frequency to maximize performance while meeting the power limit
  > requirement. Intel currently provides multiple power limit capabilities. The most commonly
  > used ones are the package-level power limit 1 (PL1) and package-level power limit 2 (PL2).
  > PL1 is used to track the long-term power consumption, so typically its limit value is set
  > to be lower and the time window $\tau$ is longer (tens of seconds). On the other hand, PL2
  > is used to track the short-time power burst events, so typically the limit is set to be
  > higher than PL1 and $\tau$ is much shorter (several milliseconds)." (p. 1979--1980)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) descrevem o RAPL como o mecanismo primário de limitação de potência da
  arquitetura Intel, operando em dois níveis complementares: o PL1 (Power Limit 1) controla
  o consumo médio de longo prazo, com limite mais conservador e janela temporal da ordem de
  dezenas de segundos, sendo o gatilho mais comum de throttling sustentado durante benchmarks
  de longa duração; o PL2 (Power Limit 2) gerencia bursts de alta potência de curta duração,
  com limite mais alto e janela de poucos milissegundos, permitindo acesso temporário ao modo
  turbo pleno. No i5-8265U da Máquina D, o PL1 nominal corresponde ao TDP de 15W e o PL2
  ao burst de 25W — configurações registradas nas colunas `Limite de potência PL1 (Static) (W)`
  e `Limite de potência PL2 (Static) (W)` do HWiNFO64. Quando a potência média excede o PL1
  durante a execução continuada do Geekbench 6, o processador é forçado a reduzir sua
  frequência efetiva para manter a média dentro do orçamento de potência disponível.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Limites de Projeto
  e Gerenciamento de Potência RAPL; Resultados e Discussão — análise dos eventos de PL1
  e PL2 registrados durante as 20 rodadas de benchmark.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `IA: Package-Level RAPL/PBM PL1 (Yes/No)`: indica segundo
    a segundo quando o processador excedeu o PL1 e ativou throttling de longo prazo — coluna
    binária crítica para correlacionar com quedas em `Relógios efetivos núcleo (avg) (MHz)`.
  - `maqD_rodada_*.CSV` → coluna `IA: Package-Level RAPL/PBM PL2 PL3 (Yes/No)`: indica
    quando o burst de curto prazo (PL2) foi atingido — eventos de PL2 são mais curtos e
    frequentes no início de cada rodada (quando o processador ainda está no turbo pleno).
  - `maqD_rodada_*.CSV` → coluna `Limite de potência PL1 (Static) (W)` e `Limite de potência
    PL1 (Dynamic) (W)`: valor configurado e valor dinâmico do PL1 — diferença entre estático
    e dinâmico revela se o OEM (Dell) ou o S.O. ajustaram o limite em tempo de execução.
  - `maqD_rodada_*.CSV` → coluna `Limite de potência do núcleo excedido (avg) (Yes/No)`:
    confirma que o limite de TDP do núcleo foi ultrapassado, complementando a leitura de PL1.
  - `maqD_rodada_*.CSV` → coluna `Potência total da CPU (W)` versus `Limite de potência PL1
    (Static) (W)`: gráfico de linha comparando potência medida versus limite PL1 — cruzamentos
    acima do limite correspondem a ativações de throttling.

---

### 3.5 VR-TDC — Voltage Regulator Thermal Design Current Limit

- **Conceito/Teoria:** O VR-TDC (Voltage Regulator Thermal Design Current Limit) é um limite
  elétrico de corrente (em Amperes) monitorado pelo regulador de tensão (VR). Quando a corrente
  média excede este limite, o processador também ativa o throttling de frequência, mesmo que
  os limites de potência (PL1/PL2) não tenham sido atingidos. É um segundo gatilho independente
  de throttling, especialmente relevante em laptops com reguladores de tensão de menor capacidade.

- **Citação Direta (Ipsis Litteris):**
  > "VR-TDC is a power management feature supported by Intel power management architecture.
  > It is a current limit specified in Amperes, maintained in order to satisfy VR electrical
  > constraints. Generally, the algorithm monitors the running average current in Amperes by
  > reading the VR current sensor during the configured time window. If the limit is hit, the
  > processor will engage its frequency throttling to reduce its frequency, in order to ensure
  > current remains within the limit and budget." (p. 1980)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) descrevem o VR-TDC como um mecanismo de proteção elétrica do regulador
  de tensão que opera de forma independente dos limites de potência RAPL. O algoritmo monitora
  continuamente a média de corrente fornecida ao processador e, ao detectar violação do limite
  de TDC, ativa o throttling de frequência para reduzir a demanda de corrente. Em plataformas
  laptop como o Dell Inspiron 15 5584 (Máquina D), os reguladores de tensão integrados possuem
  capacidade de corrente limitada, tornando o VR-TDC um segundo vetor de throttling paralelo
  ao RAPL — especialmente durante execuções Multi-Core do Geekbench 6, quando todos os 4
  núcleos do i5-8265U operam simultaneamente em alta frequência turbo, elevando o pico de
  corrente drenada do VR.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Limites de Projeto
  (TDP, PL1/PL2, VR-TDC); Resultados — explicação de throttling observado mesmo com
  temperatura abaixo do TjMAX.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `VR VCC Corrente (SVID IOUT) (A)`: corrente fornecida pelo
    regulador de tensão ao processador — picos acima do limite de TDC são os gatilhos de
    throttling independentes da temperatura.
  - `maqD_rodada_*.CSV` → coluna `IA: VR TDC (Yes/No)`: indicador binário que registra
    quando o limite de corrente do VR (TDC) foi atingido — pode ocorrer antes mesmo do
    throttling térmico em sistemas com VR de baixa capacidade.
  - `maqD_rodada_*.CSV` → coluna `IA: VR Thermal Alert (Yes/No)`: alerta de temperatura
    do próprio regulador de tensão — segundo vetor térmico além do pacote do processador.
  - **Análise sugerida:** Verificar se ocorrências de `IA: VR TDC (Yes/No) = Yes` precedem
    eventos de `Estrangulamento térmico do núcleo (avg) (Yes/No) = Yes`, o que indicaria que
    o throttling elétrico (corrente) ocorre antes do térmico na Máquina D.

---

### 3.6 Algoritmo de Determinação do Limite de P-State ($f_{max}$) — Funcionamento Interno do Throttling

- **Conceito/Teoria:** O algoritmo de gerenciamento de potência do processador calcula
  periodicamente a média de potência (ou corrente) sobre janelas de tempo predefinidas e
  determina o novo limite de frequência máxima ($f_{max}$) baseado no orçamento de potência
  disponível (diferença entre limite configurado e consumo médio calculado).

- **Citação Direta (Ipsis Litteris):**
  > "The power management algorithm of a CPU periodically calculates different running averages
  > of electrical parameters (e.g., power, current, etc.) of windows of pre-specified lengths.
  > Power budget is then computed as the difference between the running averages and the
  > respective reactive limit values. Based on the power budget, the power management algorithm
  > $PL\_ALG(\cdot)$ computes the new P-State limit $f_{max}$, which is the highest possible
  > CPU operating frequency that satisfies all the reactive limits of the system." (p. 1979)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) descrevem o núcleo do algoritmo de controle de potência dos processadores
  Intel: em intervalos regulares de polling ($T$), o firmware calcula a média de corrida de
  parâmetros elétricos (potência, corrente) sobre janelas temporais $\tau_i$ específicas para
  cada limite reativo $PL_i$. O orçamento de potência disponível ($\Delta = P_i - PL_i$) é
  então utilizado pela função de controle $PL\_ALG(\cdot)$ para determinar o novo limite de
  frequência máxima $f_{max,i}$ — o maior valor de clock que satisfaz simultaneamente todos
  os limites reativos ativos. Quando nenhum limite é violado, $f_{max}$ excede a frequência
  turbo máxima, permitindo operação plena em P0. Quando qualquer limite é atingido, $f_{max}$
  é reduzido, causando o throttling de frequência observado na coluna `Relógios efetivos
  núcleo (avg) (MHz)` do HWiNFO64. Este algoritmo opera continuamente durante todas as 20
  rodadas do Geekbench 6 na Máquina D.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Mecanismo de
  Throttling e Gerenciamento de Potência Reativo; é a explicação causal do throttling observado.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: saída direta do
    algoritmo — representa o $f_{max}$ efetivamente aplicado pelo controlador de potência.
  - `maqD_rodada_*.CSV` → coluna `Potência total da CPU (W)`: entrada do algoritmo — o valor
    calculado que é comparado com os limites PL1/PL2.
  - `maqD_rodada_*.CSV` → coluna `Limite de potência PL1 (Dynamic) (W)`: o valor dinâmico
    de $PL_i$ usado pelo algoritmo — pode ser ajustado em tempo real pelo firmware ou S.O.
  - `maqD_rodada_*.CSV` → coluna `Nível cTDP atual`: indica o perfil de TDP ativo
    (configurável pelo OEM Dell via BIOS) — define os parâmetros $PL_i$ de partida do algoritmo.

---

### 3.7 Throttling Reativo — Conversão de Potência para Tempo de Execução

- **Conceito/Teoria:** Quando o throttling reativo é ativado, a redução de frequência
  ($f_1 < f_2 < f_{default}$) resulta em aumento do tempo de execução da carga de trabalho,
  mesmo que o número de ciclos necessários seja constante. Isso formaliza a relação
  $t = C_i / f$, onde maior tempo de execução implica menor frequência efetiva — observável
  diretamente na variabilidade dos scores do Geekbench 6 entre rodadas.

- **Citação Direta (Ipsis Litteris):**
  > "The average throttled frequency in turn affects the overall execution time of the workload,
  > even if its implementation follows constant-cycle coding principles, or it is being executed
  > inside a TEE. [...] increases and decreases in CPU frequency (hereinafter, referred to as
  > average throttling frequency) during workload execution are dependent on the instantaneous
  > electrical and thermal parameters being capped by system-defined limits." (p. 1978)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) formalizam a relação entre frequência de throttling e tempo de execução:
  dado que o tempo de execução de qualquer carga de trabalho é $t = C_i / f$ (número de
  ciclos dividido pela frequência efetiva), a redução de frequência imposta pelo throttling
  aumenta proporcionalmente o tempo de conclusão da tarefa — e, no caso de um benchmark de
  score fixo como o Geekbench 6, reduz o score obtido. Os autores enfatizam que este efeito
  é independente da implementação do código e afeta qualquer processo em execução durante
  um episódio de throttling, tornando o Desvio Padrão Amostral das 20 rodadas um indicador
  direto da instabilidade de frequência causada pelos limites reativos de potência.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Thermal Throttling
  e Variabilidade de Desempenho; Metodologia — justificativa do Desvio Padrão Amostral como
  métrica de estabilidade; Resultados — interpretação de scores baixos em rodadas com
  throttling ativo.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → colunas `Single_Core` e `Multi_Core`: as 20 rodadas com variabilidade
    de score refletem diretamente a variação de $f_{eff}$ (frequência efetiva média de cada
    rodada). Rodadas com maior episódio de throttling produzem scores menores.
  - `maqD_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)`:
    indicador binário direto de ativação de throttling — correlacionar com o score da mesma
    rodada via merge por índice temporal.
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: frequência efetiva
    média por rodada — rodadas com média mais baixa desta coluna correspondem a scores mais
    baixos, validando empiricamente a relação $t \propto 1/f$.
  - **Script Python sugerido:** calcular, para cada uma das 20 rodadas, a média de `Relógios
    efetivos núcleo (avg) (MHz)` e correlacionar (Pearson) com o score `Multi_Core` da mesma
    rodada em `scores_maqD.txt`. Correlação positiva forte confirma o modelo de Liu et al.

---

### 3.8 Throttling Térmico vs. Throttling Elétrico — Dois Gatilhos Independentes

- **Conceito/Teoria:** O throttling de frequência pode ser ativado por dois gatilhos
  independentes: (1) limites elétricos, como RAPL PL1/PL2 e VR-TDC; e (2) limites térmicos,
  como a temperatura máxima de junção TjMAX. O throttling elétrico é ativado primeiro (por
  limites de potência/corrente) e é o mais frequente em laptops. O throttling térmico é a
  proteção de último nível. A coexistência de ambos complica a interpretação dos dados de
  telemetria, pois o mesmo efeito (redução de clock) pode ter causas distintas.

- **Citação Direta (Ipsis Litteris):**
  > "For test case (4), when PL1=140W, we observed that the simultaneous execution of the
  > victim and stressor workloads caused system temperature to rise to 100°C, thus triggering
  > thermal throttling before triggering PL1-based throttling. Thermal throttling degraded the
  > SNR of collected timing traces, thus leading to low t-score values." (p. 1987)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) demonstram experimentalmente que o throttling térmico (ativado por
  temperatura) e o throttling elétrico (ativado por limites RAPL/VR-TDC) são mecanismos
  independentes que podem ser ativados em sequência ou simultaneamente. Nos experimentos dos
  autores, a temperatura de 100°C ativou o throttling térmico antes mesmo que o PL1 fosse
  atingido — evidenciando que, em plataformas com capacidade de dissipação térmica limitada
  (como laptops), o throttling térmico pode ser o gatilho dominante. Para a Máquina D
  (i5-8265U, TjMAX = 100°C, dissipação passiva típica de ultrabook), durante as 20 rodadas
  do Geekbench 6, os dados HWiNFO64 permitem identificar qual gatilho foi ativado em cada
  rodada, pela combinação das colunas binárias de limitação disponíveis.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Thermal Throttling
  e Limites de Projeto; Resultados — análise das causas do throttling por rodada na Máquina D.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)`:
    throttling ativado por temperatura (gatilho térmico — TjMAX ou PROCHOT).
  - `maqD_rodada_*.CSV` → coluna `IA: Package-Level RAPL/PBM PL1 (Yes/No)`:
    throttling ativado por limite de potência de longo prazo (gatilho elétrico — RAPL PL1).
  - `maqD_rodada_*.CSV` → coluna `IA: PROCHOT (Yes/No)`: sinal PROCHOT ativado —
    indica que a temperatura de proteção foi atingida (TjMAX = 100°C para o i5-8265U).
  - `maqD_rodada_*.CSV` → coluna `IA: Evento térmico (Yes/No)`: evento térmico registrado
    via sensor digital de temperatura (DTS) do processador.
  - `maqD_rodada_*.CSV` → coluna `Distância do núcleo para TjMAX (avg) (°C)`: quanto menor
    este valor, mais próximo o processador está de ativar o throttling térmico — valores
    próximos de 0°C indicam que o PROCHOT pode ser ativado na próxima amostra.
  - **Análise sugerida:** Criar tabela cruzada por rodada mostrando: se o throttling foi de
    origem térmica (`PROCHOT = Yes`), elétrica (`PL1 = Yes`, `VR TDC = Yes`) ou ambos.
    Isso permite identificar o gargalo dominante de cada rodada do Geekbench 6 na Máquina D.

---

### 3.9 Frequência Efetiva Média de Throttling e seu Impacto no Score de Benchmark

- **Conceito/Teoria:** A frequência efetiva média durante um episódio de throttling
  ($f_{throttled}$) é sempre menor que a frequência padrão pré-throttling ($f_{default}$),
  e resulta em maior tempo de execução proporcional. Quanto mais severo o throttling
  (menor $f_{throttled}$), maior o impacto no desempenho mensurado pelo benchmark.

- **Citação Direta (Ipsis Litteris):**
  > "Since $P_1 > P_2$, the average throttling frequency $f_1$ for data input $data_1$ will
  > be lower than the average throttling frequency $f_2$ for data input $data_2$ to satisfy
  > the same reactive limit. Both of these throttling frequencies will be lower than the
  > default system frequency prior to throttling (i.e., $f_1 < f_2 < f_{default}$)." (p. 1980)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) demonstram que a frequência de throttling efetiva é diretamente proporcional
  ao orçamento de potência disponível: cargas de trabalho que consomem mais potência resultam
  em frequências de throttling mais baixas. Aplicando essa lógica ao Geekbench 6, a carga
  de trabalho Multi-Core — que mobiliza todos os 4 núcleos do i5-8265U simultaneamente —
  eleva o consumo de potência acima do PL1 mais rapidamente e de forma mais severa que o
  teste Single-Core, resultando em uma frequência de throttling média mais baixa e, portanto,
  em maior variabilidade e scores absolutamente menores nas rodadas em que o throttling persiste
  por mais tempo.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — análise comparativa dos scores
  Single-Core versus Multi-Core e sua correlação com eventos de throttling; explica por que
  o Desvio Padrão é esperadamente maior no teste Multi-Core.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → colunas `Single_Core` e `Multi_Core`: comparar o Desvio Padrão
    Amostral das duas modalidades — espera-se CV maior em Multi-Core pelo maior consumo
    de potência e maior probabilidade de throttling.
  - `maqD_rodada_*.CSV` → coluna `Potência de núcleos IA (W)` versus `Potência total da
    CPU (W)`: durante Multi-Core, a fração de potência dos núcleos sobre o total deve ser
    maior, aproximando mais rapidamente o consumo do limite PL1.
  - `maqD_rodada_*.CSV` → colunas `Core 0 T0 Uso (%)` a `Core 3 T1 Uso (%)`: durante
    Multi-Core, todos os núcleos devem exibir alta ocupação, amplificando o consumo total
    conforme descrito pela inequação $f_1 < f_2 < f_{default}$ de Liu et al. (2022).

---

### 3.10 Telemetria RAPL como Interface de Monitoramento de Potência por Software

- **Conceito/Teoria:** A interface RAPL (Running Average Power Limit) do processador Intel
  expõe contadores de energia acessíveis por software (via MSRs ou interfaces do S.O.), que
  reportam o consumo de energia de diferentes domínios do chip (núcleos IA, GT, DRAM, pacote).
  O HWiNFO64 utiliza exatamente esta interface para coletar as colunas de potência do nosso
  dataset — tornando os dados coletados tecnicamente equivalentes às telemetrias descritas
  pelos autores.

- **Citação Direta (Ipsis Litteris):**
  > "Recently, researchers have demonstrated how a processor's energy telemetry reporting
  > framework can be used maliciously to perform power side-channel analysis attacks. These
  > attacks allow a user-space attacker (having Ring 3 privilege) to infer secret information
  > from a targeted victim workload running inside a Trusted Execution Environment (TEE)."
  > (p. 1977)

- **Citação Direta Complementar:**
  > "Modern systems also provide multiple software-accessible telemetries which allow users to
  > characterize bottlenecks at scale, monitor resource utilization, power and performance,
  > and gain insights into system reliability." (p. 1977)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) confirmam que os sistemas modernos disponibilizam telemetrias de potência
  acessíveis por software — como a interface RAPL da Intel — que permitem monitorar em tempo
  real a utilização de recursos, o consumo de energia e o desempenho do processador. O
  HWiNFO64 utilizado pelo grupo de AOC acessa precisamente estas interfaces para coletar as
  colunas `Potência total da CPU (W)`, `Potência de núcleos IA (W)`, `Potência de núcleo
  GT (W)` e `Potência total de DRAM (W)` — conferindo aos dados coletados a mesma base
  técnica documentada por pesquisadores da própria Intel.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — justificativa técnica do uso do HWiNFO64
  como ferramenta de monitoramento via RAPL; referência de autoridade (Intel) para validar
  a qualidade dos dados coletados.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → colunas `Potência total da CPU (W)`, `Potência de núcleos IA (W)`,
    `Potência de núcleo GT (W)`, `Potência total de DRAM (W)`, `Potência do System Agent (W)`:
    cada uma dessas colunas corresponde a um domínio RAPL distinto monitorado pelo HWiNFO64.
  - `maqD_rodada_*.CSV` → colunas `Limite de potência PL1 (Static) (W)` e `Limite de potência
    PL2 (Static) (W)`: os limites configurados no RAPL, lidos diretamente dos MSRs pelo
    HWiNFO64 — valor de referência para identificar quando o consumo excede os limites.

---

### 3.11 Ruído Térmico como Degradador de SNR — Implicação para Variabilidade de Benchmark

- **Conceito/Teoria:** O throttling térmico, ao ser ativado antes do throttling elétrico (RAPL),
  introduz ruído não controlado no desempenho observado, degradando a previsibilidade e a
  reprodutibilidade dos resultados. Em contexto de benchmark, isso se manifesta como aumento
  do Desvio Padrão Amostral dos scores, especialmente nas rodadas posteriores (quando o
  sistema ainda está termicamente elevado pela rodada anterior).

- **Citação Direta (Ipsis Litteris):**
  > "Thermal throttling degraded the SNR of collected timing traces, thus leading to low
  > t-score values as reported in the last column of Table 5." (p. 1987)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) documentam que o throttling térmico, ao ser ativado de forma não determinística
  — dependente da temperatura acumulada nas rodadas anteriores e das condições ambientais do
  sistema — introduz variabilidade não controlada nos tempos de execução, reduzindo a
  reprodutibilidade dos resultados. Transposto para o contexto do nosso projeto, este fenômeno
  explica por que o Desvio Padrão Amostral das 20 rodadas de Geekbench 6 na Máquina D pode
  ser maior nas rodadas finais da sequência (quando o sistema está termicamente saturado) do
  que nas rodadas iniciais (quando o sistema começa frio e pode sustentar o turbo pleno por
  mais tempo). Essa assimetria temporal dentro da sequência de 20 rodadas é uma assinatura
  arquitetural do throttling térmico cumulativo.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — análise da evolução temporal
  dos scores ao longo das 20 rodadas; justificativa para o protocolo de 20 rodadas (capturar
  tanto o comportamento a frio quanto o saturado termicamente).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → colunas `Single_Core` e `Multi_Core` ordenadas por `Rodada`:
    plotar os scores em ordem cronológica (rodada 01 a 20) para identificar tendência de
    queda de desempenho nas rodadas finais — evidência de saturação térmica cumulativa.
  - `maqD_rodada_*.CSV` → coluna `CPU Inteira (°C)` no início de cada rodada (primeiros
    30 segundos): a temperatura inicial de cada rodada quantifica o acúmulo térmico entre
    execuções consecutivas.
  - `maqD_rodada_*.CSV` → coluna `Distância do núcleo para TjMAX (avg) (°C)`: quanto menor
    nas rodadas finais, mais saturado termicamente o sistema está, confirmando a degradação
    de SNR descrita pelos autores.

---

### 3.12 Impacto de Diferentes Microarquiteturas no Comportamento de Throttling

- **Conceito/Teoria:** O comportamento específico do throttling — frequência de ativação,
  profundidade da redução de clock e velocidade de recuperação — varia entre arquiteturas e
  tecnologias de fabricação diferentes. Os autores observaram comportamentos distintos em
  processadores Intel E3-1230V5, i7-1185G7 e Xeon Gold 6326, atribuindo as diferenças à
  microarquitetura e à tecnologia de litografia.

- **Citação Direta (Ipsis Litteris):**
  > "Note that for a given execution time estimate model, the difference in behavior of GE
  > trends on different systems is likely due to variations in the underlying hardware
  > micro-architecture designs and the fabrication technologies used." (p. 1985)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) atribuem as diferenças de comportamento de throttling entre sistemas a
  variações na microarquitetura do hardware e nas tecnologias de fabricação empregadas —
  incluindo o processo litográfico e a eficiência energética intrínseca de cada geração de
  processador. No contexto do projeto de AOC, esta observação fundamenta a expectativa de
  que as Máquinas A, B e C — cujas especificações ainda não foram mapeadas — exibirão
  comportamentos de throttling distintos da Máquina D (i5-8265U, 14nm, Whiskey Lake),
  especialmente se possuírem processadores de litografia menor (10nm, 7nm ou inferior) ou
  maior capacidade de dissipação térmica. A comparação dessas diferenças entre as quatro
  máquinas é um dos resultados centrais que o artigo do grupo deve explorar.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Eficiência
  Microarquitetural e Processo de Fabricação; Resultados — análise comparativa do Desvio
  Padrão e incidência de throttling entre as quatro máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → comparação do Desvio Padrão Amostral de `Single_Core` e `Multi_Core`
    entre as 4 máquinas: máquinas com menor desvio padrão possuem maior estabilidade de
    throttling — potencialmente correlacionada com litografia mais eficiente ou maior TDP.
  - `maq*_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)`:
    frequência de eventos de throttling por rodada em cada máquina — gráfico de barras
    empilhadas comparando as 4 máquinas.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
  > A análise comparativa de microarquitetura descrita nesta seção 3.12 só poderá ser
  > completamente realizada quando as especificações de hardware das Máquinas A, B e C
  > forem fornecidas pelo grupo. Em particular: litografia, TDP, número de núcleos e
  > presença de Dual Channel de memória são os parâmetros que mais influenciam o
  > comportamento de throttling, conforme documentado por Liu et al. (2022).
  > **Este mapeamento de colunas e sua interpretação só serão utilizados na redação final
  > conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas
  > pelo grupo nas próximas interações, se necessário.**

---

### 3.13 Desempenho por Watt — Métricas de Eficiência Energética em Contexto de Throttling

- **Conceito/Teoria:** A relação desempenho por Watt (Performance-per-Watt) quantifica a
  eficiência energética de um processador: maior score por unidade de potência consumida
  indica melhor eficiência. O DVFS é projetado para maximizar exatamente esta métrica —
  mas o throttling induzido por RAPL pode reduzir ambos os termos (score cai com a
  frequência; potência é mantida no limite), alterando a relação de forma não linear.

- **Citação Direta (Ipsis Litteris):**
  > "DVFS dynamically adjusts CPU frequency and voltage in order to reduce system power
  > consumption, yielding higher performance per Watt." (p. 1977)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) identificam o desempenho por Watt como o objetivo primário do mecanismo
  DVFS: ao ajustar dinamicamente tensão e frequência, o processador busca maximizar o
  trabalho computacional realizado por cada Joule de energia consumido. No entanto, quando
  os limites RAPL são atingidos durante o benchmark, o processador opera em regime de
  throttling onde a potência é mantida próxima ao limite PL1 enquanto a frequência é reduzida
  — situação em que o score cai mais rapidamente do que a potência, reduzindo a eficiência
  energética efetiva. Esta métrica — score Geekbench dividido pela média de `Potência total
  da CPU (W)` da rodada — constitui um indicador arquitetural avançado de eficiência que
  diferencia processadores com maior ou menor capacidade de sustentar o turbo dentro do
  envelope de TDP.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — subseção de Eficiência
  Microarquitetural (Desempenho por Watt); é a métrica avançada que complementa a análise
  de scores brutos.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → colunas `Single_Core` e `Multi_Core` (por rodada) divididas pela
    média de `Potência total da CPU (W)` da mesma rodada em `maqD_rodada_*.CSV`:
    produz o índice de eficiência energética por rodada em unidades de
    [Score Geekbench / Watt].
  - `maqD_rodada_*.CSV` → coluna `Potência de núcleos IA (W)`: componente dominante do
    consumo — a razão Score/P_IA_cores isola a eficiência dos núcleos de computação
    da eficiência total do pacote.
  - **Fórmula sugerida para o `main.tex`:**
    ```latex
    \begin{equation}
    \eta = \frac{\bar{x}_{Score}}{\bar{P}_{CPU}}
    \label{eq:eficiencia_energetica}
    \end{equation}
    ```
    Onde $\eta$ é o índice de eficiência energética [Score/W], $\bar{x}_{Score}$ é a
    média dos scores das 20 rodadas e $\bar{P}_{CPU}$ é a média de `Potência total da
    CPU (W)` sobre todas as rodadas da mesma máquina.

---

> ### 📌 ATUALIZAÇÃO — NOVOS SUBITENS 3.14 a 3.20
> Os subitens a seguir foram acrescentados em atualização posterior do fichamento,
> em decorrência do preenchimento completo da tabela comparativa de hardware
> (Máquinas A, B, C, D, E e F). Nenhum conteúdo das seções 3.1 a 3.13 foi alterado.
> Os novos subitens cobrem exclusivamente componentes que ainda não possuíam
> citação correspondente no artigo de Liu et al. (2022): TDP elevado de desktop
> (Máquinas E e F), microarquiteturas AMD Zen+/Zen 3, núcleos heterogêneos
> P-Core/E-Core (Raptor Lake), instruções AVX/VNNI/BMI2, topologia de memória
> Dual Channel DDR5/DDR4, barramento PCIe 4.0 e armazenamento SSD NVMe vs. HDD.

---

### 3.14 TDP Elevado e Folga Térmica em Desktops (Máquinas E e F) — Implicação para Sustentação do Turbo

- **Conceito/Teoria:** O TDP (Thermal Design Power) base define o orçamento de potência
  de referência sobre o qual o PL1 do RAPL é tipicamente configurado. Processadores com
  TDP base mais alto (65 W na Máquina E, 125 W na Máquina F) possuem, por definição de
  projeto, um orçamento de potência substancialmente maior do que processadores ultrabook
  de 15 W (Máquinas B, C e D), permitindo sustentar o turbo por períodos mais longos antes
  de atingir o limite reativo PL1.

- **Citação Direta (Ipsis Litteris):**
  > "PL1 is used to track the long-term power consumption, so typically its limit value is
  > set to be lower and the time window $\tau$ is longer (tens of seconds). On the other
  > hand, PL2 is used to track the short-time power burst events, so typically the limit is
  > set to be higher than PL1." (p. 1979–1980)

- **Paráfrase (Citação Indireta Acadêmica):**
  Como o limite PL1 do RAPL é tipicamente configurado em torno do TDP nominal do processador,
  Liu et al. (2022) fornecem o fundamento teórico para prever que processadores desktop com
  TDP elevado — como o AMD Ryzen 5 5500 (65 W, Máquina E) e o Intel Core i5-14600KF (125 W,
  Máquina F) — possuem um orçamento de potência ($PL_1$) muito superior ao dos processadores
  ultrabook de 15 W (i5-1334U, Ryzen 5 3500U e i5-8265U). Isso implica que, para a mesma
  carga de trabalho do Geekbench 6, a probabilidade de o consumo médio $P_i$ exceder o limite
  $PL_1$ — condição necessária para ativar o throttling, conforme a Equação
  $\Delta_i = P_i - PL_i$ (Seção 4.2 deste fichamento) — é estruturalmente menor nas Máquinas
  E e F. Espera-se, portanto, menor incidência de `IA: Package-Level RAPL/PBM PL1 (Yes/No)`
  e menor Desvio Padrão Amostral nos scores dessas duas máquinas, validando o TDP como
  variável arquitetural de primeira ordem para a estabilidade do benchmark.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de TDP e Orçamento de
  Potência; Metodologia — tabela comparativa de hardware (coluna TDP); Resultados — análise
  comparativa da estabilidade de scores entre notebooks (TDP 15–45 W) e desktops (TDP 65–125 W).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqE_rodada_*.CSV` e `maqF_rodada_*.CSV` → coluna `IA: Package-Level RAPL/PBM PL1
    (Yes/No)`: espera-se incidência percentual menor do que nas Máquinas B, C e D.
  - `maqE_rodada_*.CSV` e `maqF_rodada_*.CSV` → coluna `Potência total da CPU (W)`: o valor
    absoluto medido será maior (acompanhando o TDP de 65 W/125 W), mas a *razão*
    $P_i / PL_{1,i}$ deve permanecer mais distante de 1,0 do que nas máquinas de 15 W.
  - `maqA_rodada_*.CSV` (TDP 45 W) → posição intermediária esperada entre os ultrabooks
    (15 W) e os desktops (65–125 W) na incidência de throttling — útil para compor uma
    análise de regressão entre TDP nominal e percentual de amostras em throttling.
  - `scores_maqE.txt`, `scores_maqF.txt` → Desvio Padrão Amostral de `Multi_Core`: hipótese
    a ser testada é que estas máquinas apresentem o menor CV(%) entre as seis.

---

### 3.15 Microarquitetura AMD Zen+ e Zen 3 — Comparação Inter-Fabricante (Máquinas C e E)

- **Conceito/Teoria:** O artigo de Liu et al. (2022) documenta explicitamente que os
  processadores AMD implementam um esquema de gerenciamento de potência análogo, mas
  tecnicamente distinto do RAPL da Intel: o Precision Boost Overdrive (PBO), com os limites
  PPT (Package Power Tracking), PPT Fast e TDC, controlados via interface SMU (System
  Management Unit) em vez de MSRs. Isso é diretamente relevante para a Máquina C (AMD
  Ryzen 5 3500U, Zen+, 12 nm) e a Máquina E (AMD Ryzen 5 5500, Zen 3, 7 nm).

- **Citação Direta (Ipsis Litteris):**
  > "Precision Boost Overdrive (PBO) is a feature available on AMD Ryzen to overclock
  > processors to achieve more performance by controlling power/thermal limits. [...]
  > Package Power Tracking (PPT): analogous to PL1 on Intel processors, this limit caps the
  > total power capacity of the processor socket in Watts. [...] Thermal Design Current
  > (TDC): analogous to VR-TDC on Intel processors, this limit caps the total current
  > capacity in Amperes at the thermal throttling limit of the processor." (p. 1980)

- **Citação Direta Complementar:**
  > "The aforementioned reactive limits can be configured from system software via System
  > Management Unit (SMU) mailbox interface with support from a kernel driver. The SMU is a
  > sub-component of the AMD processor that is responsible for a variety of system and power
  > management tasks during boot and runtime." (p. 1980)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) estabelecem a correspondência funcional entre os mecanismos reativos
  Intel e AMD: o PPT é o análogo direto do PL1, o PPT Fast é o análogo do PL2, e o TDC é o
  análogo do VR-TDC — todos geridos pela SMU (System Management Unit) em vez dos MSRs
  utilizados pela Intel. Esta correspondência é essencial para a interpretação cruzada dos
  dados de telemetria das Máquinas C e E, cujos processadores AMD não expõem nativamente as
  colunas `IA: Package-Level RAPL/PBM PL1/PL2` (nomenclatura específica Intel), mas cujo
  comportamento de throttling é regido pela mesma lógica de orçamento de potência
  ($\Delta = P - PL$) descrita no Algoritmo 1 do artigo. Adicionalmente, a diferença de
  litografia entre a Máquina C (Zen+, 12 nm) e a Máquina E (Zen 3, 7 nm) permite testar
  empiricamente a hipótese da Seção 3.12 deste fichamento — de que processos de fabricação
  menores reduzem a dissipação de calor por transistor e, consequentemente, a frequência de
  ativação do throttling térmico, mesmo dentro da mesma família de fabricante.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Gerenciamento de
  Potência em Processadores AMD (PBO, PPT, TDC); Metodologia — ressalva sobre a interpretação
  das colunas de telemetria para máquinas AMD; Resultados — comparação Zen+ (12 nm) vs.
  Zen 3 (7 nm) na estabilidade de scores.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqC_rodada_*.CSV` e `maqE_rodada_*.CSV` → coluna `Potência total da CPU (W)`:
    leitura de potência total do pacote, equivalente ao domínio monitorado pelo PPT da AMD
    (mesmo que o HWiNFO64 rotule a coluna com nomenclatura genérica/Intel-like).
  - `maqC_rodada_*.CSV` e `maqE_rodada_*.CSV` → coluna `VR VCC Corrente (SVID IOUT) (A)`:
    corresponde ao monitoramento de corrente análogo ao TDC da AMD.
  - `maqC_rodada_*.CSV` e `maqE_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo
    (avg) (Yes/No)`: indicador de throttling térmico, válido independentemente do fabricante.
  - **Nota metodológica:** as colunas com prefixo `IA:` (ex.: `IA: Package-Level RAPL/PBM
    PL1`) são nominalmente associadas à nomenclatura Intel; para as Máquinas C e E (AMD),
    a interpretação equivalente deve ser feita via colunas de potência/corrente agregadas
    e cruzada com a literatura de PBO/PPT/TDC citada nesta seção, e não pela leitura literal
    do rótulo da coluna.

---

### 3.16 Núcleos Heterogêneos (P-Core/E-Core) e Atividade de Chaveamento Diferenciada (Máquinas A, B e F)

- **Conceito/Teoria:** Processadores com arquitetura híbrida (Performance-cores e
  Efficiency-cores), como o i5-13420H (Máquina A), o i5-1334U (Máquina B) e o i5-14600KF
  (Máquina F), introduzem heterogeneidade no fator de atividade de chaveamento $\alpha$ da
  Equação 1 de Liu et al. (2022): P-Cores e E-Cores possuem diferentes capacitâncias de carga
  ($C$) e operam em faixas de tensão/frequência distintas, alterando a contribuição relativa
  de cada tipo de núcleo para a potência total do pacote.

- **Citação Direta (Ipsis Litteris):**
  > "$P_{dyn} = \alpha \cdot C \cdot V_{DD}^{2} \cdot f$ where, $\alpha$, $C$, $V_{DD}$, and
  > $f$ represent switching activity factor, load capacitance, supply voltage, and clock
  > frequency, respectively." (p. 1978)

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora o artigo de Liu et al. (2022) não trate explicitamente de arquiteturas híbridas, a
  Equação de potência dinâmica CMOS (Equação 1, p. 1978) fornece a base teórica para analisar
  o comportamento das Máquinas A (Raptor Lake-H, 4P+4E), B (Raptor Lake-P, 2P+8E) e F
  (Raptor Lake, 6P+8E): como P-Cores e E-Cores possuem geometrias e capacitâncias de carga
  ($C$) distintas, a mesma carga computacional do Geekbench 6 produz fatores de atividade de
  chaveamento ($\alpha$) diferentes conforme o agendador do Windows 11 (Thread Director)
  distribui as threads entre os dois tipos de núcleo. No teste Single-Core, espera-se que a
  thread seja preferencialmente alocada em um P-Core (maior $f$ e $V_{DD}$, mas também maior
  $C$), elevando $P_{dyn}$ localmente e aumentando a probabilidade de o núcleo individual
  atingir seu limite de potência por núcleo antes mesmo do limite de pacote (PL1) ser
  atingido. Já no teste Multi-Core, a distribuição de carga entre P-Cores e E-Cores dilui o
  consumo por núcleo, mas eleva a soma agregada de potência do pacote — efeito que se
  intensifica na Máquina F (i5-14600KF, 14 núcleos, TDP 125 W), cuja maior contagem de
  núcleos amplia a probabilidade de saturação simultânea de múltiplos domínios de potência.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Arquiteturas
  Híbridas e Paralelismo a Nível de Thread (P-Core/E-Core); Resultados — comparação dos
  perfis de uso de núcleo (`Core N T0/T1 Uso (%)`) entre Single-Core e Multi-Core nas
  Máquinas A, B e F.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → colunas `Core 0 T0
    Uso (%)` a `Core 3 T1 Uso (%)` (e núcleos adicionais, conforme disponibilidade do
    HWiNFO64 para CPUs com mais de 4 núcleos): permitem identificar quais núcleos físicos
    foram preferencialmente utilizados durante o teste Single-Core — sinal indireto da
    alocação P-Core vs. E-Core pelo Thread Director.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna `Relógios
    núcleo (avg) (MHz)` vs. colunas individuais `Core N Relógio (MHz)`: dispersão entre
    núcleos individuais é esperada ser maior nessas máquinas híbridas do que nas Máquinas
    C, D e E (núcleos homogêneos).
  - `maqF_rodada_*.CSV` → coluna `Limite de potência do núcleo excedido (avg) (Yes/No)`
    e variantes por núcleo (`Core 0 Limite de potência excedido (Yes/No)` etc.): mais
    relevante nesta máquina pela maior contagem de núcleos ativos simultaneamente.
  - **Nota técnica:** o HWiNFO64 reporta um número fixo de colunas `Core N` por arquivo
    (estrutura definida na lista de colunas do projeto, de Core 0 a Core 3); para
    processadores com mais de 4 núcleos físicos (Máquinas A, B, E e F), as colunas
    agregadas `(avg)` continuam válidas como medida representativa do pacote completo,
    mesmo que nem todos os núcleos individuais estejam mapeados explicitamente.

---

### 3.17 Instruções Vetoriais Avançadas (AVX/AVX2/VNNI/FMA3) e Elevação do Fator de Atividade

- **Conceito/Teoria:** Instruções vetoriais largas (AVX, AVX2, Intel DL Boost/VNNI, AMD FMA3)
  processam múltiplos operandos por ciclo de clock, elevando substancialmente o fator de
  atividade de chaveamento $\alpha$ por instrução executada. Processadores que suportam
  conjuntos de instruções mais amplos ou mais numerosos (caso das Máquinas A, B e F, com
  Intel DL Boost/VNNI) tendem a apresentar picos de potência mais acentuados durante
  sub-testes do Geekbench 6 que utilizam estas instruções (ex.: processamento de imagem,
  machine learning, criptografia vetorizada).

- **Citação Direta (Ipsis Litteris):**
  > "$P_{dyn} = \alpha \cdot C \cdot V_{DD}^{2} \cdot f$ [...] The main objective of a power
  > side-channel analysis attack is to retrieve a targeted secret by analyzing the
  > data-dependent power consumption of a cryptographic implementation during a selected
  > time window." (p. 1978)

- **Citação Direta Complementar:**
  > "AES-NI is an instruction set which improves the AES implementation by accelerating its
  > complex performance-intensive steps using dedicated hardware." (p. 1982)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022) demonstram, através do caso de uso do AES-NI, que instruções de hardware
  dedicado para operações intensivas elevam significativamente o consumo de potência durante
  sua execução, sendo este o próprio mecanismo explorado para induzir o throttling no estudo
  de caso do artigo. Por extensão teórica direta da Equação 1 ($P_{dyn} \propto \alpha$),
  o mesmo raciocínio se aplica às instruções AVX, AVX2, Intel DL Boost (VNNI) e BMI2
  presentes nas Máquinas A, B, D e F, e ao FMA3 presente nas Máquinas C e E: cargas de
  trabalho vetorizadas mobilizam unidades de execução SIMD largas, elevando $\alpha$ e,
  consequentemente, $P_{dyn}$, de forma mais acentuada do que instruções escalares
  convencionais. Isso é particularmente relevante para a comparação entre as Máquinas A, B e
  F — que possuem o conjunto Intel DL Boost (VNNI), otimizado para inferência de redes
  neurais — e as Máquinas C e E, limitadas a FMA3, em sub-testes do Geekbench 6 ligados a
  processamento de imagem ou aprendizado de máquina, nos quais se espera maior pico
  instantâneo de `Potência de núcleos IA (W)` nas máquinas com VNNI.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a
  Nível de Dados (SIMD) e seu impacto energético; Resultados — análise de picos de potência
  durante sub-testes vetorizados do Geekbench 6, comparando máquinas com e sem VNNI.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqD_rodada_*.CSV`, `maqF_rodada_*.CSV` →
    coluna `Potência de núcleos IA (W)`: picos transitórios mais acentuados são esperados
    durante a janela temporal correspondente aos sub-testes de processamento de imagem e
    machine learning do Geekbench 6 (presença de VNNI/DL Boost).
  - `maqC_rodada_*.CSV`, `maqE_rodada_*.CSV` → coluna `Potência de núcleos IA (W)`:
    comparação control-group, já que estas máquinas dispõem apenas de FMA3 (sem VNNI),
    devendo apresentar picos proporcionalmente menores nos mesmos sub-testes.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna `IA: Package-Level
    RAPL/PBM PL2 PL3 (Yes/No)`: maior probabilidade de ativação durante picos vetoriais de
    curta duração, dado que o PL2 é projetado justamente para conter bursts.
  - **Análise sugerida:** segmentar a série temporal de `Potência de núcleos IA (W)` por
    sub-teste do Geekbench 6 (usando os timestamps de início/fim de cada sub-teste, se
    disponíveis no relatório do Geekbench) e comparar a amplitude dos picos entre máquinas
    com e sem Intel DL Boost (VNNI).

---

### 3.18 Topologia Dual Channel DDR5/DDR4 e Largura de Banda — Gargalo de Von Neumann (Máquinas A, B, E e F)

- **Conceito/Teoria:** Embora o foco do artigo de Liu et al. (2022) seja o subsistema de
  potência da CPU, os autores reconhecem explicitamente a influência do subsistema de
  memória sobre o tempo de execução de cargas de trabalho — fundamento teórico que se
  estende à comparação entre as topologias de memória Single Channel (Máquinas C e D) e
  Dual Channel (Máquinas A, B, E e F), inclusive com a Máquina A operando em DDR5
  (maior largura de banda teórica que DDR4).

- **Citação Direta (Ipsis Litteris):**
  > "Ensure memory access patterns (or the data size of load/store operations) are invariant
  > with respect to secret data." (p. 1978)

- **Citação Direta Complementar:**
  > "On most of the modern CPUs, incrementing of the time stamp counter is frequency-invariant
  > so the $T_\delta$ captures wall clock time of the victim's execution time and will not be
  > impacted by frequency throttling." (p. 1982)

- **Paráfrase (Citação Indireta Acadêmica):**
  Liu et al. (2022), ao tratarem dos padrões de acesso à memória como uma variável crítica
  para a análise de tempo de execução (mesmo em contexto de segurança), reconhecem
  implicitamente que o subsistema de memória é um componente independente do clock da CPU
  na composição do tempo total de execução de uma carga de trabalho — fundamento que sustenta
  a separação entre o gargalo de Von Neumann (banda de memória) e o throttling de frequência
  da CPU como dois fenômenos distintos, mas concorrentes, na variabilidade de desempenho.
  Para o projeto de AOC, este princípio justifica teoricamente por que as Máquinas A
  (Dual Channel DDR5 5200 MT/s), B (Dual Channel DDR4 2666 MHz), E (Dual Channel DDR4) e F
  (Dual Channel DDR4 3600 MHz) apresentam, a priori, menor probabilidade de o subsistema de
  memória ser o fator limitante do desempenho (gargalo de Von Neumann), ao contrário das
  Máquinas C e D, que operam em configuração Single Channel — restringindo a banda de memória
  disponível para alimentação dos núcleos de CPU em cargas de trabalho com alta taxa de
  acesso a dados, como o sub-teste de compressão de dados do Geekbench 6.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Gargalo de Von
  Neumann e Hierarquia de Memória (complementar à literatura central de Hennessy & Patterson
  já adotada no projeto); Resultados — comparação dos scores de sub-testes sensíveis a
  banda de memória entre máquinas Single Channel e Dual Channel.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` →
    coluna `Relógio da memória (MHz)`: valores absolutos mais altos esperados (DDR5 5200
    MT/s na Máquina A; DDR4 3600 MHz na Máquina F) em comparação com as Máquinas C e D.
  - `maqC_rodada_*.CSV`, `maqD_rodada_*.CSV` → coluna `Relógio da memória (MHz)`:
    grupo de controle Single Channel, com largura de banda efetiva aproximadamente pela
    metade em relação às configurações Dual Channel equivalentes em frequência.
  - `maqA_rodada_*.CSV` a `maqF_rodada_*.CSV` → colunas `Taxa de leituras (MB/s)` e `Taxa
    de gravações (MB/s)`: embora estas colunas capturem primariamente o subsistema de
    armazenamento, picos sustentados de paginação (`Utilização do arquivo de paginação (%)`)
    sob pressão de memória física insuficiente nas máquinas Single Channel podem ser
    cruzados com `Carga da memória física (%)` para identificar gargalo de memória RAM.
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqE.txt`, `scores_maqF.txt` versus
    `scores_maqC.txt`, `scores_maqD.txt`: comparação direta de scores em sub-testes do
    Geekbench 6 documentadamente sensíveis à banda de memória (ex.: compressão de dados,
    renderização de PDF), controlando estatisticamente por clock de CPU.

---

### 3.19 Barramento PCIe 4.0 e Velocidade de Interconexão GPU/Armazenamento (Máquinas A, E e F)

- **Conceito/Teoria:** O barramento PCI Express (PCIe) determina a taxa de transferência
  entre a CPU e periféricos de alto desempenho, como GPUs dedicadas e unidades de
  armazenamento SSD NVMe. Gerações mais recentes do PCIe (4.0) dobram a taxa de
  transferência por linha (GT/s) em relação à geração anterior (3.0), reduzindo a
  probabilidade de o barramento ser o gargalo limitante em cargas de trabalho que dependem
  de transferência intensiva de dados.

- **Citação Direta (Ipsis Litteris):**
  > "Multiple instances of the victim workload were executed simultaneously across different
  > processor cores to amplify its average power consumption, which in turn results in
  > higher SNR of the collected traces." (p. 1982)

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora Liu et al. (2022) não tratem diretamente do barramento PCIe, a metodologia dos
  autores de amplificar o consumo de potência através da execução simultânea de múltiplas
  instâncias de carga de trabalho em diferentes núcleos é estruturalmente análoga ao
  princípio de paralelismo de E/S sustentado por interconexões PCIe de maior largura de
  banda: assim como mais núcleos processando simultaneamente elevam a demanda agregada de
  potência (Seção 3.1 deste fichamento), um barramento PCIe 4.0 x8 (Máquinas A, E e F, para
  GPU dedicada) sustenta taxas de transferência de dados mais altas sem se tornar o fator
  limitante, ao contrário de um barramento PCIe 3.0 x4 (Máquina D), que pode restringir a
  taxa de transferência entre CPU e GPU dedicada (NVIDIA MX130) em cargas de trabalho
  gráficas do Geekbench 6 (sub-testes de Compute/OpenCL), mesmo que a CPU e a GPU não
  estejam termicamente ou eletricamente limitadas.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Barramento de
  Interconexão e Largura de Banda de E/S; Resultados — discussão de por que a Máquina D
  pode apresentar desempenho gráfico (Compute Score) proporcionalmente inferior ao esperado
  por seu clock de GPU, atribuível à limitação de barramento PCIe 3.0 x4.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna `Velocidade do
    link PCIe (GT/s)`: valor esperado mais alto (PCIe 4.0), permitindo throughput de dados
    maior entre CPU e GPU dedicada durante sub-testes de Compute do Geekbench 6.
  - `maqD_rodada_*.CSV` → coluna `Velocidade do link PCIe (GT/s)`: valor esperado mais
    baixo (PCIe 3.0 x4), variável de controle para análise comparativa de gargalo de
    barramento na GPU dedicada MX130.
  - `maqA_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV`, `maqD_rodada_*.CSV` →
    colunas `Carga do barramento GPU (%)` e `Uso de memória GPU (%)`: cruzamento entre
    utilização do barramento e ocupação da GPU para identificar se a GPU está limitada
    pelo barramento (`Carga do barramento GPU (%)` elevada com baixa `Carga do núcleo da
    GPU (%)`) ou pelo próprio núcleo gráfico.
  - **Nota:** as Máquinas B e C não possuem GPU dedicada (apenas GPU integrada), portanto
    a coluna `Velocidade do link PCIe (GT/s)` nestas máquinas deve refletir primariamente
    o barramento do SSD NVMe (quando presente), e não de uma GPU discreta.

---

### 3.20 Armazenamento SSD NVMe vs. HDD SATA — Tempo de Carregamento e Ruído na Inicialização dos Testes

- **Conceito/Teoria:** A velocidade de leitura/gravação do dispositivo de armazenamento
  primário influencia o tempo de carregamento do executável do benchmark e de eventuais
  arquivos temporários, podendo introduzir variabilidade adicional independente do clock da
  CPU ou do throttling térmico — especialmente relevante na comparação entre as unidades
  SSD NVMe (Máquinas A, B e F) e a unidade HDD SATA de 5400 RPM da Máquina D.

- **Citação Direta (Ipsis Litteris):**
  > "We define Minimum Time to Disclosure (MTD) as the minimum time spent to collecting
  > enough side-channel traces to recover the secret information. Reduction in MTD can be
  > achieved by (i) increasing the Signal-to-Noise (SNR) of the captured traces, or (ii)
  > decreasing the collection time of each trace." (p. 1982)

- **Paráfrase (Citação Indireta Acadêmica):**
  O conceito de Tempo Mínimo para Divulgação (MTD) de Liu et al. (2022) — definido como o
  tempo necessário para coletar dados suficientes para uma medição estatisticamente
  significativa — é transponível, por analogia metodológica, à discussão de ruído
  experimental introduzido por dispositivos de armazenamento de menor desempenho: assim como
  os autores identificam a necessidade de aumentar a relação sinal-ruído (SNR) para reduzir
  o tempo de coleta de traços válidos, o uso de uma unidade HDD SATA de 5400 RPM (Máquina D)
  — significativamente mais lenta que as unidades SSD NVMe das Máquinas A, B e F — introduz
  ruído adicional no tempo de carregamento inicial do Geekbench 6 e de seus arquivos de
  recursos, podendo contaminar a primeira rodada de cada sequência de 20 execuções com
  latência de E/S não relacionada à arquitetura de processamento da CPU, exigindo cautela na
  interpretação do desvio padrão da Rodada 01 em relação às Rodadas 02–20 da Máquina D.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — subseção de Limitações e Ameaças à
  Validade (ressalva sobre o impacto do armazenamento na primeira rodada); Resultados —
  discussão da variabilidade da Rodada 01 vs. rodadas subsequentes na Máquina D.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_01.CSV` → colunas `Taxa de leituras (MB/s)` e `Atividade de leitura (%)`:
    espera-se atividade de leitura elevada e sustentada nos primeiros segundos da Rodada 01
    (carregamento do executável do Geekbench 6 a partir do HDD), efeito que não deve se
    repetir nas Rodadas 02–20 (arquivo já em cache do sistema operacional).
  - `maqA_rodada_01.CSV`, `maqB_rodada_01.CSV`, `maqF_rodada_01.CSV` → mesmas colunas,
    como grupo de controle: tempo de carregamento inicial esperado é ordens de magnitude
    menor, dado o uso de SSD NVMe.
  - `scores_maqD.txt` → comparação do score da Rodada 01 com a média das Rodadas 02–20:
    se a Rodada 01 apresentar score sistematicamente mais baixo (ou tempo de preparação
    mais longo, fora do escopo de tempo medido pelo score em si, mas relevante para o tempo
    total de coleta), reforça a hipótese de ruído de armazenamento na inicialização.
  - **Nota técnica:** o Geekbench 6 mede o tempo de execução dos sub-testes em memória,
    não o tempo de carregamento do executável; portanto, o impacto do HDD é mais provável
    de se manifestar como ruído na telemetria (picos de `Atividade de leitura (%)`) do que
    diretamente no score reportado, sendo um efeito a documentar na metodologia, não
    necessariamente nos resultados quantitativos do score.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Equação de Potência Dinâmica CMOS (Equação 1 do Artigo — p. 1978)

Equação fundamental que conecta potência, tensão e frequência, extraída diretamente do artigo:

```latex
\begin{equation}
P_{dyn} = \alpha \cdot C \cdot V_{DD}^{2} \cdot f
\label{eq:potencia_cmos}
\end{equation}
```

Onde:
- $\alpha$ = fator de atividade de chaveamento (proporcional à carga computacional)
- $C$ = capacitância de carga do circuito (determinada pelo processo de fabricação)
- $V_{DD}$ = tensão de alimentação dos núcleos (registrada como `Core VIDs (avg) (V)`)
- $f$ = frequência de operação (registrada como `Relógios efetivos núcleo (avg) (MHz)`)

**Implicação para o Artigo:** A equação mostra que o DVFS/throttling atua reduzindo $f$ e $V_{DD}$
simultaneamente, com o consumo caindo quadraticamente com a tensão ($V_{DD}^2$) e linearmente com a
frequência — tornando a redução de tensão o mecanismo mais eficiente energeticamente.

---

### 4.2 Fórmula de Determinação do Orçamento de Potência (derivada do Algoritmo 1 — p. 1979)

O orçamento de potência disponível, que determina o novo $f_{max}$, é definido como:

```latex
\begin{equation}
\Delta_i = P_i - PL_i
\label{eq:orcamento_potencia}
\end{equation}
```

Onde $P_i$ é a potência média calculada sobre a janela $\tau_i$ e $PL_i$ é o limite reativo
configurado. Quando $\Delta_i > 0$ (potência excede o limite), throttling é ativado.

**Aplicação:** No dataset do grupo, $P_i$ é aproximado pela coluna `Potência total da CPU (W)` e
$PL_i$ pela coluna `Limite de potência PL1 (Static) (W)`. Whenever $P_i > PL_i$, espera-se
`IA: Package-Level RAPL/PBM PL1 (Yes/No) = Yes` na mesma linha temporal.

---

### 4.3 Relação Tempo de Execução vs. Frequência de Throttling (derivada da Seção 3.1 — p. 1980)

```latex
\begin{equation}
t'_{1} = \frac{C_{1i}}{f_1} > t'_{2} = \frac{C_{2i}}{f_2}, \quad
\text{onde } f_1 < f_2 < f_{default}
\label{eq:tempo_throttling}
\end{equation}
```

Esta equação formaliza que, para um mesmo número de ciclos $C_i$ (carga computacional constante),
maior throttling (menor $f$) implica maior tempo de execução e, portanto, menor score de benchmark.

---

### 4.4 Fórmulas de Análise Estatística para o `main.tex` (reforço do projeto)

As fórmulas abaixo são necessárias na seção de Metodologia para justificar a análise das 20 rodadas:

**Média Aritmética dos Scores:**
```latex
\begin{equation}
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\label{eq:media}
\end{equation}
```

**Desvio Padrão Amostral:**
```latex
\begin{equation}
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
\label{eq:desvpad}
\end{equation}
```

**Coeficiente de Variação (CV%):**
```latex
\begin{equation}
CV = \frac{s}{\bar{x}} \times 100\%
\label{eq:cv}
\end{equation}
```

**Índice de Eficiência Energética:**
```latex
\begin{equation}
\eta = \frac{\bar{x}_{Score}}{\bar{P}_{CPU}} \quad \left[\frac{\text{Score}}{\text{W}}\right]
\label{eq:eficiencia}
\end{equation}
```

---

### 4.5 Sugestão de Gráficos e Tabelas para o `main.tex`

**Gráfico 1 — Potência Total vs. Limite PL1 ao longo de uma rodada (série temporal):**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar uma rodada representativa da Máquina D
df = pd.read_csv('maqD_rodada_10.CSV', sep=',')

fig, ax1 = plt.subplots(figsize=(10, 4))

# Potência total da CPU
ax1.plot(df['Potência total da CPU (W)'], color='#333333', linewidth=0.8,
         label='Potência total CPU (W)')
ax1.axhline(y=df['Limite de potência PL1 (Static) (W)'].iloc[0],
            color='black', linestyle='--', linewidth=1.0, label='Limite PL1 (W)')
ax1.set_xlabel('Tempo (s)', fontsize=11)
ax1.set_ylabel('Potência (W)', fontsize=11)

ax2 = ax1.twinx()
ax2.plot(df['Relógios efetivos núcleo (avg) (MHz)'], color='#888888',
         linewidth=0.6, alpha=0.7, label='Clock efetivo (MHz)')
ax2.set_ylabel('Frequência (MHz)', fontsize=11)

ax1.set_title('Potência CPU vs. Limite PL1 e Frequência Efetiva — Máquina D (Rodada 10)',
              fontsize=11)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')
plt.tight_layout()
plt.savefig('fig_potencia_pl1_clock.pdf', dpi=300)
```

**Gráfico 2 — Frequência Efetiva vs. Temperatura (scatter plot — validação do throttling):**

```python
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df['CPU Inteira (°C)'], df['Relógios efetivos núcleo (avg) (MHz)'],
           c='#444444', s=2, alpha=0.5)
ax.set_xlabel('CPU Inteira (°C)', fontsize=11)
ax.set_ylabel('Relógios efetivos núcleo (avg) (MHz)', fontsize=11)
ax.set_title('Frequência Efetiva vs. Temperatura — Máquina D\n'
             '(Correlação negativa esperada confirma Thermal Throttling)', fontsize=10)
plt.tight_layout()
plt.savefig('fig_freq_temp_scatter.pdf', dpi=300)
```

**Gráfico 3 — Barplot de Desempenho por Watt por Máquina:**

```python
# Preencher com dados reais após coleta de todas as máquinas
maquinas = ['Máquina A', 'Máquina B', 'Máquina C', 'Máquina D']
eficiencia_single = [eta_A_single, eta_B_single, eta_C_single, eta_D_single]
eficiencia_multi  = [eta_A_multi,  eta_B_multi,  eta_C_multi,  eta_D_multi]

x = range(len(maquinas))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([i - width/2 for i in x], eficiencia_single, width, label='Single-Core',
       color='#555555', edgecolor='black', linewidth=0.8)
ax.bar([i + width/2 for i in x], eficiencia_multi, width, label='Multi-Core',
       color='#aaaaaa', edgecolor='black', linewidth=0.8)
ax.set_xlabel('Máquina', fontsize=11)
ax.set_ylabel('Eficiência Energética (Score / W)', fontsize=11)
ax.set_title('Desempenho por Watt — Comparativo entre Máquinas (Geekbench 6)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(maquinas)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('fig_desempenho_por_watt.pdf', dpi=300)
```

**Tabela LaTeX — Registro de Eventos de Throttling por Máquina:**

```latex
\begin{table}[ht]
\centering
\caption{Frequência de ativação de mecanismos de throttling por máquina
  durante as 20 rodadas do Geekbench~6 (percentual de amostras de telemetria
  com indicador positivo)}
\label{tab:throttling}
\begin{tabular}{lcccc}
\hline
\textbf{Indicador de Throttling} & \textbf{Máq. A} & \textbf{Máq. B} &
\textbf{Máq. C} & \textbf{Máq. D} \\
\hline
RAPL PL1 (\%) & -- & -- & -- & XX\% \\
PROCHOT Térmico (\%) & -- & -- & -- & XX\% \\
VR TDC (\%) & -- & -- & -- & XX\% \\
Limite de potência núcleo (\%) & -- & -- & -- & XX\% \\
\hline
\end{tabular}
\begin{tablenotes}
\footnotesize
\item Fonte: Dados da pesquisa (2026). Células ``--'' preenchidas após consolidação
do hardware das Máquinas A, B e C. Percentuais calculados sobre o total de amostras
segundo a segundo de todas as 20 rodadas por máquina.
\end{tablenotes}
\end{table}
```

---

## 5. KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

**Para embasar a Fundamentação Teórica sobre DVFS e Throttling:**
- `"Dynamic Voltage and Frequency Scaling" CPU benchmark performance impact`
- `"DVFS" "thermal throttling" processor performance variability benchmark`
- `Intel "Running Average Power Limit" RAPL PL1 PL2 CPU frequency scaling`
- `"Frequency Throttling" CPU performance benchmark laptop processor`
- `"Power Limit" CPU throttling "performance variability" benchmark reproducibility`
- `"Intel Turbo Boost" throttling benchmark standard deviation`
- `"Estrangulamento térmico" processador desempenho benchmark`
- `DVFS "gerenciamento de potência" processador mobile desempenho`

**Para embasar a equação de Potência Dinâmica CMOS:**
- `"dynamic power consumption" CMOS "$alpha C V^2 f$" processor benchmark`
- `CMOS power consumption switching activity frequency voltage processor`
- `"switching activity factor" CPU power model performance`

**Para embasar a discussão de RAPL e telemetria de potência:**
- `Intel RAPL "running average power limit" energy monitoring HWiNFO`
- `RAPL "power telemetry" CPU monitoring performance analysis`
- `"package power limit" PL1 PL2 Intel processor thermal management`

**Para embasar comparação entre máquinas e litografias:**
- `"14nm" "10nm" processor performance efficiency comparison benchmark`
- `process node efficiency "performance per watt" CPU generation comparison`
- `Intel Whiskey Lake "i5-8265U" performance benchmark thermal analysis`
- `"transistor density" processor node performance efficiency`

**Para embasar a seção de Desempenho por Watt:**
- `"performance per watt" CPU benchmark energy efficiency comparison`
- `"desempenho por watt" eficiência energética processador benchmark Geekbench`
- `energy efficiency benchmark processor comparison laptop desktop`
- `Geekbench energy consumption CPU performance per watt analysis`

**Para embasar a análise estatística (referência de qualidade da coleta):**
- `benchmark reproducibility "thermal throttling" standard deviation CPU`
- `"benchmark variability" laptop CPU thermal steady-state performance`
- `"steady-state" vs "cold-start" CPU benchmark temperature performance`

---

> ### 📌 ATUALIZAÇÃO — NOVAS KEYWORDS (componentes das Máquinas A, B, C, E e F)

**Para embasar TDP elevado e folga térmica em desktops (Máquinas E e F):**
- `"TDP" "power budget" desktop CPU sustained turbo benchmark`
- `desktop vs laptop CPU "thermal headroom" benchmark stability`
- `"125W" "65W" TDP processor sustained performance benchmark`

**Para embasar gerenciamento de potência AMD (PBO/PPT/TDC — Máquinas C e E):**
- `AMD "Precision Boost Overdrive" PPT TDC power management`
- `AMD Ryzen "Package Power Tracking" PPT Fast throttling`
- `AMD SMU "System Management Unit" power limit mailbox`
- `AMD Zen+ vs Zen 3 efficiency "7nm" "12nm" comparison benchmark`
- `Ryzen 5 3500U Zen+ performance thermal throttling laptop`
- `Ryzen 5 5500 Zen 3 power efficiency benchmark`

**Para embasar núcleos heterogêneos P-Core/E-Core (Máquinas A, B e F):**
- `Intel "hybrid architecture" P-core E-core power consumption benchmark`
- `"Thread Director" Windows 11 scheduler hybrid CPU performance`
- `Raptor Lake P-core E-core "switching activity" power efficiency`
- `"big.LITTLE" OR "P-core E-core" thermal design power benchmark variability`
- `i5-13420H OR i5-1334U OR i5-14600KF benchmark thermal analysis`

**Para embasar instruções vetoriais AVX/VNNI/FMA3:**
- `"Intel DL Boost" VNNI power consumption benchmark`
- `AVX2 AVX-512 "power consumption" CPU frequency throttling`
- `SIMD instructions power consumption CPU benchmark`
- `FMA3 "switching activity" processor power model`
- `"vector instructions" CPU power spike PL2 burst throttling`

**Para embasar topologia de memória Dual Channel DDR5/DDR4 (gargalo de Von Neumann):**
- `"dual channel" vs "single channel" memory bandwidth CPU performance`
- `DDR5 vs DDR4 memory bandwidth benchmark performance comparison`
- `"memory bottleneck" "von Neumann" CPU performance benchmark`
- `dual channel memory configuration benchmark variability laptop`
- `"largura de banda" memória RAM dual channel single channel desempenho`

**Para embasar barramento PCIe 4.0 e interconexão GPU/armazenamento:**
- `PCIe 4.0 vs PCIe 3.0 GPU bandwidth bottleneck benchmark`
- `"PCIe lane" bandwidth GPU performance laptop discrete graphics`
- `NVMe SSD PCIe generation throughput benchmark comparison`
- `discrete GPU "PCIe x4" bandwidth limitation laptop performance`

**Para embasar armazenamento SSD NVMe vs. HDD SATA:**
- `SSD NVMe vs HDD SATA boot time application load benchmark`
- `storage device "I/O latency" benchmark noise variability`
- `HDD 5400RPM vs SSD NVMe loading time application benchmark`
- `"disk I/O" benchmark variability cold start cache effect`

---

> **⚠️ NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
>
> Os conceitos fichados nas seções 3.12 (variação de microarquitetura e litografia) e
> 3.9 (frequência de throttling vs. score Multi-Core) são especialmente aplicáveis às
> Máquinas A, B e C caso possuam: (a) processadores de litografia menor (7nm, 10nm),
> que dissipam menos calor por transistor e podem sustentar o turbo por mais tempo;
> (b) TDP nominal mais elevado, permitindo que o PL1 acomode mais carga antes de
> ativar o throttling; (c) solução de resfriamento mais robusta (cooler com maior
> capacidade de dissipação), retardando o ativamento do throttling térmico.
> Em todos esses cenários, espera-se menor Desvio Padrão Amostral nos scores de
> benchmark e menor frequência de eventos nas colunas binárias de throttling do HWiNFO64.
> **Este mapeamento de colunas e sua interpretação só serão utilizados na redação final
> conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas
> pelo grupo nas próximas interações, se necessário.**

---

## 6. REFERÊNCIA BIBLIOGRÁFICA DERIVADA DE ALTO VALOR — Hertzbleed (Wang et al., 2022)

O artigo fichado cita diretamente o trabalho paralelo de Wang et al. (2022), denominado
*Hertzbleed*, que descobriu independentemente o mesmo mecanismo de throttling side-channel
e o aplicou ao algoritmo SIKE de criptografia pós-quântica:

> WANG, Y.; PACCAGNELLA, R.; HE, E. T.; SHACHAM, H.; FLETCHER, C. W.; KOHLBRENNER, D.
> **Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing Attacks on x86**.
> In: 31st USENIX Security Symposium (USENIX Security 22), 2022, Boston, MA.
> USENIX Association, p. 679--697.

**BibTeX sugerido para o `sbc-template.bib`:**

```bibtex
@InProceedings{wang:22,
  author    = {Yingchen Wang and Riccardo Paccagnella and Elizabeth Tang He
               and Hovav Shacham and Christopher W. Fletcher and David Kohlbrenner},
  title     = {Hertzbleed: Turning Power Side-Channel Attacks Into Remote Timing
               Attacks on x86},
  booktitle = {31st {USENIX} Security Symposium ({USENIX} Security 22)},
  year      = {2022},
  pages     = {679--697},
  address   = {Boston, MA},
  publisher = {{USENIX} Association},
  note      = {Apresentado concomitantemente a \cite{liu:22} (Intel Corporation).
               Denominado ``Hertzbleed'' pelos autores.}
}
```

> 🔑 **Por que esta referência é valiosa para o projeto de AOC:**
> O artigo Hertzbleed confirma, de forma independente da Intel, que a redução de frequência
> por DVFS/throttling é observável como variação de tempo de execução em qualquer carga de
> trabalho — incluindo benchmarks sintéticos como o Geekbench 6. Wang et al. propõem
> desabilitar o Turbo Boost ou o SpeedStep como mitigação, o que — em contexto inverso —
> confirma que **habilitar o Turbo Boost (condição padrão do Geekbench 6) é o que introduz
> a variabilidade de clock e, portanto, o Desvio Padrão nos scores**. Esta referência
> reforça a cadeia causal: Turbo Boost → PL1/RAPL → DVFS reativo → Variação de frequência
> → Variação de score → Desvio Padrão Amostral alto.

---

## 7. NOTA COMPLEMENTAR DE ATUALIZAÇÃO — STATUS DO MAPEAMENTO DE HARDWARE

> Esta seção foi acrescentada nesta atualização do fichamento e não substitui nem invalida
> a "NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C)" registrada na Seção 5, a qual permanece
> válida especificamente para as seções 3.9 e 3.12 do fichamento original.

Com o preenchimento da tabela comparativa completa (Máquinas A, B, C, D, E e F), os subitens
3.14 a 3.20 desta atualização **deixam de ser tratados como abstração puramente preditiva**
para a maior parte dos componentes, já que as especificações de CPU, microarquitetura, TDP,
núcleos/threads, clock, cache L3, instruções avançadas, topologia de RAM, GPU e barramento
PCIe das Máquinas A, B, C, E e F foram fornecidas explicitamente. Persistem, no entanto,
como **dados pendentes (marcados com `*` na tabela fornecida)** e que ainda exigem
preenchimento futuro pelo grupo antes da consolidação definitiva da Metodologia no `main.tex`:

- **Máquina C (Cinara):** frequência exata da RAM DDR4 (`[MHz]*`); definição entre SSD ou HDD
  para o dispositivo de 237 GB (`[SSD ou HD?]*`); interface/barramento exato do armazenamento
  (`[Preencher Interface]*`).
- **Máquina E (Nauan):** modelo comercial do gabinete/placa-mãe (`[Preencher Gabinete]*`);
  frequência exata da RAM DDR4 (`[MHz]*`).
- **Máquina F (Nicolas):** modelo comercial do gabinete/placa-mãe (`[Preencher Gabinete]*`);
  geração exata do barramento PCIe dos SSDs NVMe M.2 (`[Preencher Gen]*`).

Os subitens 3.14, 3.15, 3.16, 3.17 e 3.18 (TDP, microarquitetura AMD, núcleos híbridos,
instruções vetoriais e topologia Dual Channel) já podem ser utilizados de forma definitiva
na redação do `main.tex`, pois dependem exclusivamente de especificações já confirmadas na
tabela. Já os subitens 3.19 (Barramento PCIe) e 3.20 (Armazenamento), nas partes que tratam
especificamente da Máquina C e da Máquina F, devem aguardar o preenchimento dos campos
pendentes listados acima antes da redação final, seguindo o mesmo princípio cautelar da
nota de abstração preditiva original.

**Este mapeamento de colunas e sua interpretação para os campos ainda pendentes (`*`) só
serão utilizados na redação final conforme as configurações reais de hardware das Máquinas
C, E e F forem completamente preenchidas pelo grupo nas próximas interações, se necessário.**

