# Fichamento Científico Completo
## `fichamento_LifecycleCarbonFootprintDRAM_PIM_Patel.md`

---

> ### ⚠️ AVISO DE RELEVÂNCIA — LEITURA OBRIGATÓRIA ANTES DE USAR ESTE FICHAMENTO
>
> **Veredito: O artigo será útil para o nosso projeto de AOC? SIM, de forma PARCIAL e COMPLEMENTAR.**
>
> **Justificativa:** O foco central desta dissertação de mestrado é a *pegada de carbono e
> sustentabilidade ambiental* de arquiteturas Processing-in-Memory (PIM) baseadas em DRAM,
> comparadas a GPUs — um tema de **Ciclo de Vida Ambiental (LCA)**, fora do escopo direto do
> nosso experimento de benchmarking (Geekbench 6 + HWiNFO64 em 4 máquinas Windows 11).
> Não há, portanto, dados quantitativos de Single-Core/Multi-Core Score, nem séries de
> telemetria comparáveis às nossas colunas de CSV.
>
> Contudo, o documento contém **fundamentação teórica de Arquitetura de Computadores
> genuína e diretamente aproveitável** para a nossa Fundamentação Teórica e Discussão,
> a saber: (i) o **gargalo de Von Neumann / memory wall**; (ii) a **hierarquia de memória**
> (registradores → cache → DRAM → armazenamento); (iii) **arquitetura e temporização da
> DRAM** (tRCD, tCAS, tRP, ativação/precarga); (iv) **memória Single-Channel vs.
> Dual-Channel** e gerações DDR3/DDR4/DDR5; (v) **potência estática vs. dinâmica** e seu
> equacionamento; (vi) o **efeito da temperatura/aging sobre a latência** (análogo
> conceitual ao *thermal throttling* que estudamos); e (vii) **métricas de eficiência
> energética** (desempenho/Watt, FPS/W/mm²), que dialogam diretamente com a métrica de
> Desempenho por Watt que pretendemos calcular (Score do Geekbench ÷ Potência total da
> CPU em W).
>
> **Recomendação de uso:** citar este trabalho de forma **pontual** na Fundamentação
> Teórica (hierarquia de memória, gargalo de Von Neumann, parâmetros de temporização da
> DRAM, Single vs. Dual Channel) e, eventualmente, na Discussão (analogia entre o
> *aging-induced latency increase* da DRAM e o *thermal throttling* observado em nossas
> CPUs). **Não utilizar** as discussões de pegada de carbono, *break-even analysis* de
> PIM vs. GPU, ou os modelos de emissão embutida (ECF/OPCF) — são tangenciais ao nosso
> escopo de desempenho/temperatura/energia experimental.
>
> **Atualização (Tabela de Hardware Completa — Máquinas A a F):** com a confirmação das
> especificações reais de todas as seis máquinas do grupo (Seção 0 abaixo), a Diretriz de
> Abstração de Hardware Futuro deixa de ser hipotética para a maioria dos parâmetros: agora
> há **Dual-Channel DDR5** (Máquina A), **Dual-Channel DDR4** em múltiplas frequências
> (Máquinas B, E, F), **Single-Channel DDR4** (Máquinas C e D), **SSD NVMe** em quatro das
> seis máquinas (A, B, C, F) contra **HDD SATA** (Máquina D) e **SSD SATA + HDD** (Máquina
> E), e Cache L3 variando de 4 MB (Máquina C) a 24 MB (Máquina F). Isso torna **diretamente
> aplicável e não mais apenas preditivo** o conteúdo das Seções 3.4 (Single vs. Dual
> Channel) e 3.5 (gerações DDR) deste fichamento, e justifica a criação das novas Seções
> 3.10 a 3.13 abaixo, que tratam de DDR5, velocidade de armazenamento (SSD NVMe vs. HDD
> SATA), Cache L3 de maior porte e arquiteturas híbridas P-core/E-core.

---

## 0. TABELA DE HARDWARE CONSOLIDADA DO GRUPO (MÁQUINAS A–F)

> Esta seção registra, para referência cruzada de todas as citações deste fichamento, a
> especificação completa de hardware confirmada pelo grupo, substituindo o cenário anterior
> em que apenas a Máquina D estava consolidada. As Máquinas A, B, C, E e F passam a ter uso
> **pleno** (não mais preditivo) nas citações que dependem de configuração de RAM,
> armazenamento, cache L3 e topologia de núcleos.

| Componente / Parâmetro | Máquina A (Raony) | Máquina B (Leandro) | Máquina C (Cinara) | Máquina D (Roberta) | Máquina E (Nauan) | Máquina F (Nicolas) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tipo de Sistema** | Notebook Gamer | Notebook Ultrafino | Notebook Ultrafino | Notebook Ultrafino | Desktop Montado | Desktop Montado |
| **Modelo Comercial** | Acer Nitro ANV15-51 | Dell Inspiron 15 3530 | ASUS VivoBook X515DA | Dell Inspiron 15 5584 | [Preencher Gabinete]* | [Preencher Gabinete]* |
| **Processador (CPU)** | Intel Core i5-13420H | Intel Core i5-1334U | AMD Ryzen 5 3500U | Intel Core i5-8265U | AMD Ryzen 5 5500 | Intel Core i5-14600KF |
| **Microarquitetura / Litografia** | Raptor Lake-H / Intel 7 | Raptor Lake-P / Intel 7 | Zen+ / 12 nm | Whiskey Lake-U / 14 nm | Zen 3 / 7 nm | Raptor Lake / Intel 7 |
| **Núcleos / Threads** | 8 (4P+4E) / 12T | 10 (2P+8E) / 12T | 4 Cores / 8T | 4 Cores / 8T | 6 Cores / 12T | 14 (6P+8E) / 20T |
| **Clock (Base / Boost)** | 2.10 / 4.60 GHz | 1.30 / 4.60 GHz | 2.10 / 3.70 GHz | 1.60 / 3.90 GHz | 3.60 / 4.20 GHz | P: 3.5/5.3 GHz; E: 2.6/4.0 GHz |
| **TDP Base da CPU** | 45 W | 15 W | 15 W | 15 W | 65 W | 125 W |
| **Cache L3 Total** | 12 MB | 12 MB | 4 MB | 6 MB | 16 MB | 24 MB |
| **Instruções Avançadas** | AVX, AVX2, VNNI, BMI2 | AVX, AVX2, VNNI, BMI2 | AVX, AVX2, FMA3, BMI2 | AVX, AVX2, FMA3, BMI2 | AVX, AVX2, FMA3 | AVX, AVX2, VNNI, BMI2 |
| **RAM (Capacidade/Tipo)** | 8 GB DDR5 5200 MT/s | 16 GB DDR4 2666 MHz | 8 GB DDR4 2400 MHz | 8 GB DDR4 2400 MHz | 16 GB DDR4 [MHz]* | 32 GB DDR4 3600 MHz |
| **Topologia/Canais RAM** | Dual (1x8GB DDR5) | Dual (2x8GB) | Single (1x8GB) | Single (1x8GB) | Dual (2x8GB) | Dual (2x16GB) |
| **GPU Integrada** | Intel UHD Graphics | Intel Iris Xe (80 EUs) | AMD Radeon Vega 8 | Intel UHD Graphics 620 | Não possui | Não possui |
| **GPU Dedicada** | RTX 4050 Laptop | Não possui | Não possui | NVIDIA MX130 | AMD RX 7600 | RTX 3050 8GB |
| **Interface Barramento GPU** | PCIe 4.0 x8 | N/A | N/A | PCIe 3.0 x4 | PCIe 4.0 x8 | PCIe 4.0 x8 |
| **Armazenamento** | SSD NVMe SK Hynix 512 GB | SSD NVMe ADATA 512 GB | SSD NVMe PCIe 256 GB | HDD WD Blue 1TB (5400 RPM) | SSD SATA 120GB + HD 1TB | 2x SSD NVMe M.2 1TB |
| **Interface/Taxa do Disco** | PCIe Gen 4.0 x4 (Intel VMD) | PCIe Gen 3.0 x4 (Intel VMD) | PCIe Gen 3.0 x4 | SATA III (6 Gbps) | SATA III (6 Gbps) | [Preencher Gen]* |
| **Sistema Operacional** | Win 11 Home SL 25H2 | Win 11 Home SL 25H2 | Win 11 Home SL 25H2 | Win 11 Home SL 25H2 | Win 11 Home 25H2 | Win 11 Pro 25H2 |

> ⚠️ **Itens ainda pendentes de preenchimento:** frequência exata da RAM da Máquina E
> (`[MHz]*`), modelo do gabinete das Máquinas E e F (`[Preencher Gabinete]*`) e geração da
> interface de disco da Máquina F (`[Preencher Gen]*`). Citações que dependam estritamente
> desses três valores específicos permanecem com nota de uso preditivo até a confirmação.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  PATEL, Samrat Pravin. *Lifecycle Carbon Footprint and Sustainability Evaluation of
  DRAM-based Processing in Memory Computing Architectures*. 2025. Dissertação (Mestrado em
  Engenharia Elétrica) — University of Kentucky, Lexington, KY, 2025. Disponível em:
  https://doi.org/10.13023/etd.2025.552. Acesso em: 17 jun. 2026.

- **Código BibTeX Completo (.bib):**

```bibtex
@MastersThesis{patel:25,
  author       = {Samrat Pravin Patel},
  title        = {Lifecycle Carbon Footprint and Sustainability Evaluation of
                  {DRAM}-based Processing in Memory Computing Architectures},
  school       = {University of Kentucky},
  year         = {2025},
  address      = {Lexington, KY},
  month        = {dec},
  doi          = {10.13023/etd.2025.552},
  note         = {Advisor: Dr. Ishan G. Thakkar. Theses and
                  Dissertations--Electrical and Computer Engineering, paper 223.
                  Dispon{\'i}vel em: \url{https://uknowledge.uky.edu/ece_etds/223}}
}
```

> ⚠️ **Atenção:** É uma dissertação de mestrado (Master's Thesis), não um artigo de
> conferência/periódico. Ajustar a categoria BibTeX (`@MastersThesis`) caso o `sbc.bst`
> exija outra classe de entrada para o `sbc-template.bib`.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Dissertação de Mestrado (Master's Thesis em Electrical and Computer
  Engineering).
- **Instituição/Editora:** University of Kentucky — UKnowledge (repositório institucional).
  Orientador: Dr. Ishan G. Thakkar.
- **Palavras-Chave Originais:** Sustainability, Computing Hardware, Carbon Footprint,
  Processing-in-Memory, DRAM Aging.
- **Resumo do Escopo Geral:** A dissertação investiga a sustentabilidade ambiental do
  hardware de computação ao longo de seu ciclo de vida completo, com foco em arquiteturas
  Processing-in-Memory (PIM) baseadas em DRAM, comparando-as a GPUs tradicionais (NVIDIA
  Titan X). O autor utiliza a ferramenta ACT (Architectural Carbon Footprint Modeling Tool)
  para quantificar a pegada de carbono incorporada (manufatura) e operacional (uso) de
  cinco arquiteturas PIM (DRISA, SCOPE, LACC, ATRIA) frente a redes neurais convolucionais
  (AlexNet, VGG16, ResNet, GoogleNet), aplicando análises de *break-even* e indiferença, além
  de modelar o efeito do envelhecimento (*aging*) da DRAM sobre a latência operacional, a
  energia consumida e a frequência ótima de substituição do hardware ao longo de 10 anos.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

### 3.1. Conceito/Teoria: Gargalo de Von Neumann / *Memory Wall*

- **Citação Direta (Ipsis Litteris):** "This design dictates a rigid separation between
  processing and memory/storage units, necessitating constant data movement across long,
  energy-hungry interconnects [...] This large overhead of data movement creates a
  significant performance, scalability, and energy bottleneck often termed the 'memory
  wall'" (Página 17).

- **Paráfrase (Citação Indireta Acadêmica):** A arquitetura de Von Neumann, ao impor uma
  separação física rígida entre unidade de processamento e unidade de memória, obriga o
  deslocamento constante de dados por interconexões longas e energeticamente custosas,
  fenômeno classicamente denominado "gargalo de memória" (*memory wall*), que compromete
  simultaneamente desempenho, escalabilidade e eficiência energética do sistema
  (Patel, 2025, p. 17).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Arquitetura de
  Von Neumann e gargalos de barramento, antes de discutir Single-Channel vs. Dual-Channel.

- **Mapeamento de Colunas e Arquivos de Teste:** Este conceito sustenta teoricamente por que
  a coluna `Multi_Core` dos arquivos `scores_maqA.txt` a `scores_maqD.txt` pode não escalar
  linearmente com o número de núcleos/threads quando o barramento de memória é o fator
  limitante. Nos CSVs de telemetria, o gargalo se manifesta na correlação entre `Uso total
  da CPU (%)` elevado e `Relógio da memória (MHz)` ou `Taxa de leituras (MB/s)` /
  `Taxa de gravações (MB/s)` estagnados — indicando que a CPU aguarda dados da memória
  (latência de barramento), não que está computacionalmente saturada.

---

### 3.2. Conceito/Teoria: Hierarquia de Memória (Registradores → Cache → DRAM → Armazenamento)

- **Citação Direta (Ipsis Litteris):** "The traditional memory hierarchy comprises several
  layers, including registers, cache, dynamic random-access memory (DRAM), and storage
  solutions such as solid-state drives (SSDs) [...] At the top tier of the memory
  hierarchy, registers enable the fastest access required for CPU tasks, followed by cache
  memory, which temporarily stores frequently accessed data from main memory (DRAM). Cache
  serves to close the speed gap between the CPU and DRAM, thereby reducing latency and
  boosting performance" (Página 49).

- **Paráfrase (Citação Indireta Acadêmica):** A hierarquia de memória tradicional organiza-se
  em camadas de velocidade decrescente e capacidade crescente — registradores, memória cache,
  DRAM (memória principal) e dispositivos de armazenamento secundário, como SSDs — sendo que a
  memória cache desempenha o papel fundamental de mitigar a disparidade de velocidade entre o
  processador e a DRAM, reduzindo a latência efetiva de acesso e elevando o desempenho global
  do sistema (Patel, 2025, p. 49).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Hierarquia de
  Memória, imediatamente antes de detalhar o papel da Cache L3 nas máquinas do grupo.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a discussão sobre o impacto da
  Cache L3 (6 MB na Máquina D) sobre o `Single_Core` e `Multi_Core` dos arquivos
  `scores_maq*.txt`. Nos CSVs, correlaciona-se com `Carga da memória física (%)` e com a
  ausência de colunas diretas de *cache hit/miss* no HWiNFO64 — o que deve ser registrado como
  limitação metodológica do estudo do grupo, já que a hierarquia interna de cache não é
  diretamente instrumentada pelas colunas disponíveis.

---

### 3.3. Conceito/Teoria: Arquitetura e Temporização da DRAM (tRCD, tCAS, tRP)

- **Citação Direta (Ipsis Litteris):** "DRAM processes data through several cycles:
  activation, precharge, read, and write [...] The timing parameters associated with these
  phases- such as tRCD (row to column delay), tRP (row precharge time), and tCAS (column
  access strobe)-are vital in determining DRAM performance, impacting both speed and energy
  efficiency" (Página 50).

- **Paráfrase (Citação Indireta Acadêmica):** O funcionamento da DRAM compreende ciclos
  sequenciais de ativação de linha, precarga, leitura e escrita, regidos por parâmetros de
  temporização — notadamente tRCD (atraso entre ativação de linha e acesso à coluna), tRP
  (tempo de precarga da linha) e tCAS (latência de acesso à coluna, ou *CAS Latency*) —, os
  quais determinam conjuntamente a velocidade de resposta e a eficiência energética do
  subsistema de memória (Patel, 2025, p. 50).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de
  Memória/Subsistema de Memória, complementando a discussão de frequência de RAM (DDR4
  1333 MHz da Máquina D).

- **Mapeamento de Colunas e Arquivos de Teste:** Mapeia-se **diretamente** para as colunas
  de temporização presentes na lista de colunas do HWiNFO64 dos 80 arquivos
  `maq*_rodada_*.CSV`: `Tcas (T)`, `Trcd (T)`, `Trp (T)`, `Tras (T)`, `Trc (T)`, `Trfc (T)` e
  `Command Rate (T)`. Essas colunas devem ser cruzadas com `Relógio da memória (MHz)` e
  `Relação do relógio da memória (x)` para fundamentar empiricamente, na seção de Resultados,
  se diferenças nesses parâmetros entre as Máquinas A, B, C e D explicam variações no
  `Single_Core`/`Multi_Core` Score que não sejam atribuíveis apenas ao clock da CPU.

---

### 3.4. Conceito/Teoria: Memória Single-Channel vs. Dual-Channel

- **Citação Direta (Ipsis Litteris):** "DRAM can be configured in single-channel or
  dual-channel modes, significantly affecting data transfer bandwidth and efficiency. A
  dual-channel arrangement effectively doubles the data paths, thus enhancing throughput
  relative to single-channel configurations" (Página 50).

- **Paráfrase (Citação Indireta Acadêmica):** A configuração da DRAM em modo single-channel
  ou dual-channel exerce influência significativa sobre a largura de banda de transferência
  de dados, uma vez que o arranjo dual-channel duplica efetivamente os caminhos de dados
  disponíveis, ampliando a taxa de transferência (*throughput*) em comparação a configurações
  single-channel (Patel, 2025, p. 50).

> ✅ **ATUALIZAÇÃO — USO AGORA DIRETO (NÃO MAIS PREDITIVO):** Com a tabela de hardware
> consolidada (Seção 0), a comparação Single vs. Dual Channel deixa de ser hipotética.
> Confirma-se: **Single Channel** nas Máquinas **C** (Ryzen 5 3500U, 8 GB DDR4 2400 MHz) e
> **D** (i5-8265U, 8 GB DDR4 2400 MHz); **Dual Channel** nas Máquinas **A** (i5-13420H, 8 GB
> DDR5 5200 MT/s, 1x8GB — *atenção: DDR5 dual-channel "1x8GB" ocorre porque módulos DDR5
> trazem dois subcanais de 32 bits por pastilha, diferentemente do DDR4*), **B** (i5-1334U,
> 16 GB DDR4 2666 MHz, 2x8GB), **E** (Ryzen 5 5500, 16 GB DDR4, 2x8GB) e **F** (i5-14600KF,
> 32 GB DDR4 3600 MHz, 2x16GB). Isso permite ao grupo realizar, na seção de Resultados, uma
> comparação estatisticamente válida de `Multi_Core` Score entre máquinas de mesma família de
> CPU/uso similar, mas com topologias de canal distintas — por exemplo, contrastando C e D
> (ambas Single Channel, DDR4 2400 MHz) contra B (Dual Channel, DDR4 2666 MHz), isolando o
> efeito da topologia de canal sobre o throughput de memória em cargas multithread.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Gargalo de Von
  Neumann e Barramento de Memória, e posteriormente em Resultados e Discussão, *condicionado*
  à confirmação de hardware das demais máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:** Quando disponível, deve ser cruzado com
  `Relógio da memória (MHz)`, `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)` dos
  CSVs, comparando os scores `Multi_Core` das máquinas com RAM em canal duplo contra a
  Máquina D (single channel, DDR4 1333 MHz), evidenciando o impacto do paralelismo de
  barramento sobre a vazão de dados sob carga multithread.

---

### 3.5. Conceito/Teoria: Gerações DDR (DDR3, DDR4, DDR5) e Evolução de Desempenho/Eficiência

- **Citação Direta (Ipsis Litteris):** "different DDR standards, including DDR3, DDR4, and
  DDR5, offer progressive advancements in performance, energy efficiency, and latency [...]
  Each subsequent generation boasts higher data rates, improved power consumption, and
  enhanced bandwidth" (Página 50).

- **Paráfrase (Citação Indireta Acadêmica):** As sucessivas gerações do padrão DDR (DDR3,
  DDR4 e DDR5) representam avanços progressivos em desempenho, eficiência energética e
  latência, com cada geração subsequente apresentando taxas de transferência de dados
  superiores, consumo de potência mais comedido e maior largura de banda agregada
  (Patel, 2025, p. 50).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — contextualização da RAM DDR4
  1333 MHz utilizada na Máquina D frente à evolução tecnológica do padrão DDR.

- **Mapeamento de Colunas e Arquivos de Teste:** Suporta a discussão comparativa entre
  máquinas que eventualmente operem com DDR4 em frequências distintas, cruzando
  `Relógio da memória (MHz)` com os scores `scores_maq*.txt`. Reforça teoricamente por que
  uma RAM DDR4 operando a 1333 MHz (efetivamente abaixo do padrão nominal mais comum de
  2400 MHz para DDR4) pode representar um fator limitante de desempenho na Máquina D.

> ✅ **ATUALIZAÇÃO — APLICAÇÃO REAL COM DDR5 (MÁQUINA A):** A tabela de hardware consolidada
> (Seção 0) confirma que o grupo possui, pela primeira vez, uma amostra real de geração DDR5
> (Máquina A — i5-13420H, 8 GB DDR5 5200 MT/s), ao lado de quatro máquinas DDR4 em
> frequências distintas (2400, 2666 e 3600 MHz) e a já registrada DDR4 a 1333 MHz da Máquina
> D. Isso possibilita ao grupo, na seção de Resultados e Discussão, traçar uma escala
> evolutiva empírica DDR4 (1333–3600 MHz) → DDR5 (5200 MT/s), correlacionando
> `Relógio da memória (MHz)` de cada CSV ao `Multi_Core` Score correspondente, e discutir,
> com base nesta citação teórica, se o salto de geração (DDR4→DDR5) — e não apenas o aumento
> de frequência *dentro* da mesma geração — explica eventuais ganhos de desempenho
> desproporcionais ao clock da CPU na Máquina A. Deve-se notar, contudo, que a Máquina A é
> também a única com microarquitetura híbrida P-core/E-core Raptor Lake-H e GPU dedicada de
> alto desempenho (RTX 4050), de modo que o isolamento estatístico do efeito exclusivo da
> geração de memória exige controle cuidadoso de variáveis confundidoras (ver Seção 3.13).

---

### 3.6. Conceito/Teoria: Potência Estática (PS) vs. Potência Dinâmica (PD) e Modelo de Potência Média

- **Citação Direta (Ipsis Litteris):** "P = (1 − rS) · (rS · (PD + PS) + (1 − rA) PS) + PL
  [...] PD represents dynamic power during workload execution, PS denotes static power
  while the system is active but idle, PL indicates the power consumed in sleep mode"
  (Página 40).

- **Paráfrase (Citação Indireta Acadêmica):** O consumo médio de potência de um sistema
  computacional pode ser modelado como uma combinação ponderada de potência dinâmica
  (consumida durante a execução efetiva de carga de trabalho), potência estática (consumida
  enquanto o sistema permanece ativo, mas ocioso) e potência em modo de baixo consumo
  (*sleep*), ponderadas pelas razões de tempo em repouso (*sleep ratio*) e de atividade
  (*active ratio*) do equipamento (Patel, 2025, p. 40).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Consumo Energético,
  como base conceitual para diferenciar, na coluna `Potência total da CPU (W)` do HWiNFO64, os
  trechos de captura em idle (potência estática) dos trechos durante o Geekbench 6 (potência
  dinâmica).

- **Mapeamento de Colunas e Arquivos de Teste:** Mapeia-se para `Potência total da CPU (W)`,
  `Potência de núcleos IA (W)` e `Potência do restante do chip (W)` dos arquivos
  `maq*_rodada_*.CSV`. Recomenda-se ao grupo segmentar estatisticamente os primeiros segundos
  de cada rodada (idle/aquecimento) dos segundos de execução efetiva do benchmark, permitindo
  estimar empiricamente a fração de potência estática vs. dinâmica em cada máquina —
  análise que fundamenta diretamente o cálculo de Desempenho por Watt proposto no escopo do
  projeto.

---

### 3.7. Conceito/Teoria: Envelhecimento da DRAM (*Aging*) e seu Efeito sobre a Latência — Analogia ao Thermal Throttling

- **Citação Direta (Ipsis Litteris):** "When the operating voltage is reduced, the Internal
  Row and Column Delay tRCD increases due to the impact of the threshold voltage Vth [...]
  This upward trend in tRCD continues until the change in Vth reaches around 700 mV, after
  which the rise in Vth plateaus" (Página 52).

- **Paráfrase (Citação Indireta Acadêmica):** A redução da tensão de operação da DRAM ao
  longo de seu envelhecimento eleva a tensão de limiar (Vth) dos transistores de acesso,
  o que, por consequência, aumenta exponencialmente o atraso interno de linha-para-coluna
  (tRCD), processo que se estabiliza somente após uma variação acumulada de
  aproximadamente 700 mV no Vth (Patel, 2025, p. 52).

- **Paráfrase Complementar (Analogia Conceitual com Thermal Throttling):** Embora o mecanismo
  físico seja distinto, o efeito do envelhecimento da DRAM sobre a latência (aumento
  progressivo de tRCD para preservar a confiabilidade de retenção de dados) constitui um
  paralelo conceitual relevante ao fenômeno de *thermal throttling* observado em CPUs: em
  ambos os casos, o sistema sacrifica desempenho bruto (latência ou clock) em favor da
  confiabilidade e integridade operacional sob condições adversas — temperatura elevada, no
  caso do throttling de CPU, e degradação celular acumulada, no caso do aging de DRAM.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — como nota teórica de
  contextualização ao discutir o Estrangulamento Térmico (*Thermal Throttling*) observado nas
  máquinas do grupo, evidenciando que a relação "degradação de condição física → aumento de
  latência/redução de clock → maior variabilidade" é um padrão recorrente em Arquitetura de
  Computadores, não exclusivo de CPUs.

- **Mapeamento de Colunas e Arquivos de Teste:** Não há colunas diretas de *aging* de DRAM no
  HWiNFO64 (mensuração de curto prazo, não de longo prazo). Esta citação deve ser usada apenas
  como **analogia teórica**, não como evidência empírica direta. A correlação empírica real do
  grupo deve ocorrer entre `Estrangulamento térmico do núcleo (avg) (Yes/No)`,
  `Relógios efetivos núcleo (avg) (MHz)` e o Desvio Padrão Amostral das 20 rodadas de
  `scores_maq*.txt`, evidenciando aumento de variabilidade quando o throttling térmico é
  ativado.

---

### 3.8. Conceito/Teoria: Métricas de Eficiência Energética e Desempenho por Watt (FPS/W/mm²)

- **Citação Direta (Ipsis Litteris):** "ATRIA demonstrates significant performance gains
  compared to prior accelerators like LACC [...] Evaluation shows ATRIA achieves up to 3.2×
  higher throughput (FPS) and up to 10× better efficiency (FPS/W/mm²) relative to the best
  prior in-DRAM accelerator, despite exhibiting an average 3.5% accuracy drop" (Página 24).

- **Paráfrase (Citação Indireta Acadêmica):** A avaliação comparativa entre arquiteturas
  aceleradoras pode ser conduzida não apenas pela vazão bruta (*throughput*, medida em
  quadros por segundo), mas também por uma métrica composta de eficiência que normaliza o
  desempenho pelo consumo de potência e pela área do chip (FPS/W/mm²), permitindo comparações
  mais justas entre arquiteturas de diferentes escalas físicas e perfis energéticos
  (Patel, 2025, p. 24).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica/Metodologia — subseção de Eficiência
  Microarquitetural, como precedente bibliográfico direto para justificar a métrica de
  Desempenho por Watt proposta no projeto (Score do Geekbench 6 ÷ Potência total da CPU em W).

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta diretamente o cálculo de
  Desempenho por Watt do grupo: `Single_Core`/`Multi_Core` (de `scores_maq*.txt`) divididos
  pela média da coluna `Potência total da CPU (W)` (de `maq*_rodada_*.CSV`), por máquina.
  Embora a métrica do artigo normalize também por área de chip (mm²) — informação não
  disponível para CPUs comerciais de notebook —, a lógica de normalização energética é
  diretamente transponível para a métrica Score/Watt do projeto.

---

### 3.9. Conceito/Teoria: Velocidade de Armazenamento e seu Impacto no Carregamento de Testes (HD SATA vs. SSD)

- **Citação Direta (Ipsis Litteris):** Não há, no corpo do texto principal da dissertação,
  uma citação direta específica comparando explicitamente HD SATA a SSD NVMe em termos de
  latência de carregamento de aplicações. O documento trata de armazenamento apenas
  tangencialmente, no contexto de hierarquia de memória (Página 49) e ao mencionar SSDs como
  camada de armazenamento secundário: "storage solutions such as solid-state drives (SSDs)"
  (Página 49).

- **Paráfrase (Citação Indireta Acadêmica):** Não recomendado fundamentar esta seção
  especificamente nesta dissertação, dada a ausência de dados quantitativos comparativos entre
  HD SATA e SSD NVMe no documento.

- **Onde Encaixar no Artigo LaTeX:** Não aplicável a partir desta fonte.

- **Mapeamento de Colunas e Arquivos de Teste:** Caso o grupo deseje fundamentar a discussão
  de HD SATA (Máquina D) vs. eventual SSD NVMe (Máquinas A, B ou C), recomenda-se buscar
  referência mais específica e quantitativa (ver Seção 5 de sugestões de busca). As colunas
  empiricamente relevantes para essa discussão no nosso dataset são `Taxa de leituras (MB/s)`,
  `Taxa de gravações (MB/s)`, `Atividade de leitura (%)`, `Atividade de gravação (%)` e
  `Temperatura do disco (°C)`.

> ✅ **ATUALIZAÇÃO — COMPARAÇÃO REAL AGORA POSSÍVEL (MÁQUINAS A, B, C, F vs. D e E):** A
> tabela de hardware consolidada (Seção 0) revela um espectro completo de armazenamento no
> grupo: **SSD NVMe** em quatro máquinas (A — SK Hynix 512 GB, PCIe Gen 4.0 x4; B — ADATA
> 512 GB, PCIe Gen 3.0 x4; C — 256 GB, PCIe Gen 3.0 x4; F — 2x NVMe M.2 1TB), **HDD SATA puro**
> na Máquina D (Western Digital Blue 1TB, 5400 RPM) e uma configuração **híbrida SSD SATA +
> HDD** na Máquina E (SSD SATA 120GB + HD 1TB). Esta diversidade viabiliza, mesmo sem citação
> direta específica desta dissertação (que não compara HD SATA a SSD NVMe quantitativamente),
> uma comparação empírica robusta e multifatorial no projeto: a Máquina D (HDD SATA, 5400 RPM)
> deve apresentar tempos de carregamento/preparação de teste e maior variabilidade na coluna
> `Atividade de leitura (%)` e `Taxa de leituras (MB/s)` em comparação às Máquinas A, B, C e F
> (todas SSD NVMe). Além disso, dentro do próprio grupo de SSDs NVMe, a Máquina A (PCIe Gen
> 4.0 x4) versus B e C (PCIe Gen 3.0 x4) permite uma sub-comparação de geração de interface
> PCIe sobre a taxa de leitura/gravação, reforçando teoricamente — ainda que com base em fonte
> bibliográfica distinta desta dissertação (ver Seção 5) — a hierarquia de armazenamento como
> camada relevante mesmo quando o teste de CPU (Geekbench 6) não é primariamente limitado por
> I/O de disco, mas pode ser afetado durante o carregamento inicial do binário de teste.

---

### 3.10. Conceito/Teoria: Cache L3 de Maior Capacidade e seu Papel na Mitigação do Memory Wall (Máquinas A, B, E, F)

- **Citação Direta (Ipsis Litteris):** "Cache serves to close the speed gap between the CPU
  and DRAM, thereby reducing latency and boosting performance" (Página 49). Reaproveita-se a
  mesma citação-base da Seção 3.2, agora aplicada a um contraste empírico mais amplo.

- **Paráfrase (Citação Indireta Acadêmica):** A função estrutural da memória cache de
  reduzir a disparidade de velocidade entre processador e DRAM torna-se proporcionalmente
  mais relevante quanto maior a capacidade de cache disponível, uma vez que caches maiores
  retêm um volume superior de dados frequentemente acessados, reduzindo a frequência de
  acessos à memória principal e, por extensão, a exposição do sistema ao gargalo de
  Von Neumann (Patel, 2025, p. 49).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de
  Memória, como continuação direta da Seção 3.2, agora com aplicação empírica ampliada.

- **Mapeamento de Colunas e Arquivos de Teste:** A tabela de hardware consolidada (Seção 0)
  evidencia um espectro de Cache L3 que vai de **4 MB (Máquina C)** a **24 MB (Máquina F)**,
  passando por 6 MB (D), 12 MB (A e B) e 16 MB (E). Recomenda-se ao grupo plotar um gráfico
  de dispersão (scatterplot, sem conectar pontos entre rodadas distintas) cruzando o tamanho
  de Cache L3 de cada máquina com o `Multi_Core` Score médio das 20 rodadas de
  `scores_maq*.txt`, controlando visualmente pelo número de núcleos/threads de cada CPU. Nos
  CSVs de telemetria, a coluna `Carga da memória física (%)` pode ser usada como *proxy*
  indireto: espera-se que máquinas com Cache L3 menor (C, 4 MB) apresentem maior pressão
  sobre a hierarquia de memória sob carga multithread do Geekbench 6 do que a Máquina F
  (24 MB), ainda que esta relação não seja diretamente mensurável pelas colunas do HWiNFO64
  (que não expõem taxa de *cache miss*).

---

### 3.11. Conceito/Teoria: Arquitetura Híbrida de Núcleos (P-core/E-core) como Resposta ao Gargalo de Desempenho-por-Watt (Máquinas A, B, F)

- **Citação Direta (Ipsis Litteris):** Não há, no texto desta dissertação, uma citação
  direta especificamente sobre arquiteturas híbridas P-core/E-core (tecnologia não abordada
  pelo autor, cujo foco é PIM/DRAM). O conceito mais próximo disponível no documento é o de
  eficiência energética comparativa entre arquiteturas de diferentes perfis: "ASICs offer
  improved performance and energy efficiency, but they necessitate additional hardware,
  thereby increasing embodied energy [...] a compromise exists between the performance and
  efficiency of specialized hardware and the reusability of general-purpose hardware"
  (Página 67).

- **Paráfrase (Citação Indireta Acadêmica):** Existe um compromisso estrutural entre
  desempenho/eficiência de hardware especializado e a flexibilidade de hardware de propósito
  geral, de modo que soluções híbridas tendem a equilibrar ambas as vantagens
  (Patel, 2025, p. 67). Por extensão conceitual — não tratada literalmente pelo autor —, esse
  mesmo princípio de compromisso (*trade-off*) entre especialização e generalidade encontra
  paralelo na arquitetura híbrida de núcleos P-core (Performance, otimizados para clock
  máximo) e E-core (Efficiency, otimizados para desempenho por Watt) presente nas CPUs Intel
  de 12ª geração em diante.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível
  de Instrução e Thread (Cores Físicos vs. Threads Lógicos), como nota introdutória à
  distinção P-core/E-core antes de discutir os resultados de `Multi_Core` Score.

- **Mapeamento de Colunas e Arquivos de Teste:** Aplica-se diretamente às Máquinas **A**
  (i5-13420H: 4P+4E / 12T), **B** (i5-1334U: 2P+8E / 12T) e **F** (i5-14600KF: 6P+8E / 20T),
  todas com topologia híbrida, em contraste com C, D (núcleos homogêneos) e E (núcleos
  homogêneos Zen 3). Recomenda-se cruzar, nos arquivos `maqA/B/F_rodada_*.CSV`, as colunas
  individuais `Core 0 Relógio (MHz)` a `Core 3 Relógio (MHz)` (ou, quando disponível,
  expandir a leitura para os núcleos adicionais conforme exportação do HWiNFO64) com
  `Core 0 Uso (%)` a `Core 3 Uso (%)`, observando se o agendador do Windows 11 prioriza os
  P-cores durante o teste `Single_Core` do Geekbench 6 (carga sequencial, baixa
  paralelização) e distribui a carga entre P-cores e E-cores no teste `Multi_Core`. Essa
  análise fundamenta uma discussão de Eficiência Microarquitetural mais rica do que a simples
  contagem de núcleos físicos.

> ⚠️ **NOTA DE FICHAMENTO PREDITIVO (Diretriz de Abstração de Hardware Futuro):** Como esta
> citação é uma extensão conceitual da fonte (e não uma transcrição literal sobre P-core/
> E-core), recomenda-se ao grupo buscar bibliografia mais específica sobre arquiteturas
> híbridas (ver string de busca correspondente na Seção 5) antes de utilizá-la como
> fundamentação primária no `main.tex`. Use-a apenas como ponte conceitual complementar.

---

### 3.12. Conceito/Teoria: TDP, Litografia e a Relação entre Densidade de Transistores e Consumo Energético (Todas as Máquinas)

- **Citação Direta (Ipsis Litteris):** "Environmental impacts per chip area increase with
  feature size as technology drops below 90 nm due to CMOS logic scaling to enable
  node-to-node power scaling to allow more functional features to facilitate lowering energy
  per operation" (Página 33).

- **Paráfrase (Citação Indireta Acadêmica):** A redução do nó de litografia (tecnologia de
  fabricação em escala nanométrica cada vez menor) permite, por meio do escalonamento da
  lógica CMOS, reduzir o consumo de energia por operação computacional, ainda que às custas
  de maior complexidade de fabricação (Patel, 2025, p. 33).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Eficiência
  Microarquitetural, antecedendo a discussão de Desempenho por Watt (Score ÷ Potência total
  da CPU).

- **Mapeamento de Colunas e Arquivos de Teste:** A tabela de hardware consolidada (Seção 0)
  permite contrastar litografias distintas: **Intel 7** (10 nm classe — Máquinas A, B e F,
  arquiteturas Raptor Lake), **14 nm** (Máquina D, Whiskey Lake-U), **12 nm** (Máquina C, Zen+)
  e **7 nm** (Máquina E, Zen 3). Combinada ao TDP Base declarado (de 15 W nas Máquinas B/C/D a
  125 W na Máquina F), esta citação fundamenta teoricamente por que **TDP nominal não é
  preditor isolado de eficiência**: a Máquina F (125 W, litografia Intel 7) e a Máquina E
  (65 W, litografia 7 nm TSMC) devem ser comparadas via Desempenho por Watt
  (`Multi_Core` Score ÷ média de `Potência total da CPU (W)`), e não pelo TDP nominal de
  catálogo, que reflete apenas um limite de projeto (ver também a coluna
  `Limite de potência PL1 (Static) (W)` e `Limite de potência PL2 (Static) (W)` dos CSVs, que
  expõem os limites reais configurados pelo fabricante/BIOS, frequentemente distintos do TDP
  base anunciado).

---

### 3.13. Conceito/Teoria: Instruções Avançadas de CPU (AVX2, VNNI, FMA3) e seu Impacto no Score Sintético

- **Citação Direta (Ipsis Litteris):** Não há citação literal sobre extensões de conjunto de
  instruções x86 (AVX2, VNNI, FMA3) nesta dissertação, cujo escopo é PIM/DRAM e não
  microarquitetura de unidade de execução de CPU. O conceito tangente mais próximo do
  documento é o de operações vetoriais paralelas em hardware especializado: "Standard DRAM
  activation commands inherently operate on an entire row of cells (typically 8 KB of data)
  concurrently, enabling very-wide data-parallel operations" (Página 21).

- **Paráfrase (Citação Indireta Acadêmica):** O princípio de operações de dados amplamente
  paralelas — em que uma única instrução opera simultaneamente sobre múltiplos elementos de
  dados — não é exclusivo de arquiteturas PIM, mas constitui também o fundamento das
  extensões vetoriais SIMD (*Single Instruction, Multiple Data*) de CPUs convencionais, como
  AVX2 e FMA3, que processam múltiplos operandos de ponto flutuante em um único ciclo de
  instrução (Patel, 2025, p. 21, adaptado por extensão conceitual).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível
  de Instrução, antes da discussão sobre Núcleos Físicos vs. Threads Lógicos.

- **Mapeamento de Colunas e Arquivos de Teste:** A tabela de hardware consolidada (Seção 0)
  mostra que apenas as Máquinas **A, B e F** possuem suporte a **Intel DL Boost (VNNI)**
  além de AVX2, enquanto **C e D** dispõem de **FMA3** (sem VNNI) e **E** possui apenas
  AVX/AVX2/FMA3. Como o Geekbench 6 inclui subtestes sensíveis a extensões vetoriais (ex.:
  *Ray Tracing*, *Object Detection*, compressão), esta distinção de conjunto de instruções
  deve ser registrada como **variável confundidora relevante** ao comparar `Single_Core` e
  `Multi_Core` Score entre máquinas de gerações de CPU distintas — um Score superior na
  Máquina A ou F pode refletir não apenas clock ou núcleos, mas também a presença de VNNI
  acelerando subtestes específicos de inferência/IA do Geekbench 6. Não há coluna direta no
  HWiNFO64 que monitore o uso de instruções vetoriais; a evidência deve ser inferida
  indiretamente pela comparação de Score normalizado por clock efetivo
  (`Relógios efetivos núcleo (avg) (MHz)`) entre máquinas com e sem VNNI.

> ⚠️ **NOTA DE FICHAMENTO PREDITIVO (Diretriz de Abstração de Hardware Futuro):** Assim como
> a Seção 3.11, esta é uma extensão conceitual da fonte original (que trata de paralelismo em
> DRAM, não em unidades de execução SIMD de CPU). Recomenda-se complementar com bibliografia
> específica de arquitetura de conjunto de instruções (ISA) x86 antes de uso como
> fundamentação primária — ver sugestões de busca na Seção 5.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES (Se houver no texto original)

### 4.1. Fórmulas Matemáticas/Físicas em LaTeX Puro

**Modelo de Potência Média do Sistema (Página 40):**

```latex
P = (1 - r_S) \cdot \left( r_S \cdot (P_D + P_S) + (1 - r_A) \cdot P_S \right) + P_L
```

Onde $P_D$ é a potência dinâmica, $P_S$ a potência estática, $P_L$ a potência em modo de
baixo consumo (*sleep*), $r_S$ a razão de tempo em repouso e $r_A$ a razão de tempo ativo.

**Relação entre Capacidade de DRAM e Pegada de Carbono Incorporada (Página 32):**

```latex
E_{DRAM\_GB} = CPS_{DRAM} \times Capacity_{DRAM}
```

**Chips por Wafer — CPW (Página 33, atribuída a De Vries):**

```latex
CPW = \frac{\pi d^2}{4A} - \frac{0.58 \, \pi d}{\sqrt{A}}
```

Onde $d$ é o diâmetro do wafer e $A$ é a área do chip.

**Tempo de Indiferença e Break-even (Página 39):**

```latex
t_I = \frac{M_1 - M_0}{P_0 - P_1} \qquad t_B = \frac{M_1}{P_0 - P_1}
```

> ⚠️ Estas duas últimas fórmulas (CPW e *break-even*) pertencem ao escopo de **análise de
> ciclo de vida e sustentabilidade**, não ao escopo experimental do grupo. São transcritas
> aqui apenas para registro de fidelidade ao texto-fonte; **não recomendamos sua utilização**
> no `main.tex`, pois não há dados de manufatura/wafer no projeto do grupo. A fórmula de
> potência média (primeira acima) é a única com aplicabilidade direta ao projeto.

### 4.2. Sugestão de Gráficos/Tabelas Correspondentes

Não se recomenda replicar os gráficos de barra de *break-even* (Figura 5.1) ou os gráficos de
pegada de carbono ano a ano (Figuras 6.2–6.7) do artigo, pois pertencem a um domínio de
análise (modelagem de manufatura/emissões) sem dados correspondentes no escopo do grupo.

Em contrapartida, a Figura 6.1 do artigo (diagrama causal "DRAM Aging → Reduced Retention
Time → Increased Refresh Rate → Higher Operational Energy") pode servir de **modelo
estrutural** (não de conteúdo) para o grupo desenhar, no `main.tex`, um diagrama causal
análogo do tipo "Carga de Trabalho Sustentada → Aumento de Temperatura do Núcleo →
Estrangulamento Térmico (Throttling) → Redução do Relógio Efetivo → Maior Desvio Padrão
entre Rodadas", utilizando como base as colunas `CPU Inteira (°C)`,
`Estrangulamento térmico do núcleo (avg) (Yes/No)`, `Relógios efetivos núcleo (avg) (MHz)` e
o desvio padrão amostral do `Multi_Core` dos arquivos `scores_maq*.txt`.

---

## 5. SUGESTÕES DE BUSCA BIBLIOGRÁFICA COMPLEMENTAR (Google Acadêmico)

Para triangular e reforçar com fontes de aderência mais direta ao escopo de benchmarking e
arquitetura experimental do grupo (visto que esta dissertação cobre sustentabilidade, não
desempenho experimental bruto), sugerem-se as seguintes strings de busca:

**Em inglês:**
- "memory wall" Von Neumann bottleneck computer architecture
- DRAM timing parameters tRCD tCAS tRP latency performance
- single-channel vs dual-channel memory bandwidth benchmark
- DDR4 DDR5 memory clock speed performance comparison
- static power dynamic power CPU benchmarking model
- performance per watt CPU efficiency metric benchmark
- DDR5 vs DDR4 dual subchannel bandwidth latency benchmark
- hybrid core architecture P-core E-core performance efficiency
- AVX2 VNNI SIMD vector instructions performance benchmark
- NVMe SSD vs SATA HDD throughput latency benchmark comparison
- CPU TDP power limit PL1 PL2 performance correlation

**Em português:**
- "gargalo de Von Neumann" arquitetura de computadores barramento
- temporização DRAM tRCD tCAS tRP desempenho memória
- memória single channel dual channel desempenho benchmark
- DDR4 DDR5 frequência de memória comparação de desempenho
- potência estática potência dinâmica CPU modelo energético
- desempenho por watt eficiência energética CPU benchmark
- DDR5 versus DDR4 desempenho largura de banda benchmark
- arquitetura híbrida núcleos P-core E-core desempenho eficiência
- instruções vetoriais AVX2 VNNI desempenho benchmark
- SSD NVMe versus HDD SATA taxa de transferência desempenho
- TDP limite de potência CPU correlação desempenho

---

## 6. OBSERVAÇÕES FINAIS E PRÓXIMAS AÇÕES

1. **Uso recomendado e limitado:** Este fichamento deve ser citado de forma **pontual**
   (agora ampliado para 8 a 10 citações, dado o detalhamento adicional das Seções 3.10 a
   3.13), nas subseções de Hierarquia de Memória, Gargalo de Von Neumann/Barramento de
   Memória, Paralelismo a Nível de Instrução/Thread e Eficiência Microarquitetural, além da
   analogia já registrada na Discussão sobre Thermal Throttling. As seções 4, 5 e 6 originais
   do artigo (Embodied Energy Analysis, Breakeven Analysis, Aging/Carbon Footprint)
   **continuam a não devendo ser incorporadas** ao `main.tex`, por pertencerem a um domínio
   de pesquisa distinto (sustentabilidade/LCA).

2. **Pendência de hardware (atualizada):** Com a tabela de hardware completa (Seção 0), a
   citação referente a Single-Channel vs. Dual-Channel (Seção 3.4) e a citação sobre gerações
   DDR (Seção 3.5) **passam de uso preditivo para uso pleno e direto**. Restam pendentes
   apenas três valores pontuais: frequência exata da RAM da Máquina E, modelo de gabinete das
   Máquinas E e F, e geração da interface de disco da Máquina F (todos marcados com `*` na
   Seção 0). As novas Seções 3.11 (arquitetura híbrida P-core/E-core) e 3.13 (instruções
   AVX2/VNNI) permanecem com nota de fichamento preditivo, não por falta de dados de
   hardware, mas por serem extensões conceituais da fonte original (que não trata
   nativamente desses tópicos).

3. **Referência primária a buscar como complemento mais direto:** Para fortalecer
   especificamente a discussão de gargalo de memória e hierarquia de cache no nosso artigo,
   recomenda-se buscar e fichar complementarmente Hennessy e Patterson,
   *Computer Architecture: A Quantitative Approach*, e Mutlu et al., "A Modern Primer on
   Processing in Memory" (já referenciado dentro desta própria dissertação como [13]), que
   tratam o gargalo de Von Neumann com maior profundidade arquitetural e menor foco em
   sustentabilidade. Adicionalmente, para as novas Seções 3.11 e 3.13 (arquitetura híbrida
   P-core/E-core e instruções vetoriais AVX2/VNNI), recomenda-se buscar fonte primária
   específica de documentação técnica Intel/AMD ou artigos de caracterização de
   microarquitetura Raptor Lake, já que esta dissertação não cobre nativamente tais tópicos.

4. **Próxima ação recomendada (atualizada):** Com a tabela de hardware das Máquinas A a F
   já confirmada, a próxima ação recomendada ao grupo é (i) preencher os três valores
   pendentes residuais (frequência RAM da Máquina E, gabinetes E/F, geração de disco F) e
   (ii) iniciar a coleta efetiva dos 4 arquivos `scores_maq*.txt` e dos 80 arquivos
   `maq*_rodada_*.CSV` por máquina, agora que a base de hardware está consolidada para
   sustentar todas as comparações teóricas detalhadas neste fichamento.

---

*Fichamento gerado em: Junho de 2026*
*Gerado com base nas Diretrizes de Fichamento do Projeto — arquivo `diretrizes_fichamento_sbc`*
*Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí*
*Professor Orientador: Prof. Dr. Iago Medeiros*
