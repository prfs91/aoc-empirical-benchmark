> **VEREDITO DE RELEVÂNCIA:** ✅ **SIM, o artigo é útil para o nosso projeto de AOC.**
> Justificativa: embora o artigo trate de CPUs *3D-stacked* (Intel Lakefield e AMD Ryzen 7
> 5800X3D), tecnologia de empacotamento ausente nas nossas quatro máquinas reais (A, B, C e D —
> todas com arquiteturas planares 2D convencionais), o documento oferece fundamentação teórica
> de altíssima qualidade e diretamente aplicável aos pilares centrais do nosso escopo:
> *Dynamic Thermal Management* (DTM), *Thermal Throttling*, *Power Limit* (PL1/TDP), o papel da
> cache LLC/L3 no desempenho, o gargalo de banda de memória (Single-Channel vs. arquiteturas de
> maior banda) e, sobretudo, a metodologia experimental de cruzar séries temporais de
> temperatura e frequência de clock para explicar variabilidade de desempenho — exatamente o
> que faremos com os 80 arquivos `.CSV` do HWiNFO64. Portanto, o processamento do fichamento
> está autorizado e prossegue abaixo.
>
> **ATUALIZAÇÃO (rodada de revisão com hardware completo das Máquinas A, B, C, E e F):** com o
> preenchimento da tabela de hardware completa do grupo (seis máquinas: quatro notebooks e dois
> desktops montados), as notas de abstração preditiva originalmente registradas nos itens 3.4 e
> 3.12 — sobre Dual-Channel/banda de memória superior e cache L3 maior — tornam-se diretamente
> verificáveis, e novas subseções (3.13 a 3.17) foram acrescentadas ao final da Seção 3 para
> cobrir conceitos do artigo aplicáveis a componentes específicos das Máquinas A, B, C, E e F
> (microarquitetura híbrida P-core/E-core, litografia Intel 7 *vs.* Zen 3 *vs.* Zen+ 12 nm, GPU
> dedicada de alto TDP com barramento PCIe 4.0, e SSD NVMe *vs.* HDD SATA). Nenhum conteúdo
> previamente fichado foi removido ou alterado.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC (para `\begin{thebibliography}` do `main.tex`):**

```
LEE, J. Y.; SIM, C. Y.; CHOI, S. H.; CHUNG, S. W. Thermal Challenges and
Opportunities for Off-the-shelf 3D-stacked CPUs. In: 2025 IEEE/ACM
INTERNATIONAL SYMPOSIUM ON LOW POWER ELECTRONICS AND DESIGN (ISLPED), 2025.
Anais [...]. [S.l.]: IEEE, 2025. DOI: 10.1109/ISLPED65674.2025.11261778.
```

- **Código BibTeX Completo (para `sbc-template.bib`):**

```bibtex
@inproceedings{lee2025thermal,
  author    = {Lee, Jae Yoon and Sim, Chae Young and Choi, Seung Hun and Chung, Sung Woo},
  title     = {Thermal Challenges and Opportunities for Off-the-shelf {3D}-stacked {CPUs}},
  booktitle = {2025 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)},
  year      = {2025},
  publisher = {IEEE},
  doi       = {10.1109/ISLPED65674.2025.11261778},
  issn      = {979-8-3315-2710-5},
  keywords  = {3D CPU, dynamic thermal management, thermal-aware scheduling, energy efficiency}
}
```

> **Nota de proteção de siglas:** no BibTeX acima, `{3D}` e `{CPUs}` foram protegidos com chaves
> internas para impedir que o estilo `sbc.bst` capitalize incorretamente as siglas no título
> renderizado da bibliografia, conforme já praticado nos demais arquivos `.bib` do projeto.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo de Conferência (*Conference Paper*) — 2025 IEEE/ACM International
  Symposium on Low Power Electronics and Design (ISLPED 2025).
- **Instituição/Editora:** IEEE/ACM. Autoria vinculada ao Department of Computer Science and
  Engineering da Korea University (Seul, Coreia do Sul) e à Samsung Electronics (Hwaseong,
  Coreia do Sul).
- **Palavras-Chave Originais (Keywords):** 3D CPU, dynamic thermal management, thermal-aware
  scheduling, energy efficiency.
- **Resumo do Escopo Geral:** O artigo analisa as características térmicas de CPUs comerciais
  ("*off-the-shelf*") 2D e 3D-*stacked*, comparando-as em termos de desempenho (tempo de
  execução) e temperatura *on-chip*, utilizando como estudos de caso o Intel Lakefield
  (empilhamento via *microbump*) e o AMD Ryzen 7 5800X3D (empilhamento via *hybrid bonding*).
  Constatando que CPUs 3D são mais vulneráveis a problemas térmicos devido à maior densidade de
  potência e à dissipação de calor limitada, os autores propõem e avaliam duas técnicas de
  escalonamento térmico-consciente (*thermal-aware scheduling*): 1) baseada em *floorplan*
  (alocação de tarefas considerando a posição física dos núcleos no chip) e 2) baseada em
  *Adaptive Voltage Scaling* — AVS (alocação de tarefas considerando variação de processo entre
  núcleos). Os resultados demonstram redução de consumo energético de 10,3% e 12,4%,
  respectivamente, em relação ao escalonador *legacy* do Linux, mantendo desempenho equivalente.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

### 3.1 Conceito/Teoria: Dynamic Thermal Management (DTM) e Throttling Reativo

- **Citação Direta (Ipsis Litteris):** "Dynamic voltage and frequency scaling (DVFS) [9], a
  representative DTM technique, reduces CPU temperature by adjusting its voltage and clock
  frequency. However, the reduced clock frequency degrades system performance." (Página 1).

- **Paráfrase (Citação Indireta Acadêmica):** Lee et al. (2025) caracterizam o DVFS como a
  técnica representativa de gerenciamento térmico dinâmico (DTM), atuando na redução da
  temperatura do processador por meio do ajuste conjunto de tensão e frequência de clock; em
  contrapartida, essa redução de frequência acarreta inevitável degradação do desempenho do
  sistema (LEE et al., 2025, p. 1). Esse trade-off entre proteção térmica e desempenho é a
  premissa central que justifica, no nosso experimento, a investigação de quedas de clock
  registradas durante as 20 rodadas de Geekbench 6 em cada uma das quatro máquinas.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (subseção de Termodinâmica e
  Arquitetura) e Introdução, como justificativa motivacional do problema de variabilidade de
  desempenho investigado.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação sustenta o cruzamento, em cada um
  dos 80 arquivos `maq*_rodada_*.CSV`, entre `Relógios núcleo (avg) (MHz)` (clock nominal
  solicitado) e `Relógios efetivos núcleo (avg) (MHz)` (clock efetivamente entregue), além das
  colunas booleanas `Estrangulamento térmico do núcleo (avg) (Yes/No)` e `Core 0/1/2/3
  Estrangulamento térmico (Yes/No)`. Toda ocorrência de queda abrupta na coluna de clock efetivo,
  simultânea a "Yes" nas colunas de throttling, deve ser correlacionada com o score da rodada
  equivalente em `scores_maq*.txt` (`Single_Core`/`Multi_Core`), evidenciando empiricamente a
  relação causal DTM → degradação de desempenho.

---

### 3.2 Conceito/Teoria: Power Limit (PL1) e Thermal Design Power (TDP)

- **Citação Direta (Ipsis Litteris):** "Most Intel CPUs adopt power limit (PL) [14] to consume
  less power than a predefined threshold power. [...] Once the power consumption exceeds the PL
  threshold, the CPU reduces its clock frequency, resulting in lower on-chip temperature.
  However, CPU performance also decreases due to clock frequency reduction. [...] PL1 threshold
  is set to thermal design power (TDP)." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Os autores explicam que processadores Intel
  adotam o mecanismo de limite de potência (*Power Limit*, PL), cujo principal representante,
  o PL1, é configurado exatamente no valor do *Thermal Design Power* (TDP) do chip; uma vez que
  o consumo de potência instantâneo excede esse limiar, o processador reduz compulsoriamente a
  frequência de clock para conter a temperatura, com o custo direto de queda de desempenho
  (LEE et al., 2025, p. 3). Esse mecanismo é particularmente relevante para a Máquina D
  (Roberta), cujo processador Intel Core i5-8265U opera com um TDP base de 15 W (com
  *TDP-up* configurável a 25 W), regime no qual a sustentação do clock *boost* de 3,90 GHz por
  período prolongado depende diretamente da margem térmica e do PL1 disponível no perfil de
  energia do notebook.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Consumo Energético e Limites de
  Projeto) e Metodologia, ao justificar por que as 20 rodadas consecutivas de Geekbench 6 podem
  apresentar degradação progressiva de score ao longo do tempo de execução.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta diretamente a análise das colunas
  `IA: Package-Level RAPL/PBM PL1 (Yes/No)`, `Limite de potência PL1 (Static) (W)`, `Limite de
  potência PL1 (Dynamic) (W)`, `Potência total da CPU (W)` e `Limite de desempenho - Térmico
  (Yes/No)` em todos os arquivos `maq*_rodada_*.CSV`. Recomenda-se calcular, para cada máquina,
  o percentual de amostras (segundo a segundo) em que a coluna PL1 indica "Yes", confrontando
  esse percentual com o desvio padrão amostral do score Multi-Core daquela máquina em
  `scores_maq*.txt`.

---

### 3.3 Conceito/Teoria: Hierarquia de Memória — Impacto da Cache LLC/L3 no Desempenho

- **Citação Direta (Ipsis Litteris):** "A potential reason is that the Intel 3D CPU has a
  larger L2 and L3 cache size (512 KB L2 and 4 MB L3) compared to the Intel 2D CPU (256 KB L2
  and 3 MB L3), which is more beneficial for workloads with frequent cache accesses." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Lee et al. (2025) atribuem o melhor desempenho do
  Intel 3D CPU em cargas de trabalho intensivas em CPU, mesmo operando em frequência de clock
  inferior, à sua cache L2 e L3 de maior capacidade em relação ao CPU 2D de comparação; caches
  maiores reduzem a taxa de *misses* em acessos frequentes à hierarquia de memória, compensando
  parcialmente a perda de frequência (LEE et al., 2025, p. 3). Esse princípio é diretamente
  aplicável à Máquina D, cujo i5-8265U possui 6 MB de cache L3 — valor expressivo para um
  processador de classe ultrabook — sugerindo que, em cargas de trabalho com forte
  reaproveitamento de dados (como o subteste *Single-Core* do Geekbench 6), o impacto da
  limitação de banda de RAM DDR4 Single-Channel pode ser parcialmente mitigado pela maior
  capacidade de retenção de dados na LLC, reduzindo a frequência de acessos à memória principal.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia de Memória) e Resultados
  e Discussão, ao comparar os scores Single-Core entre máquinas com diferentes tamanhos de
  cache L3.

- **Mapeamento de Colunas e Arquivos de Teste:** Embora o HWiNFO64 não monitore diretamente a
  taxa de *cache misses* (métrica tipicamente capturada por contadores de desempenho de
  hardware/PMU, fora do escopo das colunas disponíveis), esta citação sustenta teoricamente a
  análise comparativa dos scores `Single_Core` de `scores_maq*.txt` entre as máquinas,
  correlacionando-os com a especificação estática de cache L3 de cada processador (a ser
  preenchida na Tabela de Hardware do `main.tex`) e com `Relógios efetivos núcleo (avg) (MHz)`
  como variável de controle.

---

### 3.4 Conceito/Teoria: Gargalo de Banda de Memória (Memory Bandwidth Bottleneck)

- **Citação Direta (Ipsis Litteris):** "The Intel 3D CPU adopts LPDDR4X-4267, which provides a
  maximum memory bandwidth of 17 GB/s [43]. In contrast, the Intel 2D CPU employs DDR4-2133,
  providing a bandwidth of 34.1 GB/s [5]. Thus, the lower bandwidth of LPDDR4X-4267 causes
  memory bottlenecks, increasing CPU wait time." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Os autores demonstram, com dados quantitativos de
  banda de memória, que mesmo uma tecnologia de memória nominalmente mais avançada
  (LPDDR4X-4267) pode produzir gargalo de desempenho quando sua banda agregada (17 GB/s) é
  inferior à de uma configuração concorrente (DDR4-2133, 34,1 GB/s), resultando em maior tempo
  de espera da CPU por dados (LEE et al., 2025, p. 3). Esse achado evidencia que a largura de
  banda efetiva — e não apenas a frequência nominal do módulo — é o fator determinante do
  gargalo de Von Neumann. No contexto da nossa Máquina D, a configuração de 8 GB DDR4 SDRAM
  1333 MHz em canal único (*Single Channel*) representa um cenário ainda mais limitado: a banda
  teórica de um canal único DDR4-1333 (aproximadamente 10,6 GB/s) é inferior até mesmo à
  configuração LPDDR4X-4267 citada pelos autores, sugerindo que workloads memory-intensive
  (análogos aos testes *gcc*, *omnetpp* e *xz* do SPEC CPU2017 usados pelos autores) tendem a
  penalizar desproporcionalmente o desempenho dessa máquina.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Gargalos de Arquitetura — Gargalo de
  Von Neumann) e Resultados e Discussão, ao explicar diferenças de score Multi-Core entre
  máquinas com diferentes configurações de canal de memória.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a análise das colunas `Relógio da
  memória (MHz)`, `Relação do relógio da memória (x)`, `Taxa de leituras (MB/s)`, `Taxa de
  gravações (MB/s)`, `Tcas (T)`, `Trcd (T)`, `Trp (T)`, `Tras (T)` e `Trc (T)` nos arquivos
  `maq*_rodada_*.CSV`. Recomenda-se calcular a banda teórica de cada configuração (canal único
  vs. dual channel, frequência efetiva) e correlacionar com o score `Multi_Core` médio de cada
  máquina em `scores_maq*.txt`.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):** Caso alguma das Máquinas A, B ou C
  > opere em configuração *Dual Channel* (dois pentes de RAM) e/ou com frequência DDR4/DDR5
  > superior a 1333 MHz, este conceito teórico — banda de memória efetiva como determinante do
  > gargalo de Von Neumann — deve ser utilizado para explicar ganhos superiores de score
  > Multi-Core nessas máquinas em relação à Máquina D. Este trecho teórico e seu respectivo
  > mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na
  > redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem
  > preenchidas pelo grupo nas próximas interações, se necessário.

  > ✅ **RESOLUÇÃO DA NOTA PREDITIVA (hardware completo confirmado):** Com a tabela de hardware
  > completa, confirma-se que a predição se concretiza com folga. A Máquina A (Raony) opera em
  > **Dual Channel DDR5-5200** (8 GB, 1x8GB — canal único fisicamente, mas tecnologia DDR5, que já
  > duplica os barramentos internos por *bank group*, elevando a banda mesmo em configuração de um
  > único pente); a Máquina B (Leandro) opera em **Dual Channel DDR4-2666** (16 GB, 2x8GB); a
  > Máquina E (Nauan) opera em **Dual Channel DDR4** (16 GB, 2x8GB); e a Máquina F (Nicolas) opera
  > em **Dual Channel DDR4-3600** (32 GB, 2x16GB) — a configuração de maior banda teórica de todo o
  > grupo. Já a Máquina C (Cinara) permanece em **Single Channel DDR4-2400** (8 GB, 1x8GB), assim
  > como a Máquina D. A banda teórica aproximada de cada configuração (calculada por
  > $BW = \text{frequência efetiva (MT/s)} \times 8\text{ bytes} \times n_{\text{canais}}$) é:
  > Máquina A ≈ 41,6 GB/s (DDR5-5200, 1 canal físico mas com *dual sub-channel* interno do DDR5);
  > Máquina B ≈ 42,7 GB/s (DDR4-2666, 2 canais); Máquina C ≈ 19,2 GB/s (DDR4-2400, 1 canal);
  > Máquina D ≈ 10,6 GB/s (DDR4-1333, 1 canal); Máquina E: a ser confirmada a frequência exata do
  > módulo (banda mínima estimada ≈ 25,6 GB/s em DDR4-1600 Dual Channel, podendo ser maior); Máquina
  > F ≈ 57,6 GB/s (DDR4-3600, 2 canais). Essa hierarquia de banda — F > B > E > A > C > D — deve ser
  > diretamente confrontada com a hierarquia de scores `Multi_Core` médios observados em
  > `scores_maq*.txt`, especialmente nos testes internos do Geekbench 6 sensíveis a banda de memória
  > (ex.: *Ray Tracer*, *PDF Renderer*, *Background Blur*), validando empiricamente o princípio de
  > Lee et al. (2025, p. 3) também fora do escopo dos CPUs 3D-stacked originalmente estudados pelos
  > autores.

---

### 3.5 Conceito/Teoria: Densidade de Potência e Empilhamento 3D como Agravante Térmico

- **Citação Direta (Ipsis Litteris):** "However, since multiple dies are stacked in a smaller
  area in the 3D structure, power density increases, causing higher on-chip temperatures [44].
  Additionally, the 3D structure exacerbates vertical (as well as horizontal) heat dissipation,
  resulting in even higher on-chip temperatures [24]." (Página 2).

- **Paráfrase (Citação Indireta Acadêmica):** Lee et al. (2025) explicam que o empilhamento
  vertical de múltiplos *dies* em uma área menor eleva a densidade de potência por unidade de
  volume, o que, somado à dificuldade adicional de dissipação de calor tanto na direção vertical
  quanto horizontal, resulta em temperaturas *on-chip* mais elevadas comparativamente a
  arquiteturas planares (2D) equivalentes (LEE et al., 2025, p. 2). Embora as quatro máquinas do
  nosso experimento utilizem exclusivamente processadores de arquitetura 2D convencional (sem
  empilhamento de *dies*), o princípio físico subjacente — relação direta entre densidade de
  potência, área de dissipação disponível e temperatura resultante — é diretamente aplicável à
  comparação entre as Máquinas A, B, C e D, uma vez que processadores com TDP mais elevado
  concentrado em uma área de silício similar tendem a exibir temperaturas mais altas e maior
  probabilidade de ativação de DTM, mesmo em design 2D.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Termodinâmica e Arquitetura), como
  fundamento físico geral para a relação potência-temperatura, antes de detalhar o caso
  específico de Thermal Throttling observado nos dados do grupo.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta o gráfico de dispersão (*scatter
  plot*) entre `Potência total da CPU (W)` (eixo X) e `CPU Inteira (°C)` / `Núcleo máximo (°C)`
  (eixo Y) para cada amostra temporal dos arquivos `maq*_rodada_*.CSV` de todas as quatro
  máquinas, permitindo visualizar empiricamente a correlação física potência-temperatura
  descrita pelos autores.

---

### 3.6 Conceito/Teoria: Leakage Power e seu Crescimento Exponencial com a Temperatura

- **Citação Direta (Ipsis Litteris):** "Even worse, since leakage power increases exponentially
  with temperature [25], the 3D structure becomes vulnerable to additional temperature rise
  caused by leakage power growth." (Página 2).

- **Paráfrase (Citação Indireta Acadêmica):** Os autores destacam um efeito de retroalimentação
  térmica crítico: a potência de fuga (*leakage power*), componente do consumo total de energia
  de um circuito CMOS independente da atividade de comutação, cresce exponencialmente com o
  aumento da temperatura, criando um ciclo de realimentação positiva em que o aumento de
  temperatura gera mais potência dissipada, que por sua vez eleva ainda mais a temperatura
  (LEE et al., 2025, p. 2). Esse fenômeno termodinâmico é um dos fatores que justificam, em
  qualquer arquitetura — 2D ou 3D —, por que o aumento do desvio padrão de temperatura ao longo
  de rodadas consecutivas de benchmark pode se acelerar de forma não linear: uma vez que a
  temperatura de uma máquina se aproxima do limiar térmico, pequenos incrementos adicionais de
  carga tendem a gerar saltos desproporcionais de potência dissipada, especialmente relevante em
  processadores ultrabook como o i5-8265U da Máquina D, cujo envelope térmico (TDP de 15 W) é
  reduzido.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Termodinâmica e Arquitetura), na
  subseção que aprofunda o mecanismo físico do Thermal Throttling, complementando a explicação
  puramente comportamental do fenômeno com seu embasamento em física de semicondutores.

- **Mapeamento de Colunas e Arquivos de Teste:** Reforça teoricamente a análise das colunas
  `Potência total da CPU (W)`, `Potência de núcleos IA (W)` e `Potência do System Agent (W)`
  confrontadas, em série temporal, com `CPU Inteira (°C)` nos arquivos `maq*_rodada_*.CSV`.
  Recomenda-se observar se o crescimento da potência total ao longo de uma rodada acompanha um
  perfil não linear (convexo) em relação ao tempo, à medida que a temperatura se aproxima do
  TjMax — evidência indireta de contribuição de *leakage power*.

---

### 3.7 Conceito/Teoria: Trade-off entre Power Limit Habilitado/Desabilitado e Desempenho

- **Citação Direta (Ipsis Litteris):** "The Intel 3D CPU w/o PL shows shorter execution times in
  both CPU-intensive and memory-intensive workloads, with reductions of 14% and 8%, on average,
  respectively. When PL is disabled, the overall performance of the Intel 3D CPU improves as
  clock frequency further increases. However, disabling PL leads to a significant rise in
  on-chip temperature." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Os autores demonstram experimentalmente que a
  remoção do limite de potência (PL) resulta em ganhos de desempenho mensuráveis — reduções de
  14% e 8% no tempo de execução para cargas intensivas em CPU e em memória, respectivamente —, à
  custa de elevação significativa da temperatura *on-chip*, que passa a exceder o limiar de
  acionamento de software (90 °C) em ambos os tipos de carga (LEE et al., 2025, p. 3). Esse
  resultado quantifica de forma direta o trade-off fundamental entre desempenho sustentado e
  segurança térmica que rege o comportamento de qualquer processador moderno operando sob
  perfis de energia distintos (ex.: modos "Economia de Energia", "Equilibrado" e "Alto
  Desempenho" do Windows 11), reforçando a necessidade metodológica de manter um perfil de
  energia padronizado nas quatro máquinas do nosso experimento, para que as comparações de score
  sejam estatisticamente válidas.

- **Onde Encaixar no Artigo LaTeX:** Metodologia, como justificativa para a padronização do
  perfil de energia e das configurações de BIOS/Windows entre as quatro máquinas antes da
  coleta de dados; Resultados e Discussão, ao interpretar diferenças de desempenho atribuíveis a
  diferentes políticas de potência entre fabricantes/modelos de notebook.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a comparação cruzada entre `Limite de
  potência PL1 (Dynamic) (W)`, `Limite de potência PL2 (Dynamic) (W)`, `Potência total da CPU
  (W)` e `Núcleo máximo (°C)` ao longo das 20 rodadas de cada `maq*_rodada_*.CSV`, permitindo
  identificar se alguma máquina opera com PL1 anormalmente baixo (sinal de perfil de energia
  restritivo), o que explicaria scores inferiores mesmo com hardware nominalmente comparável.

---

### 3.8 Conceito/Teoria: Métrica de Desempenho — Tempo de Execução como Proxy de Throughput

- **Citação Direta (Ipsis Litteris):** "we analyze the thermal characteristics of off-the-shelf
  2D and 3D CPUs, comparing them in terms of performance and on-chip temperature." (Resumo,
  Página 1).

- **Paráfrase (Citação Indireta Acadêmica):** A metodologia adotada pelos autores estabelece o
  tempo de execução (*execution time*) de benchmarks padronizados (SPECrate, do SPEC CPU2017)
  como métrica primária de desempenho, sempre analisada em conjunto com a temperatura *on-chip*
  correspondente — nunca isoladamente (LEE et al., 2025, p. 1). Esse princípio metodológico é
  diretamente análogo ao adotado no presente trabalho: os scores sintéticos `Single_Core` e
  `Multi_Core` do Geekbench 6 funcionam como proxies de desempenho (inversamente relacionados ao
  tempo de execução das cargas de trabalho internas do benchmark), e sua análise deve ser
  sempre acompanhada da telemetria térmica e energética simultânea capturada pelo HWiNFO64, e
  não interpretada de forma isolada.

- **Onde Encaixar no Artigo LaTeX:** Metodologia, na justificativa da escolha de cruzar os dados
  de `scores_maq*.txt` com os 80 arquivos `.CSV` de telemetria, em vez de analisar apenas os
  scores finais do Geekbench 6.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a arquitetura geral do *pipeline* de
  análise estatística do grupo: para cada rodada `XX` de cada máquina, o score em
  `scores_maq*.txt` (linha `XX`) deve ser associado ao arquivo de telemetria correspondente
  `maq*_rodada_XX.CSV`, permitindo o cálculo de métricas derivadas como desempenho por Watt e
  IPC relativo (ver itens 3.9 e 3.10 a seguir).

---

### 3.9 Conceito/Teoria: Eficiência Microarquitetural — Desempenho por Watt

- **Citação Direta (Ipsis Litteris):** "When PL is disabled, the overall performance of the
  Intel 3D CPU improves as clock frequency further increases. However, disabling PL leads to a
  significant rise in on-chip temperature. [...] These high on-chip temperatures increase
  leakage power, which further raises the on-chip temperature." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Ao demonstrar que o ganho de desempenho obtido com
  a remoção do limite de potência é proporcionalmente menor do que o aumento de potência e
  temperatura resultante (devido ao efeito adicional do *leakage power*), os autores ilustram,
  de forma implícita, a perda de eficiência energética (desempenho por Watt) que ocorre quando
  um processador é levado a operar fora de seus limites de projeto (LEE et al., 2025, p. 3).
  Esse princípio fundamenta a métrica de Desempenho por Watt proposta no escopo deste trabalho:
  ao dividir o score do Geekbench 6 pela potência média consumida durante a rodada, é possível
  comparar objetivamente a eficiência energética relativa entre as Máquinas A, B, C e D,
  independentemente de seus TDPs nominais distintos.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão, na subseção dedicada à Eficiência
  Microarquitetural (Desempenho por Watt), conforme já previsto na estrutura teórica do projeto.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta diretamente o cálculo:

  $$\text{Desempenho por Watt} = \frac{\text{Score}_{\text{Multi\_Core}}}{\overline{P}_{\text{CPU}}}$$

  onde $\text{Score}_{\text{Multi\_Core}}$ é extraído de `scores_maq*.txt` (coluna `Multi_Core`
  da rodada correspondente) e $\overline{P}_{\text{CPU}}$ é a média da coluna `Potência total da
  CPU (W)` no arquivo `maq*_rodada_*.CSV` da mesma rodada.

---

### 3.10 Conceito/Teoria: IPC Relativo — Relação entre Clock Efetivo e Desempenho Final

- **Citação Direta (Ipsis Litteris):** "Despite the lower clock frequency, the Intel 3D CPU w/
  PL shows better performance. A potential reason is that the Intel 3D CPU has a larger L2 and
  L3 cache size [...] which is more beneficial for workloads with frequent cache accesses."
  (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Este resultado é particularmente relevante para a
  discussão de IPC (*Instructions Per Cycle*) relativo: os autores demonstram que um processador
  operando em frequência de clock efetivamente inferior (2,42 GHz vs. 3,1 GHz) ainda pode
  superar seu concorrente em desempenho absoluto, evidenciando que a frequência de clock,
  isoladamente, não determina o desempenho final — a eficiência por ciclo (influenciada pela
  hierarquia de cache, largura de pipeline e demais fatores microarquiteturais) é igualmente
  determinante (LEE et al., 2025, p. 3). Esse achado justifica, no nosso experimento, a
  necessidade de calcular um indicador de "IPC relativo" aproximado — a razão entre o score do
  Geekbench 6 e o clock efetivo médio durante a rodada — em vez de assumir uma relação linear
  direta entre clock e desempenho ao comparar máquinas com microarquiteturas distintas.

- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão, na subseção de Eficiência
  Microarquitetural (IPC Relativo), complementando a análise de Desempenho por Watt.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta o cálculo:

  $$\text{IPC}_{\text{relativo}} = \frac{\text{Score}_{\text{Single\_Core ou Multi\_Core}}}{\overline{f}_{\text{efetivo}}}$$

  onde $\overline{f}_{\text{efetivo}}$ é a média da coluna `Relógios efetivos núcleo (avg)
  (MHz)` extraída do arquivo `maq*_rodada_*.CSV` correspondente à rodada cujo score está sendo
  analisado em `scores_maq*.txt`.

---

### 3.11 Conceito/Teoria: Threshold Temperature como Gatilho Formal do DTM

- **Citação Direta (Ipsis Litteris):** "Software threshold temperature refers to the predefined
  temperature limit at which software-level thermal management techniques are invoked. In
  general, the software threshold temperature for CPUs ranges between 85°C and 95°C." (Nota de
  rodapé 1, Página 2).

- **Paráfrase (Citação Indireta Acadêmica):** Os autores definem formalmente o conceito de
  temperatura limiar de software (*software threshold temperature*) como o valor predefinido
  pelo fabricante/firmware a partir do qual técnicas de gerenciamento térmico em nível de
  *software* — incluindo DVFS e *thermal throttling* — são automaticamente acionadas, situando
  essa faixa, para CPUs convencionais, entre 85 °C e 95 °C (LEE et al., 2025, p. 2). Esse valor
  é tipicamente associado, na literatura e na prática de monitoramento de hardware, ao parâmetro
  TjMax (*Temperature Junction Maximum*) divulgado pelos fabricantes de processadores, e serve
  como referência objetiva para definir, em nossa análise estatística, o limiar a partir do qual
  uma amostra de temperatura registrada pelo HWiNFO64 deve ser classificada como "em risco
  iminente de throttling", mesmo nas amostras em que a coluna booleana de throttling ainda não
  tenha sido acionada.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Termodinâmica e Arquitetura), e
  Metodologia, na definição operacional do limiar térmico de referência usado na análise dos
  dados coletados.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta o uso conjunto da coluna `Distância do
  núcleo para TjMAX (avg) (°C)` (que informa diretamente a margem remanescente até o limiar
  crítico do fabricante) com `CPU Inteira (°C)` e `Núcleo máximo (°C)` nos arquivos
  `maq*_rodada_*.CSV`. Recomenda-se sobrepor, nos gráficos de série temporal de temperatura, uma
  linha horizontal de referência representando o TjMax específico de cada processador (a ser
  confirmado para as Máquinas A, B e C; já estimável para a Máquina D a partir da própria coluna
  de distância ao TjMax).

---

### 3.12 Conceito/Teoria: Banda de Memória de Alta Capacidade (HBM/Dual-Channel) como Mitigador de Gargalo

- **Citação Direta (Ipsis Litteris):** "This performance improvement is primarily attributed to
  the additional 64 MB V-Cache, leading to reduced LLC misses. Therefore, memory stalls occur
  less frequently, resulting in performance enhancement." (Página 4).

- **Paráfrase (Citação Indireta Acadêmica):** Ao analisar o AMD Ryzen 7 5800X3D em cargas de
  trabalho intensivas em memória, os autores atribuem a melhoria de desempenho observada (18%
  de redução no tempo de execução) à cache *Last Level Cache* (LLC) adicional de 64 MB
  proporcionada pela tecnologia V-Cache, que reduz a frequência de *misses* na LLC e,
  consequentemente, diminui o número de *memory stalls* (períodos de espera da CPU por dados
  vindos da memória principal) (LEE et al., 2025, p. 4). Esse princípio — cache adicional como
  mitigador do gargalo de Von Neumann em cargas memory-bound — é diretamente transponível,
  embora em escala muito menor, para qualquer comparação de cache L3 entre as Máquinas A, B, C
  e D, especialmente em cargas de trabalho do tipo Multi-Core do Geekbench 6, que tendem a gerar
  maior pressão sobre a hierarquia de memória compartilhada.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia de Memória), reforçando o
  papel da cache L3 já discutido no item 3.3, com ênfase adicional no conceito de *memory
  stalls*.

- **Mapeamento de Colunas e Arquivos de Teste:** Reforça a recomendação de cruzar o tamanho
  estático de cache L3 de cada processador (Tabela de Hardware do `main.tex`) com o score
  `Multi_Core` médio de `scores_maq*.txt` e, secundariamente, com `Taxa de leituras (MB/s)` e
  `Taxa de gravações (MB/s)` dos arquivos `maq*_rodada_*.CSV`, como indicador indireto de
  intensidade de tráfego em memória principal (uma taxa de leitura/gravação elevada e sustentada
  pode sinalizar maior incidência de *misses* na cache L3).

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C):** Se alguma das Máquinas A, B ou C
  > possuir cache L3 sensivelmente maior que os 6 MB da Máquina D, este conceito deve
  > fundamentar a explicação de eventual vantagem de score Multi-Core dessa máquina, mesmo sob
  > clock nominal comparável. Este trecho teórico e seu respectivo mapeamento de colunas foram
  > devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as
  > configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas
  > próximas interações, se necessário.

  > ✅ **RESOLUÇÃO DA NOTA PREDITIVA (hardware completo confirmado):** A predição se confirma
  > integralmente. As Máquinas A (Raony) e B (Leandro) possuem **12 MB de cache L3**, o dobro da
  > Máquina D (6 MB); a Máquina C (Cinara) possui apenas **4 MB**, a menor de todo o grupo; e as
  > duas máquinas desktop apresentam os maiores valores absolutos: Máquina E (Nauan) com **16 MB**
  > e Máquina F (Nicolas) com **24 MB** — quatro vezes a capacidade da Máquina D. Essa amplitude
  > (4 MB a 24 MB) permite, agora, transformar a correlação cache-desempenho discutida por
  > Lee et al. (2025) em uma análise de regressão qualitativa real entre tamanho de LLC e score
  > `Single_Core`/`Multi_Core` ao longo de seis pontos de dados distintos, em vez de uma comparação
  > binária hipotética. É esperado, segundo o princípio fichado nesta seção, que a Máquina C
  > (4 MB de cache, a menor do grupo, combinada com a já discutida limitação de Single Channel
  > DDR4-2400) apresente a maior incidência relativa de *memory stalls* — e, consequentemente, a
  > maior penalização proporcional no score `Multi_Core` quando comparada ao seu desempenho
  > `Single_Core` — entre as seis máquinas do experimento.

---

### 3.13 Conceito/Teoria: Núcleos Heterogêneos (P-Core/E-Core) e Densidade de Potência Localizada

- **Citação Direta (Ipsis Litteris):** "The compute die consists of one performance core
  (Sunny Cove) and four low-power cores (Tremont) [...] Since the Intel 3D CPU has heterogeneous
  cores, we focus on the performance core, as it is more prone to thermal problems." (Páginas 2
  e 3).

- **Paráfrase (Citação Indireta Acadêmica):** Lee et al. (2025) descrevem o Intel Lakefield como
  um processador de núcleos heterogêneos, combinando um núcleo de desempenho (*performance
  core*, microarquitetura Sunny Cove) com quatro núcleos de baixo consumo (*low-power cores*,
  microarquitetura Tremont); os autores justificam o foco analítico no núcleo de desempenho
  precisamente por ele concentrar a maior densidade de potência do chip e, consequentemente, ser
  o mais vulnerável a problemas térmicos (LEE et al., 2025, p. 2–3). Esse princípio de
  heterogeneidade de núcleos — área pequena e alta frequência para núcleos de desempenho,
  versus área maior (relativamente) e baixa frequência para núcleos de eficiência — é
  diretamente aplicável às Máquinas A, B e F do nosso grupo, todas equipadas com arquitetura
  híbrida Intel *Performance-cores* (P-cores) e *Efficient-cores* (E-cores): a Máquina A
  (i5-13420H, Raptor Lake-H) combina 4 P-cores e 4 E-cores; a Máquina B (i5-1334U, Raptor Lake-P)
  combina 2 P-cores e 8 E-cores; e a Máquina F (i5-14600KF, Raptor Lake) combina 6 P-cores e 8
  E-cores. Em todas elas, é esperado — por analogia direta ao Sunny Cove do Lakefield — que os
  P-cores concentrem a maior parte do consumo de potência instantâneo e, portanto, exibam as
  temperaturas individuais mais altas e a maior propensão a throttling localizado durante o
  subteste *Single-Core* do Geekbench 6, que tende a ser escalonado preferencialmente para um
  único P-core pelo *Thread Director* da Intel.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Paralelismo a Nível de Instrução e
  Thread — subseção de arquiteturas heterogêneas multicore) e Resultados e Discussão, ao
  interpretar diferenças de temperatura por núcleo nas Máquinas A, B e F.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a análise individualizada das colunas
  `Core 0 (°C)` a `Core 3 (°C)` (e, havendo telemetria por núcleo adicional disponibilizada pelo
  HWiNFO64 para CPUs com mais de 4 núcleos monitorados, as colunas equivalentes para núcleos 4 a
  13 nas Máquinas A, B e F) confrontadas com `Core 0 T0/T1 Uso (%)` a `Core 3 T0/T1 Uso (%)` nos
  arquivos `maq*_rodada_*.CSV`. Recomenda-se verificar se, nas Máquinas A, B e F, a dispersão de
  temperatura entre núcleos (desvio padrão *intra-chip*, calculado a cada amostra temporal) é
  estatisticamente maior do que nas Máquinas C e D (núcleos homogêneos), validando empiricamente
  o princípio de concentração de potência em núcleos de desempenho descrito pelos autores.

---

### 3.14 Conceito/Teoria: Litografia/Processo de Fabricação como Determinante de Densidade de Potência

- **Citação Direta (Ipsis Litteris):** "The compute die [...] fabricated with Intel's 10 nm+
  process technology. [...] fabricated with TSMC's 7 nm process technology." (Página 2).

- **Paráfrase (Citação Indireta Acadêmica):** Ao especificar, para cada *die* analisado, o nó de
  processo litográfico exato (10 nm+ da Intel para o compute die do Lakefield; 7 nm da TSMC para
  o CCD do Ryzen 7 5800X3D), Lee et al. (2025) estabelecem implicitamente a litografia como
  variável estrutural determinante da densidade de potência e, consequentemente, do
  comportamento térmico do chip — processos mais avançados (menor nó) permitem maior densidade
  de transistores por área, o que tanto viabiliza mais núcleos/cache no mesmo *footprint* quanto
  intensifica o desafio de dissipação de calor por unidade de área (LEE et al., 2025, p. 2). Esse
  princípio fundamenta diretamente a comparação entre as seis máquinas do grupo, que abrangem
  três litografias distintas: **Intel 7** (equivalente a ~10 nm aprimorado, usado nas Máquinas A,
  B e F — i5-13420H, i5-1334U e i5-14600KF, todos Raptor Lake), **Zen 3 em 7 nm TSMC** (Máquina E
  — Ryzen 5 5500) e **Zen+ em 12 nm** (Máquina C — Ryzen 5 3500U), além da litografia mais antiga
  do grupo, **14 nm** (Máquina D — Whiskey Lake-U). Espera-se, com base no princípio do artigo,
  que a Máquina D — litografia menos avançada do grupo — exiba a maior dificuldade relativa em
  sustentar clocks de *boost* sob carga prolongada dentro de seu envelope de TDP de 15 W, dado
  que processos mais antigos tendem a apresentar maior potência de fuga (*leakage*) e menor
  eficiência energética por transistor.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Eficiência Microarquitetural) e
  Metodologia, na tabela comparativa de hardware, ao justificar a inclusão da coluna de
  litografia como variável explicativa de desempenho térmico.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta o cruzamento da especificação estática
  de litografia de cada processador (Tabela de Hardware do `main.tex`) com a série temporal de
  `CPU Inteira (°C)`, `Núcleo máximo (°C)` e `Potência total da CPU (W)` extraída dos arquivos
  `maq*_rodada_*.CSV` de cada máquina. Recomenda-se calcular, para cada litografia representada
  no grupo (14 nm, 12 nm, 7 nm e Intel 7), a temperatura média normalizada pelo TDP nominal
  ($\overline{T}_{\text{CPU}} / \text{TDP}$), permitindo comparar objetivamente a eficiência
  térmica por watt de projeto entre nós de processo distintos.

---

### 3.15 Conceito/Teoria: GPU Dedicada de Alto TDP e Interface PCIe como Fator de Carga Térmica do Sistema

- **Citação Direta (Ipsis Litteris):** "Most Intel CPUs adopt power limit (PL) [14] to consume
  less power than a predefined threshold power. Especially, PL plays an important role in 3D
  CPUs to prevent overheating, since 3D CPUs normally exhibit higher on-chip temperature due to
  their increased power density." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Embora o trecho original trate especificamente do
  PL como mecanismo de proteção térmica do *die* da CPU, o princípio subjacente — de que o
  orçamento térmico de um sistema é compartilhado e limitado, e que componentes adicionais de
  alta potência intensificam a pressão sobre esse orçamento — generaliza-se diretamente ao
  conjunto CPU+GPU em sistemas com GPU dedicada (LEE et al., 2025, p. 3). Esse princípio é
  central para interpretar as Máquinas A (RTX 4050 Laptop, PCIe 4.0 x8), E (Radeon RX 7600, PCIe
  4.0 x8) e F (RTX 3050 8GB, PCIe 4.0 x8), nas quais a GPU dedicada compete por espaço térmico e,
  em notebooks (Máquina A), por orçamento de potência total do chassi com a própria CPU — efeito
  conhecido na literatura como *power/thermal budget sharing*. Já a Máquina D, com GPU dedicada
  de baixo TDP (MX130) e interface mais restrita (PCIe 3.0 x4), representa o extremo oposto do
  espectro: a GPU dedicada de baixo consumo praticamente não compete termicamente com a CPU, mas
  também oferece capacidade de processamento gráfico desprezível para cargas paralelas.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Consumo Energético e Limites de
  Projeto), como extensão do conceito de Power Limit do item 3.2 para o nível de sistema
  completo (CPU+GPU), e Metodologia, ao registrar a presença/ausência de GPU dedicada como
  variável de controle relevante para a interpretação dos dados de potência total do sistema.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a análise conjunta das colunas
  `Potência total da CPU (W)`, `Potência das linhas GPU (avg) (W)`, `GPU Core (NVVDD) Saida de
  Energia (W)`, `Potência total do sistema (W)` e `Velocidade do link PCIe (GT/s)` nos arquivos
  `maq*_rodada_*.CSV` das Máquinas A, E e F (as únicas com GPU dedicada de TDP relevante). Para a
  Máquina A (notebook com GPU dedicada de alto desempenho), recomenda-se verificar se há queda de
  `Relógios efetivos núcleo (avg) (MHz)` da CPU simultânea a picos de `Carga do núcleo da GPU
  (%)`, evidência indireta de compartilhamento de orçamento térmico/energético entre CPU e GPU
  dentro do chassi compacto do notebook gamer — fenômeno que não ocorre estruturalmente nos
  desktops montados E e F, cujas fontes de alimentação e dissipadores são fisicamente
  independentes para CPU e GPU.

---

### 3.16 Conceito/Teoria: Armazenamento (SSD NVMe vs. HDD SATA) como Fator Externo de Variabilidade

- **Citação Direta (Ipsis Litteris):** "Since memory-intensive workloads involve more frequent
  memory accesses [57], we expected the PoP memory of the Intel 3D CPU to reduce memory access
  latency, leading to performance improvement. However, the Intel 3D CPU w/ PL exhibits lower
  performance than the Intel 2D CPU, potentially due to memory bandwidth difference." (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Embora os autores tratem exclusivamente de latência
  e banda da memória principal (DRAM), o raciocínio metodológico empregado — atribuir
  diferenças de desempenho em cargas com acesso frequente a um nível de armazenamento a
  limitações de latência/banda desse subsistema — é diretamente extensível, por analogia
  estrutural da hierarquia de memória, ao subsistema de armazenamento secundário (Patterson e
  Hennessy, 2014, *apud* discussão geral de hierarquia de memória). Esse princípio justifica por
  que a Máquina D, único equipamento do grupo com armazenamento em **HDD SATA mecânico
  (Western Digital Blue, 1TB, 5400 RPM)**, é a mais suscetível a *I/O stalls* durante o
  carregamento inicial do executável do Geekbench 6 e de seus módulos de teste, ao passo que as
  Máquinas A, B e C utilizam **SSD NVMe** (interfaces PCIe Gen 4.0 x4, Gen 3.0 x4 e Gen 3.0 x4,
  respectivamente) e a Máquina F utiliza **dois SSDs NVMe M.2** em configuração que sugere
  possível uso em RAID ou separação SO/dados — ambas reduzindo drasticamente a latência de
  acesso a disco em relação ao HDD mecânico da Máquina D. A Máquina E, com **SSD SATA de 120 GB**
  combinado a um HDD de 1TB, ocupa posição intermediária: o SSD SATA, embora não mecânico,
  ainda opera no barramento SATA III (6 Gbps), com latência superior ao NVMe via PCIe.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia de Memória — subseção de
  velocidade de armazenamento), explicitamente prevista no escopo teórico do projeto ("HD SATA
  vs. SSD NVMe no carregamento dos testes"), e Metodologia, ao registrar o tipo de
  armazenamento de cada máquina como variável de controle para o tempo de carregamento (*loading
  time*) do benchmark, que não compõe o score final do Geekbench 6, mas pode influenciar a
  duração total da sessão de coleta.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a análise das colunas `Taxa de leituras
  (MB/s)`, `Taxa de gravações (MB/s)`, `Atividade de leitura (%)`, `Atividade de gravação (%)` e
  `Temperatura do disco (°C)` nos arquivos `maq*_rodada_*.CSV`, especificamente nos primeiros
  segundos de cada rodada (momento de carregamento do executável do Geekbench 6 a partir do
  disco). Recomenda-se comparar o pico de `Taxa de leituras (MB/s)` no início de cada rodada
  entre a Máquina D (HDD SATA, pico esperado próximo a ~100–150 MB/s, limite físico de discos
  mecânicos 5400 RPM) e as demais máquinas com SSD NVMe (pico esperado de centenas a milhares de
  MB/s, a depender da geração PCIe), evidenciando empiricamente o gargalo de armazenamento como
  fator de variabilidade entre máquinas — mesmo não impactando diretamente o score *compute* do
  Geekbench 6, que é executado preferencialmente em memória RAM após o carregamento inicial.

---

### 3.17 Conceito/Teoria: Conjunto de Instruções Avançadas (SIMD) como Multiplicador de Carga Térmica

- **Citação Direta (Ipsis Litteris):** "For CPU-intensive workloads, the Intel 3D CPU w/ PL
  exhibits shorter execution time than the Intel 2D CPU by 3%, on average. [...] the average peak
  on-chip temperature of the Intel 3D CPU w/ PL among CPU-intensive workloads reaches 91°C."
  (Página 3).

- **Paráfrase (Citação Indireta Acadêmica):** Embora o artigo não detalhe o conjunto de
  instruções SIMD (*Single Instruction, Multiple Data*) utilizado nas cargas de trabalho do
  SPECrate, a correlação que os autores estabelecem entre cargas CPU-intensivas e picos de
  temperatura particularmente elevados (91 °C, próximo ao limiar de 90 °C) é consistente com a
  literatura geral de microarquitetura, segundo a qual instruções vetoriais avançadas (AVX,
  AVX2, FMA3) processam múltiplos dados por ciclo de clock, elevando substancialmente a
  densidade de potência instantânea dos núcleos de execução em relação a instruções escalares
  convencionais (LEE et al., 2025, p. 3, por extensão analítica). Esse princípio é diretamente
  relevante para diferenciar o comportamento térmico esperado entre as máquinas do grupo: as
  Máquinas A, B, D e F (processadores Intel com **Intel DL Boost/VNNI**, exceto a D que possui
  apenas **FMA3**) e a Máquina E (AMD, **FMA3**) possuem capacidades vetoriais distintas, sendo
  esperado que o subteste de Machine Learning do Geekbench 6 (que tipicamente explora VNNI
  quando disponível) gere picos de potência e temperatura proporcionalmente mais acentuados nas
  Máquinas A, B e F do que na Máquina C (Ryzen 5 3500U, sem FMA3 listado nas instruções
  disponíveis, apenas AVX/AVX2/BMI2), refletindo diretamente na coluna de potência por núcleo
  durante esse subteste específico.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Termodinâmica e Arquitetura), como
  complemento qualitativo à discussão de densidade de potência (item 3.5), relacionando o
  conjunto de instruções suportado por cada CPU ao comportamento térmico observado durante
  subtestes específicos do Geekbench 6.

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta a observação de picos localizados (não
  a média da rodada completa) nas colunas `Potência de núcleos IA (W)`, `CPU Inteira (°C)` e
  `Core 0/1/2/3 (°C)` durante os intervalos de tempo correspondentes aos subtestes de *Machine
  Learning* e *Ray Tracer* do Geekbench 6 (identificáveis pelo timestamp aproximado dentro de
  cada arquivo `maq*_rodada_*.CSV`, cruzado com a duração documentada de cada subteste). Esta
  análise é qualitativa, já que o HWiNFO64 não identifica diretamente qual instrução SIMD está
  sendo executada a cada instante — a inferência é feita exclusivamente pela correlação temporal
  entre o subteste em execução e o comportamento da telemetria de potência/temperatura.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmulas Matemáticas/Físicas em LaTeX Puro

O artigo não apresenta equações matemáticas formais explícitas (não há blocos de equação
numerados no corpo do texto); os resultados são reportados em forma de percentuais de redução/
aumento de tempo de execução e temperatura, extraídos diretamente dos gráficos de barra (Fig. 2
a Fig. 8). Não havendo equação original a transcrever, seguem, em conformidade com a diretriz de
rigor teórico do projeto (Seção 5 das instruções gerais), as equações clássicas de potência
dinâmica CMOS e de potência de fuga mencionadas implicitamente pelos autores na Página 2
(relação leakage-temperatura) e na Página 5 (relação tensão-potência via CPPC), e que devem ser
formalmente apresentadas na Fundamentação Teórica do nosso artigo:

**Potência dinâmica em circuitos CMOS** (citada implicitamente na Página 5: *"dynamic power
consumption is proportional to the square of the supply voltage"*):

$$P_{din} = \alpha \cdot C \cdot V_{DD}^{2} \cdot f$$

onde $\alpha$ é o fator de atividade de comutação, $C$ é a capacitância de carga, $V_{DD}$ é a
tensão de alimentação e $f$ é a frequência de operação.

**Média Aritmética** (a ser utilizada na análise estatística dos scores e da telemetria,
conforme exigência metodológica do projeto):

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**Desvio Padrão Amostral** (a ser utilizado para quantificar a variabilidade das 20 rodadas de
cada máquina, conforme exigência metodológica do projeto):

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

> **Nota de rigor teórico:** as duas últimas fórmulas (Média Aritmética e Desvio Padrão
> Amostral) não constam no artigo de Lee et al. (2025), mas são incluídas aqui por exigência
> direta da Seção 5 das diretrizes gerais do projeto, que solicita sua presença formal em
> LaTeX para justificar a análise estatística do grupo. Já a fórmula de potência dinâmica CMOS é
> uma equação clássica e consolidada da literatura de Arquitetura de Computadores e
> microeletrônica digital, citada para formalizar a relação tensão-potência mencionada
> textualmente pelos autores na Página 5.

### 4.2 Sugestão de Gráficos/Tabelas Correspondentes

1. **Gráfico de barras com hastes de erro (Tempo de execução / Score por máquina)** — análogo às
   Figuras 2 e 4 do artigo (Páginas 3 e 4): substituir "tempo de execução" pelos scores
   `Single_Core` e `Multi_Core` médios de `scores_maq*.txt`, com hastes de erro representando o
   desvio padrão amostral das 20 rodadas, em tons de cinza/hachura conforme padrão SBC.

2. **Gráfico de barras com hastes de erro (Temperatura média on-chip por máquina)** — análogo às
   Figuras 3 e 6 do artigo: barplot com a média de `CPU Inteira (°C)` por máquina ao longo das
   20 rodadas, com a haste de erro representando a temperatura de pico (`Núcleo máximo (°C)`)
   observada, replicando a lógica de "*the error bars denote the peak on-chip temperature*"
   utilizada pelos autores em todas as suas figuras de temperatura.

3. **Gráfico de série temporal duplo (Temperatura e Clock vs. Tempo)** — análogo à Figura 5 do
   artigo (Página 4), que sobrepõe clock efetivo e temperatura on-chip ao longo do tempo de uma
   única execução: plotar, para uma rodada representativa de cada máquina, `CPU Inteira (°C)` e
   `Relógios efetivos núcleo (avg) (MHz)` em dois eixos Y sobrepostos ao longo do `Time`,
   marcando com uma linha vertical pontilhada o instante em que `Estrangulamento térmico do
   núcleo (avg)` muda de "No" para "Yes" — replicando a anotação "*DTM invoked*" usada pelos
   autores na Figura 5.

4. **Gráfico de dispersão (Potência vs. Temperatura)** — fundamentado na relação física discutida
   no item 3.5/3.6 deste fichamento: *scatter plot* de `Potência total da CPU (W)` (eixo X)
   contra `CPU Inteira (°C)` (eixo Y), uma nuvem de pontos por máquina, evidenciando
   qualitativamente a correlação potência-temperatura em condições reais de operação.

5. **Tabela comparativa de Desempenho por Watt e IPC Relativo entre as quatro máquinas** —
   inspirada na lógica de comparação entre condições experimentais (Intel 2D / 3D w/ PL / 3D w/o
   PL) das Tabelas implícitas nas Figuras 2-3 e 4-6 do artigo: montar, no `main.tex`, uma tabela
   com colunas Máquina, Score Multi-Core médio, Potência média (W), Desempenho/Watt e IPC
   Relativo, calculados conforme as fórmulas dos itens 3.9 e 3.10 deste fichamento.

6. **Gráfico de dispersão (Banda de Memória Teórica vs. Score Multi-Core) — seis máquinas** —
   fundamentado na resolução da nota preditiva do item 3.4: *scatter plot* com a banda teórica de
   RAM (eixo X, calculada conforme a fórmula apresentada na resolução do item 3.4) contra o score
   `Multi_Core` médio (eixo Y) das seis máquinas, permitindo visualizar diretamente a relação
   entre topologia/frequência de memória e desempenho agregado discutida por Lee et al. (2025).

7. **Gráfico de barras agrupadas (Temperatura por Núcleo — Máquinas Híbridas P/E-core)** —
   fundamentado no item 3.13: barplot com `Core 0 (°C)` a `Core 3 (°C)` (e núcleos adicionais
   monitorados, se disponíveis no log) para uma rodada representativa das Máquinas A, B e F,
   evidenciando visualmente a assimetria térmica entre P-cores e E-cores prevista pela analogia
   com o núcleo de desempenho Sunny Cove do Intel Lakefield discutido no artigo.

---

## 5. SUGESTÕES DE BUSCA BIBLIOGRÁFICA COMPLEMENTAR (Google Acadêmico)

Para triangular e reforçar os conceitos fichados acima com referências adicionais de alto
impacto, sugerem-se as seguintes strings de busca:

**Em inglês:**
- `"dynamic thermal management" CPU "clock frequency" performance degradation survey`
- `"power limit" PL1 PL2 Intel "thermal design power" throttling`
- `"3D stacked" CPU thermal characterization on-chip temperature`
- `"last level cache" LLC size impact memory-bound workload performance`
- `"leakage power" temperature exponential CMOS dependence`
- `"software threshold temperature" TjMax CPU throttling firmware`
- `"memory bandwidth bottleneck" DDR4 single channel CPU performance`

**Em português:**
- `"gerenciamento térmico dinâmico" processador desempenho frequência`
- `"limite de potência" TDP throttling processador notebook`
- `"empilhamento 3D" processador temperatura caracterização térmica`
- `"cache de último nível" tamanho desempenho carga intensiva memória`
- `"potência de fuga" temperatura dependência exponencial CMOS`
- `"gargalo de banda de memória" DDR4 canal único desempenho processador`
- `TjMax temperatura limite estrangulamento térmico firmware processador`

---

*Fichamento elaborado em conformidade com as Diretrizes de Fichamento de AOC do projeto
UFPA — Campus Tucuruí (2026). Nenhum dado quantitativo foi inventado; todas as citações,
percentuais, temperaturas e frequências refletem estritamente o conteúdo original do artigo de
Lee, Sim, Choi e Chung (2025), ISLPED 2025.*

> **Histórico de revisão:** versão atualizada com a inclusão das especificações completas de
> hardware das Máquinas A, B, C, E e F. Foram acrescentadas as subseções 3.13 a 3.17 e as
> sugestões de gráfico 6 e 7, além da resolução das notas de abstração preditiva dos itens 3.4 e
> 3.12. Todo o conteúdo originalmente fichado (itens 3.1 a 3.12, Seções 1, 2 e 4.1) foi
> integralmente preservado sem alterações.
