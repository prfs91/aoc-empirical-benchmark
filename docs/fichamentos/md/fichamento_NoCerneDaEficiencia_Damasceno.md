# Fichamento Científico — `fichamento_NoCerneDaEficiencia_Damasceno.md`

> **Arquivo gerado por:** Sistema de Fichamento Científico — Projeto AOC / UFPA Tucuruí  
> **Data de geração:** Junho de 2026 (atualizado com hardware completo das Máquinas A, B, C, E e F)  
> **Veredito de Relevância:** ✅ **SIM — Alta aderência ao escopo do projeto.**  
> O TCC analisa benchmarks CPU-bound (Rodinia), mede potência via Intel RAPL (análogo ao HWiNFO64),
> e discute consumo energético por compilador em hardware real. Fornece vocabulário, metodologia
> e fórmulas diretamente aplicáveis à nossa análise comparativa de 6 máquinas com Geekbench 6.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

DAMASCENO, Erick Vinícius. **No Cerne da Eficiência: Uma Análise Comparativa sobre Compiladores e seu Desempenho**. 2023. 83 f. Trabalho de Conclusão de Curso (Bacharelado em Engenharia de Computação) — Faculdade de Engenharia de Computação, Universidade Federal do Pará, Campus Universitário de Tucuruí, Tucuruí, 2023.

- **Código BibTeX Completo (.bib):**

```bibtex
@MastersThesis{damasceno:23,
  author      = {Erick Vin{\'i}cius Damasceno da Silva},
  title       = {No Cerne da Efici{\^e}ncia: Uma An{\'a}lise Comparativa
                 sobre Compiladores e seu Desempenho},
  school      = {Faculdade de Engenharia de Computa{\c{c}}{\~a}o,
                 Universidade Federal do Par{\'a} ({UFPA}),
                 Campus Universit{\'a}rio de Tucuru{\'i}},
  year        = {2023},
  address     = {Tucuru{\'i}, Par{\'a}, Brasil},
  month       = {novembro},
  type        = {Trabalho de Conclus{\~a}o de Curso (Bacharelado em
                 Engenharia de Computa{\c{c}}{\~a}o)},
  note        = {Orientador: Prof. Dr. Marcos T{\'u}lio Amaris Gonz{\'a}lez.
                 Conceito obtido: Excelente. 83~p.}
}
```

> ⚠️ **NOTA EDITORIAL:** A entrada usa o tipo `@MastersThesis` por ser a aproximação BibTeX
> mais próxima para TCCs no padrão SBC/abntex2. Caso o `sbc.bst` exija `@TechReport` ou
> `@Misc`, substituir e manter todos os campos acima. Inserir no `sbc-template.bib` e citar
> com `\cite{damasceno:23}`.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Trabalho de Conclusão de Curso — Bacharelado em Engenharia de Computação (83 p.)
- **Instituição/Editora:** Universidade Federal do Pará (UFPA) — Campus Universitário de Tucuruí — Faculdade de Engenharia de Computação
- **Orientador:** Prof. Dr. Marcos Túlio Amaris González
- **Banca:** Prof. Dr. Otávio Noura Teixeira; Prof. Dr. Daniel da Conceição Pinheiro
- **Conceito:** EXCELENTE — Defesa em 14/12/2023
- **Palavras-Chave Originais:** HPC. Compiladores. Computação Paralela. Clang. ICC. GCC.
- **Resumo do Escopo Geral:**
  O trabalho realiza uma análise comparativa da eficiência energética e do tempo de execução
  de cinco benchmarks da suíte Rodinia (LU Decomposition, Back Propagation, StreamCluster,
  LavaMD e Myocyte), cada um compilado por três compiladores distintos da linguagem C
  (GCC 11.4.0, Clang 14.0.0 e ICC 2021.10.0) com suporte a paralelismo OpenMP.
  A coleta de consumo energético é realizada via Intel RAPL, acessado pela ferramenta Joule It
  (da Power API), em um sistema Linux Ubuntu 22.04 com processador Intel Core i7-5500U
  (2 núcleos, 4 threads, DDR3L 1600 MHz). A análise inclui detecção de outliers por Boxplot
  e One-Class SVM. O resultado central aponta o ICC como o compilador mais eficiente
  energeticamente (30,76% do consumo total excluindo anomalias), seguido de GCC (33,23%)
  e Clang (36,01%), embora com variações significativas entre benchmarks específicos.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 Benchmarking como Método Científico de Avaliação de Desempenho

- **Conceito/Teoria:** Benchmarks são instrumentos padronizados de avaliação do desempenho computacional, desenvolvidos para submeter sistemas a cargas de trabalho controladas e reprodutíveis.

- **Citação Direta (Ipsis Litteris):**
  > "À medida que os softwares avançaram e foram acompanhados por hardware projetado para enfrentar desafios de alta performance, surgiu a necessidade de estabelecer critérios de eficiência e uma metodologia para avaliar o desempenho dessas plataformas. Para atender a essa demanda, foram desenvolvidas ferramentas projetadas para submeter esses sistemas a testes rigorosos, com o objetivo de mensurar sua capacidade de processamento. Essas ferramentas, conhecidas como benchmarks, têm a finalidade de avaliar a capacidade da máquina em solucionar uma variedade de problemas matemáticos ou mesmo realizar simulações de cenários do mundo real." (p. 16)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) define benchmarks como ferramentas projetadas para submeter sistemas computacionais a cargas de trabalho padronizadas e mensuráveis, com o propósito de avaliar objetivamente a capacidade de processamento do hardware sob avaliação. A necessidade de tais instrumentos surge da complexidade crescente dos sistemas de hardware e software de alto desempenho, que demanda critérios formalizados de eficiência e comparação.

- **Onde Encaixar no Artigo LaTeX:** **Introdução** — justificativa da escolha do Geekbench 6 como instrumento de avaliação; **Fundamentação Teórica** — definição formal de benchmark.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: são os scores brutos produzidos pelo Geekbench 6 — equivalente exato à saída dos benchmarks da suíte Rodinia analisados pelo autor.

---

### 3.2 Intel RAPL como Ferramenta de Medição de Potência e Energia

- **Conceito/Teoria:** O Intel RAPL (Running Average Power Limit) é um conjunto de registradores MSR (Model-Specific Registers) que permite monitorar programaticamente o consumo de energia da CPU, núcleos IA, GPU integrada e DRAM em processadores Intel modernos.

- **Citação Direta (Ipsis Litteris):**
  > "A funcionalidade Intel RAPL (Running Average Power Limit) é um recurso de hardware incorporado em processadores Intel mais modernos, proporcionando a capacidade de monitorar o consumo de energia da CPU, e em alguns casos, da DRAM e da GPU integrada, de maneira programática." (p. 33)

- **Citação Direta Complementar:**
  > "O RAPL é um conjunto de Model-Specific Registers (MSRs) adequados para rastrear o consumo de energia e foi introduzido na linha de processadores Sandy Bridge. [...] Os MSRs RAPL são registradores de 32 bits e são atualizados aproximadamente a cada 1 milissegundo, o que permite a coleta de informações de consumo de energia em tempo real (ou quase em tempo real)." (p. 34)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), fundamentado em Khan et al. (2018), descreve o Intel RAPL como um recurso de hardware integrado aos processadores Intel a partir da microarquitetura Sandy Bridge, capaz de registrar o consumo energético dos domínios PKG (pacote), PP0 (núcleos IA), PP1 (GPU integrada) e DRAM com granularidade temporal de aproximadamente 1 ms. A interface opera via registradores MSR de 32 bits, cujos valores são expostos ao software por meio do subsistema `powercap` do kernel Linux, sendo atualizados a cada milissegundo — o que permite a instrumentação de consumo energético em tempo quasi-real durante a execução de benchmarks.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre ferramentas de medição de potência; embasamento teórico para justificar o uso do HWiNFO64 como equivalente funcional do RAPL no ambiente Windows.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`: coluna equivalente ao domínio PKG do RAPL, que integra potência dos núcleos IA, GT e System Agent.
  - `maqD_rodada_*.CSV` → `Potência de núcleos IA (W)`: equivalente ao domínio PP0 do RAPL.
  - `maqD_rodada_*.CSV` → `Potência total de DRAM (W)`: equivalente ao domínio DRAM do RAPL.
  - `maqD_rodada_*.CSV` → `IGPU Potência (W)`: equivalente ao domínio PP1 do RAPL.

---

### 3.3 Benchmarks CPU-Bound e o Perfil de Utilização de Recursos

- **Conceito/Teoria:** Benchmarks classificados como CPU-bound são aqueles cujo gargalo de desempenho reside no processador — ou seja, a maior parte do consumo energético e do tempo de execução é atribuída à CPU, e não à memória ou ao armazenamento.

- **Citação Direta (Ipsis Litteris):**
  > "Ao analisar a média percentual de consumo, percebemos que este benchmark consome predominantemente mais de 80% de CPU em todos os casos." (p. 61 — referindo-se ao LU Decomposition)

- **Citação Direta Complementar (LavaMD e Myocyte):**
  > "A análise da distribuição média entre CPU e DRAM neste benchmark revela uma predominância significativa no uso de CPU, ultrapassando os 90%." (p. 63 — referindo-se ao LavaMD)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) demonstra empiricamente que os benchmarks da suíte Rodinia utilizados em seu estudo (LU Decomposition, StreamCluster, LavaMD, Myocyte e Back Propagation) apresentam perfil consistentemente CPU-bound, com o processador absorvendo entre 79% e 93% do consumo energético total registrado pelo Intel RAPL em todas as configurações de compilador testadas. Esse comportamento evidencia que, para cargas de trabalho intensivas em computação numérica paralela, a capacidade do processador — medida por frequência de clock, número de núcleos e eficiência microarquitetural — é o fator dominante de desempenho.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — definição de cargas CPU-bound; **Resultados e Discussão** — justificativa de que os scores do Geekbench 6 refletem primariamente a capacidade de processamento (CPU), sendo a memória e o armazenamento fatores secundários (porém não desprezíveis para a Máquina D com HD SATA).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Uso total da CPU (%)`: confirmar o perfil CPU-bound do Geekbench 6 para a Máquina D; espera-se utilização próxima a 100% durante as 20 rodadas.
  - `maqD_rodada_*.CSV` → `Carga da memória física (%)`: verificar se a memória RAM também satura; se sim, pode indicar pressão simultânea de CPU e RAM.
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: os scores sintetizam o desempenho CPU-bound de cada máquina.

---

### 3.4 Paralelismo Multi-Thread com OpenMP e Uso de Múltiplos Núcleos

- **Conceito/Teoria:** OpenMP (Open Multi-Processing) é uma API de paralelismo de memória compartilhada que permite a paralelização de laços e regiões de código em processadores multi-core, escalando o desempenho conforme o número de threads disponíveis.

- **Citação Direta (Ipsis Litteris):**
  > "A interface de programação de aplicativos (API) OpenMP (Open Multi-Processing) foi inicialmente lançada em 1997 e é um padrão para escrever aplicações paralelas de memória compartilhada em C, C++ e Fortran. O OpenMP oferece a vantagem de ser facilmente implementado em códigos seriais existentes que permite uma paralelização incremental. Além disso, destaca-se por ser amplamente utilizado, altamente portátil e idealmente adequado para arquiteturas multi-core, que tornam-se cada vez mais populares em computadores desktop do dia a dia." (p. 20)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), com base em Kiessling (2009), apresenta o OpenMP como o padrão dominante para exploração de paralelismo de memória compartilhada em arquiteturas multi-core, destacando sua portabilidade e facilidade de integração incremental em código sequencial. A eficácia do OpenMP está intrinsecamente ligada ao número de núcleos físicos e threads lógicas disponíveis no processador: sistemas com maior número de threads exploram mais eficientemente as diretivas de paralelização, reduzindo o tempo de execução de benchmarks computacionalmente intensivos.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre paralelismo a nível de thread e diferenças entre núcleos físicos e threads lógicas; embasamento para discutir a diferença entre o i5-8265U (4 núcleos / 8 threads, Máquina D) e os demais processadores do grupo.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Core 0 T0 Uso (%)`, `Core 0 T1 Uso (%)`, `Core 1 T0 Uso (%)` ... `Core 3 T1 Uso (%)`: monitorar a utilização individual de cada thread durante as rodadas do Geekbench 6. Cargas de CPU próximas a 100% em todos os threads confirmam exploração plena do paralelismo.
  - `maqD_rodada_*.CSV` → `Core C0 Ocupação (avg) (%)`: mede o tempo em que os núcleos estão em estado ativo (não em modo de baixo consumo), confirmando a carga de trabalho paralela efetiva.
  - `scores_maq*.txt` → coluna `Multi_Core`: reflete diretamente o ganho de paralelismo; a razão `Multi_Core / Single_Core` é um indicador do speedup real obtido pela Máquina D com seus 4 núcleos / 8 threads.

---

### 3.5 Crescimento Exponencial do Consumo Energético em Função da Carga

- **Conceito/Teoria:** Em benchmarks de álgebra linear e simulações numéricas, o consumo energético e o tempo de execução crescem de forma exponencial com o tamanho da entrada, modelado pela função `f(x) = a · b^x`, onde `b` é o fator de crescimento e diferencia compiladores entre si.

- **Citação Direta (Ipsis Litteris):**
  > "Ao analisar o gráfico comparativo do consumo total de energia para o Benchmark Lu Decomposition, emerge uma tendência exponencial. [...] Observa-se claramente uma propensão a um maior crescimento de consumo no benchmark compilado em Clang em comparação aos demais. [...] Essa disparidade no fator de crescimento não só destaca a variação no padrão de consumo entre os compiladores, mas também fornece informações valiosas sobre o desempenho diferenciado do Benchmark Lu Decomposition sob diferentes ambientes de compilação."
  > A equação apresentada pelo autor é: $f(x) = a \cdot b^x$ (p. 59)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) observa que o consumo energético do benchmark LU Decomposition cresce exponencialmente em função do tamanho da entrada, podendo ser modelado pela função $f(x) = a \cdot b^x$, onde o fator de crescimento $b$ varia entre compiladores: o Clang apresentou o maior fator de crescimento exponencial, implicando penalidade energética crescente com o aumento da carga; o ICC, por sua vez, apresentou o menor fator $b$, evidenciando maior eficiência de otimização de código para cargas pesadas. Esse resultado tem implicações diretas para sistemas embarcados ou de baixo TDP, como notebooks, onde o limite de potência (PL1 e PL2) pode ser atingido mais rapidamente sob cargas com crescimento exponencial de demanda.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — comportamento esperado do consumo energético sob carga crescente; **Resultados e Discussão** — discussão da tendência dos scores Multi-Core em rodadas consecutivas e possíveis efeitos de aquecimento cumulativo (thermal throttling).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`: plotar a evolução da potência ao longo das 20 rodadas; se crescer progressivamente, indica efeito cumulativo de aquecimento.
  - `maqD_rodada_*.CSV` → `Limite de potência PL1 (Dynamic) (W)` e `Limite de potência PL2 (Dynamic) (W)`: verificar se os limites de potência são atingidos durante as rodadas, forçando redução de clock.
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: a possível tendência de queda dos scores nas últimas rodadas pode indicar saturação térmica com comportamento análogo ao crescimento exponencial de consumo documentado pelo autor.

---

### 3.6 Relação Direta entre Tempo de Execução e Consumo Energético (Correlação Perfeita)

- **Conceito/Teoria:** Em benchmarks CPU-bound executados em hardware estável, o consumo energético total é diretamente proporcional ao tempo de execução, formando uma relação de correlação próxima a 1,00. Isso implica que qualquer fator que aumente o tempo de execução (throttling térmico, frequência reduzida, gargalo de memória) também aumenta o consumo energético total.

- **Citação Direta (Ipsis Litteris):**
  > "Ao estabelecermos uma correlação entre o tempo de execução e o consumo total de cada compilador empregado no Stream Cluster, torna-se evidente uma relação direta entre essas variáveis. [...] Essa representação gráfica aponta para uma conexão intrínseca entre o tempo de execução e o consumo total." (p. 58)

- **Citação Direta Complementar:**
  > "Ao correlacionar o tempo de duração das execuções com seus consumos totais, observamos uma relação de 1 para 1 em suas compilações correspondentes [...]. Essa proporção direta sugere que, à medida que o tempo de execução aumenta ou diminui, o consumo total acompanha essa variação de maneira proporcional, indicando uma estreita correspondência entre essas duas métricas cruciais." (p. 60 — referindo-se ao LU Decomposition)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) demonstra empiricamente, por meio de gráficos de correlação, que todos os cinco benchmarks avaliados apresentam correlação próxima de 1,00 entre tempo de execução e consumo energético total, independentemente do compilador utilizado. Esse resultado valida o modelo teórico de que, para cargas de trabalho com potência de processamento aproximadamente constante durante a execução (P ≈ cte), a energia total consumida é dada por $E = P \cdot t$, de modo que qualquer variação no tempo de execução reflete-se proporcionalmente no consumo de energia. Para o contexto do presente trabalho, isso implica que scores de benchmark mais baixos — indicadores de maior tempo de execução por unidade de trabalho — correspondem diretamente a maior consumo energético por rodada.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — relação entre métricas de desempenho e consumo energético; **Resultados e Discussão** — justificativa para correlacionar scores do Geekbench 6 com as colunas de potência do HWiNFO64.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`: calcular a média por rodada; o produto `Potência_média × duração_da_rodada` é o estimador de energia consumida por rodada.
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: scores mais altos ↔ menor tempo de execução ↔ menor consumo energético por tarefa. A correlação esperada é negativa entre score e consumo médio de potência normalizado pela duração.

---

### 3.7 Detecção de Outliers e Anomalias Estatísticas com Boxplot

- **Conceito/Teoria:** O boxplot é uma técnica de visualização estatística que permite identificar outliers (valores discrepantes) em distribuições de dados, sendo fundamental para garantir a integridade das análises de desempenho antes de calcular médias e desvios padrões.

- **Citação Direta (Ipsis Litteris):**
  > "Nesta observação visual, fica evidente que, à exceção do benchmark Myocyte [...] nenhum dos outros benchmarks [...] apresenta qualquer anomalia aparente em seus dados. Diante desse cenário, optaremos por realizar uma análise mais detalhada exclusivamente nos dados referentes ao benchmark Myocyte, onde se destaca a possível presença de outliers que requerem uma investigação minuciosa." (p. 70)

- **Citação Direta Complementar (EXIT_CODE SIGKILL):**
  > "É relevante observar que o ajuste foi realizado considerando um EXIT_CODE diferente de zero [...]. O EXIT_CODE destacado possui o valor 137, que corresponde a SIGKILL, indicando que o sistema interrompeu o processo de maneira inesperada para evitar o travamento do mesmo." (p. 72)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) incorpora a análise de outliers via Boxplot como etapa obrigatória do pipeline de tratamento de dados, anterior ao cálculo das médias percentuais de consumo. O autor identifica que o benchmark Myocyte — compilado em Clang e ICC — gerou valores anômalos correspondentes a interrupções forçadas pelo sistema operacional (sinal SIGKILL, código de saída 137), caracterizando falhas de execução que distorceriam as médias finais se não fossem detectadas e tratadas. Esse caso é arquiteturalmente relevante: o comportamento de SIGKILL indica que o processo ultrapassou o limite de memória ou tempo alocado pelo SO, fenômeno que pode ocorrer na Máquina D sob carga pesada de Multi-Core devido à RAM limitada a 8 GB em Single Channel.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificativa do protocolo de validação estatística das 20 rodadas por máquina; **Resultados e Discussão** — identificação de rodadas anômalas que devem ser descartadas antes de calcular médias finais.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core` de todas as rodadas: aplicar boxplot para identificar rodadas discrepantes em cada máquina. Rodadas com score Z-score > 2,5 devem ser investigadas.
  - `maqD_rodada_*.CSV` → `Carga da memória física (%)`: verificar se rodadas com score baixo (possíveis outliers) correspondem a momentos de alta pressão de memória — evidência de gargalo RAM na Máquina D.
  - `maqD_rodada_*.CSV` → `Utilização do arquivo de paginação (%)`: uso elevado de swap indica pressão de memória física, podendo causar degradação de desempenho anômala e scores outliers.

---

### 3.8 One-Class SVM para Detecção de Anomalias em Dados de Desempenho

- **Conceito/Teoria:** O algoritmo One-Class SVM (Support Vector Machine) é um método de aprendizado de máquina não supervisionado que modela a distribuição dos dados normais e classifica como anomalias todos os pontos que se desviam significativamente dessa distribuição aprendida.

- **Citação Direta (Ipsis Litteris):**
  > "Com base no Boxplot apresentado na Figura 25, implementou-se uma adaptação do modelo de aprendizado com o GCC como referência, uma vez que este não apresentava quaisquer anomalias. [...] Após essa calibração, prosseguiu-se com a análise dos dados pós-treinamento, evidenciando a frequência de anomalias nos dados das compilações do Clang e do ICC." (p. 72–73)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) aplica o algoritmo One-Class SVM para refinamento da detecção de anomalias nos dados do benchmark Myocyte, usando os dados coletados pelo compilador GCC — que não apresentou outliers no Boxplot preliminar — como conjunto de treinamento de referência. O modelo treinado é então aplicado aos dados dos compiladores Clang e ICC para quantificar a proporção de amostras anômalas, revelando padrões de comportamento atípico que confirmam a presença de erros de execução intermitentes. Essa abordagem em dois estágios (Boxplot → SVM) é metodologicamente robusta e pode ser adaptada para a validação das 20 rodadas de Geekbench 6 nas quatro máquinas do nosso experimento.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — protocolo de validação de dados; mencionável como método avançado alternativo ao simples descarte de outliers por Z-score.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: treinar o modelo com as rodadas consideradas normais (ex.: rodadas com scores dentro do intervalo IQR) e detectar anomalias nas demais.
  - `maqD_rodada_*.CSV` → `CPU Inteira (°C)` e `Núcleo máximo (°C)`: incluir temperatura como feature adicional do modelo para distinguir anomalias termicamente induzidas (thermal throttling) de anomalias por sobrecarga de memória.

---

### 3.9 Eficiência Relativa entre Compiladores: ICC, GCC e Clang

- **Conceito/Teoria:** A eficiência de um compilador pode ser quantificada pela diferença percentual média do consumo energético total em relação a um compilador de referência (GCC). Diferenças positivas indicam maior consumo (menor eficiência); negativas indicam menor consumo (maior eficiência).

- **Citação Direta (Ipsis Litteris):**
  > "A análise indica que, do total de energia consumida, o GCC foi responsável por 33,23%, o Clang por 36,01%, e o ICC por 30,76%, respectivamente. Além disso, o ICC demonstrou ser 7,43% mais eficiente que o GCC, enquanto o Clang foi 8,35% menos eficiente." (Resumo, p. 7)

- **Citação Direta Complementar (impacto por benchmark individual):**
  > "Notamos uma redução média de 15,13% no consumo pelo ICC em relação ao GCC e um aumento médio de 10,87% pelo Clang." (p. 59 — StreamCluster)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) demonstra que a escolha do compilador impacta significativamente a eficiência energética de aplicações de computação intensiva, com variações de até 15% entre compiladores para um mesmo benchmark. Desconsiderando as anomalias do benchmark Myocyte, o ICC Intel C++ Compiler revelou-se o mais eficiente (30,76% do consumo total), seguido pelo GCC (33,23%) e pelo Clang (36,01%), correspondendo a uma vantagem de 7,43% do ICC sobre o GCC. Esse resultado é atribuível às otimizações de alto nível (IPO, PGO e HLO) implementadas pelo ICC especificamente para arquiteturas Intel, que produzem código-objeto mais bem adaptado às características microarquiteturais do processador em uso.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — introdução ao conceito de eficiência microarquitetural e desempenho por watt; **Resultados e Discussão** — analogia com a nossa métrica de eficiência relativa entre máquinas (desempenho por watt = Score Geekbench / Potência média da CPU).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: numerador da nossa métrica de eficiência.
  - `maqD_rodada_*.CSV` → `Potência total da CPU (W)`: denominador da nossa métrica de eficiência. A equação análoga à análise do autor é: $\eta = \text{Score} / \overline{P}_{\text{CPU}}$.

---

### 3.10 Impacto das Otimizações de Alto Nível do Compilador na Arquitetura do Processador

- **Conceito/Teoria:** Compiladores modernos aplicam otimizações interprocedurais (IPO), guiadas por perfil (PGO) e de alto nível (HLO) para explorar características específicas da microarquitetura do processador, como pipelines, vetorização SIMD e previsão de desvios.

- **Citação Direta (Ipsis Litteris):**
  > "O Intel C Compiler vai além da simples compilação e incorpora três técnicas distintas de otimização de alto nível para programas compilados:
  > 1. Otimização Interprocedural (IPO): Esta técnica visa aprimorar o desempenho considerando a inter-relação entre diferentes partes do código.
  > 2. Otimização Guiada por Perfil (PGO): A otimização PGO baseia-se na análise do comportamento do programa durante a execução onde ajusta o código para as características específicas de uso.
  > 3. Otimizações de Alto Nível (HLO): Essas otimizações visam melhorar o código em um nível mais abstrato que incorpora melhorias que transcendem a estrutura individual das funções." (p. 23–24)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), com base em Ren (2014) e Machado et al. (2017), descreve como o compilador ICC Intel aplica três classes de otimizações microarquiteturais — IPO (Otimização Interprocedural), PGO (Otimização Guiada por Perfil) e HLO (Otimizações de Alto Nível) — que em conjunto exploram características específicas dos processadores Intel para maximizar a eficiência do código gerado. Esse nível de especialização arquitetural explica por que o ICC supera o GCC e o Clang em eficiência energética para benchmarks executados em hardware Intel: as otimizações são calibradas para a microarquitetura específica do processador em uso, como a previsão de desvios, o prefetching de cache e as instruções SIMD disponíveis.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre eficiência microarquitetural e IPC (Instruções por Ciclo); conexão com a coluna `Relógios efetivos núcleo (avg) (MHz)` vs. score final do Geekbench 6 (nossa análise de IPC relativo).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)` vs. `Relógios núcleo (avg) (MHz)`: a razão entre clock efetivo e clock nominal é um proxy do IPC relativo — um clock efetivo próximo ao nominal com alto score indica alto IPC.
  - `maqD_rodada_*.CSV` → `Relação do relógio do núcleo (avg) (x)`: o multiplicador de clock mostra se o processador operou no boost máximo ou foi limitado por throttling.
  - `scores_maq*.txt` → coluna `Single_Core`: reflete diretamente a eficiência por ciclo (IPC × frequência efetiva), sendo a métrica mais sensível à microarquitetura.

---

### 3.11 Tamanho do Binário Gerado como Indicador de Qualidade de Otimização

- **Conceito/Teoria:** O tamanho do arquivo binário gerado pelo compilador é um indicador da estratégia de otimização adotada: binários maiores podem indicar maior expansão de código por inlining e desenrolamento de loops; binários menores podem indicar eliminação mais agressiva de código morto.

- **Citação Direta (Ipsis Litteris):**
  > "A nossa análise revela uma tendência positiva quando os arquivos executáveis possuem tamanhos maiores. Isso sugere que os compiladores capazes de obter melhor desempenho são provavelmente aqueles que geram binários maiores, indicando possivelmente um uso mais cauteloso de abreviações em sua escrita e proporcionando um arquivo mais detalhado para interpretação pelo processador." (p. 78)

- **Citação Direta Complementar (dados quantitativos):**
  > "Ao examinar a LU Decomposition, percebemos que o Clang gerou um arquivo aproximadamente 15% menor em comparação ao GCC, enquanto o ICC produziu um arquivo significativamente maior, cerca de 384% maior." (p. 77)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) observa correlação empírica entre o tamanho dos binários gerados e a eficiência de desempenho, com o ICC produzindo binários entre 147% e 468% maiores que o GCC, enquanto o Clang gerou binários comparáveis ou até menores. O autor interpreta essa correlação como evidência de que o ICC emprega técnicas de expansão de código mais agressivas — como inlining interprocedural e desenrolamento de loops — que aumentam o tamanho do executável mas reduzem o número de ciclos necessários para a execução. Esse trade-off entre footprint de memória e eficiência computacional é particularmente relevante em sistemas com cache L3 limitada, como o Intel Core i7-5500U (4 MB de cache L3) utilizado pelo autor.

> ⚠️ **NOTA EDITORIAL — Máquinas A, B e C:**
> Este trecho é relevante para discutir o impacto do tamanho do cache L3 no desempenho entre as
> máquinas do nosso grupo. A Máquina D possui 6 MB de cache L3 (i5-8265U), enquanto as Máquinas
> A, B e C podem ter configurações diferentes. Este trecho teórico e seu respectivo mapeamento de
> colunas foram devidamente fichados de forma preditiva e **só serão utilizados na redação final
> conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo
> nas próximas interações, se necessário.**

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — hierarquia de memória e impacto do cache L3 no desempenho; **Resultados e Discussão** — ao discutir por que a Máquina D pode apresentar scores distintos das demais mesmo com clock similar.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Ring/LLC Relógio (MHz)`: o clock do Last Level Cache (LLC = L3) indica a frequência de operação da cache compartilhada; valores mais altos reduzem a latência de acesso e podem compensar binários maiores.
  - `maqD_rodada_*.CSV` → `Relógio da memória (MHz)`: frequência da RAM; para a Máquina D (DDR4 1333 MHz Single Channel), a baixa largura de banda pode ser gargalo para binários maiores com alto volume de dados na hierarquia de memória.

---

### 3.12 Variabilidade Estatística dos Resultados de Benchmark (Desvio Padrão)

- **Conceito/Teoria:** O desvio padrão amostral dos resultados de benchmark quantifica a variabilidade das medições entre rodadas, sendo um indicador de estabilidade do sistema. Alta variabilidade pode indicar presença de outliers, interferência de processos de background, throttling térmico intermitente ou gargalos de I/O.

- **Citação Direta (Ipsis Litteris):**
  > "Numa análise inicial, os resultados deste benchmark apresentam peculiaridades que despertam surpresa. Uma irregularidade estatística torna-se evidente, sobretudo nos inputs situados entre aproximadamente 660 e 760, tanto na compilação com Clang quanto na compilada com ICC. [...] Essa disparidade levanta suspeitas de incoerências que merecem uma investigação." (p. 67 — referindo-se ao Myocyte)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) demonstra que irregularidades estatísticas nos resultados de benchmark — traduzidas por picos de consumo energético que desviam significativamente da tendência central — podem ter causas arquiteturais identificáveis, como interrupções forçadas do sistema operacional (SIGKILL), pressão de memória ou comportamento não-determinístico do scheduler de threads. Para o presente trabalho, o desvio padrão amostral das 20 rodadas por máquina cumpre papel metodológico equivalente: além de quantificar a reprodutibilidade dos scores, serve como sinalizador de instabilidade arquitetural — um desvio padrão elevado em uma máquina específica pode indicar throttling térmico intermitente (especialmente na Máquina D, com HD SATA que pode introduzir latências variáveis no carregamento dos workloads do Geekbench 6).

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — apresentação e justificativa das fórmulas de média e desvio padrão amostral; **Resultados e Discussão** — interpretação arquitetural do desvio padrão alto/baixo por máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: calcular desvio padrão amostral ($s$) das 20 rodadas por máquina. Um alto $s$ na Máquina D pode indicar throttling térmico (detectável via `CPU Inteira (°C)`) ou variabilidade de I/O (detectável via `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`).
  - `maqD_rodada_*.CSV` → `Estrangulamento térmico do núcleo (avg) (Yes/No)`: confirmar se rodadas com score baixo coincidem com eventos de throttling térmico.
  - `maqD_rodada_*.CSV` → `IA: Package-Level RAPL/PBM PL1 (Yes/No)`: confirmar se o limite de potência PL1 foi atingido durante rodadas com score baixo.

---

### 3.13 Relação entre Tempo de Execução, Consumo de DRAM e Banda de Memória

- **Conceito/Teoria:** Em benchmarks CPU-bound, a memória DRAM representa uma fração menor do consumo total (tipicamente 7–21%), mas pode se tornar um gargalo arquitetural em sistemas com configuração Single Channel ou baixa frequência de RAM.

- **Citação Direta (Ipsis Litteris):**
  > "Ao examinarmos as percentagens médias dos componentes individuais em relação ao consumo total, torna-se evidente que o Stream Cluster, de acordo com o propósito inicial do benchmark, é predominantemente consumidor de recursos da CPU em ambos os compiladores. [Distribuição: CPU = 81,56%–83,88%; DRAM = 16,09%–18,42%]" (p. 58)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) constata que, mesmo em benchmarks predominantemente CPU-bound, a DRAM absorve entre 6% e 21% do consumo energético total dependendo do tipo de carga: benchmarks de dinâmica molecular (LavaMD, Myocyte) com mais de 90% de CPU e menos de 10% de DRAM, enquanto benchmarks de clustering (StreamCluster) e de álgebra linear (LU Decomposition) apresentam maior demanda de DRAM (13–18%). Esse dado é arquiteturalmente relevante para a Máquina D: com RAM DDR4 1333 MHz operando em Single Channel (largura de banda teórica ≈ 10,66 GB/s), o subsistema de memória pode se tornar gargalo em benchmarks com alta intensidade de acessos à memória, deprimindo os scores Multi-Core de maneira desproporcional ao número de núcleos disponíveis.

> ⚠️ **NOTA EDITORIAL — Máquinas A, B e C:**
> Se qualquer das Máquinas A, B ou C operar com memória Dual Channel ou frequência DDR4 superior
> a 2133 MHz, a diferença de largura de banda em relação à Máquina D poderá ser discutida com
> base neste trecho. **Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente
> fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais
> de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se
> necessário.**

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — gargalo de Von Neumann e impacto de Single Channel vs. Dual Channel; **Resultados e Discussão** — ao discutir possível penalidade de largura de banda da Máquina D vs. outras máquinas com RAM Dual Channel.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Relógio da memória (MHz)`: confirmar a frequência real de operação da RAM durante as rodadas (esperado: 1333 MHz para a Máquina D).
  - `maqD_rodada_*.CSV` → `Carga da memória física (%)`: valores elevados (>80%) indicam pressão sobre o subsistema de memória, podendo degradar scores Multi-Core.
  - `maqD_rodada_*.CSV` → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: taxas de I/O do HD SATA; picos de leitura durante benchmark indicam acesso a disco (swap ou carregamento de dados), causando latências imprevisíveis.

---

### 3.14 Suíte de Benchmarks Rodinia e o Modelo de Avaliação Multi-Domínio

- **Conceito/Teoria:** A suíte Rodinia é um conjunto diversificado de benchmarks para avaliação de sistemas de computação paralela, organizado segundo a Taxonomia Berkeley Dwarf, que classifica cargas de trabalho por padrões de paralelismo e acesso à memória.

- **Citação Direta (Ipsis Litteris):**
  > "O Rodinia se destaca de outros conjuntos de benchmarks por meio de várias características distintas: [1] Aproveita Hierarquias de Memória Não Tradicionais [...] [2] Versões Múltiplas com Camadas de Otimização [...] [3] Modelo de 'Offloading' [...] [4] Desafio para Compiladores: O Rodinia fornece um conjunto de aplicativos que, devido à complexidade ou características específicas, podem representar um desafio para os compiladores na geração automática de código acelerador." (p. 26–27)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), com base em Che et al. (2010), descreve a suíte Rodinia como uma coleção de benchmarks especialmente concebida para avaliar arquiteturas paralelas heterogêneas, caracterizando-se pela cobertura de múltiplos domínios de aplicação (álgebra linear, bioinformática, mineração de dados, processamento de imagens e simulações físicas) e pela exploração de hierarquias de memória não convencionais. A diversidade de padrões de acesso à memória e de intensidade computacional dos benchmarks Rodinia os torna representativos de cargas de trabalho reais, o que justifica sua ampla adoção como referência na literatura de avaliação de desempenho de processadores multi-core.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — contextualização do Geekbench 6 como suite sintética multi-domínio; analogia com a diversidade de workloads da Rodinia para justificar o uso de scores Single-Core e Multi-Core como métricas complementares.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: ambos os scores do Geekbench 6 são compostos por sub-testes de múltiplos domínios (processamento de imagem, criptografia, compressão, ML), analogamente à cobertura multi-domínio da Rodinia.

---

### 3.15 Protocolo de Coleta Padronizada e Reprodutibilidade Experimental

- **Conceito/Teoria:** A reprodutibilidade de experimentos de benchmarking requer a padronização rigorosa do protocolo de coleta: mesma carga de entrada, mesmo número de repetições, mesmas condições ambientais e mesma metodologia de exclusão de outliers.

- **Citação Direta (Ipsis Litteris):**
  > "O método de coleta foi estabelecido da seguinte maneira: foi determinado um valor máximo de entrada, garante assim que o sistema não seja sobrecarregado a ponto de travar, mas permanecesse próximo desse limite, servindo como uma carga máxima para o sistema. [...] Este método pode ser descrito da seguinte maneira: $\frac{V_{max} - V_{min}}{128} = \text{Value}$" (p. 51)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) estabelece um protocolo de coleta que determina empiricamente o valor máximo de entrada para cada benchmark (aquele que leva o sistema ao limite sem causar travamento) e distribui 128 amostras igualmente espaçadas entre o valor mínimo e o máximo. Essa abordagem garante cobertura uniforme do espaço de carga e reprodutibilidade das medições. Para o contexto do presente trabalho, o protocolo análogo consiste na execução de 20 rodadas idênticas do Geekbench 6 por máquina, com o sistema em estado limpo (sem processos de background ativos), garantindo que os scores reflitam exclusivamente a capacidade arquitetural de cada hardware.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — justificativa do protocolo de 20 rodadas padronizadas por máquina com o Geekbench 6; comparação com a metodologia do autor.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → todas as 20 rodadas de `Single_Core` e `Multi_Core` por máquina: verificar uniformidade da distribuição dos scores para confirmar a padronização do protocolo de coleta.
  - `maqD_rodada_*.CSV` → verificar o horário (`Date`, `Time`) de cada rodada: intervalos muito curtos entre rodadas podem indicar que o sistema não esfriou adequadamente, introduzindo viés térmico acumulativo.

---

### 3.16 Hardware do Experimento: Processador de 2 Núcleos como Baseline Comparativo

- **Conceito/Teoria:** O hardware utilizado no experimento influencia diretamente os resultados obtidos. O processador Intel Core i7-5500U (2 núcleos, 4 threads, DDR3L 1600 MHz) utilizado por Damasceno (2023) é um baseline relevante de comparação com os processadores das nossas quatro máquinas.

- **Citação Direta (Ipsis Litteris):**
  > "O sistema computacional empregado para a execução deste estudo está equipado com uma unidade central de processamento (CPU) Intel Core i7 5500U. Este processador apresenta uma frequência base de operação de 2400 MHz (2.4 GHz) e pode operar em modo turbo que atinge uma frequência de 3000 MHz (3.0 GHz). Composta por dois núcleos físicos e quatro threads, a CPU foi fabricada na litografia de 14 nm e pertence à microarquitetura Haswell." (p. 45)

- **Citação Direta Complementar (memória):**
  > "No que diz respeito à memória de acesso randômico (RAM), o sistema utiliza uma capacidade total de 10 GB. Essa memória RAM é baseada na arquitetura DDR3L [...] a uma frequência de 1600 MHz (1.6 GHz)." (p. 45)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) conduz seus experimentos em um processador Intel Core i7-5500U de 5ª geração (microarquitetura Broadwell, 14 nm), com 2 núcleos físicos e 4 threads lógicas, clock base de 2,4 GHz e boost de 3,0 GHz, equipado com 10 GB de RAM DDR3L a 1600 MHz. Esse hardware, embora da mesma família Intel que o i5-8265U da Máquina D do nosso grupo (Whiskey Lake-U, 8ª geração, 14 nm, 4 núcleos/8 threads, boost de 3,9 GHz), é arquiteturalmente inferior em número de núcleos e velocidade de clock, além de operar com memória DDR3L em vez de DDR4. Essa diferença geracional permite contextualizar os resultados do presente trabalho: a Máquina D possui mais do dobro de threads e clock boost 30% superior ao hardware de referência do autor.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — tabela comparativa de hardware das 4 máquinas; footnote ou referência cruzada para contextualizar os valores de potência e desempenho esperados.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → `Single_Core` e `Multi_Core` da Máquina D: como o i5-8265U tem o dobro de núcleos físicos em relação ao i7-5500U de Damasceno (2023), espera-se que o score Multi-Core da Máquina D seja aproximadamente o dobro do score Single-Core, refletindo o ganho de paralelismo.
  - `maqD_rodada_*.CSV` → `Core 0 Relógio (MHz)` ... `Core 3 Relógio (MHz)`: monitorar os clocks individuais de cada núcleo; o i5-8265U possui 4 núcleos vs. 2 do i7-5500U — todos 4 núcleos ativos em cargas Multi-Core é o diferencial esperado.

---

### 3.17 Arquiteturas Híbridas P-Core/E-Core e Heterogeneidade de Núcleos

- **Conceito/Teoria:** Processadores Intel a partir da 12ª geração (Alder Lake) introduzem uma arquitetura híbrida composta por núcleos de performance (P-cores) e núcleos de eficiência (E-cores), cada um com microarquitetura, clock e consumo distintos, exigindo escalonamento heterogêneo por parte do sistema operacional (Intel Thread Director).

- **Citação Direta (Ipsis Litteris):**
  > "Composta por dois núcleos físicos e quatro threads, a CPU foi fabricada na litografia de 14 nm e pertence à microarquitetura Haswell." (p. 45)

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora o hardware de referência de Damasceno (2023) — Intel Core i7-5500U, microarquitetura Haswell de 2 núcleos homogêneos — não contemple heterogeneidade de núcleos, o autor estabelece a premissa de que o número de núcleos físicos e threads lógicas é determinante direto do desempenho Multi-Core observado nos benchmarks paralelizados via OpenMP. Essa premissa, generalizada para arquiteturas híbridas modernas, implica que o desempenho Multi-Core de processadores com P-cores e E-cores (como o i5-13420H da Máquina A, o i5-1334U da Máquina B e o i5-14600KF da Máquina F) não é uma simples soma proporcional ao número total de threads, pois P-cores e E-cores operam em frequências, IPC (instruções por ciclo) e TDP individuais distintos. O escalonador de threads do Windows 11 — apoiado pelo Intel Thread Director — direciona threads de alta prioridade (como os sub-testes Single-Core do Geekbench 6) preferencialmente aos P-cores, enquanto cargas Multi-Core distribuem trabalho também aos E-cores, que possuem menor clock máximo e ausência de Hyper-Threading.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção dedicada à heterogeneidade de núcleos (P-core/E-core) como evolução do paralelismo simétrico discutido pelo autor; **Resultados e Discussão** — ao comparar os scores Multi-Core das Máquinas A (4P+4E/12T), B (2P+8E/12T) e F (6P+8E/20T) com as máquinas homogêneas C e D (núcleos simétricos).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → `Core 0 Relógio (MHz)` até `Core 3 Relógio (MHz)`: nas Máquinas A, B e F, comparar os clocks dos núcleos individuais para identificar quais correspondem a P-cores (clock mais alto) e quais a E-cores (clock mais baixo), já que o HWiNFO64 numera os núcleos sequencialmente sem distinguir o tipo.
  - `maqA_rodada_*.CSV` → `Core 0 T0 Uso (%)` e `Core 0 T1 Uso (%)`: a presença de utilização em ambos os threads (T0 e T1) de um mesmo núcleo confirma que esse núcleo é um P-core com Hyper-Threading habilitado; E-cores não possuem essa segunda thread lógica.
  - `scores_maq*.txt` → coluna `Multi_Core`: comparar a razão `Multi_Core / Single_Core` entre máquinas homogêneas (C: 4C/8T, D: 4C/8T) e híbridas (A: 8C/12T, B: 10C/12T, F: 14C/20T) para quantificar a perda de eficiência de escalonamento em arquiteturas heterogêneas.

---

### 3.18 Extensões Vetoriais SIMD Avançadas: AVX-512, VNNI e a Diferenciação Microarquitetural

- **Conceito/Teoria:** As extensões SIMD (Single Instruction, Multiple Data) permitem que uma única instrução opere sobre múltiplos dados simultaneamente. O Intel DL Boost (VNNI — Vector Neural Network Instructions) é uma extensão especializada para acelerar operações de inteligência artificial com inteiros de baixa precisão (INT8), disponível apenas nos processadores Intel mais recentes.

- **Citação Direta (Ipsis Litteris):**
  > "As tecnologias SIMD introduzidas pela Intel, como MultiMedia eXtensions (MMX), Streaming SIMD Extensions (SSE), Advanced Vector eXtensions (AVX), Fused Multiply Add (FMA) e AVX-512, representam avanços significativos. O desenvolvimento dos processadores também testemunhou a expansão da largura do registrador de 64 bits para 512 bits, e o aumento do número de registradores vetoriais de 8 para 32. Esses registradores mais amplos proporcionam mais caminhos de paralelismo, enquanto o aumento no número de registradores vetoriais reduz movimentos de dados extras para a memória cache." (p. 37–38, citando Amiri e Shahbahrami 2020)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), ao revisar Amiri e Shahbahrami (2020), descreve a evolução das extensões SIMD da Intel — de MMX a AVX-512 — destacando que registradores vetoriais mais largos (até 512 bits) e mais numerosos (até 32 registradores) ampliam o paralelismo de dados disponível por ciclo de clock e reduzem o tráfego de dados entre registradores e cache. Esse referencial é diretamente aplicável à diferenciação entre as máquinas do nosso grupo: processadores com suporte a Intel DL Boost (VNNI) — Máquinas A, B e F — possuem instruções especializadas para multiplicação-acumulação de inteiros de 8 bits em paralelo, originalmente projetadas para inferência de redes neurais, mas que também beneficiam sub-testes de compressão e processamento de imagem do Geekbench 6. Já os processadores AMD (Máquinas C e E) e o Intel de 8ª geração (Máquina D) carecem dessa extensão, dependendo de FMA3/AVX2 convencionais, potencialmente menos eficientes para cargas vetorizadas de inteiros de baixa precisão.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre paralelismo a nível de instrução (ILP) e extensões SIMD como complemento ao paralelismo de threads já discutido na Seção 3.4 deste fichamento; **Resultados e Discussão** — ao explicar diferenças inesperadas de score Single-Core entre máquinas com clocks de boost semelhantes mas conjuntos de instruções distintos (ex.: Máquina A com VNNI vs. Máquina C sem VNNI).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → coluna `Single_Core`: processadores com VNNI (Máquinas A, B, F) podem apresentar vantagem desproporcional em sub-testes de processamento de imagem e compressão do Geekbench 6 mesmo com clock nominal inferior a processadores sem VNNI.
  - `maqA_rodada_*.CSV`, `maqF_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)`: em cargas fortemente vetorizadas (AVX2/AVX-512), é esperado um *AVX offset* — redução do clock efetivo em relação ao clock nominal — fenômeno documentado para processadores Intel sob carga vetorial pesada, podendo ser identificado comparando esta coluna com `Relógios núcleo (avg) (MHz)`.

---

### 3.19 Memória DDR5 e o Avanço da Largura de Banda em Relação ao DDR4/DDR3L

- **Conceito/Teoria:** A geração DDR5 de memórias RAM oferece frequências base superiores (a partir de 4800 MT/s) e arquitetura interna com dois canais independentes de 32 bits por módulo (Sub-Channels), o que amplia significativamente a largura de banda teórica em relação ao DDR4 e, sobretudo, ao DDR3L utilizado por Damasceno (2023).

- **Citação Direta (Ipsis Litteris):**
  > "No que diz respeito à memória de acesso randômico (RAM), o sistema utiliza uma capacidade total de 10 GB. Essa memória RAM é baseada na arquitetura DDR3L, uma variante da DDR3 com ênfase na eficiência energética [...]. Adicionalmente, a memória opera a uma frequência de 1600 MHz (1.6 GHz) que contribui para um desempenho eficiente e econômico em termos de energia." (p. 45)

- **Paráfrase (Citação Indireta Acadêmica):**
  O hardware de referência de Damasceno (2023) opera com memória DDR3L a 1600 MHz, geração tecnológica duas vezes anterior à DDR5 da Máquina A do nosso grupo (DDR5 5200 MT/s). Embora o autor não discuta explicitamente a influência da geração de memória sobre os resultados de benchmark, a literatura de arquitetura de computadores estabelece que a largura de banda teórica de memória escala proporcionalmente à frequência efetiva e ao número de canais ativos. Para o presente trabalho, esse salto geracional (DDR3L 1600 MHz → DDR4 2400–3600 MHz → DDR5 5200 MT/s) constitui uma variável de controle relevante: mesmo operando em configuração single-channel "lógica" de 1×8GB, a Máquina A se beneficia da arquitetura interna de sub-canais independentes do DDR5, que mitiga parcialmente a desvantagem de não possuir dois módulos físicos — em contraste com a Máquina D (DDR4 Single Channel 1×8GB, sem essa mitigação arquitetural).

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre evolução das gerações de memória DDR e impacto na largura de banda (extensão da discussão de gargalo de Von Neumann); **Resultados e Discussão** — ao comparar o comportamento Multi-Core da Máquina A (DDR5, Single Channel "lógico" mas com sub-canais) frente à Máquina D (DDR4, Single Channel tradicional).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV` → `Relógio da memória (MHz)`: confirmar a frequência efetiva de operação do módulo DDR5 5200 MT/s durante a execução do Geekbench 6.
  - `maqA_rodada_*.CSV` → `Relação do relógio da memória (x)`: razão de multiplicação do controlador de memória, útil para validar se o sistema está operando no perfil JEDEC padrão ou em XMP/EXPO.
  - `maqA_rodada_*.CSV`, `maqD_rodada_*.CSV` → `Carga da memória física (%)`: comparar a pressão sobre a memória física entre a Máquina A (DDR5) e a Máquina D (DDR4), relacionando com eventuais diferenças no score `Multi_Core`.

---

### 3.20 TDP Elevado e Processadores Desktop Multi-Core de Alto Desempenho (Caso da Máquina F)

- **Conceito/Teoria:** O TDP (Thermal Design Power) define o envelope térmico de projeto de um processador e está diretamente relacionado à capacidade de sustentar clocks elevados sob carga Multi-Core prolongada. Processadores desktop com TDP elevado (>100 W) dissipam mais energia, mas também dispõem de maior margem para sustentar o boost máximo em todos os núcleos simultaneamente, fenômeno conhecido como *all-core boost*.

- **Citação Direta (Ipsis Litteris):**
  > "Este processador apresenta uma frequência base de operação de 2400 MHz (2.4 GHz) e pode operar em modo turbo que atinge uma frequência de 3000 MHz (3.0 GHz)." (p. 45)

- **Paráfrase (Citação Indireta Acadêmica):**
  O hardware de referência de Damasceno (2023) opera em um envelope de baixo TDP (típico de processadores U-series para notebooks ultrafinos, na faixa de 15–25 W), com uma diferença de apenas 600 MHz entre clock base e boost. Esse comportamento contrasta fortemente com processadores desktop de TDP elevado, como o i5-14600KF da Máquina F (125 W, 14 núcleos, boost de até 5,3 GHz nos P-cores) e o Ryzen 5 5500 da Máquina E (65 W, 6 núcleos, boost de 4,2 GHz). Em arquitetura de computadores, processadores com maior envelope de potência (TDP) sustentam o boost de clock em todos os núcleos por períodos mais longos (PL2/Tau elevado), uma vez que o limite de dissipação térmica é menos restritivo. Esse fator arquitetural é determinante para explicar por que se espera que a Máquina F atinja o score Multi-Core mais alto do grupo: a combinação de TDP de 125 W com 14 núcleos heterogêneos permite sustentar mais ciclos de clock elevado por núcleo sob carga total do que processadores de notebook restritos a 15–45 W.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre a relação entre TDP, sustentação de boost de clock e arquitetura desktop vs. mobile; **Resultados e Discussão** — comparação direta entre o desempenho sustentado da Máquina F (desktop, 125 W) frente às máquinas notebook do grupo (A, B, C, D), todas limitadas por TDP entre 15 e 45 W.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqF_rodada_*.CSV`, `maqE_rodada_*.CSV` → `Potência total da CPU (W)`: comparar o consumo de pico sustentado das Máquinas E e F (desktops) com o consumo das máquinas notebook, esperando valores mais próximos do TDP nominal (65 W e 125 W, respectivamente) sustentados por mais tempo.
  - `maqF_rodada_*.CSV` → `Limite de potência PL1 (Dynamic) (W)` e `Limite de potência PL2 (Dynamic) (W)`: verificar se a Máquina F atinge e sustenta o PL2 dinâmico por mais tempo que as máquinas notebook antes de retornar ao PL1, validando a hipótese de maior sustentação de boost em desktops.
  - `maqF_rodada_*.CSV` → `Relógios núcleo (avg) (MHz)`: confirmar se os P-cores do i5-14600KF sustentam clocks próximos do boost máximo (5,3 GHz) durante toda a execução do Multi-Core, sem degradação por throttling.
  - `scores_maq*.txt` → coluna `Multi_Core` de todas as máquinas: a Máquina F (TDP 125 W, 14C/20T) é a candidata teórica ao maior score absoluto do grupo, segundo a relação entre TDP e sustentação de boost discutida nesta seção.

---

### 3.21 Armazenamento NVMe via PCIe e o Tempo de Carregamento de Workloads

- **Conceito/Teoria:** A interface PCIe (Peripheral Component Interconnect Express) determina a largura de banda disponível para SSDs NVMe, com gerações sucessivas (PCIe 3.0 → 4.0) dobrando a taxa de transferência teórica por linha (lane). SSDs NVMe sobre PCIe Gen 4.0 alcançam taxas de leitura sequencial muito superiores a HDDs SATA mecânicos, reduzindo a latência de carregamento de dados de benchmarks que dependem de I/O.

- **Citação Direta (Ipsis Litteris):**
  > "Dando Permissão ao Intel RAPL [...] Para a realização da aquisição do consumo energético, tornou-se imperativo conceder permissões para a utilização do Intel RAPL (Running Average Power Limit) por meio de um script externo." (p. 49) — *citação contextual sobre a infraestrutura de coleta, não sobre armazenamento diretamente, mas o autor não discute armazenamento como variável; a lacuna teórica é suprida pela hierarquia de memória já fichada na Seção 3.11 deste documento (Damasceno 2023, p. 78).*

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora Damasceno (2023) não disserte detalhadamente sobre o impacto do tipo de armazenamento — uma vez que seu experimento ocorre majoritariamente em memória RAM sem dependência intensiva de I/O em disco —, o referencial teórico de hierarquia de memória que o autor estabelece na Seção 3.11 deste fichamento (tamanho do binário e tempo de interpretação pelo processador) permite extrapolação direta: o tempo necessário para carregar um binário do disco para a memória RAM antes da execução é parte do tempo total medido em qualquer benchmark, incluindo o Geekbench 6. Para o nosso grupo, esse efeito é mais saliente na Máquina D, cujo armazenamento é um HDD Western Digital Blue SATA de 5400 RPM — ordens de magnitude mais lento que os SSDs NVMe PCIe Gen 4.0 das Máquinas A (via Intel VMD) e F. Em contraste, as Máquinas A e F utilizam SSDs NVMe sobre PCIe 4.0 x4, com taxas de leitura sequencial teóricas que podem superar 7000 MB/s, contra os aproximadamente 100–150 MB/s típicos de um HDD SATA de 5400 RPM — uma diferença de mais de 50×.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre hierarquia de armazenamento (HDD vs. SSD SATA vs. SSD NVMe) como extensão da hierarquia de memória cache já discutida; **Metodologia** — justificativa de por que o tempo de carregamento do aplicativo Geekbench 6 pode variar entre máquinas antes mesmo do início da medição do score; **Resultados e Discussão** — ao discutir se a Máquina D apresenta maior variabilidade (desvio padrão) nos tempos de inicialização do benchmark devido ao HDD mecânico.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Taxa de leituras (MB/s)` e `Temperatura do disco (°C)`: monitorar a atividade do HDD da Máquina D durante a rodada; picos de leitura no início de cada rodada podem indicar tempo de carregamento do binário do Geekbench 6 a partir do disco mecânico.
  - `maqA_rodada_*.CSV`, `maqF_rodada_*.CSV` → `Taxa de leituras (MB/s)`: nas Máquinas A e F (SSD NVMe PCIe Gen 4.0), espera-se picos de leitura ordens de magnitude mais rápidos e de duração muito mais curta que na Máquina D.
  - `maqD_rodada_*.CSV` → `Atividade de leitura (%)` e `Atividade total (%)`: quantificar o percentual de tempo em que o disco da Máquina D está ativo durante cada rodada, como proxy do impacto do armazenamento lento sobre o tempo total da rodada.

---

### 3.22 Microarquiteturas AMD Zen e a Comparação Cross-Vendor de Eficiência

- **Conceito/Teoria:** Processadores AMD baseados nas microarquiteturas Zen+ (12 nm) e Zen 3 (7 nm) representam gerações distintas da linha de produtos AMD, com diferenças substanciais de IPC (instruções por ciclo), eficiência energética por nó de fabricação e suporte a extensões vetoriais (FMA3, AVX2), mas sem o conjunto Intel DL Boost (VNNI) presente apenas em processadores Intel mais recentes.

- **Citação Direta (Ipsis Litteris):**
  > "Cada fornecedor de GPP, como HP, Sun, Intel e AMD, apresenta sua própria Arquitetura de Conjunto de Instruções (ISA) e microarquitetura SIMD com perspectivas distintas. A Intel, em particular, tem desempenhado um papel proeminente na expansão das tecnologias SIMD tanto do ponto de vista de hardware quanto de software." (p. 37–38)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023), ao revisar Amiri e Shahbahrami (2020), reconhece explicitamente que diferentes fabricantes de processadores de propósito geral (GPPs) — incluindo Intel e AMD — implementam ISAs e microarquiteturas SIMD distintas, o que impede uma comparação direta de desempenho baseada apenas em clock ou contagem de núcleos. Essa observação é central para a comparação cross-vendor do nosso grupo: a Máquina C (AMD Ryzen 5 3500U, Zen+, 12 nm, sem VNNI) e a Máquina E (AMD Ryzen 5 5500, Zen 3, 7 nm, sem VNNI) compartilham o conjunto de instruções AVX2/FMA3, mas a transição de Zen+ para Zen 3 representa um salto de duas gerações microarquiteturais, com Zen 3 apresentando IPC significativamente superior por ciclo de clock, reorganização da topologia de cache (CCX unificado com acesso direto a 32 MB de cache L3 compartilhado, embora a Máquina E possua apenas 16 MB) e menor litografia (7 nm vs. 12 nm), traduzindo-se em maior eficiência energética por instrução executada mesmo a clocks nominalmente similares.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção comparativa entre ISAs e microarquiteturas de diferentes fabricantes (extensão direta da discussão de SIMD vendor-specific do autor); **Resultados e Discussão** — comparação isolada entre as Máquinas C e E (mesma fabricante AMD, gerações Zen+ e Zen 3) para isolar o efeito da evolução microarquitetural quando o fabricante é mantido constante.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqC_rodada_*.CSV`, `maqE_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)` vs. coluna `Single_Core` de `scores_maqC.txt` e `scores_maqE.txt`: calcular o IPC relativo (score por MHz efetivo) para isolar a vantagem microarquitetural pura da geração Zen 3 sobre Zen+, independentemente da diferença de clock absoluto.
  - `maqC_rodada_*.CSV`, `maqE_rodada_*.CSV` → `Potência total da CPU (W)`: comparar a eficiência energética (score/W) entre as duas gerações AMD, esperando vantagem da Máquina E (Zen 3, 7 nm) sobre a Máquina C (Zen+, 12 nm) mesmo considerando o TDP base superior da Máquina E (65 W vs. 15 W) — análise normalizada pelo desempenho por Watt já fundamentada na Seção 3.9 deste fichamento.

---

### 3.23 Largura de Barramento PCIe da GPU e seu Impacto Indireto em Cargas CPU-Bound

- **Conceito/Teoria:** A interface de barramento PCIe que conecta a GPU dedicada ao processador (PCIe 3.0 x4, 4.0 x8, etc.) determina a largura de banda disponível para transferência de dados entre CPU e GPU, sendo relevante principalmente para cargas que dependem de transferência intensiva de dados, mas com efeito secundário também sobre cargas CPU-bound que competem por linhas (lanes) PCIe compartilhadas no chipset.

- **Citação Direta (Ipsis Litteris):**
  > "Para avaliar o desempenho de sistemas paralelos, o LavaMD é projetado para ser executado em paralelo, aproveitando vários núcleos de CPU ou aceleradores, como GPUs. Isso permite que o benchmark avalie o desempenho de hardware em cargas de trabalho intensivas em computação." (p. 29)

- **Paráfrase (Citação Indireta Acadêmica):**
  Embora os benchmarks Rodinia analisados por Damasceno (2023) sejam executados exclusivamente em CPU (sem offloading para GPU neste trabalho específico), o autor reconhece a relevância arquitetural de aceleradores GPU para cargas de computação intensiva, mencionando o modelo de offloading como uma característica notável da suíte Rodinia (Seção 3.14 deste fichamento). Esse referencial é extensível à nossa discussão sobre a interface PCIe das GPUs dedicadas do grupo: a Máquina A possui GPU RTX 4050 Laptop conectada via PCIe 4.0 x8, enquanto a Máquina D possui GPU MX130 conectada via PCIe 3.0 x4 — uma diferença de até 4× na largura de banda teórica disponível. Embora o Geekbench 6 CPU seja predominantemente CPU-bound (Seção 3.3 deste fichamento), o subsistema PCIe compartilhado entre CPU e GPU no chipset pode introduzir contenção residual em sistemas com menor número de lanes disponíveis, sendo um fator a considerar caso o grupo execute também o Geekbench 6 GPU Compute para complementar a análise.

- **Onde Encaixar no Artigo LaTeX:** **Fundamentação Teórica** — subseção sobre arquitetura de barramento de E/S (PCIe) como parte da hierarquia de comunicação CPU-periféricos; **Trabalhos Futuros** — caso o grupo deseje expandir a análise para o Geekbench 6 Compute (GPU), esta seção fornece a base teórica necessária.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV`, `maqD_rodada_*.CSV` → `Velocidade do link PCIe (GT/s)`: confirmar a velocidade de operação real do link PCIe da GPU dedicada durante a execução do benchmark, validando se o sistema opera na geração PCIe esperada (4.0 para a Máquina A, 3.0 para a Máquina D).
  - `maqA_rodada_*.CSV` → `PCI Express Error Counters (avg)`, `Correctable Error Count`: monitorar erros de comunicação PCIe que possam introduzir variabilidade espúria nos resultados, especialmente relevante para a Máquina A com barramento PCIe 4.0 x8 de maior velocidade nominal.

---

### 3.24 Sistemas Operacionais Windows 11: Variações de Build e Edição (Home vs. Pro)

- **Conceito/Teoria:** Diferentes edições e builds do mesmo sistema operacional podem apresentar políticas distintas de gerenciamento de energia, agendamento de processos em segundo plano e telemetria, fatores que, embora frequentemente considerados desprezíveis, podem introduzir variabilidade sistemática entre máquinas em testes de benchmark de alta sensibilidade.

- **Citação Direta (Ipsis Litteris):**
  > "O sistema operacional Linux Ubuntu empregado nesta pesquisa está na versão 22.04.1 LTS e utiliza a arquitetura de 64 bits. Esta versão foi selecionada em virtude de sua estabilidade e do suporte a longo prazo, aspectos cruciais para ambientes acadêmicos e pesquisas científicas que demandam consistência e confiabilidade em suas operações." (p. 46)

- **Paráfrase (Citação Indireta Acadêmica):**
  Damasceno (2023) padroniza rigorosamente o sistema operacional (Ubuntu 22.04.1 LTS, 64 bits) como variável de controle do experimento, justificando a escolha pela estabilidade e previsibilidade de comportamento que uma distribuição LTS (Long Term Support) oferece para fins de reprodutibilidade científica. Esse princípio metodológico de controle de variáveis de sistema operacional é diretamente relevante para o nosso grupo: cinco das seis máquinas utilizam Windows 11 Home Single Language ou Home padrão em builds 25H2, mas a Máquina F utiliza Windows 11 **Pro** 25H2 — edição que, embora compartilhe o mesmo kernel NT, pode diferir em políticas de gerenciamento de energia corporativas (Group Policy), recursos de virtualização habilitados por padrão (Hyper-V) e processos de telemetria em segundo plano, introduzindo uma variável de confusão não controlada na comparação entre a Máquina F e as demais. O princípio metodológico do autor recomenda que essa diferença de edição seja registrada e discutida como limitação do experimento, análoga à forma como ele documenta precisamente a versão e arquitetura do seu próprio sistema operacional.

- **Onde Encaixar no Artigo LaTeX:** **Metodologia** — subseção de limitações do experimento, registrando explicitamente que a Máquina F roda Windows 11 Pro enquanto as demais rodam Windows 11 Home, como possível fonte de variabilidade não controlada; **Resultados e Discussão** — caso a Máquina F apresente desvio padrão anormalmente alto ou baixo em relação ao esperado por seu hardware, esta diferença de edição do SO deve ser citada como hipótese explicativa.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqF.txt` → colunas `Single_Core` e `Multi_Core`: calcular o desvio padrão amostral das 20 rodadas da Máquina F e compará-lo ao das demais máquinas; um desvio padrão anormalmente elevado pode ser parcialmente atribuído a processos de background específicos do Windows 11 Pro (ex.: serviços de domínio, Hyper-V em segundo plano).
  - `maqF_rodada_*.CSV` → `Carga da memória física (%)`: verificar se há consumo basal de memória superior ao esperado, possivelmente atribuível a serviços adicionais da edição Pro rodando em segundo plano durante a coleta.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmulas Matemáticas/Físicas em LaTeX Puro

**Equação 1 — Função de Crescimento Exponencial do Consumo (p. 59)**

Apresentada pelo autor para modelar o consumo energético do benchmark LU Decomposition em função do tamanho da entrada:

```latex
% ============================================================
% EQUAÇÃO DE CRESCIMENTO EXPONENCIAL DO CONSUMO
% Fundamentado em: Damasceno (2023, p. 59)
% Aplicação: Modelagem do comportamento esperado do consumo
%            energético em função da carga de trabalho.
% ============================================================
\begin{equation}
    f(x) = a \cdot b^{x}
    \label{eq:crescimento_exponencial}
\end{equation}

\noindent onde $x$ representa o tamanho da entrada (ou o número
da rodada), $a$ é o consumo base e $b > 1$ é o fator de
crescimento, que varia conforme o compilador e o tipo de
benchmark. Para o presente trabalho, $x$ pode ser interpretado
como o índice da rodada (1 a 20) e $f(x)$ como o consumo médio
de potência em Watts registrado na coluna
\texttt{Potência total da CPU (W)} do HWiNFO64 \cite{damasceno:23}.
```

---

**Equação 2 — Cálculo de Energia Total por Rodada**

Derivada da relação de correlação perfeita (1:1) entre duração e consumo demonstrada pelo autor (p. 58–60):

```latex
% ============================================================
% EQUAÇÃO DE ENERGIA TOTAL POR RODADA
% Fundamentado em: Damasceno (2023, p. 58-60)
% ============================================================
\begin{equation}
    E_{rodada} = \overline{P}_{\text{CPU}} \cdot \Delta t
    \label{eq:energia_rodada}
\end{equation}

\noindent onde $\overline{P}_{\text{CPU}}$ é a média da coluna
\texttt{Potência total da CPU (W)} durante a rodada $i$ e
$\Delta t$ é a duração da rodada em segundos. A correlação
unitária ($r \approx 1{,}00$) entre duração e consumo
demonstrada por \cite{damasceno:23} valida esta estimativa
para cargas CPU-bound estáveis.
```

---

**Equação 3 — Protocolo de Espaçamento de Coleta (p. 51)**

```latex
% ============================================================
% EQUAÇÃO DO PROTOCOLO DE COLETA — Damasceno (2023, p. 51)
% Análogo ao protocolo de 20 rodadas do nosso projeto.
% ============================================================
\begin{equation}
    \delta = \frac{V_{max} - V_{min}}{N}
    \label{eq:protocolo_coleta}
\end{equation}

\noindent onde $\delta$ é o incremento entre amostras consecutivas,
$V_{max}$ e $V_{min}$ são os valores máximo e mínimo da entrada,
e $N$ é o número total de amostras. Em \cite{damasceno:23}, $N = 128$;
no presente trabalho, $N = 20$ (rodadas do Geekbench 6).
```

---

**Equação 4 — Diferença Percentual de Eficiência entre Compiladores (p. 59, 62, 65)**

Calculada pelo autor como métrica de comparação de eficiência energética entre compiladores:

```latex
% ============================================================
% EQUAÇÃO DE EFICIÊNCIA RELATIVA — Damasceno (2023)
% Adaptada para comparação entre máquinas no nosso projeto.
% ============================================================
\begin{equation}
    \Delta E_{rel} (\%) = \frac{\overline{E}_{X} - \overline{E}_{ref}}
                               {\overline{E}_{ref}} \times 100
    \label{eq:eficiencia_relativa}
\end{equation}

\noindent onde $\overline{E}_{X}$ é o consumo médio do compilador
(ou máquina) avaliado e $\overline{E}_{ref}$ é o consumo médio do
compilador (ou máquina) de referência. Valores positivos indicam
maior consumo (menor eficiência); valores negativos indicam
economia de energia (maior eficiência) \cite{damasceno:23}.
No presente trabalho, $\overline{E}_{ref}$ pode ser o score médio
ou o consumo médio da máquina tomada como referência de comparação.
```

---

**Equação 5 — Métrica de Desempenho por Watt**

Derivada da discussão de eficiência do autor (Seção 6, p. 78), adaptada para o contexto do Geekbench 6:

```latex
% ============================================================
% MÉTRICA DE DESEMPENHO POR WATT — derivada de Damasceno (2023)
% ============================================================
\begin{equation}
    \eta = \frac{S_{\text{Geekbench}}}{\overline{P}_{\text{CPU}}}
    \quad \left[\frac{\text{pontos}}{\text{W}}\right]
    \label{eq:desempenho_por_watt}
\end{equation}

\noindent onde $S_{\text{Geekbench}}$ é o score médio do
Geekbench~6 (Single-Core ou Multi-Core) das 20 rodadas e
$\overline{P}_{\text{CPU}}$ é a média da coluna
\texttt{Potência total da CPU (W)} coletada simultaneamente
via HWiNFO64. Esta métrica quantifica a eficiência
microarquitetural de cada máquina, permitindo comparação
normalizada independente da potência absoluta do processador.
```

---

### 4.2 Sugestão de Gráficos e Tabelas para o `main.tex`

**Gráfico 1 — Barplot de Scores com Hastes de Erro (Analogia à Figura 1 do TCC)**

Baseado na análise comparativa de consumo por compilador (Figuras 1, 5, 9, 13, 17 do TCC):

```python
# Script Python — Matplotlib/Pandas — Análogo ao pipeline de Damasceno (2023)
# Plotar barplot de scores Single_Core e Multi_Core por máquina
# com hastes de erro representando o desvio padrão amostral (s)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar dados de scores
maquinas = ['A', 'B', 'C', 'D']
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

for ax, col in zip(axes, ['Single_Core', 'Multi_Core']):
    medias, stds = [], []
    for m in maquinas:
        df = pd.read_csv(f'scores_maq{m}.txt', sep=';')
        medias.append(df[col].mean())
        stds.append(df[col].std(ddof=1))   # desvio padrão amostral
    ax.bar(maquinas, medias, yerr=stds, capsize=5,
           color=['#333333','#555555','#777777','#999999'],
           edgecolor='black')
    ax.set_title(f'Score {col}', fontsize=11, fontweight='bold')
    ax.set_xlabel('Máquina', fontsize=10)
    ax.set_ylabel('Score Geekbench 6 (pontos)', fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('barplot_scores_por_maquina.pdf', dpi=300)
# Legenda para o main.tex:
# Figura X — Scores médios do Geekbench 6 por máquina,
# com barras de erro representando o desvio padrão amostral
# (n = 20 rodadas). Fonte: Os autores (2026).
```

---

**Gráfico 2 — Correlação Potência vs. Score (Analogia às Figuras 2, 6, 10, 14, 18 do TCC)**

Baseado na correlação 1:1 entre duração e consumo documentada em todas as seções de resultados:

```python
# Scatter plot: Potência média da CPU por rodada vs. Score Multi_Core
# Esperado: correlação negativa (potência alta = score baixo se há throttling)

import glob

fig, ax = plt.subplots(figsize=(7, 5))
for m in ['A', 'B', 'C', 'D']:
    scores = pd.read_csv(f'scores_maq{m}.txt', sep=';')
    potencias = []
    for i in range(1, 21):
        csv_path = f'maq{m}_rodada_{i:02d}.CSV'
        df_csv = pd.read_csv(csv_path, sep=',', decimal=',')
        # Nome exato da coluna no HWiNFO64
        col_pot = 'Potência total da CPU (W)'
        potencias.append(df_csv[col_pot].mean())
    ax.scatter(potencias, scores['Multi_Core'],
               label=f'Máquina {m}', s=60)

ax.set_xlabel('Potência Média da CPU (W)', fontsize=10)
ax.set_ylabel('Score Multi-Core', fontsize=10)
ax.set_title('Desempenho vs. Consumo por Rodada', fontsize=11)
ax.legend(); ax.grid(linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('scatter_potencia_vs_score.pdf', dpi=300)
```

---

**Gráfico 3 — Distribuição Percentual CPU/RAM por Máquina (Analogia às Figuras 3, 7, 11, 15 do TCC)**

```python
# Barplot empilhado: % consumo CPU vs. RAM (potência) por máquina
# Análogo às Figuras 3, 7, 11, 15 do TCC de Damasceno (2023)
# Substituindo domínios RAPL pelos campos equivalentes do HWiNFO64

fig, ax = plt.subplots(figsize=(7, 5))
cpu_pcts, dram_pcts = [], []
for m in ['A', 'B', 'C', 'D']:
    all_cpu, all_dram = [], []
    for i in range(1, 21):
        df_csv = pd.read_csv(f'maq{m}_rodada_{i:02d}.CSV',
                             sep=',', decimal=',')
        all_cpu.append(df_csv['Potência de núcleos IA (W)'].mean())
        all_dram.append(df_csv['Potência total de DRAM (W)'].mean())
    total = np.mean(all_cpu) + np.mean(all_dram)
    cpu_pcts.append(100 * np.mean(all_cpu) / total)
    dram_pcts.append(100 * np.mean(all_dram) / total)

x = np.arange(len(maquinas))
ax.bar(x, cpu_pcts, label='CPU (núcleos IA)', color='#333333')
ax.bar(x, dram_pcts, bottom=cpu_pcts, label='DRAM', color='#888888')
ax.set_xticks(x); ax.set_xticklabels([f'Maq. {m}' for m in maquinas])
ax.set_ylabel('Distribuição Percentual (%)')
ax.set_title('Distribuição do Consumo CPU vs. DRAM por Máquina')
ax.legend(); plt.tight_layout()
plt.savefig('barplot_distribuicao_cpu_dram.pdf', dpi=300)
```

---

**Tabela LaTeX — Comparativo de Hardware das 6 Máquinas (Metodologia)**

Baseado na Seção 4.1 do TCC (Componentes de Hardware, p. 45) e atualizada com os dados completos das Máquinas A, B, C, D, E e F fornecidos pelo grupo:

```latex
% ============================================================
% TABELA COMPARATIVA DE HARDWARE — Seção de Metodologia
% Padrão SBC: sem linhas verticais, legenda ANTES da tabela
% Tabela dividida em duas partes (table* ou rotação) recomendada
% para caber em coluna única A4 — ver nota abaixo.
% ============================================================

\begin{table}[ht]
\caption{Especificações de hardware das seis máquinas avaliadas.
         Fonte: Os autores (2026).}
\label{tab:hardware}
\centering
\footnotesize
\begin{tabular}{lll}
\hline
\textbf{Parâmetro} & \textbf{Máq. A (Raony)} & \textbf{Máq. B (Leandro)} \\
\hline
Fator de Forma      & Notebook Gamer        & Notebook Ultrafino \\
Modelo              & Acer Nitro ANV15-51   & Dell Inspiron 15 3530 \\
Processador         & Intel Core i5-13420H  & Intel Core i5-1334U \\
Microarquitetura    & Raptor Lake-H / Intel 7 & Raptor Lake-P / Intel 7 \\
Núcleos / Threads   & 8 (4P+4E) / 12        & 10 (2P+8E) / 12 \\
Clock Base / Boost  & 2,10 / 4,60 GHz       & 1,30 / 4,60 GHz \\
TDP Base            & 45 W                  & 15 W \\
Cache L3            & 12 MB                 & 12 MB \\
Instr. Avançadas    & AVX2, VNNI, BMI2      & AVX2, VNNI, BMI2 \\
RAM                 & 8 GB DDR5 5200 MT/s   & 16 GB DDR4 2666 MHz \\
Canal de Memória    & Dual Channel (1x8GB)  & Dual Channel (2x8GB) \\
GPU Integrada       & Intel UHD Graphics    & Intel Iris Xe (80 EUs) \\
GPU Dedicada        & RTX 4050 Laptop       & Não possui \\
Barramento GPU      & PCIe 4.0 x8           & N/A \\
Armazenamento       & SSD NVMe 512 GB       & SSD NVMe 512 GB \\
Interface do Disco  & PCIe 4.0 x4 (Intel VMD) & PCIe 3.0 x4 (Intel VMD) \\
Sistema Operacional & Windows 11 Home 25H2  & Windows 11 Home 25H2 \\
\hline
\end{tabular}

\vspace{6pt}

\begin{tabular}{lll}
\hline
\textbf{Parâmetro} & \textbf{Máq. C (Cinara)} & \textbf{Máq. D (Roberta)} \\
\hline
Fator de Forma      & Notebook Ultrafino    & Notebook Ultrafino \\
Modelo              & ASUS M515D            & Dell Inspiron 15 5584 \\
Processador         & AMD Ryzen 5 3500U     & Intel Core i5-8265U \\
Microarquitetura    & Zen+ / 12 nm          & Whiskey Lake-U / 14 nm \\
Núcleos / Threads   & 4 / 8                 & 4 / 8 \\
Clock Base / Boost  & 2,10 / 3,70 GHz       & 1,60 / 3,90 GHz \\
TDP Base            & 15 W                  & 15 W \\
Cache L3            & 4 MB                  & 6 MB \\
Instr. Avançadas    & AVX2, FMA3            & AVX2, FMA3, BMI2 \\
RAM                 & 8 GB DDR4 [MHz]*      & 8 GB DDR4 2400 MHz \\
Canal de Memória    & Single Channel (1x8GB)& Single Channel (1x8GB) \\
GPU Integrada       & AMD Radeon Vega 8     & Intel UHD Graphics 620 \\
GPU Dedicada        & Não possui            & NVIDIA GeForce MX130 \\
Barramento GPU      & N/A                   & PCIe 3.0 x4 \\
Armazenamento       & [SSD ou HD?]* (237 GB)& HDD WD Blue 1 TB (5400 RPM) \\
Interface do Disco  & [Preencher]*          & SATA III (6 Gbps) \\
Sistema Operacional & Windows 11 Home 25H2  & Windows 11 Home 25H2 \\
\hline
\end{tabular}

\vspace{6pt}

\begin{tabular}{lll}
\hline
\textbf{Parâmetro} & \textbf{Máq. E (Nauan)} & \textbf{Máq. F (Nicolas)} \\
\hline
Fator de Forma      & Desktop Montado       & Desktop Montado \\
Modelo              & [Preencher Gabinete]* & [Preencher Gabinete]* \\
Processador         & AMD Ryzen 5 5500      & Intel Core i5-14600KF \\
Microarquitetura    & Zen 3 / 7 nm          & Raptor Lake / Intel 7 \\
Núcleos / Threads   & 6 / 12                & 14 (6P+8E) / 20 \\
Clock Base / Boost  & 3,60 / 4,20 GHz       & P: 3,5/5,3 GHz; E: 2,6/4,0 GHz \\
TDP Base            & 65 W                  & 125 W \\
Cache L3            & 16 MB                 & 24 MB \\
Instr. Avançadas    & AVX2, FMA3            & AVX2, VNNI, BMI2 \\
RAM                 & 16 GB DDR4 [MHz]*     & 32 GB DDR4 3600 MHz \\
Canal de Memória    & Dual Channel (2x8GB)  & Dual Channel (2x16GB) \\
GPU Integrada       & Não possui            & Não possui \\
GPU Dedicada        & AMD Radeon RX 7600    & RTX 3050 8GB \\
Barramento GPU      & PCIe 4.0 x8           & PCIe 4.0 x8 \\
Armazenamento       & SSD SATA 120GB + HD 1TB & 2x SSD NVMe M.2 (1TB) \\
Interface do Disco  & SATA III (6 Gbps)     & [Preencher Gen]* \\
Sistema Operacional & Windows 11 Home 25H2  & \textbf{Windows 11 Pro 25H2} \\
\hline
\end{tabular}

\vspace{2pt}
{\footnotesize Nota: Os campos marcados com ``*'' (frequência de
RAM da Máquina C e E, tipo de armazenamento e interface da Máquina C,
gabinete das Máquinas E e F, e geração PCIe do disco da Máquina F)
permanecem pendentes de confirmação pelo grupo. A Máquina F opera em
Windows 11 \textbf{Pro}, divergindo da edição Home das demais
máquinas — ver discussão na Seção 3.24 deste fichamento.}
\end{table}
```

> ⚠️ **NOTA TÉCNICA DE FORMATAÇÃO SBC:** Como o template SBC exige coluna única (largura
> útil ≈ 15 cm) e a tabela completa com 6 máquinas e ~17 parâmetros não cabe em uma única
> tabela de 7 colunas sem violar a margem, a tabela acima foi dividida em 3 blocos de 2
> máquinas cada (A+B, C+D, E+F), todos com a mesma legenda numerada via `\label{tab:hardware}`
> e referenciados no texto como "Tabela~\ref{tab:hardware}". Alternativamente, o grupo pode optar
> por girar a tabela com o pacote `rotating` (`\begin{sidewaystable}`) para exibir as 6 máquinas
> em uma única tabela horizontal, caso a banca aceite página em paisagem.

---

## 5. KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

As seguintes strings de busca são recomendadas para encontrar artigos complementares ao TCC de Damasceno (2023), organizadas por tema e aplicáveis ao nosso projeto de AOC:

### 5.1 Benchmarking e Avaliação de Desempenho de CPU
- `"Geekbench" "benchmark" "CPU performance" "multi-core" comparison`
- `synthetic benchmark "processor performance" "single-core" "multi-core" evaluation`
- `"Rodinia benchmark suite" multicore CPU evaluation performance`
- `benchmark avaliação desempenho processador multi-core portátil`

### 5.2 Intel RAPL e Medição de Consumo Energético
- `"Intel RAPL" "power measurement" CPU energy consumption accuracy`
- `"Running Average Power Limit" benchmark energy profiling`
- `"HWiNFO" OR "HWiNFO64" power telemetry CPU measurement Windows`
- `medição consumo energético CPU "Intel RAPL" benchmark portátil`

### 5.3 Thermal Throttling e Estabilidade de Desempenho
- `"thermal throttling" laptop CPU performance degradation benchmark`
- `"CPU throttling" temperature frequency reduction benchmark stability`
- `"power limit throttling" "TDP" notebook Intel performance variance`
- `estrangulamento térmico processador notebook desempenho benchmark`

### 5.4 OpenMP e Paralelismo Multi-Core
- `"OpenMP" multi-core CPU performance parallel benchmark evaluation`
- `"thread-level parallelism" "multi-core" performance scaling benchmark`
- `paralelismo OpenMP desempenho multi-core benchmark computação paralela`

### 5.5 Compiladores e Otimização de Código
- `"GCC" "ICC" "Clang" compiler comparison energy efficiency benchmark`
- `compiler optimization CPU performance energy consumption HPC`
- `"Intel C Compiler" optimization "interprocedural optimization" performance`
- `compiladores GCC ICC eficiência energética benchmark comparação`

### 5.6 Detecção de Outliers e Análise Estatística de Benchmark
- `outlier detection benchmark performance measurement statistical analysis`
- `"standard deviation" benchmark performance variability CPU measurement`
- `reprodutibilidade benchmark desvio padrão análise estatística`

### 5.7 Arquiteturas Híbridas, SIMD Avançado e Hardware Heterogêneo (Acréscimo)
- `"hybrid architecture" "P-core" "E-core" performance scheduling benchmark`
- `"Intel Thread Director" heterogeneous core scheduling Windows performance`
- `"AVX-512" "VNNI" vector instructions performance comparison Intel AMD`
- `"DDR5" vs "DDR4" memory bandwidth latency benchmark performance`
- `"all-core boost" TDP sustained clock desktop processor benchmark`
- `"AMD Zen 3" vs "Zen+" IPC microarchitecture comparison performance`
- `"NVMe SSD" vs "SATA HDD" storage latency benchmark loading time`
- `"PCIe Gen 4" vs "PCIe Gen 3" bandwidth GPU bus interface impact`
- `arquitetura híbrida núcleos eficiência desempenho processador heterogêneo`
- `desempenho cache L3 capacidade comparação processadores multi-core`

---

## 6. NOTA SOBRE ATUALIZAÇÃO DE HARDWARE (MÁQUINAS A, B, C, E e F) E PENDÊNCIAS REMANESCENTES

> ⚠️ **NOTA EDITORIAL — Atualização de Hardware (substitui a nota preditiva da versão anterior):**
>
> Com o preenchimento das especificações de hardware das Máquinas A, B, C, E e F, as seções
> que antes eram fichadas em caráter **preditivo** (3.11, 3.13 e os Gráficos 2 e 3 da Seção 4.2,
> na versão original deste documento) **passam a ter aplicação direta e confirmada**, pois:
> - A Máquina A confirma memória **DDR5** e GPU dedicada com **PCIe 4.0 x8** — ambos os cenários
>   antes hipotéticos discutidos nas Seções 3.11 e 3.13 (cache, banda de memória e barramento
>   PCIe), agora com hardware real correspondente.
> - As Máquinas B, E e F confirmam memória **Dual Channel**, cenário também antes tratado de
>   forma preditiva na Seção 3.13 e agora aplicável de forma direta a essas três máquinas.
> - As Máquinas E e F confirmam TDP elevado (65 W e 125 W), justificando a nova Seção 3.20
>   (TDP elevado e sustentação de boost), que não constava na versão original deste fichamento.
>
> **Pendências remanescentes** (campos marcados com `*` na tabela fornecida pelo grupo e ainda
> sem confirmação, conforme registrado na Tabela~\ref{tab:hardware} da Seção 4.2 deste documento):
> - Frequência da RAM DDR4 da Máquina C e da Máquina E;
> - Tipo de armazenamento (SSD ou HD) e interface de disco da Máquina C;
> - Modelo do gabinete das Máquinas E e F (montagens customizadas, sem modelo comercial único);
> - Geração da interface PCIe do armazenamento NVMe da Máquina F.
>
> Esses campos pendentes não impedem a redação das seções de Metodologia e Resultados com base
> nos dados já confirmados, mas devem ser preenchidos pelo grupo antes da versão final do artigo
> para completude da Tabela~\ref{tab:hardware}. **Este aviso será removido tão logo o líder do
> grupo confirme os últimos quatro campos pendentes listados acima.**

---

*Fichamento concluído. Arquivo pronto para inclusão no repositório do projeto.*
*Referência BibTeX: `damasceno:23` — inserir no `sbc-template.bib` e citar com `\cite{damasceno:23}`.*
