# FICHAMENTO CIENTÍFICO — Reliable Benchmarking: Requirements and Solutions

> **Veredito de Relevância:** SIM, o artigo é altamente útil para o nosso projeto de AOC. O texto trata diretamente de fundamentos de benchmarking experimental, medição confiável de CPU time/memória/energia, isolamento de execuções, efeitos de hyperthreading/Turbo Boost/NUMA sobre o desempenho, e — crucialmente — apresenta diretrizes formais de apresentação estatística de resultados (arredondamento por algarismos significativos, alinhamento decimal, scatter plots, quantile plots). Todos esses pontos sustentam diretamente nossa Metodologia e nossa seção de Resultados e Discussão, especialmente a justificativa do desvio padrão amostral e da variabilidade entre rodadas do Geekbench 6.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

BEYER, D.; LÖWE, S.; WENDLER, P. Reliable benchmarking: requirements and solutions. *International Journal on Software Tools for Technology Transfer*, v. 21, p. 1–29, 2019. DOI: 10.1007/s10009-017-0469-y.

- **Código BibTeX Completo (.bib):**

```bibtex
@article{beyer2017benchmarking,
  author    = {Beyer, Dirk and L{\"o}we, Stefan and Wendler, Philipp},
  title     = {Reliable benchmarking: requirements and solutions},
  journal   = {International Journal on Software Tools for Technology Transfer},
  year      = {2017},
  volume    = {21},
  pages     = {1--29},
  doi       = {10.1007/s10009-017-0469-y},
  publisher = {Springer},
  note      = {Corrected publication 2020}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo de Periódico (Regular Paper) — *International Journal on Software Tools for Technology Transfer* (Springer). Versão preliminar publicada em SPIN 2015.
- **Instituição/Editora:** LMU Munich (Alemanha) e One Logic (Passau, Alemanha); publicado pela Springer.
- **Palavras-Chave Originais:** Benchmarking · Resource measurement · Process control · Process isolation · Container · Competition.
- **Resumo do Escopo Geral:** O artigo identifica um conjunto de requisitos indispensáveis para benchmarking confiável e medição de recursos (tempo de CPU e memória) de ferramentas automáticas como *solvers* e verificadores. Os autores discutem as limitações de métodos e ferramentas de benchmarking existentes, investigam experimentalmente o impacto de características de hardware (hyperthreading, Turbo Boost, NUMA, múltiplas CPUs) sobre execuções paralelas, e apresentam o **BenchExec**, um framework de código aberto baseado em *cgroups* e *namespaces* do Linux que cumpre todos os requisitos levantados. Por fim, oferecem diretrizes para apresentação cientificamente válida de resultados de benchmarking (unidades, algarismos significativos, *scatter plots* e *quantile plots*).

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

### 3.1 Conceito/Teoria: Definição de Benchmarking Confiável e Replicabilidade

- **Citação Direta (Ipsis Litteris):** "We call a measurement reliable, if the measurement method ensures high accuracy (only small systematic and random measurement error, i.e., no bias or 'volatile' effects, resp.) and sufficient precision" (Página 2).
- **Paráfrase (Citação Indireta Acadêmica):** Os autores definem que uma medição é considerada confiável quando o método de mensuração garante alta exatidão — isto é, erro sistemático e aleatório reduzido — aliada a precisão suficiente, sendo este o pilar metodológico que viabiliza a replicabilidade de experimentos computacionais (Beyer, Löwe e Wendler 2017) (Página 2).
- **Onde Encaixar no Artigo LaTeX:** Introdução e Metodologia. Serve como justificativa teórica para o protocolo de 20 rodadas por máquina adotado pelo grupo, reforçando que a repetição experimental visa controlar erro aleatório.
- **Mapeamento de Colunas e Arquivos de Teste:** Sustenta o uso das 20 linhas de dados de `scores_maqA.txt` a `scores_maqD.txt` (colunas `Single_Core` e `Multi_Core`) como amostra estatística destinada a estimar exatidão e precisão da medição de desempenho, em vez de uma única execução isolada.

---

### 3.2 Conceito/Teoria: Medição de Tempo de CPU vs. Tempo de Parede (Wall Time)

- **Citação Direta (Ipsis Litteris):** "Measuring the wall time, i.e., the elapsed time between start and end of a tool execution, is insufficient because this does not allow a meaningful comparison of the resource usage of multithreaded tools and may be inadvertently influenced by input/output operations (I/O). Measuring the CPU time is more meaningful but also more difficult, especially if child processes are involved" (Página 2).
- **Paráfrase (Citação Indireta Acadêmica):** Segundo Beyer, Löwe e Wendler (2017), o tempo de parede (*wall time*) é uma métrica insuficiente para comparação de desempenho em ferramentas multithread, pois pode ser distorcido por operações de entrada e saída, enquanto o tempo de CPU, embora mais significativo, exige maior rigor de medição, sobretudo quando há processos filhos envolvidos (Página 2).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (seção de Métricas de Desempenho), complementando a discussão clássica de Tempo de Execução vs. Vazão (Patterson e Hennessy).
- **Mapeamento de Colunas e Arquivos de Teste:** Conceito de natureza metodológica, sem coluna direta na telemetria. Relaciona-se indiretamente com a coluna `Uso total da CPU (%)` dos arquivos `maq*_rodada_*.CSV`, pois reforça que o aproveitamento real de CPU (e não apenas o tempo decorrido do teste) é o que deve ser correlacionado ao *score* do Geekbench 6.

---

### 3.3 Conceito/Teoria: Consumo de Memória de Pico (Peak Memory Consumption) e Memória Compartilhada

- **Citação Direta (Ipsis Litteris):** "the memory usage of a process is defined as the peak size of all memory pages that occupy some system resources […] If a tool spawns several processes, these can use shared memory, such that the total memory usage of a group of processes is less than the sum of their individual memory usages" (Página 4).
- **Paráfrase (Citação Indireta Acadêmica):** Os autores estabelecem que o consumo de memória relevante para benchmarking é o pico de páginas de memória efetivamente ocupadas — e não o tamanho do espaço de endereçamento — e que, em cenários de múltiplos processos, a memória compartilhada deve ser contabilizada apenas uma vez, sob risco de superestimar o uso real de recursos (Beyer, Löwe e Wendler 2017) (Página 4).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia de Memória) e Resultados e Discussão, ao analisar picos de carga de memória física durante o benchmark.
- **Mapeamento de Colunas e Arquivos de Teste:** Coluna `Memória física utilizada (MB)` e `Carga da memória física (%)` dos arquivos `maq*_rodada_*.CSV`. Recomenda-se extrair o valor máximo (pico), e não apenas a média, dessas séries temporais para alinhar a análise ao conceito de "peak memory consumption" descrito pelos autores.

---

### 3.4 Conceito/Teoria: Influência de Características Microarquiteturais — Hyperthreading

- **Citação Direta (Ipsis Litteris):** "For the 2414 solved programs from the benchmark set, 16 h of CPU time were necessary using two separate physical cores and 25 h of CPU time were necessary using the same physical core, an increase of 53% caused by the inappropriate core assignment. This shows that hyperthreading can have a significant negative impact" (Página 9).
- **Paráfrase (Citação Indireta Acadêmica):** O experimento conduzido pelos autores demonstrou que a execução de duas tarefas paralelas em núcleos virtuais (*hyperthreads*) pertencentes ao mesmo núcleo físico aumentou o tempo de CPU necessário em 53%, evidenciando que o compartilhamento de unidades de execução e cache em arquiteturas SMT (*Simultaneous Multithreading*) pode degradar significativamente o desempenho quando comparado ao uso de núcleos físicos independentes (Beyer, Löwe e Wendler 2017) (Página 9).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica, na seção de Paralelismo a Nível de Instrução e Thread (Cores físicos vs. Threads lógicos), reforçando teoricamente por que o desempenho Multi-Core do Geekbench não escala linearmente com o número de threads lógicas.
- **Mapeamento de Colunas e Arquivos de Teste:** Coluna `Multi_Core` de `scores_maq*.txt`, confrontada com as colunas `Core 0 T0 Uso (%)` até `Core 3 T1 Uso (%)` dos arquivos `maq*_rodada_*.CSV`, permitindo observar se threads lógicas do mesmo núcleo físico (T0/T1) atingem utilização simultânea alta — o que, segundo o artigo, indicaria contenção de recursos compartilhados (cache L1/L2 e unidades de execução), tal como ocorre na CPU i5-8265U (Whiskey Lake-U, 4 cores/8 threads) da Máquina D.

---

### 3.5 Conceito/Teoria: Turbo Boost e Variação Dinâmica de Frequência do Núcleo

- **Citação Direta (Ipsis Litteris):** "Modern CPUs often adjust their frequency by several hundred MHz depending on how many of their cores are currently used, with the CPU running faster when less cores are used (this is commonly called 'Turbo Boost' or 'Turbo Core')" (Página 8).
- **Paráfrase (Citação Indireta Acadêmica):** Beyer, Löwe e Wendler (2017) explicam que processadores modernos ajustam dinamicamente sua frequência de operação conforme o número de núcleos ativos, elevando o clock quando poucos núcleos estão em uso — tecnologia conhecida como *Turbo Boost* — o que introduz uma fonte adicional e não determinística de variação no tempo de execução medido (Página 8).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica e Resultados e Discussão. Fundamenta diretamente a diferença esperada entre o *score* Single-Core (clock boost mais alto, poucos núcleos ativos) e o *score* Multi-Core (clock sustentado mais baixo, todos os núcleos ativos) no Geekbench 6.
- **Mapeamento de Colunas e Arquivos de Teste:** Colunas `Relógios núcleo (avg) (MHz)` e `Relógios efetivos núcleo (avg) (MHz)` dos arquivos `maq*_rodada_*.CSV`, comparadas entre rodadas de menor e maior `Uso total da CPU (%)`. Para a Máquina D, espera-se observar o clock subindo do *base* de 1,60 GHz para próximo do *boost* de 3,90 GHz nos instantes de carga concentrada em poucos núcleos.

---

### 3.6 Conceito/Teoria: Arquitetura NUMA (Nonuniform Memory Access)

- **Citação Direta (Ipsis Litteris):** "In a NUMA architecture, a single CPU or a group of CPUs can access parts of the system memory locally, i.e., directly, while other parts of the system memory are remote, i.e., they can only be accessed indirectly via another CPU, which is slower" (Página 5).
- **Paráfrase (Citação Indireta Acadêmica):** Em arquiteturas com acesso não uniforme à memória (NUMA), cada CPU ou grupo de CPUs possui uma região de memória local de acesso direto e rápido, ao passo que o acesso a regiões remotas — pertencentes a outra CPU — ocorre de forma indireta e mais lenta, gerando um efeito de desempenho dependente da topologia física do sistema (Beyer, Löwe e Wendler 2017) (Página 5).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Gargalos de Arquitetura / Hierarquia de Memória), como contraponto teórico avançado ao gargalo de Von Neumann discutido para sistemas single-socket.
- **Nota de Abstração Preditiva:** Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário. **Justificativa:** as quatro máquinas do estudo são notebooks/desktops domésticos com Windows 11 Home e, com altíssima probabilidade, possuem CPU única (single-socket), portanto sem topologia NUMA real — esse fenômeno é tipicamente observado apenas em servidores multi-soquete, como o sistema com dois Intel Xeon E5-2650 v2 utilizado nos experimentos originais dos autores.
- **Mapeamento de Colunas e Arquivos de Teste:** Não há coluna equivalente na lista de telemetria fornecida (HWiNFO64 não expõe métricas de NUMA em sistemas single-socket). Caso uma das Máquinas A, B ou C revele-se um sistema multi-soquete, as colunas `Relógio de barramento (MHz)` e `Carga da memória física (%)` poderiam ser usadas como *proxies* indiretos de contenção de barramento de memória.

> **Atualização complementar (sem alteração do fichamento original):** com a confirmação da tabela completa de hardware, as Máquinas E e F são *Desktops Montados* (AMD Ryzen 5 5500 e Intel Core i5-14600KF, respectivamente), e não notebooks. Ainda assim, ambas seguem sendo configurações de **CPU única (single-socket)** de uso doméstico/gamer, portanto a ressalva quanto à inaplicabilidade do conceito de NUMA permanece válida para as seis máquinas do estudo (A a F). A diretriz de abstração preditiva continua vigente.

---

### 3.7 Conceito/Teoria: Impacto do Compartilhamento de Cache L3 e Largura de Banda de Memória

- **Citação Direta (Ipsis Litteris):** "For the 2414 solved programs from the benchmark set, 16 h of CPU time were necessary if only one physical core was used, whereas 20 h of CPU time were necessary with eight physical cores used; the increase of 22% is caused by the contention on cache and memory accesses" (Página 9).
- **Paráfrase (Citação Indireta Acadêmica):** Os autores demonstram empiricamente que o aumento do número de núcleos físicos ativos simultaneamente em uma mesma CPU eleva o tempo de CPU necessário em 22%, efeito atribuído à disputa pelo cache de nível 3 compartilhado e pela largura de banda de acesso à memória RAM, escalando linearmente com a quantidade de núcleos utilizados (Beyer, Löwe e Wendler 2017) (Página 9).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Hierarquia de Memória — papel do Cache L3) e Resultados e Discussão, ao justificar por que o ganho de desempenho Multi-Core não é proporcional ao número de núcleos.
- **Mapeamento de Colunas e Arquivos de Teste:** Coluna `Multi_Core` de `scores_maq*.txt` correlacionada com `Uso total da CPU (%)` e `Taxa de leituras (MB/s)` / `Taxa de gravações (MB/s)` dos arquivos `maq*_rodada_*.CSV`. Para a Máquina D, o Cache L3 de 6 MB compartilhado entre os 4 núcleos físicos é o parâmetro arquitetural diretamente associado a este fenômeno.

---

### 3.8 Conceito/Teoria: Avaliação de Desempenho como Método Científico

- **Citação Direta (Ipsis Litteris):** "Performance evaluation is an effective and inexpensive method for assessing research results" (Página 1).
- **Paráfrase (Citação Indireta Acadêmica):** Tichy (1998), citado por Beyer, Löwe e Wendler (2017), defende que a avaliação de desempenho constitui um método eficaz e de baixo custo para validar resultados de pesquisa em ciência da computação experimental, fundamentando a prática de benchmarking como instrumento científico legítimo (Página 1).
- **Onde Encaixar no Artigo LaTeX:** Introdução, como justificativa geral da relevância científica de se realizar benchmarking comparativo entre as quatro máquinas do estudo.
- **Mapeamento de Colunas e Arquivos de Teste:** Conceito introdutório e estrutural; não se vincula a uma coluna específica, mas legitima o uso conjunto de todos os arquivos `scores_maq*.txt` e `maq*_rodada_*.CSV` como corpus experimental do trabalho.

---

### 3.9 Conceito/Teoria: Médias e Desvio Padrão Amostral — Necessidade de Algarismos Significativos Fixos

- **Citação Direta (Ipsis Litteris):** "One has to define how precise a measurement is, and show all results with a constant number of significant digits according to the precision of the measurement […] The naive approach of rounding all numbers to a fixed amount of decimal places […] should not be used" (Página 20).
- **Paráfrase (Citação Indireta Acadêmica):** Beyer, Löwe e Wendler (2017) recomendam que medições inexatas — como tempo e consumo de energia — sejam reportadas com um número constante de algarismos significativos compatível com a precisão real do instrumento de medição, alertando que o arredondamento ingênuo por número fixo de casas decimais introduz ruído estatístico em grandes valores e erro de arredondamento desproporcional em valores pequenos (Página 20).
- **Onde Encaixar no Artigo LaTeX:** Metodologia, na subseção de tratamento estatístico dos dados, antes da apresentação das fórmulas de Média e Desvio Padrão.
- **Mapeamento de Colunas e Arquivos de Teste:** Aplica-se a todas as médias calculadas a partir das colunas críticas de telemetria (`Potência total da CPU (W)`, `CPU Inteira (°C)`, `Relógios efetivos núcleo (avg) (MHz)`) e dos scores do Geekbench 6 (`Single_Core`, `Multi_Core`), orientando o número de casas decimais a ser exibido nas Tabelas do `main.tex`.

---

### 3.10 Conceito/Teoria: Comparação de Resultados via *Scatter Plots*

- **Citação Direta (Ipsis Litteris):** "In a scatter plot, data points on the diagonal show cases where both tools have the same value […] and the distance of a data point from the diagonal correlates to the difference between the results" (Página 21).
- **Paráfrase (Citação Indireta Acadêmica):** Os autores descrevem o gráfico de dispersão (*scatter plot*) como uma ferramenta visual em que pontos próximos à diagonal indicam equivalência de desempenho entre duas condições comparadas, enquanto o afastamento da diagonal é proporcional à magnitude da diferença observada entre as duas séries de dados (Beyer, Löwe e Wendler 2017) (Página 21).
- **Onde Encaixar no Artigo LaTeX:** Resultados e Discussão, como base metodológica para os gráficos comparativos entre máquinas (por exemplo, Potência vs. Score, ou Temperatura vs. Clock).
- **Mapeamento de Colunas e Arquivos de Teste:** Sugere-se plotar `Potência total da CPU (W)` (eixo X) vs. `Single_Core`/`Multi_Core` score (eixo Y) para cada uma das quatro máquinas, permitindo visualizar eficiência energética relativa entre A, B, C e D.

---

### 3.11 Conceito/Teoria: Limites de Energia — Package RAPL/PBM (PL1/PL2) e Restrição Térmica de Projeto

- **Citação Direta (Ipsis Litteris):** "Explicitly setting a limit for memory usage is important and should always be done, because otherwise the amount of memory available to the tool is the amount of free memory in the system, which varies over time and depends on lots of external factors" (Página 4).
- **Paráfrase (Citação Indireta Acadêmica):** Embora o trecho original trate de limites de memória, o princípio metodológico de que recursos do sistema devem ter limites explícitos e documentados — sob pena de variação não controlada nos resultados — aplica-se, por extensão arquitetural, aos limites de potência PL1 e PL2 (*Running Average Power Limit* — RAPL) que regulam o TDP sustentado e o TDP de pico de processadores Intel modernos, atuando como mecanismo de controle análogo ao limite de memória descrito pelos autores (Página 4).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Consumo Energético e Limites de Projeto) e Resultados e Discussão, ao interpretar eventos de *throttling* por excesso de potência.
- **Mapeamento de Colunas e Arquivos de Teste:** Colunas `IA: Package-Level RAPL/PBM PL1 (Yes/No)`, `Limite de potência PL1 (Dynamic) (W)`, `Limite de potência PL2 (Dynamic) (W)` e `Potência total da CPU (W)` dos arquivos `maq*_rodada_*.CSV`. Recomenda-se calcular a frequência relativa (%) de ocorrência de "Yes" nessas colunas booleanas ao longo das 20 rodadas de cada máquina, como indicador quantitativo de quão frequentemente o sistema operou no limite de seu envelope térmico/energético de projeto.

---

### 3.12 Conceito/Teoria: Isolamento de Execuções e Independência de Medições (Validade Interna do Experimento)

- **Citação Direta (Ipsis Litteris):** "For accurate results, each tool execution should be performed in isolation, as on a dedicated machine without other tool executions, neither in parallel nor in sequential combination, for example to avoid letting the order of tool executions influence the results" (Página 3).
- **Paráfrase (Citação Indireta Acadêmica):** Para garantir a validade de resultados experimentais, cada execução de benchmark deveria, idealmente, ocorrer de forma isolada, sem interferência de execuções paralelas ou da ordem sequencial das rodadas, de modo a evitar que fatores externos não controlados influenciem nas medições obtidas (Beyer, Löwe e Wendler 2017) (Página 3).
- **Onde Encaixar no Artigo LaTeX:** Metodologia, como justificativa do protocolo experimental adotado pelo grupo (processos em segundo plano minimizados, mesma versão de S.O. Windows 11 Home, 20 rodadas sequenciais por máquina).
- **Mapeamento de Colunas e Arquivos de Teste:** Relaciona-se à coluna `Rodada` dos arquivos `scores_maq*.txt`, sugerindo-se verificar se há tendência (*drift*) crescente ou decrescente do score ao longo das 20 rodadas — o que indicaria efeito de ordem (ex.: aquecimento progressivo) e violação parcial do princípio de independência das execuções.

---

### 3.13 Conceito/Teoria: Impacto de Múltiplas CPUs/Domínios de Potência em Sistemas de Alto TDP (Desktops E e F)

- **Citação Direta (Ipsis Litteris):** "if more physical cores per CPU are used, using n physical cores of each of the two CPUs with 2n parallel tool executions (red bars) is slower than using n physical cores of only one of the CPUs. The maximal difference occurs for eight cores per CPU, which uses 22 h of CPU time compared to 20 h (an increase of 14%)" (Página 10).
- **Paráfrase (Citação Indireta Acadêmica):** Beyer, Löwe e Wendler (2017) demonstram que, mesmo quando cada núcleo físico possui memória local própria, a distribuição da carga de trabalho entre múltiplos domínios de CPU pode gerar um custo de desempenho adicional e não totalmente explicado por contenção de cache ou memória, evidenciando que processadores com maior número de núcleos físicos ativos simultaneamente tendem a apresentar overhead de coordenação crescente conforme mais unidades de execução entram em operação plena (Página 10).
- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica (Paralelismo a Nível de Instrução e Thread) e Resultados e Discussão, ao explicar por que o ganho de desempenho Multi-Core das Máquinas E (AMD Ryzen 5 5500, 6 Cores/12 Threads, TDP 65 W) e F (Intel Core i5-14600KF, 14 Cores/20 Threads, TDP 125 W) não escala de forma proporcional ao número de núcleos físicos disponíveis quando comparado às máquinas notebook (A, B, C, D), que possuem TDPs muito menores (15–45 W) e, consequentemente, ativam menos núcleos em frequência plena de forma sustentada.
- **Mapeamento de Colunas e Arquivos de Teste:** Coluna `Multi_Core` de `scores_maqE.txt` e `scores_maqF.txt`, confrontada com `Uso total da CPU (%)`, `Core 0 T0 Uso (%)` até `Core 3 T1 Uso (%)` (estendendo a leitura para os núcleos adicionais presentes nos arquivos CSV dessas máquinas) e `Potência total da CPU (W)` dos arquivos `maqE_rodada_*.CSV` e `maqF_rodada_*.CSV`. Especificamente para a Máquina F (arquitetura híbrida Raptor Lake, 6 P-Cores + 8 E-Cores), recomenda-se segmentar a análise entre núcleos de desempenho (P-Cores) e núcleos eficientes (E-Cores), pois o artigo trata implicitamente apenas de núcleos homogêneos — o que exige cautela na extrapolação do conceito original para arquiteturas heterogêneas modernas (ver nota de abstração predita abaixo).
- **Nota de Abstração Preditiva:** Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário. **Justificativa:** o artigo original foi escrito com base em CPUs Intel Xeon homogêneas (sem núcleos híbridos P-core/E-core), de modo que a aplicação direta do conceito de "overhead de múltiplos domínios de CPU" às arquiteturas híbridas das Máquinas A (Raptor Lake-H, 4P+4E), B (Raptor Lake-P, 2P+8E) e F (Raptor Lake, 6P+8E) exige adaptação teórica cuidadosa, já que parte da variação de desempenho nessas CPUs decorre do *thread scheduler* do Windows 11 ao alocar tarefas entre P-Cores e E-Cores, e não exclusivamente de contenção de cache/memória entre domínios físicos como descrito pelos autores.

---

### 3.14 Conceito/Teoria: Heterogeneidade de Conjuntos de Instruções (ISA) como Fonte de Variabilidade entre Ferramentas/Plataformas

- **Citação Direta (Ipsis Litteris):** "tools are written in different programming languages, require different libraries, may spawn child processes, write to storage media, or perform other I/O. All of this has to be considered in the design of a benchmarking environment, ideally in a way that does not exclude any tools from being benchmarked" (Página 2).
- **Paráfrase (Citação Indireta Acadêmica):** Os autores alertam que a heterogeneidade entre os ambientes avaliados — decorrente de diferenças de implementação, bibliotecas e capacidades da plataforma subjacente — deve ser cuidadosamente considerada no projeto do ambiente de benchmarking, de modo a não comprometer a comparabilidade dos resultados entre diferentes alvos de teste (Beyer, Löwe e Wendler 2017) (Página 2).
- **Paráfrase Aplicada ao Cenário do Grupo:** Por extensão direta deste princípio, a heterogeneidade de **conjuntos de instruções avançadas (ISA)** entre as CPUs do nosso estudo — com a Máquina C (AMD Ryzen 5 3500U, Zen+) e a Máquina E (AMD Ryzen 5 5500, Zen 3) não possuindo suporte a Intel DL Boost (VNNI), presente nas Máquinas A, B, D e F (todas Intel) — constitui uma fonte legítima de variabilidade de desempenho que deve ser documentada na Metodologia, pois o Geekbench 6 pode utilizar instruções vetoriais (AVX2, FMA3, VNNI) de forma diferenciada conforme a disponibilidade de cada ISA, afetando o *score* Single-Core e Multi-Core independentemente da frequência de clock ou do TDP nominal.
- **Onde Encaixar no Artigo LaTeX:** Metodologia (tabela comparativa de hardware, na linha "Instruções Avançadas (CPU)") e Resultados e Discussão, como variável de controle a ser mencionada ao comparar scores entre máquinas Intel e AMD.
- **Mapeamento de Colunas e Arquivos de Teste:** Não há coluna telemétrica direta no HWiNFO64 para uso de instruções vetoriais específicas; a variável de controle é estrutural (definida na tabela de hardware da Metodologia) e deve ser cruzada qualitativamente com os scores `Single_Core` e `Multi_Core` de `scores_maqA.txt` a `scores_maqF.txt`, evitando-se atribuir exclusivamente ao clock ou ao TDP eventuais discrepâncias de desempenho entre famílias de CPU Intel e AMD.
- **Nota de Abstração Preditiva:** Este trecho teórico foi fichado de forma preditiva com base na coluna "Instruções Avançadas (CPU)" da tabela de hardware fornecida pelo grupo. Sua aplicação na redação final deve ser revisada caso o Geekbench 6 publique, em versões futuras de sua documentação, detalhamento explícito sobre quais sub-testes exploram diretamente VNNI versus apenas AVX2/FMA3, de modo a evitar inferência especulativa sobre a causa exata de eventuais diferenças de score entre as Máquinas C/E (AMD) e as demais (Intel).

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES (Se houver no texto original)

- **Fórmulas Matemáticas/Físicas em LaTeX Puro:**

  1. Notação científica para representação de algarismos significativos (Página 20):
  $$4{,}321 \times 10^{4}\ \text{s}$$

  2. Linha de regressão linear simples utilizada para o efeito de Turbo Boost e cache compartilhado (Página 10), na forma:
  $$y = a \cdot x + b$$
  onde, no caso reportado sem Turbo Boost, $a = 1800$ e $b = 56000$; com Turbo Boost, $a = 2600$ e $b = 44000$ (tempo de CPU em segundos em função do número de execuções paralelas $x$).

  3. Reta de referência para *scatter plots* comparativos (Página 22):
  $$y = x \qquad y = x + 10 \qquad y = x - 10 \qquad y = 10x \qquad y = \dfrac{x}{10}$$

  > **Observação:** o artigo não apresenta as fórmulas clássicas de Média Aritmética ($\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$) e Desvio Padrão Amostral ($s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}$) explicitamente — essas equações deverão ser extraídas de literatura estatística clássica (ex.: Montgomery, Patterson e Hennessy) e citadas separadamente na Metodologia, sem atribuição a este artigo, para não incorrer em invenção de citação.

- **Sugestão de Gráficos/Tabelas Correspondentes:**
  - **Gráfico de Dispersão (Scatter Plot):** reproduzir o padrão da Figura 2 do artigo (Página 9), plotando, para cada rodada, o tempo/score em condição "ideal" (poucos núcleos ativos / baixa carga térmica) no eixo X e o resultado em condição de maior contenção (alta carga simultânea) no eixo Y, com linha diagonal de referência $y=x$.
  - **Gráfico de Barras com Barras de Erro (Barplot):** para cada Máquina (A, B, C, D), plotar a média do score `Single_Core` e `Multi_Core` (extraído de `scores_maq*.txt`) com haste de erro equivalente ao desvio padrão amostral das 20 rodadas, em tons de cinza, seguindo o padrão visual sóbrio exigido pela SBC. *(Atualização complementar: com a confirmação das Máquinas E e F na tabela de hardware, o mesmo barplot deve ser estendido para as seis máquinas (A–F), preservando a ordenação por TDP crescente no eixo X para evidenciar visualmente a relação entre TDP e score Multi-Core discutida na Seção 3.13.)*
  - **Tabela de Algarismos Significativos:** replicar a lógica da Tabela 1 do artigo (Página 21) para apresentar, no `main.tex`, os valores médios de `Potência total da CPU (W)` e `CPU Inteira (°C)` com alinhamento decimal consistente, evitando o erro de arredondamento ingênuo criticado pelos autores.
