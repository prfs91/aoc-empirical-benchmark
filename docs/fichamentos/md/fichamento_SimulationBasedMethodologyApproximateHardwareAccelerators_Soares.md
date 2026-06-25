# Fichamento Científico Completo
## `fichamento_SimulationBasedMethodologyApproximateHardwareAccelerators_Soares.md`

---

> ### ⚠️ VEREDITO DE RELEVÂNCIA — LEITURA OBRIGATÓRIA ANTES DE USAR ESTE FICHAMENTO
>
> **O artigo será útil para o nosso projeto de AOC? SIM, de forma indireta/conceitual — com ressalvas de escopo.**
>
> Trata-se de uma **Tese de Doutorado em Microeletrônica (UFRGS/PGMICRO, 2018)**, de autoria
> de Leonardo Bandeira Soares, sobre **Computação Aproximada** aplicada ao projeto de
> **aceleradores de hardware ASIC** (somadores aproximados, filtros FIR, detector de bordas
> Canny, estimativa de movimento HEVC). O escopo primário do documento — projeto de circuitos
> VLSI/CMOS em nível de transístor e RTL, síntese lógica em bibliotecas de células-padrão (45 nm
> e 65 nm), simulação pós-síntese e estimação de potência via *netlist* — **não coincide
> diretamente** com o nosso experimento empírico de *benchmarking* de sistemas computacionais
> comerciais (Geekbench 6 + HWiNFO64 em notebooks/desktops com Windows 11).
>
> Entretanto, o documento possui **forte aderência conceitual indireta** com pilares centrais
> da disciplina de Arquitetura e Organização de Computadores que estruturam nosso artigo:
> 1. A discussão sobre **TDP (Thermal Design Power)**, a era do **Dark Silicon** e a necessidade
>    de desligar blocos funcionais do chip para respeitar limites térmicos — conceito que
>    fundamenta diretamente nossa análise da coluna `IA: Package-Level RAPL/PBM PL1 (Yes/No)`
>    e do `Limite de desempenho - Térmico (Yes/No)`.
> 2. A relação quadrática entre **tensão de alimentação e potência dinâmica dissipada**
>    (fundamento teórico clássico de CMOS), que sustenta a discussão de `DVFS` e da coluna
>    `Core VIDs (avg) (V)` correlacionada às colunas de potência.
> 3. A definição formal de **eficiência energética** como operações por unidade de energia —
>    base teórica direta para a nossa métrica de Desempenho por Watt (Score Geekbench / `Potência
>    total da CPU (W)`).
> 4. A discussão sobre arquiteturas **multi-core e many-core** como resposta ao fim do
>    *Dennard Scaling* — fundamenta a comparação entre os 4 núcleos físicos / 8 threads lógicos
>    presentes nas máquinas do nosso experimento.
> 5. O uso rigoroso de **métricas objetivas de desempenho** (frequência máxima via método de
>    bisseção, taxa de quadros suportada, métricas de qualidade) e de **análise estatística
>    multi-configuração** como modelo metodológico de rigor experimental, embora aplicado a um
>    domínio distinto (simulação de circuitos, não execução real de software).
> 6. *(Acrescentado após análise da Tabela Comparativa de Hardware das Máquinas A a F)* A
>    discussão sobre **densidade de potência por nó tecnológico CMOS (W/mm²)** e a transição de
>    transistores planares para **FinFET**, que fundamenta teoricamente a comparação entre as
>    diferentes litografias presentes no nosso conjunto de máquinas (Intel 7, 7 nm, 12 nm, 14 nm).
>
> **Recomendação de uso:** este fichamento deve ser citado prioritariamente na
> **Fundamentação Teórica/Introdução**, nas subseções sobre TDP, Dark Silicon, DVFS, eficiência
> energética e litografia/nó tecnológico. **Não deve ser citado na Metodologia ou Resultados**
> como referência de *benchmarking* de sistemas comerciais, pois o domínio experimental do autor
> (síntese de circuitos ASIC) é incompatível com o nosso protocolo de coleta (execução de
> software real em hardware comercial). Os conceitos sobre somadores aproximados, filtros FIR e
> Canny edge detection são de baixíssima aplicabilidade direta ao nosso escopo e foram fichados
> apenas de
> forma sumária, sem aprofundamento, conforme item 3.5 abaixo.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  SOARES, Leonardo Bandeira. **A Simulation-Based Methodology focused on Energy-efficient
  Approximate Hardware Accelerators Design**. 2018. 128 f. Tese (Doutorado em Microeletrônica)
  — Programa de Pós-Graduação em Microeletrônica, Instituto de Informática, Universidade
  Federal do Rio Grande do Sul, Porto Alegre, 2018. Orientador: Sergio Bampi; Coorientador:
  Eduardo Antonio César da Costa.

- **Código BibTeX Completo (.bib):**

```bibtex
@PhdThesis{soares:18,
  author       = {Leonardo Bandeira Soares},
  title        = {A Simulation-Based Methodology focused on Energy-efficient
                   Approximate Hardware Accelerators Design},
  school       = {Instituto de Inform{\'a}tica, Universidade Federal do Rio
                   Grande do Sul ({UFRGS})},
  year         = {2018},
  address      = {Porto Alegre},
  type         = {Tese (Doutorado em Microeletr{\^o}nica)},
  note         = {Orientador: Sergio Bampi. Coorientador: Eduardo Antonio
                   C{\'e}sar da Costa. Programa de P{\'o}s-Gradua{\c{c}}{\~a}o
                   em Microeletr{\^o}nica ({PGMICRO}). 128f.}
}
```

> O ano (2018), a instituição (UFRGS), o programa (PGMICRO) e os orientadores (Sergio Bampi e
> Eduardo Antonio César da Costa) constam explicitamente na folha de rosto e na ficha
> catalográfica do documento, dispensando verificação externa adicional.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

| Campo | Conteúdo |
|---|---|
| **Grau/Tipo** | Tese de Doutorado em Microeletrônica |
| **Instituição/Editora** | Universidade Federal do Rio Grande do Sul (UFRGS) — Instituto de Informática — Programa de Pós-Graduação em Microeletrônica (PGMICRO) |
| **Ano** | 2018 (defesa em Porto Alegre, BR–RS) |
| **Orientador / Coorientador** | Prof. Dr. Sergio Bampi / Prof. Dr. Eduardo Antonio César da Costa |
| **Palavras-Chave Originais** | Computação Aproximada; Eficiência energética; Concepção de circuitos CMOS *(Approximate Computing; Energy efficiency; CMOS circuit design)* |
| **Resumo do Escopo Geral** | A tese propõe um fluxo de projeto baseado em simulações para explorar a integração entre somadores aproximados do estado da arte e arquiteturas de aceleradores de hardware ASIC, com o objetivo de melhorar a eficiência energética em aplicações tolerantes a erros (computação aproximada). São avaliados três estudos de caso — filtros FIR para processamento de áudio, detecção de bordas Canny para visão computacional, e estimativa de movimento para codificação de vídeo HEVC — com resultados de redução de consumo energético de até 57,4% (design-time) e até 64% de redução de potência dinâmica em arquiteturas configuráveis em tempo de execução (run-time). |

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

### 3.1 — TDP (Thermal Design Power) e a Era do Dark Silicon

- **Conceito/Teoria:** Limite de Potência Térmica de Projeto (TDP) e a necessidade de desligar
  porções do chip ("Dark Silicon") para respeitar a capacidade de dissipação térmica do sistema
  de arrefecimento.

- **Citação Direta (Ipsis Litteris):**
  > "The heat may be controlled through the use of a TDP (Thermal Design Power) constraint
  > which limits the maximum number of transistors simultaneously powered on and working at
  > full performance (SHAFIQUE et al., 2014). When the TDP is violated, the cooling system of a
  > given chip cannot handle the heat dissipation." (Página 18).

- **Paráfrase (Citação Indireta Acadêmica):** Conforme Soares (2018), o TDP estabelece um
  limite de projeto que restringe a quantidade de transistores que podem operar simultaneamente
  em desempenho máximo, de modo que, quando esse limite é ultrapassado, o sistema de
  arrefecimento torna-se incapaz de dissipar o calor gerado, fenômeno descrito na literatura
  como "Dark Silicon" — a necessidade de manter parcelas crescentes do chip desligadas ou
  subutilizadas a cada novo nó tecnológico (Página 18).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica / Introdução — subseção sobre
  Termodinâmica e Arquitetura, imediatamente antes da definição de Thermal Throttling.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação fundamenta teoricamente a leitura
  da coluna `IA: Package-Level RAPL/PBM PL1 (Yes/No)` (que indica se o processador está sendo
  contido pelo limite de potência de longo prazo definido pelo TDP do fabricante) e da coluna
  `Limite de potência PL1 (Static) (W)` / `Limite de potência PL1 (Dynamic) (W)` presentes nos 80
  arquivos `maq*_rodada_*.CSV`. Quando essas colunas reportam "Yes" ou valores de potência
  reduzidos dinamicamente, isso evidencia empiricamente, em hardware comercial, o mesmo
  mecanismo de contenção térmica/energética discutido teoricamente pelo autor para chips ASIC.

---

### 3.2 — Fim do Dennard Scaling e Ascensão das Arquiteturas Multi-core/Many-core

- **Conceito/Teoria:** Transição de processadores de núcleo único para arquiteturas
  multi-core e many-core como resposta ao esgotamento da Lei de Dennard e ao "muro de potência"
  (*power wall*).

- **Citação Direta (Ipsis Litteris):**
  > "The previously mentioned power wall in deep sub-micron technologies made many CPU
  > (Central Processing Unit) manufacturers started to design multi- and many-cores CPUs. The
  > multi- and many-cores manufacturing trend was the solution to accomplish the growing
  > workload requirements and to overcome the limitation imposed by the end of Dennard
  > Scaling." (Página 17–18).

- **Paráfrase (Citação Indireta Acadêmica):** Segundo Soares (2018), o esgotamento da Lei de
  Dennard e o consequente "muro de potência" levaram os fabricantes de processadores a adotar o
  paradigma de múltiplos núcleos (multi-core e many-core) como estratégia para sustentar o
  crescimento da demanda computacional sem extrapolar os limites de dissipação de potência
  impostos pela escala de integração dos transistores (Página 17–18).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Paralelismo a
  Nível de Instrução e Thread (Multicore vs. Threads Lógicos).

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a discussão sobre a arquitetura
  4 Cores / 8 Threads (SMT — *Simultaneous Multithreading*) presente, por exemplo, na Máquina D
  (Roberta). É diretamente correlacionável com as colunas `Core 0 T0 Uso (%)` até
  `Core 3 T1 Uso (%)` dos arquivos `.CSV`, que registram a utilização individual de cada thread
  lógico (T0/T1) por núcleo físico (Core 0 a Core 3), bem como com a coluna `Multi_Core` dos
  arquivos `scores_maq*.txt`, cujo ganho relativo sobre o `Single_Core` evidencia
  empiricamente o benefício do paralelismo multi-core/many-core descrito teoricamente pelo
  autor.

---

### 3.3 — Definição Formal de Eficiência Energética

- **Conceito/Teoria:** Definição quantitativa de eficiência energética como razão entre
  operações computacionais e energia consumida (ou seu inverso).

- **Citação Direta (Ipsis Litteris):**
  > "Energy efficiency is defined in (MARKOVIC et al., 2004) as being the maximum number of
  > operations (i.e., instruction fetching/decoding, arithmetic) per energy budget or the
  > minimum consumed energy per operation." (Página 19).

- **Paráfrase (Citação Indireta Acadêmica):** Conforme apontado por Soares (2018), com base na
  definição de Markovic et al. (2004), a eficiência energética em sistemas digitais é
  formalmente caracterizada pelo número máximo de operações computacionais (busca/decodificação
  de instruções, operações aritméticas) realizadas dentro de um orçamento energético fixo, ou,
  de forma equivalente, pela quantidade mínima de energia consumida por operação executada
  (Página 19).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Eficiência
  Microarquitetural (Desempenho por Watt).

- **Mapeamento de Colunas e Arquivos de Teste:** Esta é a citação-chave que **fundamenta
  formalmente** a métrica de "Desempenho por Watt" proposta no nosso projeto. A operacionalização
  empírica desse conceito teórico se dá através da razão entre o `Single_Core`/`Multi_Core`
  Score (arquivos `scores_maq*.txt`) e a média da coluna `Potência total da CPU (W)` (arquivos
  `maq*_rodada_*.CSV`), constituindo um proxy direto de "operações por unidade de energia"
  aplicado ao domínio do *benchmarking* sintético, análogo à definição teórica empregada pelo
  autor para circuitos ASIC.

---

### 3.4 — DVFS (Dynamic Voltage Frequency Scaling) e a Relação Quadrática Tensão-Potência

- **Conceito/Teoria:** Relação quadrática entre tensão de alimentação e potência dinâmica
  dissipada em circuitos CMOS digitais, fundamento físico do DVFS (escalonamento dinâmico de
  tensão e frequência).

- **Citação Direta (Ipsis Litteris):**
  > "Near-threshold computing and ultra-low voltage operation leverage the strong quadratic
  > relationship between the power supply voltage and the dynamic power dissipation in CMOS
  > digital circuits. Therefore, when lowering the supply voltage one can reduce the dynamic
  > power dissipation at the expense of decreased computational performance." (Página 20).

- **Paráfrase (Citação Indireta Acadêmica):** De acordo com Soares (2018), a computação em
  tensão *near-threshold* e em ultrabaixa tensão explora a forte relação quadrática existente
  entre a tensão de alimentação e a potência dinâmica dissipada em circuitos digitais CMOS, de
  modo que a redução da tensão de alimentação implica redução proporcionalmente quadrática da
  potência dinâmica, ao custo de uma redução no desempenho computacional — relação que constitui
  o fundamento físico subjacente às técnicas modernas de DVFS (Página 20).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Termodinâmica e
  Arquitetura / Consumo Energético, imediatamente antes da fórmula clássica de potência
  dinâmica $P_{din} = \alpha \cdot C \cdot V^2 \cdot f$.

  > ⚠️ **Nota de fidelidade:** o autor cita a relação quadrática de forma textual, mas **não
  > apresenta explicitamente** a fórmula $P = \alpha C V^2 f$ nesta passagem. Essa equação é
  > consolidada na literatura clássica de Arquitetura de Computadores (ex.: Hennessy e Patterson)
  > e pode ser citada separadamente, sem atribuição a Soares (2018), para não incorrer em
  > invenção de fórmula não presente no documento original.

- **Mapeamento de Colunas e Arquivos de Teste:** Correlaciona-se com as colunas
  `Core VIDs (avg) (V)` (tensão entregue aos núcleos) e `Relógios núcleo (avg) (MHz)`
  (frequência de operação) em conjunto com `Potência total da CPU (W)`, permitindo ao grupo
  observar empiricamente, nos 80 arquivos `.CSV`, como variações de tensão/frequência (DVFS
  operado pelo *firmware* da CPU) se refletem na potência total medida — fenômeno cujo fundamento
  físico é exatamente a relação quadrática V²f descrita pelo autor.

---

### 3.5 — Computação Aproximada, Somadores Aproximados e Aplicações Tolerantes a Erro
*(Fichamento sumário — baixíssima aplicabilidade direta ao escopo do projeto)*

- **Conceito/Teoria:** Paradigma de Computação Aproximada (*Approximate Computing*): redução
  deliberada da exatidão computacional em favor de eficiência energética, em aplicações
  tolerantes a ruído/erro (multimídia, visão computacional, processamento de sinais).

- **Citação Direta (Ipsis Litteris):**
  > "The approximate computing paradigm emerged to increase performance and to reduce power
  > dissipation (HAN; ORSHANSKY, 2013). The key approach in approximate hardware is to reduce
  > the computation accuracy in favor of energy-efficiency." (Página 21).

- **Paráfrase (Citação Indireta Acadêmica):** Soares (2018) descreve a computação aproximada
  como um paradigma que sacrifica deliberadamente parte da exatidão dos resultados
  computacionais em troca de ganhos de desempenho e eficiência energética, sendo aplicável a
  domínios cujas saídas toleram um intervalo de respostas aceitáveis em vez de um único
  resultado exato (Página 21).

- **Onde Encaixar no Artigo LaTeX:** **Não recomendado para o núcleo do artigo.** Caso o grupo
  opte por uma menção breve na Introdução/Trabalhos Relacionados, deve ser tratado como
  contraste — diferenciando explicitamente o nosso experimento (medição empírica de hardware
  comercial executando *software* real, sem qualquer alteração de exatidão computacional) do
  experimento do autor (projeto e síntese de circuitos digitais aproximados em nível de
  transístor/RTL).

- **Mapeamento de Colunas e Arquivos de Teste:** **Nenhum mapeamento direto aplicável.** O
  nosso conjunto de dados (Geekbench 6 + HWiNFO64) não envolve qualquer técnica de aproximação
  de hardware; os processadores das Máquinas A, B, C e D operam de forma precisa (não
  aproximada) durante toda a coleta. Citado aqui apenas por completude do fichamento, sem
  função estatística no artigo.

---

### 3.6 — Metodologia Experimental: Múltiplas Configurações, Casos de Teste Reais e Busca por
Frequência Máxima

- **Conceito/Teoria:** Rigor metodológico via avaliação sistemática de múltiplas configurações
  experimentais sobre casos de teste reais, e determinação da frequência máxima de operação
  através do método de busca por bisseção.

- **Citação Direta (Ipsis Litteris):**
  > "To estimate the maximum frequency, many timing syntheses were performed by using the
  > bisection search method. This analysis is essential to determine the maximum throughput for
  > each design." (Página 85).

- **Paráfrase (Citação Indireta Acadêmica):** Para a determinação da frequência máxima de
  operação de cada arquitetura avaliada, Soares (2018) empregou múltiplas sínteses temporais
  conduzidas pelo método de busca por bisseção, procedimento essencial para estabelecer a
  vazão (*throughput*) máxima sustentável de cada projeto de hardware (Página 85).

- **Onde Encaixar no Artigo LaTeX:** Metodologia — subseção sobre rigor experimental e
  repetição de medições (a título de paralelo metodológico, não de técnica idêntica).

  > ⚠️ **Nota de aderência metodológica:** o método de bisseção do autor busca a *frequência
  > máxima de síntese estável de um circuito simulado*, enquanto nosso protocolo mede a
  > *frequência de clock real reportada pelo sensor de hardware* (`Relógios núcleo (avg) (MHz)`)
  > durante 20 rodadas de *benchmark* em sistema físico já fabricado. São procedimentos distintos
  > que não devem ser equiparados tecnicamente; a citação serve apenas como reforço retórico do
  > princípio geral de "múltiplas medições para caracterização robusta de desempenho".

- **Mapeamento de Colunas e Arquivos de Teste:** Reforça indiretamente a justificativa
  metodológica da repetição de 20 rodadas por máquina (arquivos `scores_maqA.txt` a
  `scores_maqD.txt`, colunas `Single_Core` e `Multi_Core`) como prática de caracterização
  estatística robusta de desempenho, análoga — em princípio geral, não em técnica — às múltiplas
  sínteses realizadas pelo autor.

---

### 3.7 — Litografia/Nó Tecnológico CMOS e Densidade de Potência (W/mm²)
*(Seção acrescentada após o recebimento da Tabela Comparativa de Hardware das Máquinas A a F)*

- **Conceito/Teoria:** Aumento da densidade de potência (W/mm²) a cada novo nó tecnológico
  CMOS, mesmo com a adoção de transistores FinFET, e o consequente esgotamento da Lei de
  Dennard como motivador da escalada de litografia (planar → FinFET) observada na evolução dos
  processadores.

- **Citação Direta (Ipsis Litteris):**
  > "Although these technologies substantially attenuate the short-channel effects of deep
  > sub-micron planar bulk, the integration capability and the previously mentioned Dark Silicon
  > projections indicate that power density also affects these technologies. The same
  > observation is also provided in (BAILEY, 2016) which shows an increase in power density
  > (i.e., W/mm²) for the 22 nm Intel's FinFET-based processor when compared to the 32 nm
  > planar-based one." (Página 19–20).

- **Paráfrase (Citação Indireta Acadêmica):** Soares (2018) destaca que, mesmo com a transição
  da tecnologia planar para transistores FinFET — que atenuam substancialmente os efeitos de
  canal curto característicos dos nós CMOS planares ultra-submicrométricos —, a densidade de
  potência por área de silício (W/mm²) continua a crescer a cada novo nó tecnológico, conforme
  evidenciado pela comparação entre o processador FinFET de 22 nm da Intel e seu antecessor
  planar de 32 nm (Página 19–20). Esse mesmo corpo teórico é complementado, na Introdução do
  documento, pela constatação de que a redução do comprimento de canal do transistor escala-se
  em ritmo mais acelerado do que a tensão nominal de alimentação, rompendo a premissa da Lei de
  Dennard e impondo o aumento de potência por área a cada nova geração litográfica (Página 17).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Microarquitetura e
  Litografia (item 3 das Diretrizes Gerais do projeto: "RAM DDR4 1333 MHz vs clocks maiores",
  estendida aqui para a comparação de nós litográficos da CPU), imediatamente antes ou depois da
  citação de TDP/Dark Silicon (item 3.1 deste fichamento), já que ambas as discussões do autor
  são contíguas e mutuamente reforçadas no texto original.

- **Justificativa de Uso e Correlação com a Tabela de Hardware (Máquinas A–F):** Esta é a
  citação mais diretamente aplicável à coluna **"Microarquitetura / Litografia"** da tabela
  fornecida pelo grupo, pois fundamenta teoricamente a comparação entre nós tecnológicos
  distintos presentes no nosso próprio conjunto de máquinas:
    - **Zen 3 / 7 nm** (Máquina E, Nauan) e **Zen+ / 12 nm** (Máquina C, Cinara) — arquiteturas
      AMD em diferentes gerações de litografia, processadas por foundries externas (TSMC),
      análogas em escala aos nós "deep sub-micron" discutidos pelo autor;
    - **Raptor Lake-H / Intel 7** (Máquina A, Raony), **Raptor Lake-P / Intel 7** (Máquina B,
      Leandro) e **Raptor Lake / Intel 7** (Máquina F, Nicolas) — nó "Intel 7" (equivalente
      *class* a ~10 nm, com transistores FinFET), versus **Whiskey Lake-U / 14 nm** (Máquina D,
      Roberta), que utiliza transistores FinFET de geração anterior, mais distante do limite de
      escala atual.
    - **Recomendação de uso:** o grupo pode citar Soares (2018) para justificar teoricamente
      *por que* se espera maior densidade de potência (e, por extensão, maior necessidade de
      controle térmico/TDP) nos processadores de nó mais avançado (Intel 7, 7 nm) quando
      comparados ao nó de 14 nm da Máquina D — mesmo que a Máquina D possua TDP base nominal
      mais baixo (15 W) por se tratar de um processador de baixo consumo (segmento U/*Ultra-low
      power*), e não por ser eletricamente "menos denso". É importante que o grupo não confunda
      o TDP nominal informado pelo fabricante (que reflete o segmento de mercado do produto) com
      a densidade de potência por área de silício (W/mm²) discutida pelo autor, que é uma
      propriedade física do nó litográfico e não do *binning* comercial do produto.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação **não possui mapeamento direto**
  com nenhuma coluna numérica dos arquivos `.CSV` do HWiNFO64, pois a densidade de potência por
  área de silício (W/mm²) não é uma grandeza monitorada por sensores de software (ela depende da
  área física do *die*, informação não exposta pelo HWiNFO64). Seu uso deve ser exclusivamente
  **teórico/comparativo na Fundamentação Teórica**, como pano de fundo explicativo para a
  diferença de comportamento térmico-energético observado entre litografias distintas. A
  validação empírica indireta desse fenômeno pode ser feita correlacionando a coluna
  `Potência total da CPU (W)` (potência absoluta medida) com o TDP nominal de cada máquina
  (informação da Tabela de Hardware, não do CSV), permitindo inferir — ainda que de forma
  aproximada — o quão próximo cada processador opera do seu limite de projeto durante as 20
  rodadas de benchmark.

---

### 3.8 — Comparação Energética entre Plataformas de Aceleração (ASIC vs. GPU vs. FPGA)
*(Citação de menor relevância, fichada por completude após verificação da coluna "GPU Dedicada")*

- **Conceito/Teoria:** Comparação de eficiência energética entre diferentes plataformas de
  processamento (ASIC dedicado, FPGA e GPU de uso geral) para a mesma carga de trabalho
  (detecção de bordas Canny), citada pelo autor a partir de trabalho de terceiros.

- **Citação Direta (Ipsis Litteris):**
  > "The work in (POSSA et al., 2014) presents a comparison between two different
  > implementations to accelerate the edge detection application: the use of Graphic Processing
  > Units (GPUs), and the FPGA architecture. [...] They concluded that the FPGA solution
  > provides a more energy-efficient design than the GPU implementation, but no comparison is
  > given to ASICs." (Página 71).

- **Paráfrase (Citação Indireta Acadêmica):** Soares (2018) reporta o resultado de Possa et al.
  (2014), segundo o qual, na tarefa de detecção de bordas Canny, uma implementação em FPGA
  apresentou eficiência energética superior à de uma implementação equivalente em GPU de
  propósito geral, embora os autores originais não tenham estendido essa comparação a soluções
  ASIC (Página 71). O próprio Soares (2018) complementa, a partir de Kuon e Rose (2007), que
  soluções ASIC tendem a ser ainda mais eficientes energeticamente que FPGAs em termos de área e
  potência dissipada (Página 71).

- **Onde Encaixar no Artigo LaTeX:** **Uso facultativo e de baixa prioridade** — apenas se o
  grupo desejar uma frase de contextualização na Introdução ou Trabalhos Relacionados sobre a
  hierarquia geral de eficiência energética entre classes de hardware (ASIC > FPGA > GPU de
  propósito geral > CPU de propósito geral), antes de justificar por que o nosso experimento se
  concentra em CPUs e GPUs comerciais de uso geral.

- **Justificativa de Uso e Correlação com a Tabela de Hardware (Máquinas A–F):** Esta citação
  **não deve ser usada para comparar tecnicamente** as GPUs dedicadas das nossas máquinas
  (NVIDIA GeForce RTX 4050 Laptop, MX130, RX 7600, RTX 3050) entre si, pois o trabalho citado por
  Soares (2018) trata de uma comparação ASIC/FPGA/GPU para uma tarefa específica de visão
  computacional embarcada (Canny edge detection em hardware dedicado), e não de desempenho de
  GPUs comerciais executando cargas de trabalho gráficas/Geekbench como as do nosso experimento.
  Citar esta passagem fora desse contexto incorreria em generalização indevida. Seu único uso
  legítimo é como **pano de fundo conceitual amplo** (hierarquia de eficiência energética entre
  classes de arquitetura de hardware), nunca como evidência comparativa entre as GPUs reais do
  nosso conjunto de máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:** **Nenhum mapeamento direto aplicável.** Não há
  correlação válida com as colunas `Carga do núcleo da GPU (%)`, `GPU Clock (MHz)` ou
  `Potência das linhas GPU (avg) (W)` dos arquivos `.CSV`, pois estas medem o comportamento de
  GPUs comerciais de uso geral (NVIDIA/AMD) durante execução de *benchmark* sintético, contexto
  tecnicamente distinto do estudo de caso ASIC/FPGA/GPU mencionado pelo autor.

---

> ### 🔎 VERIFICAÇÃO QUANTO AOS DEMAIS COMPONENTES DA TABELA COMPARATIVA (MÁQUINAS A–F)
>
> Após releitura integral do documento à luz da Tabela Comparativa de Hardware fornecida pelo
> grupo, **confirma-se que não há, no texto de Soares (2018), nenhuma menção, discussão ou dado
> quantitativo** sobre os seguintes componentes presentes na tabela, não sendo gerada, portanto,
> nenhuma citação para eles, em respeito à diretriz de **não invenção de dados**:
> - Memória RAM (capacidade, tipo DDR4/DDR5, frequência em MT/s ou MHz, topologia Single/Dual
>   Channel) — o documento não aborda hierarquia de memória principal (DRAM) em nenhum momento;
>   a única ocorrência da sigla correlata é "SRAM" (Static RAM), em contexto de memória *on-chip*
>   de FPGA, sem relação com os módulos DDR4/DDR5 das nossas máquinas.
> - Cache L3 (capacidade em MB) dos processadores — não há discussão sobre hierarquia de cache
>   de CPUs comerciais.
> - Armazenamento (SSD NVMe, HDD SATA, interface PCIe Gen 3.0/4.0) — não há qualquer menção a
>   dispositivos de armazenamento persistente, taxas de leitura/escrita ou interfaces de
>   barramento de disco.
> - Instruções avançadas de CPU (AVX, AVX2, FMA3, BMI2, Intel DL Boost/VNNI) — não há menção a
>   nenhum conjunto de instruções vetoriais ou extensões de CPU comerciais.
> - Arquiteturas híbridas de núcleos (P-cores/E-cores, como nas Máquinas A, B e F) — o documento
>   discute heterogeneidade arquitetural apenas no sentido de aceleradores ASIC dedicados
>   integrados a processadores de propósito geral (item 3.2 deste fichamento), e não no sentido
>   de núcleos heterogêneos dentro do próprio processador (*big.LITTLE*-style), tecnologia
>   posterior à publicação da tese (2018).
> - GPU integrada/dedicada como unidade de processamento gráfico comercial — a única menção a
>   GPU é a citação de terceiros tratada no item 3.8 acima, em contexto de ASIC/FPGA, não de
>   GPUs comerciais.
>
> **Estes componentes deverão ser fundamentados, na Fundamentação Teórica do `main.tex`, com
> referências bibliográficas distintas**, a serem buscadas conforme as strings sugeridas na
> Seção 5 (já existentes) e nas novas strings acrescentadas na Seção 5 abaixo.

---

> ### 🔮 NOTA SOBRE HARDWARE FUTURO (MÁQUINAS A, B e C)
>
> Os conceitos fichados nas seções 3.1 a 3.4 (TDP/Dark Silicon, multi-core/many-core, eficiência
> energética e DVFS) são **genéricos e aplicáveis a qualquer configuração de hardware x86**,
> independentemente das especificações finais das Máquinas A, B e C. Não há, neste artigo,
> menção específica a parâmetros como Dual Channel de memória, cache L3 de tamanhos distintos ou
> litografias específicas que exigissem a aplicação da diretriz de abstração preditiva de
> hardware futuro. **Este aviso é, portanto, apenas informativo: não há trecho condicionado a
> dados ainda não preenchidos pelo grupo.**
>
> **Atualização pós-recebimento da Tabela Comparativa de Hardware (Máquinas A a F):** com a
> tabela completa em mãos, confirma-se que as Máquinas A, B, C, E e F (Raony, Leandro, Cinara,
> Nauan e Nicolas) já possuem especificações de litografia plenamente definidas (Intel 7, Zen+
> 12 nm, Zen 3 7 nm), o que tornou possível redigir a nova Seção 3.7 com correlação direta e não
> mais preditiva. Os campos ainda pendentes de preenchimento na tabela fornecida (`[Preencher
> Gabinete]*` para as Máquinas E e F, `[MHz]*` para a RAM da Máquina E, e `[Preencher Gen]*` para
> a interface de disco da Máquina F) não impactam nenhuma das citações deste fichamento, pois
> nenhuma delas depende de modelo de gabinete, frequência de RAM ou geração de PCIe do
> armazenamento.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES (Se houver no texto original)

- **Fórmulas Matemáticas/Físicas em LaTeX Puro:**

  Equação de estimativa de tensão escalada aproximada (Página 87), citando Gupta et al. (2013),
  relacionando atraso de circuito e tensão de alimentação:

  ```latex
  % Equação (32) - Página 87 - relação delay-tensão (citada de Gupta et al., 2013)
  \text{Delay} \propto \frac{1}{V_{DD}}
  ```

  Equação de estimativa da tensão aproximada escalada (Página 87):

  ```latex
  % Equação (33) - Página 87
  V_{DDAPP} = V_{DD} \left(1 - \frac{\text{slack}}{T_c}\right)
  ```

  > ⚠️ **Nota de fidelidade:** as Equações (32) e (33) foram transcritas a partir da descrição
  > textual do autor (o PDF não preserva os caracteres matemáticos originais na extração de
  > texto, apenas a numeração "(32)" e "(33)" entre parênteses). A estrutura lógica foi
  > reconstruída com base na descrição verbal explícita do autor: "the supply voltage is
  > inversely proportional to the delay of a given circuit" e na definição de $V_{DDAPP}$ como
  > função de $V_{DD}$, do *slack* (diferença de atraso entre versão precisa e aproximada) e do
  > período de clock $T_c$. **Recomenda-se verificar visualmente a página 87 do PDF original
  > antes de transcrever ao `main.tex`**, pois a extração textual não captura símbolos
  > matemáticos com precisão total.

  Equação de tempo de simulação exaustiva (Página 55), relevante apenas como exemplo da
  complexidade combinatória de busca (NP-completo):

  ```latex
  % Equação (13) - Página 55
  T_{sim} = t \cdot k^{n}
  ```
  onde $n$ é o número de somadores e $k$ é o intervalo do parâmetro de aproximação explorado.

- **Sugestão de Gráficos/Tabelas Correspondentes:**

  O autor utiliza, na Tabela 4.8 (Página 86), um modelo de tabela comparativa de eficiência
  energética entre múltiplas configurações (precisa vs. aproximada) com linhas para `# of cells`,
  `Area (EG)`, `Dynamic Power (mW)`, `Total Power (mW)` e `MEF` (Mean Energy per Frame) por
  resolução de vídeo. **Sugestão de adaptação para o nosso `main.tex`:** montar tabela análoga
  comparando as quatro Máquinas (A, B, C, D) com linhas para Score Single-Core (média ± desvio
  padrão), Score Multi-Core (média ± desvio padrão), Potência total da CPU média (W) e a métrica
  derivada de Desempenho por Watt (Score/W), seguindo o padrão de tabela sem linhas verticais
  grossas exigido pelo template SBC, com legenda *antes* do `\begin{tabular}` e nota de rodapé
  "Fonte: Dados da pesquisa (2026)".

  Para os gráficos de barra em Matplotlib, a Tabela 4.7 do autor (frequência máxima e taxas de
  quadro suportadas por resolução) sugere o padrão de barras agrupadas por categoria (aqui:
  por Máquina) com hastes de erro de desvio padrão amostral, em tons de cinza com hachuras
  distintas, consistente com a Diretriz 10 já adotada no fichamento de Kelleher (2011) presente
  no projeto.

---

## 5. SUGESTÕES DE BUSCA BIBLIOGRÁFICA COMPLEMENTAR (Google Acadêmico)

Para triangular e reforçar os conceitos de TDP, Dark Silicon, DVFS e eficiência energética
extraídos deste documento com referências adicionais de maior aderência direta ao escopo de
*benchmarking* de hardware comercial, sugerem-se as seguintes strings de busca:

**Em inglês:**
- "Dark Silicon" power density CMOS scaling Esmaeilzadeh
- "Thermal Design Power" TDP CPU throttling mechanism
- "Dynamic Voltage Frequency Scaling" DVFS energy efficiency survey
- "Dennard scaling" end multicore power wall
- "performance per watt" CPU benchmarking energy efficiency metric

**Em português:**
- "limite de potência térmica" TDP processadores
- "escalonamento dinâmico de tensão e frequência" DVFS arquitetura
- "fim da lei de Dennard" multinúcleo desempenho energético
- "eficiência energética" desempenho por watt avaliação de hardware
- "estrangulamento térmico" CPU desempenho variabilidade

> ### ➕ NOVAS STRINGS (acrescentadas após análise da Tabela Comparativa de Hardware A–F)
>
> As buscas abaixo visam **suprir as lacunas bibliográficas identificadas** na seção
> "Verificação quanto aos demais componentes da Tabela Comparativa" (Seção 3), já que o
> documento de Soares (2018) não aborda memória RAM, cache, armazenamento, instruções
> vetoriais ou núcleos híbridos P-core/E-core.
>
> **Em inglês:**
> - "Intel 7" process node FinFET power density comparison
> - "dual channel" vs "single channel" memory bandwidth latency benchmark
> - "L3 cache size" impact CPU performance benchmark
> - "NVMe SSD" vs "SATA HDD" latency throughput benchmark comparison
> - "hybrid core architecture" P-core E-core scheduling performance
> - "AVX2" "AVX-512" "VNNI" instruction set performance impact benchmark
> - "Zen 3" vs "Zen+" microarchitecture IPC comparison AMD
>
> **Em português:**
> - "memória dual channel" vs "single channel" desempenho largura de banda
> - "cache L3" desempenho processador benchmark comparação
> - "SSD NVMe" "HD SATA" desempenho latência taxa de transferência
> - "núcleos heterogêneos" arquitetura híbrida desempenho energético processador
> - "conjunto de instruções vetoriais" AVX desempenho processamento
> - "nó de fabricação" 7nm 14nm comparação densidade de transistores

---

## 6. SÍNTESE DE RECOMENDAÇÕES PARA O GRUPO

1. **Uso recomendado:** citar Soares (2018) **apenas** nas subseções teóricas de TDP/Dark
   Silicon, multi-core/many-core, definição formal de eficiência energética e litografia/nó
   tecnológico (itens 3.1, 3.2, 3.3 e 3.7), com no máximo 3 a 4 citações ao longo do artigo.

2. **Uso não recomendado:** não utilizar este fichamento como base para a Metodologia ou para
   discussão de Resultados, pois o domínio experimental do autor (síntese de circuitos ASIC
   simulados) é estruturalmente distinto do nosso protocolo de medição empírica de hardware
   comercial em execução real. O item 3.8 (comparação ASIC/FPGA/GPU) é de uso facultativo e
   estritamente conceitual, não devendo ser usado como evidência comparativa entre as GPUs
   comerciais das Máquinas A a F.

3. **Substituição/complemento possível:** para a seção de Resultados e Discussão sobre
   Desempenho por Watt e DVFS, priorizar referências de literatura clássica de Arquitetura de
   Computadores (ex.: Hennessy e Patterson, *Computer Architecture: A Quantitative Approach*) ou
   artigos de caracterização empírica de TDP/DVFS em CPUs comerciais, de aderência mais direta.
   Para memória RAM (Dual/Single Channel, DDR4/DDR5), cache L3, armazenamento (NVMe/SATA),
   instruções vetoriais (AVX/VNNI) e núcleos híbridos P-core/E-core — componentes da Tabela
   Comparativa de Hardware **não cobertos por este documento** (ver Seção 3, bloco de
   verificação) —, buscar referências distintas a partir das novas strings acrescentadas na
   Seção 5.

4. **Próxima ação recomendada:** nenhuma pendência de dados de hardware impede o uso das
   citações já fichadas (ver Nota sobre Hardware Futuro, Seção 3, já atualizada com a Tabela
   Comparativa completa das Máquinas A a F). Restam apenas os campos pontuais marcados com
   `*` na tabela fornecida pelo grupo (modelo de gabinete das Máquinas E e F, frequência da RAM
   da Máquina E, e geração de PCIe do armazenamento da Máquina F), que não impactam nenhuma
   citação deste fichamento e podem ser preenchidos posteriormente sem necessidade de
   reprocessamento deste documento.

---

*Fichamento gerado em: Junho de 2026*
*Gerado com base nas Diretrizes de Fichamento do Projeto — arquivo `diretrizes_fichamento_sbc`*
*Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí*
*Professor Orientador: Prof. Dr. Iago Medeiros*
