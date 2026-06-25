# FICHAMENTO CIENTÍFICO — VEREDITO DE RELEVÂNCIA

**O artigo será útil para o nosso projeto de AOC? SIM, e de forma altamente estratégica.**

Justificativa: o documento analisado é a Tese de Doutorado de Adriano Marques Garcia (PUCRS, 2023), que propõe e avalia o framework **SPBench** para *benchmarking* de processamento paralelo de fluxos de dados (*stream processing*) em arquiteturas multi-core. Embora o domínio de aplicação (Interfaces de Programação Paralela — PPIs — como TBB, FastFlow, OpenMP, GrPPI, SPar) seja mais específico do que o nosso escopo de AOC, a **Seção 5.3 (Experimental Setup)** apresenta uma tabela de hardware (Tabela 5.2) com especificações reais de três computadores de teste (dois Intel Xeon e um AMD Ryzen), incluindo cache L1/L2/L3, número de núcleos físicos e threads lógicos, clock e RAM — dados diretamente comparáveis à nossa Tabela de Hardware (Máquinas A, B, C, D). Além disso, a tese fundamenta com rigor metodológico: (1) a metodologia estatística de média de múltiplas execuções com desvio padrão como barra de erro (idêntica à nossa abordagem); (2) a influência do clock de processador no desempenho (latência) versus o número de núcleos no throughput; (3) o papel do cache e da hierarquia de memória no gargalo de desempenho; (4) métricas de desempenho consolidadas (latência, throughput, uso de CPU e memória) com fundamentação em Bordin et al.; e (5) referências teóricas clássicas como a Lei de Amdahl [Amd67] e a Lei de Gustafson [Gus88]. Portanto, o documento contém aderência direta a Benchmarking, hardware multi-core, métricas de desempenho e estatística experimental — todos pilares do nosso escopo de AOC.

**Atualização (revisão com a tabela de hardware completa de seis máquinas):** a releitura do documento, motivada pelo detalhamento de novos componentes (vetorização SIMD/VNNI, GPU dedicada, tipo e interface de armazenamento, TDP e topologia de RAM), revelou quatro trechos adicionais de alta relevância — sobre vetorização como extensão do paralelismo de dados, arquiteturas heterogêneas CPU+GPU, gargalo de I/O em armazenamento convencional vs. memória, e a importância metodológica de fixar o *CPU governor* para reprodutibilidade — todos fichados nas novas subseções 3.10 a 3.13 abaixo.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

GARCIA, A. M. **Easing the Benchmarking of Parallel Stream Processing on Multi-cores**. 2023. Tese (Doutorado em Ciência da Computação) — Escola Politécnica, Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS), Porto Alegre, 2023.

- **Código BibTeX Completo (.bib):**

```bibtex
@phdthesis{garcia2023easing,
  author      = {Garcia, Adriano Marques},
  title       = {Easing the Benchmarking of Parallel Stream Processing on Multi-cores},
  school      = {Pontifical Catholic University of Rio Grande do Sul ({PUCRS})},
  year        = {2023},
  address     = {Porto Alegre, Brazil},
  type        = {Doctoral Thesis},
  note        = {Programa de P{\'o}s-Gradua{\c{c}}{\~a}o em Ci{\^e}ncia da Computa{\c{c}}{\~a}o, Escola Polit{\'e}cnica},
  advisor     = {Fernandes, Luiz Gustavo Le{\~a}o}
}
```

> **Nota de proteção de siglas:** termos como `PUCRS`, `PPI`, `SPBench`, `TBB`, `CPU` devem ser envolvidos em chaves duplas (`{PUCRS}`) quando inseridos em campos de texto livre do `.bib`, conforme já demonstrado, para evitar que o `sbc.bst` aplique minúsculas indevidamente.

> **Nota de referência correlata identificada:** Nas Referências da própria tese, consta um trabalho anterior do mesmo autor diretamente relevante ao nosso eixo de TDP/clock/energia: GARCIA, A. M.; SERPA, M.; GRIEBLER, D.; SCHEPKE, C.; FERNANDES, L. G. L.; NAVAUX, P. O. A. "The impact of CPU frequency scaling on power consumption of computing infrastructures". In: International Conference on Computational Science and its Applications, 2020, pp. 142–157. Esta referência (citada na tese como [GSG+ 20b], Página 24) não foi fichada em detalhe aqui por não fazer parte do corpo de texto principal do documento anexado (consta apenas na lista de publicações do autor), mas é sugerida como busca bibliográfica complementar de alto valor para a seção de Consumo Energético do nosso artigo — ver lista de buscas ao final deste fichamento.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Tese de Doutorado (Doctoral Thesis) em Ciência da Computação.
- **Instituição/Editora:** Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS) — Escola Politécnica — Programa de Pós-Graduação em Ciência da Computação. Orientador: Prof. Ph.D. Luiz Gustavo Leão Fernandes; Coorientadores: Prof. Ph.D. Dalvan Griebler e Prof. Ph.D. Claudio Schepke.
- **Palavras-Chave Originais:** o documento não apresenta uma lista formal de *keywords* em uma página dedicada (comum em teses no formato PUCRS), mas os termos-chave recorrentes no resumo e introdução são: *Stream Processing*, *Parallel Programming Interfaces (PPIs)*, *Benchmarking*, *Multi-core*, *C++*, *Latency*, *Throughput*, *Memory Usage*, *Programmability*.
- **Resumo do Escopo Geral:** A tese propõe o **SPBench**, um framework para a construção de *benchmarks* customizáveis de processamento paralelo de fluxos de dados (*stream processing*) em arquiteturas multi-core baseadas em C++. O autor argumenta que há uma lacuna de *benchmarks* representativos para esse domínio e que avaliar PPIs (Interfaces de Programação Paralela) como TBB, FastFlow, OpenMP, GrPPI, SPar e WindFlow é uma tarefa custosa e pouco padronizada. A pesquisa conduz uma extensa avaliação experimental de desempenho (latência, vazão/throughput, uso de memória) e de programabilidade dessas PPIs, utilizando quatro aplicações reais (Bzip2, Lane Detection, Face Recognizer e Ferret) executadas em três computadores com arquiteturas distintas (dois Intel Xeon e um AMD Ryzen), variando o grau de paralelismo e os padrões estruturais (farm, pipeline, pipeline de farms).

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

### 3.1 Conceito/Teoria: Configuração Experimental de Hardware Multi-core (Setup de Bancada)

- **Citação Direta (Ipsis Litteris):** "All experiments in this thesis were done on three different computers. [...] We used two computers with Intel processors and a computer with an AMD processor." (Página 119/120, Seção 5.3).

- **Paráfrase (Citação Indireta Acadêmica):** O autor conduz seus experimentos de desempenho em três máquinas com microarquiteturas distintas — duas baseadas em processadores Intel Xeon (Silver 4210 e E5-2620 v3) e uma baseada em um processador AMD Ryzen 5 5600X —, evidenciando a importância metodológica de testar a mesma carga de trabalho em diferentes plataformas de hardware para isolar o efeito da microarquitetura sobre o desempenho medido (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia**, como justificativa metodológica para o uso de múltiplas máquinas (Máquinas A, B, C e D) em nosso próprio experimento, citando o precedente da literatura.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação sustenta a abordagem geral do nosso protocolo experimental, no qual cada uma das quatro máquinas gera 20 rodadas de `scores_maq*.txt` e 20 arquivos `.CSV` de telemetria HWiNFO64. Não há mapeamento de coluna específica aqui — é uma validação da arquitetura experimental geral (múltiplas plataformas, múltiplas rodadas).

---

### 3.2 Conceito/Teoria: Tabela Comparativa de Hardware (Cache, Núcleos, Threads, Clock, RAM)

- **Citação Direta (Ipsis Litteris):** "The first Intel one has 144 GB of RAM and two Intel® Xeon® Silver 4210 CPU @ 2.20GHz processors (a total of 20 cores and 40 threads). The other Intel computer has two Intel® Xeon® E5-2620 v3 @ 2.40 GHz processors (total of 12 cores and 24 threads) and 32 GB of RAM. The AMD one has 16 GB of RAM and an AMD Ryzen™ 5 5600X CPU @ 3.70GHz (a total of 6 cores and 12 threads)." (Página 120, Seção 5.3, Tabela 5.2).

- **Paráfrase (Citação Indireta Acadêmica):** A Tabela 5.2 do autor detalha, para cada uma das três máquinas de teste, o sistema operacional, a arquitetura (x86-64), o modelo da CPU, a frequência de clock, o número de núcleos físicos e threads lógicos, os tamanhos de cache L1d, L1i, L2 e L3, o *governor* de energia (Performance) e a quantidade total de memória RAM. Essa estruturação tabular de hardware é o padrão consolidado na literatura de arquitetura de computadores para garantir reprodutibilidade experimental (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia**, como modelo direto de formatação para a nossa própria Tabela de Hardware Comparativo (Máquinas A, B, C e D), incluindo a Máquina D (Dell Inspiron, i5-8265U) da Roberta.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação se relaciona diretamente com os metadados estáticos de hardware de cada máquina do nosso estudo (não provém de uma coluna específica do CSV, mas sim das especificações fixas reportadas na nossa Tabela de Hardware). Internamente, ela valida o uso de colunas dinâmicas correlatas no HWiNFO64, como `Relógios núcleo (avg) (MHz)` (correspondendo ao "Clock Frequency" reportado estaticamente pelo autor) e `Relação do relógio do núcleo (avg) (x)` (multiplicador de clock).

  > **NOTA PREDITIVA:** A Máquina A do autor (Xeon Silver 4210, 20 núcleos/40 threads, **Dual Channel** implícito por arquitetura de servidor, cache L3 de 27,5 MiB) representa um cenário de hardware muito superior ao da nossa Máquina D (i5-8265U, 4 núcleos/8 threads, cache L3 de 6 MB, RAM **Single Channel**). Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.

---

### 3.3 Conceito/Teoria: Influência do Clock de Processador sobre a Latência (Throughput vs. Latência)

- **Citação Direta (Ipsis Litteris):** "Although the AMD computer has half the number of cores of the Xeon E5-2620 v3, the AMD Ryzen 5 5600X is a newer processor model with a higher clock frequency. As such, it can deliver higher throughput than the Xeon E5-2620 computer. [...] Regarding latency, [...] The benchmarks achieved the best latency results when running on the AMD computer, followed by the Xeon E5-2620 computer and then by the Xeon Silver computer. Here, the clock frequency of the processors again plays a major role since it can process individual data items faster." (Páginas 126-127, Seção 5.5.2).

- **Paráfrase (Citação Indireta Acadêmica):** O autor demonstra empiricamente que, embora o número de núcleos físicos favoreça métricas agregadas de vazão (*throughput*) em cargas de trabalho altamente paralelas, a frequência de clock individual de cada núcleo é o fator dominante na determinação da latência de processamento de itens individuais. Um processador com clock mais alto processa cada item de dado mais rapidamente, mesmo possuindo menos núcleos físicos disponíveis para paralelismo (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** (para diferenciar Tempo de Execução/Latência de Vazão/Throughput) e **Resultados e Discussão**, ao explicarmos por que os scores *Single-Core* do Geekbench 6 dependem mais do clock e os scores *Multi-Core* dependem mais do paralelismo entre núcleos.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação sustenta diretamente a correlação entre as colunas `Relógios núcleo (avg) (MHz)` e `Relógios efetivos núcleo (avg) (MHz)` do HWiNFO64 com o score `Single_Core` dos arquivos `scores_maq*.txt`. Sustenta também a hipótese de que diferenças no `Single_Core` entre as Máquinas A, B, C e D estarão mais associadas ao clock médio do núcleo do que ao número total de threads, enquanto o `Multi_Core` dependerá mais da soma de `Uso total da CPU (%)` em múltiplos núcleos simultâneos.

---

### 3.4 Conceito/Teoria: Metodologia Estatística — Média de Execuções e Desvio Padrão como Barra de Erro

- **Citação Direta (Ipsis Litteris):** "All performance results represent an average of at least five executions of the benchmarks. The standard deviation is presented as error bars in all the performance graphs." (Página 124-125, Seção 5.5.1, Experimental Methodology).

- **Paráfrase (Citação Indireta Acadêmica):** Para garantir confiabilidade estatística dos resultados de desempenho, o autor adota o protocolo de repetir cada *benchmark* no mínimo cinco vezes, reportando a média aritmética como valor representativo e o desvio padrão amostral como medida de dispersão, exibido graficamente por meio de barras de erro. Essa prática mitiga o viés de ruído experimental pontual e expõe a variabilidade inerente à execução em sistemas multi-tarefa (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — esta é a citação mais importante do fichamento para fundamentar diretamente nossa decisão de coletar 20 rodadas por máquina (ao invés de apenas 5, reforçando ainda mais a robustez estatística do nosso próprio desenho experimental) e de utilizar barras de erro de desvio padrão em todos os gráficos de barras (barplots) do Matplotlib.

- **Mapeamento de Colunas e Arquivos de Teste:** Aplica-se a TODAS as colunas dos 4 arquivos `scores_maq*.txt` (colunas `Single_Core` e `Multi_Core`, calculadas sobre as 20 rodadas) e a todas as colunas críticas dos 80 arquivos `.CSV` de telemetria (ex.: `Potência total da CPU (W)`, `CPU Inteira (°C)`, `Uso total da CPU (%)`), nas quais devemos sempre reportar Média ± Desvio Padrão Amostral.

---

### 3.5 Conceito/Teoria: Métricas de Desempenho Consolidadas em Benchmarking (Latência, Throughput, Uso de CPU/Memória)

- **Citação Direta (Ipsis Litteris):** "Bordin et. al [BGM+ 20] conducted a survey in this respect and identified the metrics that are more frequently found in stream processing benchmarks. These metrics are latency, throughput, and resource usage, such as CPU and memory." (Página 70-71, Seção 3.2.4).

- **Paráfrase (Citação Indireta Acadêmica):** Com base em uma revisão sistemática da literatura conduzida por Bordin et al., o autor identifica que as métricas mais recorrentes para avaliação de desempenho em sistemas de processamento paralelo são a latência (tempo de resposta por item), o throughput (vazão de itens processados por unidade de tempo) e o consumo de recursos do sistema, notadamente o uso de CPU e de memória (GARCIA, 2023 apud BORDIN et al., 2020).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, na subseção de Métricas de Desempenho, complementando a discussão sobre MIPS, FLOPS e Scores Sintéticos (Geekbench) com a tríade Latência/Throughput/Uso de Recursos amplamente validada na literatura de sistemas paralelos.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta tríade de métricas se mapeia diretamente: (1) Latência/Throughput → aproximado pelos scores `Single_Core` e `Multi_Core` do Geekbench 6 (que sintetizam tempo de execução de cargas de trabalho padronizadas); (2) Uso de CPU → coluna `Uso total da CPU (%)`; (3) Uso de Memória → coluna `Carga da memória física (%)` e `Memória física utilizada (MB)` dos arquivos `.CSV`.

---

### 3.6 Conceito/Teoria: Lei de Amdahl e Lei de Gustafson (Limites do Paralelismo)

- **Citação Direta (Ipsis Litteris):** "Amdahl's law [Amd67] describes this limit, which refers to the non-parallelizable parts of a program. Even in highly parallelizable applications, intrinsically serial parts will be impossible to avoid. [...] On the other hand, Gustafson's law [Gus88] says that parallel regions grow faster than sequential ones when you scale up the problem." (Página 29-30, Seção 2.1).

- **Paráfrase (Citação Indireta Acadêmica):** A Lei de Amdahl estabelece um limite teórico para o ganho de desempenho (*speedup*) obtido pela paralelização, determinado pela fração do programa que permanece intrinsecamente sequencial e, portanto, não pode ser acelerada por mais núcleos de processamento que sejam adicionados. Em contraponto, a Lei de Gustafson argumenta que, ao escalar o tamanho do problema, a porção paralelizável cresce proporcionalmente mais rápido que a porção sequencial, sugerindo que o limite de Amdahl é dependente da escala do problema analisado (GARCIA, 2023 apud AMDAHL, 1967; GUSTAFSON, 1988).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, como base clássica e obrigatória para qualquer discussão sobre Paralelismo a Nível de Instrução e Thread, especialmente ao explicar por que o ganho de desempenho do score `Multi_Core` do Geekbench 6 não escala linearmente com o número de threads lógicos disponíveis em arquiteturas como a da Máquina D (4 núcleos/8 threads via Hyper-Threading).

- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta teoricamente a análise da razão entre o score `Multi_Core` e o score `Single_Core` multiplicado pelo número de núcleos físicos (medida indireta de eficiência de paralelização), e também o cruzamento com a coluna `Uso total da CPU (%)`, observando se a carga atinge ou não 100% em todos os núcleos simultaneamente durante o benchmark Multi-Core.

  > **NOTA TEÓRICA GERAL:** As leis de Amdahl e Gustafson são fundamentos clássicos e atemporais da Arquitetura de Computadores (não dependem de hardware específico das Máquinas A/B/C/D), portanto sua citação é válida e aplicável imediatamente, sem necessidade da nota de ressalva preditiva.

---

### 3.7 Conceito/Teoria: Propriedades de Avaliação de PPIs — Desempenho, Portabilidade e Programabilidade

- **Citação Direta (Ipsis Litteris):** "[MRR12] says that a PPI should be: 'Expressive, composable, debuggable, and maintainable'. [...] according to [MRR12] the performance of a PPI should be 'achievable, scalable, predictable, and tunable'." (Páginas 28-30, Seção 2.1).

- **Paráfrase (Citação Indireta Acadêmica):** Toda interface ou tecnologia de programação paralela deve equilibrar três propriedades fundamentais: programabilidade/produtividade (custo de desenvolvimento e manutenção do código paralelo), portabilidade (capacidade de manter desempenho relativo equivalente ao migrar entre arquiteturas distintas) e desempenho propriamente dito (capacidade de entregar ganhos de forma alcançável, escalável, previsível e ajustável) (GARCIA, 2023 apud MCCOOL et al., 2012).

- **Onde Encaixar no Artigo LaTeX:** **Introdução** ou **Fundamentação Teórica**, como justificativa ampla de por que a avaliação multidimensional de hardware (não apenas o score bruto, mas também temperatura, energia e estabilidade) é relevante na literatura de Engenharia de Computação.

- **Mapeamento de Colunas e Arquivos de Teste:** Aplica-se de forma conceitual e indireta a todo o conjunto de dados do projeto, justificando por que avaliamos não apenas o score final (`Single_Core`/`Multi_Core`), mas também a "previsibilidade" do sistema (medida pelo desvio padrão entre as 20 rodadas) e a "escalabilidade térmica" (medida pelas colunas `CPU Inteira (°C)` e `Estrangulamento térmico do núcleo (avg) (Yes/No)`).

---

### 3.8 Conceito/Teoria: Uso de Memória como Fator Crítico de Escalabilidade

- **Citação Direta (Ipsis Litteris):** "The evaluation of memory usage is a crucial aspect of developing and optimizing stream processing applications. [...] As the amount of data being processed increases, so does the memory required to handle that data." (Página 143, Seção 5.6).

- **Paráfrase (Citação Indireta Acadêmica):** O monitoramento do consumo de memória é apontado como um indicador crítico de escalabilidade em aplicações que processam grandes volumes de dados, uma vez que o crescimento do volume de entrada está diretamente associado ao crescimento da demanda por memória disponível, podendo se tornar um gargalo de desempenho independente da capacidade de processamento da CPU (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** **Resultados e Discussão**, ao analisarmos a coluna `Carga da memória física (%)` em conjunto com o `Uso total da CPU (%)`, especialmente relevante para a Máquina D, que possui apenas 8 GB de RAM em configuração Single Channel — um cenário de maior risco de saturação de memória sob carga.

- **Mapeamento de Colunas e Arquivos de Teste:** Mapeia diretamente para as colunas `Carga da memória física (%)`, `Memória física utilizada (MB)`, `Memória física disponível (MB)` e `Utilização do arquivo de paginação (%)` (esta última especialmente relevante caso a Máquina D, com apenas 8 GB de RAM, recorra ao *paging* durante o benchmark Multi-Core do Geekbench 6).

---

### 3.9 Conceito/Teoria: Sobrecarga de Sincronização e Contenção de Dados em Multithreading (Locking vs. Lock-Free)

- **Citação Direta (Ipsis Litteris):** "OpenMP and C++ Threads benchmarks use the same communication queues. The shared queue they use has a locking system to avoid data racing. This way, when using a high number of parallel workers, the average time they have to wait to access the queues increases. Consequently, items take longer to be processed, increasing the latency and reducing throughput. FastFlow, on the other hand, uses lock-free queues." (Página 126-127, Seção 5.5.2).

- **Paráfrase (Citação Indireta Acadêmica):** O autor demonstra que mecanismos de sincronização baseados em bloqueio (*locking*) para evitar condições de corrida em filas compartilhadas introduzem sobrecarga proporcional ao número de threads concorrentes, degradando tanto a latência quanto a vazão em cenários de alto paralelismo. Em contraste, estruturas de dados livres de bloqueio (*lock-free*) mitigam esse efeito ao evitar a espera ativa por acesso exclusivo a recursos compartilhados (GARCIA, 2023).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, na subseção de Paralelismo a Nível de Instrução e Thread, como complemento avançado à discussão sobre Cores físicos vs. Threads lógicos, explicando por que o ganho de desempenho do Hyper-Threading nem sempre é proporcional ao número de threads lógicas adicionais (contenção de recursos compartilhados do núcleo físico).

- **Mapeamento de Colunas e Arquivos de Teste:** Embora o Geekbench 6 seja uma caixa-preta sem acesso direto às filas internas, este conceito fundamenta teoricamente por que o ganho percentual do score `Multi_Core` sobre o `Single_Core` da Máquina D (4 núcleos/8 threads) tende a ser sublinear, podendo ser cruzado com a coluna `Uso total da CPU (%)` para verificar se a CPU realmente atinge saturação plena durante o teste Multi-Core.

---

### 3.10 Conceito/Teoria: Vetorização SIMD como Extensão do Paralelismo de Largura de Dados (AVX/AVX2/VNNI)

- **Citação Direta (Ipsis Litteris):** "Although there are mechanisms of automatic parallelism, such as vectorization (an extension of data width parallelism), it has not been universally successful [MRR12]. This automatic hardware parallelism has low portability because the performance relies on a specific architecture." (Página 28-29, Seção 2.1.3).

- **Paráfrase (Citação Indireta Acadêmica):** A vetorização é caracterizada como um mecanismo de paralelismo automático em nível de hardware, definido como uma extensão do paralelismo de largura de dados (*data width parallelism*), no qual uma única instrução processa múltiplos dados simultaneamente. Entretanto, o autor ressalta que esse tipo de paralelismo apresenta baixa portabilidade de desempenho, pois seus ganhos dependem diretamente da microarquitetura específica do processador utilizado (GARCIA, 2023 apud MCCOOL et al., 2012).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, na subseção de Paralelismo a Nível de Instrução, como base conceitual direta para justificar a coluna "Instruções Avançadas (CPU)" da nossa Tabela de Hardware — especificamente os conjuntos AVX, AVX2, FMA3, BMI2 e Intel DL Boost (VNNI) presentes nas Máquinas A, B, C, D e F.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação fundamenta teoricamente por que máquinas com conjuntos de instruções vetoriais mais avançados — como a Máquina A (i5-13420H) e a Máquina F (i5-14600KF), que possuem **Intel DL Boost (VNNI)** além de AVX2 — podem apresentar ganhos de desempenho no score `Single_Core` e `Multi_Core` do Geekbench 6 que não são explicados apenas pelo clock ou número de núcleos, mas sim pela capacidade de processar múltiplos dados por ciclo de clock através de instruções SIMD mais largas. Por outro lado, a Máquina C (Ryzen 5 3500U, Zen+) e a Máquina E (Ryzen 5 5500, Zen 3), que dispõem apenas de AVX, AVX2 e FMA3 (sem VNNI), servem de contraponto comparativo direto para isolar esse efeito microarquitetural nos resultados de `scores_maq*.txt`. Esta diferença reforça a necessidade de cautela ao comparar diretamente scores entre famílias de CPU distintas (Intel vs. AMD), pois parte da diferença de desempenho pode ser atribuída ao conjunto de instruções e não somente à frequência ou ao número de núcleos.

---

### 3.11 Conceito/Teoria: Arquiteturas Heterogêneas CPU+GPU e Paralelismo de Dados em Aceleradores

- **Citação Direta (Ipsis Litteris):** "In addition, multi-core systems can also combine with accelerators, such as GPUs, to form heterogeneous architectures, significantly increasing scalability potential [RM19]. In a CPU+GPU architecture, operators with high data parallelism potential can run on the GPU while the CPU manages sources, sinks, and other non-data-parallel stages, for instance." (Página 44-45, Seção 2.2.5).

- **Paráfrase (Citação Indireta Acadêmica):** Sistemas multi-core podem ser combinados com aceleradores de hardware, como GPUs, formando arquiteturas heterogêneas que ampliam significativamente o potencial de escalabilidade do sistema. Nesse modelo, operadores ou tarefas com alto potencial de paralelismo de dados são delegados à GPU, enquanto a CPU permanece responsável pelo gerenciamento de operações sequenciais, controle de fluxo, leitura de fontes (*sources*) e escrita de resultados (*sinks*) (GARCIA, 2023 apud RIBEIRO; MELLO, 2019).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, complementando a discussão de Paralelismo a Nível de Instrução e Thread com uma subseção sobre arquiteturas heterogêneas, e na **Metodologia**, para justificar por que registramos as colunas de GPU do HWiNFO64 (`GPU Clock (MHz)`, `Carga do núcleo da GPU (%)`) mesmo em um benchmark primariamente orientado à CPU.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação fundamenta diretamente a relevância de analisarmos a presença (ou ausência) de GPU dedicada na nossa Tabela de Hardware. As Máquinas A (RTX 4050 Laptop), D (MX130), E (RX 7600) e F (RTX 3050) possuem GPU dedicada com interface PCIe própria (coluna "Interface de Barramento GPU"), permitindo um eventual offload de tarefas paralelizáveis, enquanto as Máquinas B e C dependem exclusivamente de suas GPUs integradas (Iris Xe e Radeon Vega 8, respectivamente). Embora o Geekbench 6 (em sua componente CPU) não distribua diretamente carga à GPU, este conceito justifica teoricamente por que, em testes futuros com cargas heterogêneas, devemos monitorar simultaneamente `Uso total da CPU (%)` e `Carga do núcleo da GPU (%)` para identificar eventual cooperação ou contenção de recursos entre os dois subsistemas de processamento.

---

### 3.12 Conceito/Teoria: Hierarquia de Armazenamento — Gargalo de I/O em Sistemas de Disco Convencionais vs. Processamento em Memória

- **Citação Direta (Ipsis Litteris):** "These databases, if stored in conventional storage systems, could present a huge I/O performance bottleneck during processing. Conventional solutions are no longer able to efficiently handle the large volume of data generated by IoT devices, for instance [AHN+ 20]." (Página 44, Seção 2.2.5).

- **Citação Direta (Ipsis Litteris) — complementar:** "We run all the benchmarks using the in-memory mode in SPBench, which allows for achieving higher frequencies since reading data from memory is faster than reading it from disk." (Página 167, Seção 6.5).

- **Paráfrase (Citação Indireta Acadêmica):** Sistemas de armazenamento convencionais (discos tradicionais) podem se tornar um gargalo significativo de entrada/saída (I/O) durante o processamento de grandes volumes de dados, uma vez que a velocidade de leitura do disco é substancialmente inferior à velocidade de leitura a partir da memória RAM. O próprio autor demonstra esse princípio na prática ao optar por executar seus benchmarks em modo *in-memory* justamente para eliminar essa limitação e atingir frequências de processamento mais altas e estáveis (GARCIA, 2023 apud AHMED et al., 2020).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica**, na subseção de Hierarquia de Memória, como base teórica direta para a comparação entre HD SATA (mais lento) e SSD NVMe (mais rápido) presentes em nossa Tabela de Hardware, e na **Resultados e Discussão**, ao explicarmos possíveis quedas ou instabilidades de desempenho associadas ao tipo de armazenamento de cada máquina.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta é uma das citações mais relevantes da nova tabela de hardware, pois a coluna "Armazenamento (Tipo/Capacidade)" revela uma diversidade significativa: a Máquina D (HDD Western Digital Blue 1TB, 5400 RPM, interface SATA III) representa o cenário de maior risco de gargalo de I/O, enquanto as Máquinas A, B, C e F utilizam SSDs NVMe com interfaces PCIe (Gen 3.0 ou Gen 4.0), e a Máquina E utiliza uma configuração híbrida (SSD SATA 120GB + HD 1TB SATA III). Esta hierarquia de armazenamento deve ser cruzada com a coluna `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)` dos arquivos `.CSV` do HWiNFO64: espera-se que a Máquina D apresente taxas de transferência sensivelmente menores e maior variabilidade (desvio padrão) na duração de carregamento de dados do Geekbench 6, especialmente em testes que dependem de leitura de arquivos temporários, o que pode contribuir para explicar eventuais discrepâncias nos scores `Single_Core`/`Multi_Core` mesmo entre processadores com especificações de clock/cache relativamente próximas (ex.: Máquina C, com SSD NVMe, vs. Máquina D, com HDD).

---

### 3.13 Conceito/Teoria: Reprodutibilidade Experimental — Fixação do CPU Governor e Descrição Completa do Ambiente de Hardware/Software

- **Citação Direta (Ipsis Litteris):** "The hardware needs to be detailed so that another user can reproduce it. So do the software versions and configurations, such as compiler, CPU governor policy, libraries, and operating system. Despite efforts to provide a sufficient description of the test environments, many scientists cannot even reproduce their own experiments after one year [DL15]." (Página 51, Seção 2.3 — Benchmarks).

- **Citação Direta (Ipsis Litteris) — complementar (Tabela 5.2):** "Governor: Performance / Performance / Performance" e "We used GCC 9.4.0 with -O3 flag, and performance governor was enabled in all of them." (Páginas 120, Seção 5.3).

- **Paráfrase (Citação Indireta Acadêmica):** A reprodutibilidade experimental em benchmarking exige a descrição detalhada não apenas do hardware utilizado, mas também das configurações de software, incluindo a política de governança de frequência da CPU (*CPU governor policy*), versões de compilador, bibliotecas e sistema operacional. O autor reforça essa exigência ao fixar explicitamente o *governor* de energia da CPU como "Performance" (modo de máximo desempenho, sem economia de energia) em todas as três máquinas de seu experimento, eliminando uma fonte de variabilidade incontrolada nos resultados (GARCIA, 2023 apud DOSSANTOS; LOPES, 2015).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia**, como justificativa metodológica crítica para documentarmos explicitamente o sistema operacional (Windows 11 Home/Pro, com diferentes builds e versões 25H2), já que, diferentemente do autor (que padronizou Linux/Ubuntu com *governor* fixo), nosso ambiente Windows não permite o mesmo nível de controle explícito sobre o *power plan* da CPU — uma limitação que deve ser declarada como ameaça à validade interna do experimento.

- **Mapeamento de Colunas e Arquivos de Teste:** Esta citação fundamenta a necessidade de relatar, na Metodologia do nosso artigo, o plano de energia do Windows 11 utilizado durante a coleta (ex.: "Desempenho Máximo" ou "Equilibrado") como equivalente ao *CPU governor* do autor, e de cruzar essa informação com as colunas `Relógios núcleo (avg) (MHz)` e `Relógios efetivos núcleo (avg) (MHz)` dos arquivos `.CSV`, observando se houve *throttling* por economia de energia (e não apenas por temperatura) em alguma das seis máquinas — em especial nos notebooks ultrafinos B, C e D, cujo TDP base de 15 W (coluna "TDP Base da CPU") os torna mais suscetíveis a políticas agressivas de redução de clock para economia de bateria, mesmo quando conectados à energia elétrica.

  > **NOTA PREDITIVA:** A comparação de TDP entre as seis máquinas (15 W nos ultrafinos B/C/D, 45 W no notebook gamer A, 65 W no desktop E e 125 W no desktop F) é um dado estático da nossa própria Tabela de Hardware, não extraído da tese de Garcia. A citação acima fundamenta teoricamente *por que* monitorar o clock dinâmico é relevante diante de TDPs tão diferentes, mas a análise quantitativa do impacto do TDP sobre os scores reais só poderá ser redigida na seção de Resultados após o preenchimento das colunas de telemetria (`Potência total da CPU (W)`, `Relógios núcleo (avg) (MHz)`) de todas as seis máquinas, incluindo as ainda pendentes de coleta (E e F, conforme indicado pelos campos "[Preencher Gabinete]*" e "[Preencher Gen]*" na tabela fornecida).

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES (Se houver no texto original)

- **Fórmulas Matemáticas/Físicas em LaTeX Puro:**

O documento original não apresenta equações matemáticas formalmente tipografadas (não há blocos de equação numerados no texto extraído das Seções 2, 3 e 5). As leis de Amdahl e Gustafson são referenciadas conceitualmente, por nome e citação bibliográfica (Página 29-30), mas sem fórmula explícita impressa no corpo do texto da tese. Por rigor científico, **não inventamos** a equação correspondente a partir do texto da tese; caso desejado, a forma clássica da Lei de Amdahl, conforme consolidada na literatura padrão de Arquitetura de Computadores (ex.: Hennessy e Patterson), pode ser inserida separadamente no artigo, citando a fonte primária [Amd67] e/ou um livro-texto consolidado, e não esta tese.

- **Sugestão de Gráficos/Tabelas Correspondentes:**

1. **Tabela de Hardware Comparativo:** A Tabela 5.2 do autor (Página 120) é o modelo estrutural ideal para nossa Tabela de Hardware das Máquinas A, B, C e D no `main.tex`, organizando linhas por categoria (Sistema Operacional, CPU, Memória) e colunas por máquina.
2. **Gráfico de Barras com Hastes de Erro (Latência/Throughput):** As Figuras 5.4 e 5.5 do autor (Páginas 126-127) demonstram o padrão de gráfico de linhas/barras comparando múltiplas plataformas de hardware lado a lado com a mesma escala no eixo Y — sugerimos replicar esse padrão no Matplotlib para comparar os scores `Single_Core` e `Multi_Core` das quatro máquinas em um único gráfico de barras com a mesma escala, facilitando a comparação visual direta.
3. **Gráfico de Caracterização de Carga (Figura 5.1/5.2):** O padrão de múltiplos subplots por métrica (CPU%, Memória, Throughput instantâneo) ao longo do tempo de execução pode inspirar um gráfico de série temporal segundo a segundo das colunas `Uso total da CPU (%)`, `CPU Inteira (°C)` e `Potência total da CPU (W)` extraídas dos 20 arquivos `.CSV` de cada máquina, evidenciando o comportamento dinâmico do hardware durante as 20 rodadas do Geekbench 6.

---

## SUGESTÕES DE BUSCA TEXTUAL (GOOGLE ACADÊMICO)

Para localizar e validar as referências citadas indiretamente nesta tese (Bordin et al. 2020; McCool et al. 2012; Amdahl 1967; Gustafson 1988) e integrá-las ao `sbc-template.bib`, sugerimos as seguintes strings de busca exatas:

**Em inglês:**
- "Amdahl's law" "validity of the single processor approach"
- Gustafson "Reevaluating Amdahl's law" 1988
- Bordin survey "stream processing" benchmarks metrics latency throughput
- McCool "Structured Parallel Programming" patterns book
- "SPBench" framework stream processing benchmarking multi-core
- FastFlow TBB OpenMP latency throughput comparison multi-core
- lock-free queue vs locking mechanism multithreading latency overhead
- SIMD vectorization AVX AVX2 performance microarchitecture
- Intel Deep Learning Boost VNNI instruction set performance
- CPU+GPU heterogeneous architecture data parallelism
- NVMe SSD vs HDD I/O bottleneck benchmarking performance
- "CPU frequency scaling" power consumption computing infrastructure Garcia
- CPU governor performance policy benchmark reproducibility

**Em português:**
- "Lei de Amdahl" limite paralelização desempenho
- "Lei de Gustafson" escalabilidade paralela
- métricas de desempenho processamento paralelo latência vazão
- benchmarking processamento paralelo multi-core C++
- sobrecarga de sincronização threads contenção de dados
- avaliação de desempenho interfaces de programação paralela
- vetorização SIMD instruções AVX desempenho microarquitetura
- arquitetura heterogênea CPU GPU paralelismo de dados
- gargalo de entrada e saída SSD NVMe versus HDD desempenho
- escalonamento de frequência da CPU consumo de energia
- política de governor da CPU reprodutibilidade experimental

---

**Observação final de rigor científico:** Todas as citações diretas acima foram transcritas integralmente do texto extraído via OCR/parsing do PDF fornecido (tese de Adriano Marques Garcia, PUCRS, 2023), preservando ortografia e numeração de página conforme indicado no rodapé de cada página do documento original. Nenhum dado quantitativo ou teórico foi extrapolado além do que está expresso no documento.
