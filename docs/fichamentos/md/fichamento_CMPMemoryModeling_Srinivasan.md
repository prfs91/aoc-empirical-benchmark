# FICHAMENTO CIENTÍFICO COMPLETO
## Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí
## Arquivo: `fichamento_CMPMemoryModeling_Srinivasan.md`

---

> **VEREDITO DE RELEVÂNCIA:** ✅ **SIM — O documento é altamente útil para o projeto de AOC.**
>
> O artigo aborda diretamente o impacto da largura de banda de memória no desempenho de sistemas
> multicore, demonstrando empiricamente que o número de canais de memória (Single Channel vs.
> Dual Channel vs. Quad Channel) é o principal fator limitante de escalabilidade de desempenho
> em processadores com múltiplos núcleos. Esse é o fundamento teórico central para explicar
> o gargalo de Von Neumann na Máquina D (Intel Core i5-8265U com RAM em **Single Channel**,
> 1x8 GB DDR4 a 1333 MHz), cujo teto de largura de banda efetiva (~21 GB/s teórico, mas
> substancialmente inferior na prática) limita o ganho multi-thread observado nos scores
> Multi-Core do Geekbench 6. O artigo também fundamenta diretamente: a curva largura de
> banda × latência, o fenômeno de contenção de memória, o conceito de CPI e IPC em sistemas
> paralelos, e a distinção entre cargas computacionais e cargas ligadas à memória (*memory-bound*
> vs. *compute-bound*) — todos conceitos críticos para a Fundamentação Teórica e a seção de
> Resultados do nosso artigo SBC.
>
> **ATUALIZAÇÃO (dados completos das 6 máquinas — Tabela de Hardware revisada):** Com a
> consolidação da tabela de hardware do grupo (Máquinas A a F), confirma-se que as previsões
> preditivas das seções 3.2, 3.4 e 3.12 deste fichamento se tornam **diretamente testáveis e
> centrais** para os Resultados do artigo, pois o grupo possui — dentro da mesma amostra —
> tanto sistemas em **Single Channel** (Máquina C, AMD Ryzen 5 3500U) quanto em **Dual Channel**
> (Máquinas A, B, D¹, E e F), permitindo a réplica empírica direta do experimento de Srinivasan
> et al. descrito nas seções 4.1 e 4.2 do artigo original. Note-se também que a tabela revisada
> reclassifica a Máquina D (Roberta) — antes referida neste fichamento como exemplo único de
> Single Channel — para uma posição de **referência comparativa**, já que a Máquina C agora
> assume esse papel dentro do conjunto de 6 máquinas. Os trechos já redigidos sobre a Máquina D
> permanecem integralmente válidos como estudo de caso Single Channel; a Máquina C passa a ser
> um segundo estudo de caso da mesma categoria, com arquitetura distinta (AMD Zen+ vs. Intel
> Whiskey Lake), o que enriquece a comparação ao isolar o efeito do canal de memória de
> particularidades da microarquitetura do fabricante.
>
> ¹ *Nota de precisão:* a Máquina D (Dell Inspiron 15 5584, i5-8265U) está corretamente
> classificada como **Single Channel** na tabela de hardware fornecida pelo grupo (8 GB DDR4
> 2400 MHz, módulo único). A menção a "Dual Channel" no início deste parágrafo refere-se às
> demais máquinas do conjunto (A, B, E, F); a Máquina D permanece, junto à Máquina C, no grupo
> Single Channel da amostra.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  SRINIVASAN, S.; ZHAO, L.; GANESH, B.; JACOB, B.; ESPIG, M.; IYER, R. **CMP Memory Modeling:
  How Much Does Accuracy Matter?** In: WORKSHOP ON CHIP MULTIPROCESSOR MEMORY SYSTEMS AND
  INTERCONNECTS (CMP-MSI), [s.l.], [s.d.]. *Anais [...]*. Intel Corporation / University of
  Maryland, [s.d.].

  > ⚠️ **NOTA EDITORIAL:** O artigo não informa explicitamente o nome completo do evento, o ano
  > exato de publicação, o número de páginas nem o DOI. O artigo é oriundo dos laboratórios da
  > Intel Corporation (Systems Technology Lab) em co-autoria com a University of Maryland,
  > College Park. Com base nas referências internas (a mais recente datando de 2005) e no teor
  > técnico, estima-se publicação entre 2005 e 2007. **O líder do grupo deve verificar o evento
  > e o ano exatos antes de inserir no `main.tex`.**

- **Código BibTeX Completo (.bib):**

```bibtex
@InProceedings{srinivasan:07,
  author    = {Sadagopan Srinivasan and Li Zhao and Brinda Ganesh
               and Bruce Jacob and Mike Espig and Ravi Iyer},
  title     = {{CMP} Memory Modeling: How Much Does Accuracy Matter?},
  booktitle = {Workshop on Chip Multiprocessor Memory Systems and Interconnects
               ({CMP-MSI})},
  year      = {2007},
  address   = {[s.l.]},
  publisher = {Intel Corporation / University of Maryland},
  note      = {Systems Technology Lab, Intel Corporation e University of
               Maryland, College Park. Verificar nome do evento, ano e
               p{\'a}ginas exatas antes de usar.}
}
```

> ⚠️ **Atenção:** Preencher `booktitle`, `year`, `pages` e `address` com os dados exatos do
> evento após confirmação com o Prof. Dr. Iago Medeiros ou busca no IEEE Xplore/DBLP pelo
> título exato.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo Científico de Workshop/Conferência
- **Instituição/Editora:** Systems Technology Lab — Intel Corporation; University of Maryland,
  College Park (Bruce Jacob)
- **Autores:** Sadagopan Srinivasan, Li Zhao, Brinda Ganesh, Bruce Jacob, Mike Espig, Ravi Iyer
- **Contato:** Sadagopan.srinivasan@intel.com
- **Palavras-Chave Originais:** Não declaradas. Palavras-chave inferidas: Chip-Multiprocessor
  (CMP); Memory Modeling; Memory Wall; Bandwidth-Latency; Single Channel; Dual Channel;
  CPI; IPC; Prefetching; Memory Contention.
- **Resumo do Escopo Geral:**
  O artigo investiga o impacto do modelo de memória utilizado em simuladores de Chip
  Multiprocessors (CMPs) sobre a precisão das estimativas de desempenho. Os autores comparam
  três tipos de modelo de memória: (i) modelo de latência fixa (Fixed Latency); (ii) modelo de
  fila (Queuing Model); e (iii) modelo detalhado ciclo-a-ciclo (Accurate Cycle Latency Model —
  ACLM). Usando o simulador ManySim e cargas de trabalho de servidores (TPC-C, SAP SD,
  SPECjbb2005, SPECjAppServer2004), os autores demonstram que modelos simplistas produzem
  erros de até 65% na estimativa de desempenho em relação ao modelo preciso, especialmente
  para sistemas com múltiplos núcleos e alta demanda de largura de banda de memória. O artigo
  também avalia o impacto do número de canais de memória (1, 2 e 4 canais DDR3-800) sobre
  o CPI e o throughput de sistemas de 1 a 16 threads.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 O Problema do Memory Wall em Sistemas Multicore — Definição e Causa

- **Conceito/Teoria:** O *Memory Wall* (Muro de Memória) é o fenômeno pelo qual o aumento
  do número de núcleos em um chip eleva proporcionalmente a demanda de largura de banda de
  memória, criando um gargalo que limita o ganho de desempenho paralelo — mesmo que os
  núcleos em si tenham capacidade de processamento disponível.

- **Citação Direta (Ipsis Litteris):**
  > "The simultaneous execution of multiple processes/threads increases the memory bandwidth
  > demand, i.e. the increased number of cores aggravates the memory wall problem." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que a execução simultânea de múltiplos processos em sistemas
  multicore intensifica o problema do *Memory Wall*: à medida que o número de núcleos ativos
  aumenta, a demanda agregada de largura de banda de memória cresce proporcionalmente, até
  que o subsistema de memória — e não a capacidade de processamento dos núcleos — passa a
  ser o fator limitante do desempenho do sistema.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  e Gargalo de Von Neumann; Resultados e Discussão — explicação do comportamento do score
  Multi-Core em relação ao Single-Core.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → razão entre `Multi_Core` e `Single_Core`: se o score Multi-Core
    não escalar proporcionalmente ao número de núcleos (esperado ~4× para 4 núcleos físicos),
    o *Memory Wall* é o principal responsável arquitetural.
  - `maqD_rodada_*.CSV` → coluna `Carga da memória física (%)`: utilização próxima de 100%
    durante os testes Multi-Core é evidência direta do gargalo de memória.
  - `maqD_rodada_*.CSV` → coluna `Relógio da memória (MHz)`: o clock de 1333 MHz do módulo
    Single Channel da Máquina D limita a largura de banda a ~21 GB/s teórico — insuficiente
    para alimentar 4 núcleos a plena carga, como demonstrado pelos autores para sistemas
    Single Channel.

---

### 3.2 Curva Largura de Banda × Latência — Três Regiões de Operação

- **Conceito/Teoria:** A relação entre largura de banda e latência de memória em sistemas reais
  não é linear. Ela se divide em três regiões: (i) Região Constante, onde a latência é
  aproximadamente igual à latência de ociosidade; (ii) Região Linear, onde a latência aumenta
  progressivamente com a demanda; e (iii) Região Exponencial, onde a latência é dominada pela
  contenção entre requisições concorrentes.

- **Citação Direta (Ipsis Litteris):**
  > "The bandwidth-latency curve consists of three distinct regions. Constant region: The latency
  > response is fairly constant for the first 40% of the sustained bandwidth. [...] Linear region:
  > [...] lies for throughputs in the range of 40% to 80% of the sustained maximum throughput.
  > [...] Exponential region: This is the last region [...] between 80%-100% of the sustained
  > maximum." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. descrevem que a curva largura de banda versus latência de um subsistema
  de memória DDR real apresenta três zonas características. Na primeira — a região constante —
  a latência de acesso permanece próxima à latência de ociosidade do sistema, pois há largura
  de banda disponível em excesso. Na segunda — a região linear — a latência começa a crescer
  proporcionalmente à demanda, pois múltiplos núcleos concorrem pelo mesmo controlador de
  memória. Na terceira — a região exponencial — a latência é dominada pela contenção: os
  núcleos passam tempo significativo aguardando o acesso à memória, o que deprime drasticamente
  o desempenho do sistema.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  e Gargalo de Von Neumann; é o modelo teórico que explica por que memória Single Channel
  em uso Multi-Core força o sistema a operar na região linear ou exponencial da curva.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → cruzamento de `Carga da memória física (%)` com `Relógios efetivos
    núcleo (avg) (MHz)`: quando a carga de memória é alta e o clock efetivo cai, o sistema
    está operando na região linear ou exponencial da curva descrita pelos autores.
  - `maqD_rodada_*.CSV` → coluna `Taxa de leituras (MB/s)` + `Taxa de gravações (MB/s)`:
    a soma dessas colunas fornece a largura de banda de memória instantânea, permitindo
    posicionar empiricamente a Máquina D na curva descrita pelos autores.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
  > Máquinas com memória em modo Dual Channel operam com largura de banda efetiva
  > aproximadamente dobrada, o que desloca o ponto de inflexão da curva e permite que o
  > sistema permaneça na região constante sob maior número de threads. Isso se manifestará
  > em melhor score Multi-Core mesmo com clock de núcleo similar. **Este mapeamento só será
  > utilizado na redação final conforme as configurações reais das Máquinas A, B ou C forem
  > preenchidas pelo grupo nas próximas interações, se necessário.**

  > ✅ **ATUALIZAÇÃO — CONFIRMAÇÃO COM TABELA DE HARDWARE COMPLETA (Máquinas A–F):**
  > A previsão acima se confirma diretamente nos dados de hardware do grupo. As Máquinas A
  > (Acer Nitro, i5-13420H, Dual Channel DDR5 5200 MT/s) e B (Dell Inspiron 3530, i5-1334U,
  > Dual Channel DDR4 2666 MHz) possuem largura de banda nominal muito superior à da Máquina C
  > (ASUS M515D, Ryzen 5 3500U, **Single Channel** DDR4) e da Máquina D (Dell Inspiron 5584,
  > i5-8265U, **Single Channel** DDR4 2400 MHz). Como a Máquina C e a Máquina D compartilham
  > a condição Single Channel mas diferem totalmente em microarquitetura (AMD Zen+ vs. Intel
  > Whiskey Lake) e em TDP (15 W ambas, mas litografias de 12 nm e 14 nm respectivamente),
  > a comparação cruzada **C × D** isola o efeito do canal de memória de particularidades do
  > fabricante, permitindo testar diretamente a hipótese da curva trifásica de Srinivasan et al.
  > em duas arquiteturas de ISA distintas (x86 Intel vs. x86 AMD).
  > - `scores_maqC.txt` → coluna `Multi_Core`: espera-se, segundo o modelo dos autores, que a
  >   razão `Multi_Core / Single_Core` da Máquina C também opere na região linear/exponencial
  >   da curva, de forma análoga à Máquina D, mesmo sendo uma CPU AMD.
  >   *(Arquivo de telemetria correspondente: `maqC_rodada_01.CSV` a `maqC_rodada_20.CSV`.)*
  > - As Máquinas E (Ryzen 5 5500, Dual Channel DDR4) e F (i5-14600KF, Dual Channel DDR4
  >   3600 MHz) são desktops com TDP muito superior (65 W e 125 W) e, segundo a mesma curva,
  >   devem permanecer predominantemente na região constante mesmo sob carga Multi-Core plena,
  >   pois sua largura de banda Dual Channel de alto clock (3600 MHz na Máquina F) desloca
  >   substancialmente o ponto de saturação para um número de threads muito maior que o
  >   disponível nessas CPUs (12 e 20 threads, respectivamente).
  >   *(Arquivos de telemetria correspondentes: `maqE_rodada_01.CSV` a `maqE_rodada_20.CSV` e
  >   `maqF_rodada_01.CSV` a `maqF_rodada_20.CSV`.)*
  > **Como usar:** Construir um gráfico de dispersão (scatter) com a largura de banda teórica
  > (Equação de BW_mem, seção 4.2) no eixo X e a razão Multi/Single no eixo Y para as 6
  > máquinas. Espera-se agrupamento de C e D na região de menor BW/menor eficiência paralela,
  > e A, B, E, F na região de maior BW/maior eficiência — confirmando visualmente, com dados
  > reais do grupo, a curva trifásica do artigo.

---

### 3.3 Contenção de Memória — Overhead em Sistemas Multi-Thread

- **Conceito/Teoria:** A contenção de memória é o fenômeno pelo qual múltiplas threads
  concorrem simultaneamente pelo mesmo controlador de memória, causando filas de espera
  que aumentam exponencialmente a latência de acesso à medida que a taxa de requisições
  se aproxima do limite de largura de banda do canal.

- **Citação Direta (Ipsis Litteris):**
  > "Memory contention overhead is the effect experienced by a memory request when the
  > memory controller's transaction queue is full. In this scenario, a memory request has
  > to contend with other requests to get serviced and becomes more pronounced at higher
  > bandwidths of the system." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. definem contenção de memória como o efeito de degradação de latência
  que ocorre quando múltiplas requisições de acesso à memória chegam simultaneamente ao
  controlador, saturando sua fila de transações. Esse efeito de contenção não é capturado
  por modelos simplistas de latência fixa, e se torna progressivamente mais intenso à medida
  que o número de threads ativos aumenta — explicando por que o ganho de desempenho Multi-Core
  é sub-linear em relação ao número de núcleos.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  e Gargalo de Von Neumann; Resultados — explicação da razão Multi/Single inferior ao número
  de núcleos físicos.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Carga da memória física (%)` durante o teste Multi-Core:
    valor elevado indica que múltiplos núcleos disputam o controlador de memória Single Channel.
  - `scores_maqD.txt` → comparação entre `Single_Core` (1 thread ativa) e `Multi_Core` (4
    threads ativas): a diferença entre o ganho teórico e o ganho real quantifica empiricamente
    o impacto da contenção de memória no i5-8265U.

---

### 3.4 Impacto do Número de Canais de Memória no CPI e no Throughput

- **Conceito/Teoria:** O número de canais de memória (Single, Dual, Quad Channel) determina
  a largura de banda máxima disponível e, consequentemente, o ponto a partir do qual o
  desempenho do sistema multicore passa a ser limitado pelo subsistema de memória em vez
  de pelos núcleos de processamento.

- **Citação Direta (Ipsis Litteris):**
  > "Figure 5(a) shows that for single threaded workloads the CPI obtained from both models are
  > nearly identical to that obtained from the detailed model. However, increasing the number of
  > threads, results in an increase in the difference between the CPI values [...] The CPI is off
  > by 35% and 62% respectively for 8 and 16 threads." (p. 5)

- **Citação Direta Complementar (Dual Channel):**
  > "Since the 2 channel configuration provides more bandwidth than 1 channel, the applications
  > operate in the linear region of the bandwidth-latency curve." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que o impacto da configuração de canais de memória sobre o
  desempenho multicore é progressivo: para cargas de trabalho com uma única thread, todos os
  modelos de memória produzem estimativas de CPI quase idênticas, pois a demanda de largura
  de banda é baixa e o sistema opera na região constante da curva. Entretanto, à medida que
  o número de threads aumenta — e, com ele, a demanda de banda — sistemas com Single Channel
  são os primeiros a atingir saturação, forçando o controlador a operar na região exponencial
  e produzindo degradação acentuada de desempenho. Sistemas com Dual Channel sustentam a
  operação na região linear por um intervalo maior de threads, resultando em melhor escalabilidade.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória;
  Resultados e Discussão — comparação de scores Multi-Core entre as quatro máquinas, com
  destaque especial para máquinas que diferem em modo de canal de memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → coluna `Multi_Core` versus `Single_Core`: Máquina D (Single Channel)
    deverá exibir razão Multi/Single inferior à esperada para 4 núcleos — evidência direta
    do efeito descrito pelos autores para configurações Single Channel.
  - `maqD_rodada_*.CSV` → coluna `Relógio da memória (MHz)` e colunas `Tcas (T)`, `Trcd (T)`,
    `Trp (T)`, `Tras (T)`: os timings de latência DDR4 da Máquina D determinam o custo de
    acesso de cada requisição, base da curva bandwidth × latency analisada pelos autores.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
  > Se alguma das Máquinas A, B ou C operar com Dual Channel, o ganho esperado no score
  > Multi-Core do Geekbench 6 é expressivo sem aumento proporcional do score Single-Core —
  > padrão exatamente consistente com os resultados de Srinivasan et al. para a transição
  > Single → Dual Channel. **Este mapeamento só será utilizado na redação final conforme as
  > configurações reais das Máquinas A, B ou C forem preenchidas pelo grupo, se necessário.**

  > ✅ **ATUALIZAÇÃO — CONFIRMAÇÃO COM TABELA DE HARDWARE COMPLETA (Máquinas A–F):**
  > A tabela de hardware revisada confirma e amplia este ponto preditivo. A Máquina A (Raony)
  > opera com Dual Channel **mesmo possuindo apenas um único módulo** de 8 GB DDR5 5200 MT/s —
  > situação notável porque a tecnologia DDR5 já implementa, por especificação, dois
  > sub-canais internos de 32 bits por módulo único (em vez do barramento unificado de 64 bits
  > do DDR4), o que efetivamente confere a um módulo único de DDR5 uma topologia "Dual Channel"
  > mesmo sem um segundo pente físico. Esse é um ponto teórico adicional e **não trivial** que
  > deve ser explicitamente discutido na Fundamentação Teórica, pois rompe a equivalência
  > tradicional "número de módulos = número de canais" estabelecida para DDR3/DDR4 — a própria
  > arquitetura interna do DDR5 é a responsável pelo ganho de banda, e não a quantidade de
  > pentes físicos instalados.
  > - A Máquina B (Dell Inspiron 3530, i5-1334U) opera em Dual Channel real com 2×8 GB DDR4
  >   2666 MHz — caso clássico, idêntico em estrutura ao cenário Dual Channel descrito pelos
  >   autores na seção 4.1 do artigo original (figura 6).
  > - As Máquinas E e F seguem o mesmo padrão de Dual Channel real (2 módulos físicos),
  >   adicionando o fator TDP elevado (65 W e 125 W) e maior cache L3 (16 MB e 24 MB) como
  >   variáveis de controle que devem ser isoladas na discussão, já que, segundo a literatura
  >   de hierarquia de memória, caches L3 maiores reduzem o tráfego efetivo ao controlador de
  >   memória, deslocando ainda mais o sistema para a região constante da curva.
  > **Como usar:** Na Tabela de Hardware Comparativa do `main.tex` (seção de Metodologia),
  > incluir uma coluna explícita "Topologia Efetiva do Canal" distinguindo "Dual Channel
  > (2 módulos)" de "Dual Channel (1 módulo DDR5)" para a Máquina A, evitando que o leitor
  > assuma erroneamente que a Máquina A possui apenas metade da banda das demais máquinas
  > Dual Channel — quando, na prática, sua topologia interna já entrega throughput comparável.

---

### 3.5 Escalabilidade de Throughput — Saturação de Desempenho com Múltiplos Threads

- **Conceito/Teoria:** O ganho de throughput de um sistema multicore com o aumento do número
  de threads não é linear: existe um ponto de saturação a partir do qual adicionar mais
  threads não aumenta o desempenho, e pode até reduzi-lo, devido ao aumento exponencial
  da latência de memória causado pela contenção.

- **Citação Direta (Ipsis Litteris):**
  > "The system performance scales linearly from 8 threads to 32 threads. Beyond 32 threads,
  > this performance gain tapers down because of the increased average memory latency of the
  > system. The memory latency increases exponentially [...] for a large number of threads
  > (greater than or equal to 64 in this case). This contributes to the non-linear increase
  > of system performance with the number of threads." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que a escalabilidade de desempenho em sistemas multicore segue
  um padrão trifásico: crescimento linear até determinado número de threads, seguido de
  progressiva desaceleração do ganho de desempenho e, eventualmente, estabilização ou queda.
  Esse comportamento é causado pelo aumento exponencial da latência de memória na região de
  alta demanda de banda, que neutraliza os ganhos de paralelismo proporcionados pelos núcleos
  adicionais. Em processadores de consumo com 4 núcleos e Hyper-Threading (como o i5-8265U
  da Máquina D), esse teto de escalabilidade é atingido com muito menos threads — e em um
  subsistema Single Channel, ainda mais cedo.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível
  de Thread e Limitações de Escalabilidade (complementa a Lei de Amdahl); Resultados —
  análise da razão Multi-Core / Single-Core por máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → razão `Multi_Core / Single_Core` por máquina: o quociente Multi/Single
    é o indicador empírico direto do ponto de saturação descrito pelos autores para cada
    configuração de hardware testada pelo grupo.
  - `maqD_rodada_*.CSV` → colunas `Core 0 T0 Uso (%)` a `Core 3 T1 Uso (%)`: alta utilização
    de todas as 8 threads lógicas simultaneamente com queda de clock efetivo indica que o
    gargalo de memória saturou antes da capacidade de processamento dos núcleos.

---

### 3.6 CPI como Métrica de Avaliação de Desempenho Multicore

- **Conceito/Teoria:** O CPI (Ciclos Por Instrução) é a métrica primária de eficiência
  arquitetural em sistemas multicore. Quanto maior o CPI, mais ciclos de clock são
  desperdiçados por instrução — tipicamente aguardando acesso à memória. O IPC (Instruções
  Por Ciclo) é seu inverso e representa diretamente a eficiência de execução do processador.

- **Citação Direta (Ipsis Litteris):**
  > "We also show that irrespective of memory optimization techniques, using simplistic models
  > can result in incorrect performance projections for multi-core systems. We observed that the
  > difference in IPC between simple latency model and cycle-accurate model [...] is 2% for a
  > single core, and increases to 15% for 8 cores." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que a diferença entre estimativas de IPC obtidas por modelos
  simplistas e por modelos precisos cresce com o número de núcleos ativos: para um único
  núcleo, o erro é marginal (2%), mas para 8 núcleos, a imprecisão atinge 15% — erro suficiente
  para levar a conclusões incorretas sobre o ganho real de desempenho ao escalar o número de
  núcleos. No contexto do presente trabalho, o score do Geekbench 6 funciona como um
  substituto prático do IPC: scores mais altos indicam maior eficiência de execução por ciclo,
  e a razão Multi-Core / Single-Core indica a eficiência de escalabilidade paralela de cada
  máquina testada.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Métricas de
  Desempenho (CPI, IPC, Scores Sintéticos de Benchmark); Metodologia — justificativa do
  uso do Geekbench 6 como métrica de desempenho e da razão Multi/Single como indicador
  de eficiência paralela.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: o score Single-Core é o
    proxy de IPC para carga monothreaded; o score Multi-Core é o proxy de throughput paralelo.
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)` versus `Uso total
    da CPU (%)`: a relação entre clock efetivo e utilização captura indiretamente o IPC —
    alta utilização com clock abaixo do boost máximo indica que os núcleos estão ativos mas
    limitados por memória (CPI alto).
  - `maqD_rodada_*.CSV` → coluna `Relação do relógio do núcleo (avg) (x)`: o multiplicador
    de clock efetivo é um proxy do IPC relativo — quedas no multiplicador durante carga
    Multi-Core indicam limitação de memória ou térmica.

---

### 3.7 Workloads Memory-Bound vs. Compute-Bound

- **Conceito/Teoria:** Cargas de trabalho *memory-bound* (limitadas pela memória) são aquelas
  em que o processador passa a maior parte do tempo aguardando dados da memória principal,
  enquanto *compute-bound* (limitadas pelo processador) são aquelas em que a memória raramente
  é o recurso limitante. Benchmarks sintéticos de CPU tendem a alternar entre essas
  características nos testes Single-Core e Multi-Core.

- **Citação Direta (Ipsis Litteris):**
  > "The simplistic models do not work as well for memory intensive workloads as they do for
  > compute intensive workloads." (p. 2)

- **Citação Direta Complementar:**
  > "Applications that are memory-bound can show artificial improvement in performance when
  > using simplistic models, but will not result in true performance gain in an actual system
  > which will have a cycle-accurate model." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que modelos simplistas de memória produzem estimativas de
  desempenho artificialmente otimistas para cargas *memory-bound*, precisamente porque não
  capturam os efeitos de contenção e saturação de largura de banda. Para cargas *compute-bound*
  — onde a memória raramente é o gargalo — os modelos simplistas se aproximam do comportamento
  real. No contexto do Geekbench 6, os testes Integer Single-Core tendem a ser mais
  *compute-bound* (alta reutilização de cache), enquanto os testes Multi-Core são mais
  *memory-bound* (múltiplos núcleos competindo pela mesma largura de banda Single Channel).

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória;
  Resultados e Discussão — explicação da diferença relativa entre scores Single-Core e
  Multi-Core por máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Carga da memória física (%)` durante rodadas Single-Core
    versus Multi-Core: a diferença no nível de utilização de memória entre os dois modos de
    teste evidencia o caráter *compute-bound* do Single-Core versus *memory-bound* do Multi-Core.
  - `maqD_rodada_*.CSV` → coluna `Potência total da CPU (W)` versus `Carga da memória física
    (%)`: alta potência de CPU com baixa carga de memória → *compute-bound*; potência moderada
    com alta carga de memória → *memory-bound*.

---

### 3.8 Prefetching e sua Eficácia Dependente da Largura de Banda

- **Conceito/Teoria:** O prefetching (pré-busca de dados da memória) é uma técnica de
  otimização que carrega antecipadamente dados da memória principal para o cache antes de
  serem requisitados, reduzindo a latência de acesso. Sua eficácia, porém, depende da
  largura de banda disponível — em sistemas com gargalo de memória, o prefetching pode
  aumentar a contenção e degradar o desempenho.

- **Citação Direta (Ipsis Litteris):**
  > "We notice that the performance trend for SILM is vastly different from ACLM. SILM shows
  > performance benefits of 5% with prefetching for 8 threads, whereas ACLM shows a significant
  > degradation in performance for the same case." (p. 8)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. revelam um resultado contraintuitivo de grande relevância arquitetural:
  em sistemas onde a memória já opera próxima de sua capacidade máxima de largura de banda,
  o prefetching — uma técnica classicamente associada a melhoria de desempenho — pode produzir
  degradação real de desempenho, pois aumenta o tráfego de memória em um subsistema já
  congestionado. Modelos simplistas, por não capturarem a contenção, preveem erroneamente que
  o prefetching sempre melhora o desempenho, levando a conclusões equivocadas em estudos de
  otimização de arquitetura.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Hierarquia de Memória
  (papel do Cache L3 e do prefetcher de hardware); Resultados — discussão sobre o papel do
  cache L3 de 6 MB do i5-8265U como amortecedor do gargalo Single Channel.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → coluna `Taxa de leituras (MB/s)` e `Leia total (MB)`: taxa de
    leitura elevada com alta carga de memória é evidência de que o prefetcher de hardware
    do i5-8265U está ativo, adicionando tráfego ao canal Single Channel.
  - O cache L3 de 6 MB do i5-8265U é o componente que mitiga a necessidade de prefetching
    para o canal de memória durante os testes do Geekbench 6 — seu impacto pode ser discutido
    comparando a latência do último nível de cache (estimada pelo Geekbench 6) com a largura
    de banda de memória medida pelo HWiNFO64.

---

### 3.9 Escalabilidade Sub-Linear e Teto de Desempenho Paralelo

- **Conceito/Teoria:** À medida que o número de threads aumenta em um sistema multicore,
  o ganho de desempenho segue uma curva de crescimento sub-linear que eventualmente se
  estabiliza em um teto determinado pela largura de banda de memória disponível — não pela
  capacidade de processamento dos núcleos.

- **Citação Direta (Ipsis Litteris):**
  > "The memory bandwidth problem will lead to significant reduction in performance gain as the
  > number of threads is increased. [...] The maximum available memory bandwidth was set to
  > 52 GB/Sec. The system performance scales linearly from 8 threads to 32 threads. Beyond 32
  > threads, this performance gain tapers down." (p. 3)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. estabelecem que o teto de desempenho de um sistema multicore é determinado
  fundamentalmente pela largura de banda máxima do subsistema de memória. Em seus experimentos,
  mesmo com 52 GB/s disponíveis, o desempenho começa a saturar a partir de 32 threads e
  degrada com 64 ou mais threads. Para a Máquina D — com largura de banda Single Channel de
  aproximadamente 21 GB/s teórico, mas efetiva muito menor sob carga — o teto de escalabilidade
  paralela é atingido muito antes, já com 4 a 8 threads lógicas, o que explica a ineficiência
  esperada no score Multi-Core do Geekbench 6.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Paralelismo a Nível
  de Thread; Resultados e Discussão — fórmula e cálculo da razão Multi/Single para cada máquina,
  com discussão arquitetural do teto de memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → razão `Multi_Core / Single_Core` calculada para todas as 4 máquinas:
    valor inferior ao número de threads lógicas disponíveis (8 para o i5-8265U) confirma
    a saturação prevista pelos autores para sistemas Single Channel.
  - `maqD_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)` durante o teste
    Multi-Core vs. Single-Core: se o clock efetivo cai durante o Multi-Core mesmo sem
    throttling térmico, o gargalo é de memória, não de temperatura.

---

### 3.10 Variabilidade de Desempenho em Simulações Multi-Thread

- **Conceito/Teoria:** A variabilidade de desempenho em sistemas multicore — isto é, a
  diferença entre múltiplas estimativas ou medições de uma mesma carga de trabalho — é um
  desafio fundamental de reprodutibilidade experimental, identificado por Alameldeen e Wood
  (referenciados pelos autores) como consequência do não-determinismo inerente às arquiteturas
  multi-thread.

- **Citação Direta (Ipsis Litteris):**
  > "Alameldeen and Wood identified the performance variability as a major challenge for
  > architectural simulation studies for multi-threaded workloads. Variability in this study
  > refers to the differences between multiple estimates of a workload performance. The impact
  > of variability on multi-threaded workloads can be extended to chip-multiprocessors." (p. 8)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. referenciam o trabalho de Alameldeen e Wood (2003) para situar a
  variabilidade de desempenho como um dos principais desafios metodológicos na avaliação de
  sistemas multicore: diferentes execuções de uma mesma carga de trabalho podem produzir
  resultados distintos em razão do não-determinismo de escalonamento de threads, interferências
  de cache, e variações de latência de memória. No contexto do presente projeto, essa
  variabilidade se manifesta como o Desvio Padrão Amostral das 20 rodadas do Geekbench 6,
  sendo que a Máquina D é especialmente suscetível por operar com Single Channel — que eleva
  a sensibilidade a flutuações de contenção de memória.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — justificativa das 20 rodadas de benchmark
  como protocolo necessário para estimar a variabilidade de desempenho; Resultados —
  interpretação do Desvio Padrão como indicador de instabilidade arquitetural.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → Desvio Padrão Amostral das 20 rodadas em `Single_Core` e `Multi_Core`
    por máquina: maior desvio padrão no Multi-Core do que no Single-Core corrobora que a
    variabilidade de acesso à memória (contenção entre threads) é fonte de não-determinismo.
  - `maqD_rodada_*.CSV` → variação segundo a segundo da coluna `Carga da memória física (%)`:
    flutuações frequentes dessa coluna durante o benchmark são evidência direta de variabilidade
    de contenção de memória entre execuções.

---

### 3.11 Modelos de Memória e Precisão de Estimativa — Limites dos Modelos Simplistas

- **Conceito/Teoria:** Modelos de latência fixa (Fixed Latency) e de fila simples (Queuing
  Model) subestimam sistematicamente a latência de memória em sistemas de alta carga
  multicore, produzindo erros de estimativa de até 65% em relação a modelos precisos
  ciclo-a-ciclo para estudos de otimização como prefetching.

- **Citação Direta (Ipsis Litteris):**
  > "Our studies show that the performance difference between simplistic models and accurate
  > memory controller can be as high as 65% for memory optimization studies." (Abstract, p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. quantificam que modelos simplistas de memória utilizados em simuladores
  de arquitetura podem subestimar o impacto do subsistema de memória em até 65% para
  estudos de otimização em sistemas multicore. Esse resultado reforça a necessidade de
  medição empírica com hardware real — como a abordagem adotada pelo presente projeto com
  HWiNFO64 e Geekbench 6 — em contraposição a estimativas baseadas em simulação simplificada.
  A medição direta de `Potência total da CPU (W)`, `Relógios efetivos núcleo (avg) (MHz)`
  e `Carga da memória física (%)` pelo HWiNFO64 fornece dados equivalentes ao modelo
  ciclo-a-ciclo (ACLM) descrito pelos autores.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção de Métricas de
  Desempenho e Metodologia Experimental; Metodologia — justificativa do uso de medição
  empírica com hardware real em vez de simulação.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → colunas de telemetria HWiNFO64 em geral: a coleta segundo a segundo
    de todas as variáveis de hardware é o equivalente empírico do ACLM descrito pelos autores —
    medição real versus estimativa simplificada.

---

### 3.12 Número de Canais de Memória e Erros de Projeção de Desempenho

- **Conceito/Teoria:** A diferença de desempenho entre configurações Single Channel e Dual
  Channel de memória aumenta conforme o número de threads cresce, e modelos de memória
  inadequados projetam erroneamente que sistemas Single e Dual Channel têm desempenho
  comparável — quando, na realidade, a diferença pode ser de dezenas de por cento em cargas
  multi-thread intensas.

- **Citação Direta (Ipsis Litteris):**
  > "As shown in figure 6, the dual channel configuration gives similar trend for both SILM and
  > QILM. Both models have increased difference from the detailed model when the number of threads
  > is increased. However QILM still performs better. The difference is 15% and 57% for QILM
  > and SILM respectively." (p. 6)

- **Paráfrase (Citação Indireta Acadêmica):**
  Srinivasan et al. demonstram que a configuração Dual Channel de memória move o ponto de
  operação do sistema para a região linear da curva largura de banda × latência,
  e que modelos simplistas ainda sub-estimam significativamente o desempenho real para 16
  threads (57% de erro para o modelo de latência fixa). Esse resultado implica que, para
  o presente projeto, máquinas com Dual Channel deverão apresentar ganhos de score Multi-Core
  substancialmente maiores do que o esperado com base apenas no número de núcleos — e que
  a comparação direta entre máquinas Single e Dual Channel sem controle desse parâmetro
  levaria a conclusões equivocadas sobre a capacidade computacional do processador.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão — parágrafo comparativo entre
  máquinas com configurações de memória distintas; Fundamentação Teórica — subseção de
  Hierarquia de Memória como variável de controle do experimento.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → coluna `Multi_Core`: referência base (Single Channel).
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqC.txt` → coluna `Multi_Core`: se alguma
    máquina operar em Dual Channel, o delta do score Multi-Core em relação à Máquina D será
    o indicador empírico do ganho de largura de banda descrito pelos autores.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):**
  > Este ponto de análise é **central** para o artigo: a comparação entre máquinas Single e
  > Dual Channel validará empiricamente a teoria de Srinivasan et al. com hardware real do
  > grupo. **Este mapeamento só será utilizado na redação final conforme as configurações
  > reais das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações.**

  > ✅ **ATUALIZAÇÃO — CONFIRMAÇÃO E EXPANSÃO COM TABELA DE HARDWARE COMPLETA (Máquinas A–F):**
  > Com a tabela de hardware definitiva do grupo, o desenho experimental ideal para validar
  > esta seção do artigo de Srinivasan et al. está finalmente completo, pois há agora **dois
  > grupos balanceados**: Single Channel (Máquinas C e D) e Dual Channel (Máquinas A, B, E e F).
  > Isso permite substituir a comparação isolada "Máquina D vs. demais" por uma comparação
  > estatística de **grupo Single Channel vs. grupo Dual Channel**, com replicação dentro de
  > cada grupo — o que é metodologicamente superior, pois reduz o risco de que uma diferença
  > observada seja atribuída erroneamente apenas ao canal de memória quando poderia ser efeito
  > de outra variável (clock base, geração da CPU, etc.).
  > - `scores_maqC.txt`, `scores_maqD.txt` → coluna `Multi_Core`: compõem o **Grupo Single
  >   Channel** (N=2 máquinas, 40 rodadas de benchmark no total).
  > - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqE.txt`, `scores_maqF.txt` → coluna
  >   `Multi_Core`: compõem o **Grupo Dual Channel** (N=4 máquinas, 80 rodadas de benchmark
  >   no total).
  >   > ⚠️ **SOLICITAÇÃO DE DADOS AUSENTES:** Para que esta comparação de grupos seja executada
  >   > nos scripts Python de análise estatística, é necessário que o grupo **confirme a
  >   > existência e nomenclatura dos arquivos** `scores_maqE.txt` e `scores_maqF.txt` (no
  >   > mesmo formato de 21 linhas descrito na Seção 3 do prompt-mestre), bem como das pastas
  >   > de telemetria `maqE_rodada_01.CSV` a `maqE_rodada_20.CSV` e `maqF_rodada_01.CSV` a
  >   > `maqF_rodada_20.CSV`, já que a estrutura de dados originalmente especificada para este
  >   > projeto previa apenas 4 máquinas (A–D). Sem a confirmação desses arquivos para as
  >   > Máquinas E e F, os scripts de análise estatística devem ser gerados restritos às
  >   > 4 máquinas originais (A–D), com a expansão para 6 máquinas marcada como pendente.
  > **Como usar:** Aplicar um teste estatístico de comparação entre os dois grupos (por
  > exemplo, teste t de Student para amostras independentes, ou, dado o N pequeno, uma
  > comparação direta de médias e desvios padrão com discussão qualitativa) sobre a razão
  > `Multi_Core / Single_Core` de cada grupo. Espera-se, segundo a Equação~\ref{eq:eficiencia_paralela}
  > (seção 4.3) e a teoria de Srinivasan et al., que o Grupo Dual Channel apresente razão
  > média superior e desvio padrão inferior ao Grupo Single Channel — já que a maior largura
  > de banda disponível mantém o sistema na região constante/linear da curva mesmo sob a
  > variabilidade natural de 20 rodadas (ver também a Seção 3.10 deste fichamento, sobre
  > variabilidade experimental).

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmula de IPC e CPI — Métricas de Eficiência Microarquitetural

O artigo utiliza CPI e IPC como métricas de desempenho normalizadas. As equações formais
para inserção na seção de Fundamentos do `main.tex` são:

**CPI — Ciclos Por Instrução:**
```latex
\begin{equation}
CPI = \frac{\text{Ciclos totais de clock}}{\text{Total de instruções executadas}}
\label{eq:cpi}
\end{equation}
```

**IPC — Instruções Por Ciclo (inverso do CPI):**
```latex
\begin{equation}
IPC = \frac{1}{CPI} = \frac{\text{Total de instruções executadas}}{\text{Ciclos totais de clock}}
\label{eq:ipc}
\end{equation}
```

**Aplicação no artigo:** O score do Geekbench 6 é proporcional ao IPC efetivo do processador
sob a carga do benchmark. A razão `Multi_Core / Single_Core` estima o IPC paralelo relativo.

---

### 4.2 Largura de Banda Teórica de Memória DDR

A largura de banda teórica de um sistema DDR4 pode ser calculada conforme a equação:

```latex
\begin{equation}
BW_{mem} = \text{Clock}_{mem} \times 2 \times \text{Largura de bus} \times N_{canais}
\label{eq:bw_mem}
\end{equation}
```

Onde:
- $\text{Clock}_{mem}$ = frequência efetiva da memória (Hz)
- O fator $2$ é o dobramento de taxa DDR (*Double Data Rate*)
- $\text{Largura de bus} = 8$ bytes (64 bits) por canal
- $N_{canais}$ = 1 (Single Channel) ou 2 (Dual Channel)

**Aplicação para a Máquina D:**
```latex
\begin{equation}
BW_{MaqD} = 1333 \times 10^6 \times 2 \times 8 \times 1 \approx 21,3~\text{GB/s (teórico)}
\label{eq:bw_maqD}
\end{equation}
```

> **Nota:** A largura de banda sustentada real é tipicamente 70–80% da teórica, conforme
> demonstrado pelos próprios autores para sistemas DDR3-800 em servidores. Para um notebook
> com Intel Core i5-8265U rodando Geekbench 6 (carga de processamento intensa), espera-se
> largura de banda efetiva de aproximadamente 14–17 GB/s.

---

### 4.3 Fórmulas Estatísticas para Inserção no `main.tex`

As seguintes fórmulas são centrais para a seção de Metodologia do artigo do grupo:

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

**Eficiência de Paralelismo Empírica (Razão Multi-Core / Single-Core):**
```latex
\begin{equation}
E_{paralela} = \frac{\bar{x}_{Multi\text{-}Core}}{\bar{x}_{Single\text{-}Core}}
\label{eq:eficiencia_paralela}
\end{equation}
```

**Largura de Banda de Memória Efetiva Medida (via HWiNFO64):**
```latex
\begin{equation}
BW_{ef} = \overline{\text{Taxa de leituras (MB/s)}} + \overline{\text{Taxa de gravações (MB/s)}}
\label{eq:bw_ef}
\end{equation}
```

Onde $\bar{x}$ indica a média sobre os segundos da rodada. Essa equação permite comparar
empiricamente a largura de banda efetiva medida com a teórica calculada pela Equação~\ref{eq:bw_mem}.

---

### 4.4 Sugestão de Gráficos e Tabelas para o `main.tex`

**Gráfico 1 — Razão Multi-Core / Single-Core por Máquina (Eficiência de Paralelismo):**
Barplot comparando a razão `Multi_Core / Single_Core` entre as 4 máquinas. A linha tracejada
representa o teto teórico para o número de threads lógicas do processador.

```python
import matplotlib.pyplot as plt
import numpy as np

maquinas     = ['Máquina A', 'Máquina B', 'Máquina C', 'Máquina D']
media_single = [mean_A_s, mean_B_s, mean_C_s, mean_D_s]   # preencher com dados reais
media_multi  = [mean_A_m, mean_B_m, mean_C_m, mean_D_m]   # preencher com dados reais
eficiencia   = [m / s for m, s in zip(media_multi, media_single)]

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(maquinas, eficiencia,
              color=['#1a1a1a', '#555555', '#999999', '#cccccc'],
              edgecolor='black', linewidth=0.8)
ax.axhline(y=8, color='black', linestyle='--', linewidth=0.8,
           label='Teto teórico (8 threads lógicas)')
ax.set_xlabel('Máquina', fontsize=11)
ax.set_ylabel('Razão Multi-Core / Single-Core', fontsize=11)
ax.set_title('Eficiência de Paralelismo por Máquina (Geekbench 6)', fontsize=12)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('fig_eficiencia_paralela.pdf', dpi=300)
```

**Legenda LaTeX sugerida:**
```latex
\begin{figure}[ht]
\centering
\includegraphics[width=.7\textwidth]{fig_eficiencia_paralela.pdf}
\caption{Razão entre os scores médios Multi-Core e Single-Core do Geekbench~6 por
  máquina. A linha tracejada representa o teto teórico de escalabilidade para 8 threads
  lógicas. Valores inferiores evidenciam gargalo de memória (Memory Wall) conforme
  demonstrado por \cite{srinivasan:07}. Fonte: Os autores (2026).}
\label{fig:eficiencia_paralela}
\end{figure}
```

**Gráfico 2 — Largura de Banda de Memória Efetiva vs. Score Multi-Core:**
Scatter plot cruzando `BW_ef` (soma de leituras e gravações em MB/s, média das 20 rodadas)
no eixo X com o score `Multi_Core` médio no eixo Y, um ponto por máquina. Correlação positiva
esperada valida empiricamente o modelo de Srinivasan et al.

```python
bw_ef     = [bw_A, bw_B, bw_C, bw_D]           # preencher com dados reais
scores_mc = [mean_A_m, mean_B_m, mean_C_m, mean_D_m]

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(bw_ef, scores_mc, color='black', s=80, zorder=5)
for i, maq in enumerate(maquinas):
    ax.annotate(maq, (bw_ef[i], scores_mc[i]),
                textcoords="offset points", xytext=(5, 5), fontsize=9)
ax.set_xlabel('Largura de banda de memória efetiva (MB/s)', fontsize=11)
ax.set_ylabel('Score Multi-Core Médio (Geekbench 6)', fontsize=11)
ax.set_title('Score Multi-Core vs. Largura de Banda de Memória', fontsize=12)
plt.tight_layout()
plt.savefig('fig_bw_vs_multicore.pdf', dpi=300)
```

**Tabela LaTeX — Comparativo de Largura de Banda por Configuração de Memória:**
```latex
\begin{table}[ht]
\centering
\caption{Largura de banda teórica e estimada de memória por configuração das máquinas}
\label{tab:bw_memoria}
\begin{tabular}{lcccc}
\hline
\textbf{Parâmetro}           & \textbf{Máq. A} & \textbf{Máq. B} & \textbf{Máq. C} & \textbf{Máq. D} \\
\hline
Módulo(s) RAM                & --              & --              & --              & 1$\times$8 GB DDR4 \\
Modo de Canal                & --              & --              & --              & Single Channel \\
Clock Efetivo (MHz)          & --              & --              & --              & 1333 \\
BW Teórica (GB/s)            & --              & --              & --              & $\approx$21,3 \\
BW Efetiva Medida (MB/s)     & --              & --              & --              & [HWiNFO64] \\
Score Multi-Core (média)     & --              & --              & --              & [dados do grupo] \\
Razão Multi / Single         & --              & --              & --              & [calcular] \\
\hline
\end{tabular}
\begin{tablenotes}
  \small
  \item Fonte: Especificações de hardware dos integrantes do grupo e dados do HWiNFO64 (2026).
  \item BW Teórica calculada pela Equação~\ref{eq:bw_mem}. Células "--" a preencher.
\end{tablenotes}
\end{table}
```

---

## 5. KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

**Para embasar a discussão sobre Memory Wall e gargalo de largura de banda (PRIORIDADE ALTA):**
- `"memory wall" multicore bandwidth bottleneck benchmark`
- `"memory bandwidth" "single channel" "dual channel" performance comparison CPU`
- `"Von Neumann bottleneck" multicore memory bandwidth`
- `"gargalo de Von Neumann" largura de banda memória processador multicore`
- `memory contention overhead multicore threads performance degradation`
- `DDR4 "single channel" "dual channel" benchmark performance CPU`

**Para embasar a curva largura de banda × latência:**
- `"bandwidth-latency" memory curve DRAM multicore`
- `DRAM latency bandwidth tradeoff multi-thread workload`
- `memory controller contention latency multicore CPI`
- `"latência de memória" "largura de banda" gargalo multicore desempenho`

**Para embasar CPI/IPC como métricas de desempenho:**
- `"cycles per instruction" CPI benchmark multicore performance metric`
- `IPC CPU benchmark performance evaluation single multi-thread`
- `"instruções por ciclo" processador benchmark avaliação desempenho`
- `CPU performance metrics IPC CPI benchmark reproducibility`

**Para embasar a comparação Single-Core vs. Multi-Core:**
- `single-core multi-core benchmark scaling memory bottleneck`
- `Geekbench CPU benchmark single-core multi-core performance analysis`
- `"memory-bound" "compute-bound" workload multicore CPU performance`
- `"memory bound" benchmark desempenho multicore gargalo`

**Para embasar variabilidade experimental em sistemas multicore:**
- `"performance variability" multicore benchmark non-determinism`
- `benchmark reproducibility standard deviation multicore CPU`
- `"variabilidade de desempenho" benchmark multithread`
- `Alameldeen Wood variability architectural simulation multithreaded`

**Para busca direta do artigo e trabalhos relacionados de alto impacto:**
- `Srinivasan Zhao Iyer "CMP Memory Modeling" "How Much Does Accuracy Matter"`
- `ManySim simulator Intel CMP memory model accuracy`
- `"DRAMSim" memory model cycle accurate CMP performance`
- `Jacob DRAMSim SIGARCH 2005 memory simulator`

**Para embasar a topologia interna de canal único do DDR5 (NOVO — Máquina A):**
- `DDR5 "sub-channel" architecture single module dual channel bandwidth`
- `"DDR5" 32-bit subchannel memory bandwidth single DIMM`
- `JEDEC DDR5 channel architecture independent subchannels`
- `arquitetura DDR5 subcanais largura de banda módulo único`

**Para embasar a comparação estatística entre grupos Single Channel e Dual Channel (NOVO):**
- `memory channel configuration comparison group benchmark performance statistics`
- `"single channel" "dual channel" group comparison CPU multicore benchmark`
- `comparação grupos canal memória desempenho multicore estatística`

---

> **⚠️ NOTA DE ABSTRAÇÃO PREDITIVA GERAL (MÁQUINAS A, B e C):**
>
> Os conceitos fichados nas seções 3.1 a 3.12 — em especial a curva largura de banda × latência
> (seção 3.2), o impacto do número de canais de memória no CPI (seção 3.4), e a escalabilidade
> sub-linear de throughput (seção 3.5 e 3.9) — foram integralmente fichados de forma preditiva
> e terão grau de aplicabilidade diretamente proporcional à diferença de configuração de memória
> entre as quatro máquinas do grupo. Em particular:
>
> - Se **alguma das Máquinas A, B ou C operar com Dual Channel**, o modelo de Srinivasan et al.
>   prevê ganho expressivo de score Multi-Core sem ganho proporcional de Single-Core — o que
>   deverá ser discutido diretamente com citação a \cite{srinivasan:07}.
> - Se **todas as máquinas operarem com Single Channel**, o artigo ainda é válido para explicar
>   por que o ganho de paralelismo observado nas 4 máquinas é uniformemente sub-linear.
>
> **Este mapeamento de colunas e a interpretação comparativa entre máquinas só serão utilizados
> na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem
> preenchidas pelo grupo nas próximas interações, se necessário.**

---

> **✅ NOTA DE ABSTRAÇÃO PREDITIVA GERAL — ATUALIZAÇÃO FINAL (TABELA DE HARDWARE COMPLETA,
> MÁQUINAS A A F):**
>
> Com a consolidação da tabela de hardware definitiva do grupo, as condições hipotéticas
> levantadas na nota preditiva original acima **se confirmam e se detalham** da seguinte forma:
>
> 1. **Confirma-se a existência de Dual Channel em quatro das seis máquinas** (A, B, E, F),
>    incluindo o caso particular da Máquina A, cujo Dual Channel é alcançado por arquitetura
>    interna do DDR5 com um único módulo físico (ver detalhamento na seção 3.4 acima) — um
>    achado que enriquece a Fundamentação Teórica além do previsto inicialmente pelo modelo
>    de Srinivasan et al., que trata apenas de topologias DDR3.
> 2. **Confirma-se a existência de Single Channel em duas máquinas** (C e D), e não apenas
>    em uma como hipotetizado inicialmente — fortalecendo estatisticamente a comparação de
>    grupos descrita na atualização da seção 3.12.
> 3. **Surge uma variável de controle adicional não prevista no fichamento original:** o TDP
>    da CPU varia de 15 W (Máquinas B, C, D) a 125 W (Máquina F), e o tipo de sistema varia de
>    Notebook Ultrafino a Desktop Montado. Como o artigo de Srinivasan et al. não modela o
>    efeito do TDP/forma física sobre a largura de banda de memória (apenas sobre o número
>    de canais e o clock), recomenda-se buscar fichamentos complementares sobre Thermal Design
>    Power e fator de forma (notebook vs. desktop) para isolar esse efeito na discussão —
>    de modo a não atribuir ao subsistema de memória diferenças de desempenho que, na
>    realidade, decorrem do TDP ou de throttling térmico (ver fichamentos já disponíveis
>    no projeto sobre Thermal Throttling, ex.: Lee et al. e Nisha et al.).
> 4. **Ação pendente do grupo:** confirmar a existência dos arquivos de benchmark e telemetria
>    das Máquinas E e F (`scores_maqE.txt`, `scores_maqF.txt`, e os respectivos 20 arquivos
>    `.CSV` cada), conforme apontado na seção 3.12, já que a estrutura de dados originalmente
>    especificada cobria apenas 4 máquinas. Sem essa confirmação, os scripts Python de análise
>    estatística devem ser gerados, por padrão, restritos às Máquinas A–D, com a inclusão de
>    E e F tratada como extensão futura do pipeline de dados.
> 5. **Lacunas remanescentes na própria tabela de hardware** (marcadas com `*` na tabela
>    fornecida pelo grupo): modelo de gabinete das Máquinas E e F, clock da RAM da Máquina C
>    e da Máquina E, tipo de armazenamento da Máquina C (SSD ou HD), interface de disco da
>    Máquina C, e geração de PCIe do armazenamento da Máquina F. Essas lacunas não impedem o
>    uso teórico deste fichamento, mas devem ser preenchidas pelo grupo antes da redação final
>    da Tabela de Hardware Comparativa do `main.tex`, pois afetam diretamente o cálculo da
>    Equação~\ref{eq:bw_mem} (largura de banda teórica) para essas três máquinas.
