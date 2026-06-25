# Fichamento Científico — Padrão SBC/AOC-UFPA
**Arquivo:** `fichamento_StatisticalPerformanceComparisons_Chen.md`
**Gerado por:** Claude (co-autor do projeto AOC — UFPA Campus Tucuruí)
**Data de geração:** 16 de junho de 2026
**Última atualização:** 25 de junho de 2026 — Acréscimo dos itens 3.13 e 3.14, motivado pela expansão da tabela de hardware para 6 máquinas (inclusão das Máquinas E e F, e detalhamento de núcleos híbridos P+E nas Máquinas A, B e F). Nenhum conteúdo pré-existente foi alterado ou removido.

---

## ✅ VEREDITO DE RELEVÂNCIA

**O artigo SERÁ ÚTIL para o nosso projeto de AOC? SIM — ALTAMENTE RELEVANTE.**

Justificativa: Chen et al. (2015) abordam diretamente o problema da **variabilidade estatística em comparações de desempenho computacional via benchmarks**, fornecendo fundamento teórico rigoroso para: (1) justificar por que as **20 rodadas do Geekbench 6 por máquina** constituem uma amostra finita com limitações estatísticas conhecidas; (2) apresentar formalmente as equações de **Média Aritmética Amostral** ($\bar{X}$) e **Desvio Padrão Amostral** ($S$), as quais utilizamos diretamente na Metodologia do artigo; (3) demonstrar que **distribuições de desempenho frequentemente não seguem distribuição normal**, validando nossa cautela interpretativa na análise dos Resultados e Discussão; (4) criticar fundamentadamente a prática de comparar sistemas apenas pela média geométrica de scores — crítica que se aplica diretamente às limitações do Geekbench 6; (5) introduzir o conceito de **confiança estatística** como dimensão obrigatória em toda comparação de desempenho, reforçando o papel metodológico do Desvio Padrão nas nossas análises com o HWiNFO64. Trata-se de artigo publicado em periódico IEEE de alto impacto (Transactions on Computers, Qualis A1), com acesso autorizado pela UFPA, conferindo máximo rigor científico à metodologia do trabalho.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC (para `\begin{thebibliography}` no `main.tex`):**

> CHEN, T.; GUO, Q.; TEMAM, O.; WU, Y.; BAO, Y.; XU, Z.; CHEN, Y. Statistical Performance Comparisons of Computers. **IEEE Transactions on Computers**, v. 64, n. 5, p. 1442–1455, maio 2015.

- **Código BibTeX Completo (.bib) — para inserir no `sbc-template.bib`:**

```bibtex
@Article{chen:15,
  author    = {Tianshi Chen and Qi Guo and Olivier Temam and Yue Wu
               and Yungang Bao and Zhiwei Xu and Yunji Chen},
  title     = {Statistical Performance Comparisons of Computers},
  journal   = {{IEEE} Transactions on Computers},
  year      = {2015},
  volume    = {64},
  number    = {5},
  pages     = {1442--1455},
  month     = may,
  doi       = {10.1109/TC.2014.2315614},
  issn      = {0018-9340},
  publisher = {{IEEE}},
  note      = {Authorized licensed use limited to:
               {UNIVERSIDADE} {FEDERAL} {DO} {PARA}.
               Downloaded on June 16, 2026 at 04:40:17 {UTC}
               from {IEEE} Xplore.}
}
```

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo de Periódico Científico (IEEE Transactions on Computers, Vol. 64, No. 5, Maio 2015)
- **Instituição/Editora:** State Key Laboratory of Computer Architecture, Institute of Computing Technology, Chinese Academy of Sciences (ICT/CAS), Beijing, China; Department of ECE, Carnegie Mellon University, EUA; INRIA Saclay, França / IEEE
- **Autores:** Tianshi Chen; Qi Guo; Olivier Temam; Yue Wu; Yungang Bao; Zhiwei Xu (Senior Member, IEEE); Yunji Chen (autor correspondente)
- **DOI:** 10.1109/TC.2014.2315614
- **Recebido:** 20 ago. 2013 | **Revisado:** 14 jan. 2014 | **Aceito:** 5 mar. 2014 | **Publicado:** 3 abr. 2014
- **Palavras-Chave Originais:** Performance comparison; performance distribution; t-statistics; hierarchical performance testing
- **Resumo do Escopo Geral:**
  O artigo formula comparações de desempenho entre computadores como um **problema estatístico formal**, demonstrando empiricamente que práticas tradicionais (comparação pela média geométrica, uso indiscriminado do teste t) conduzem a resultados incorretos e potencialmente enganosos. Os autores propõem o **framework HPT (Hierarchical Performance Testing)**, baseado em testes estatísticos não paramétricos (Wilcoxon Rank-Sum Test e Wilcoxon Signed-Rank Test), que é capaz de quantificar a **confiança** de uma comparação de desempenho mesmo quando as distribuições não são normais e o número de observações é pequeno. O framework foi implementado como software open-source e integrado ao benchmark suite PARSEC 3.0. O estudo empírico abrange dados do SPEC CPU2006, SPEC MPI2007 e SPLASH-2/PARSEC, demonstrando erros de 8,0% a 56,3% nas comparações pela média geométrica em relação ao método proposto.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO

---

### 3.1 — Variabilidade Não Determinística do Desempenho

- **Conceito/Teoria:** Desempenho computacional como variável aleatória (Performance Distribution)

- **Citação Direta (Ipsis Litteris):**
  > "From a statistical viewpoint, the non-deterministic performance of a computer is a random variable obeying a certain probability distribution called performance distribution." (p. 1443)

- **Paráfrase (Citação Indireta Acadêmica):**
  Do ponto de vista estatístico, o desempenho não determinístico de um computador constitui uma variável aleatória que obedece a uma determinada distribuição de probabilidade, denominada *distribuição de desempenho* (Chen et al. 2015, p. 1443). Consequentemente, medir o desempenho de um sistema equivale a amostrar estatisticamente essa distribuição subjacente, o que implica que qualquer comparação entre sistemas deve considerar não apenas as médias, mas também a variabilidade intrínseca das observações coletadas.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** (subseção de Análise Estatística), para justificar conceitualmente a necessidade de múltiplas rodadas e o uso do Desvio Padrão.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: cada valor por rodada é exatamente uma *observação de desempenho* que amostra a distribuição de desempenho da máquina no Geekbench 6.
  - `maq*_rodada_*.CSV` → coluna `Relógios efetivos núcleo (avg) (MHz)`: variações entre rodadas desta coluna evidenciam a natureza não determinística do desempenho de clock efetivo, corroborando o modelo de variável aleatória dos autores.
  - `maq*_rodada_*.CSV` → coluna `Uso total da CPU (%)`: oscilações de carga entre rodadas distintas da mesma máquina confirmam que o desempenho observado é influenciado por fatores estocásticos do sistema operacional (escalonamento, interrupções, serviços em background).

---

### 3.2 — Importância da Confiança Estatística em Comparações de Desempenho

- **Conceito/Teoria:** Confiança estatística como dimensão obrigatória em comparações de desempenho

- **Citação Direta (Ipsis Litteris):**
  > "We argue that the performance comparison of two computers can be statistically formulated as the comparison between their performance distributions based on (statistical) performance sampling." (p. 1443)

- **Citação Direta (Ipsis Litteris) — Exemplo Empírico:**
  > "Following this methodology, the performance speedup of PowerEdge T710 over Xserve on SPEC CPU2006, estimated by the data collected from SPEC.org, is 3:50. However, after checking this performance speedup with the hierarchical performance testing (HPT) technique suggested in later parts of this paper, we found that the confidence of such a performance speedup is only 0:31, which is rather unreliable (0:95 is the statistically acceptable level of confidence)." (p. 1443)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015) argumentam que toda comparação de desempenho entre sistemas computacionais deve ser necessariamente acompanhada de uma estimativa de confiança, que quantifica a confiabilidade do resultado obtido. Os autores ilustram esse ponto com um exemplo concreto: a diferença de desempenho estimada pela média geométrica entre dois servidores SPEC CPU2006 apresentou confiança de apenas 0,31 — valor muito abaixo do limiar estatisticamente aceitável de 0,95 —, enquanto o método HPT indicou que o acelerador real (com confiança de 0,95) era de 2,24, e não 3,50 como sugerido pela média geométrica. Este exemplo evidencia que comparações por meio de métricas únicas sem estimativa de confiança podem induzir a erros superiores a 56% na estimativa do speedup real (p. 1443).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** (subseção de Análise Estatística), para justificar por que reportamos Desvio Padrão em todos os gráficos e tabelas, e não apenas a média dos scores.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: o Desvio Padrão Amostral calculado sobre as 20 rodadas para cada máquina é o indicador de confiança mais imediato disponível na nossa metodologia. Uma máquina com alto Desvio Padrão nos scores Single_Core sugere distribuição de desempenho com alta dispersão, tornando as comparações entre máquinas menos confiáveis.
  - `maq*_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)`: eventos de throttling em rodadas específicas geram outliers nos scores, aumentando a dispersão amostral e reduzindo a confiança da comparação — exatamente o fenômeno discutido pelos autores em relação a outliers de desempenho.

---

### 3.3 — Média Aritmética Amostral e Desvio Padrão Amostral (Fórmulas Clássicas)

- **Conceito/Teoria:** Definição formal de Média Amostral ($\bar{X}$) e Desvio Padrão Amostral ($S$)

- **Citação Direta (Ipsis Litteris):**
  > "Consider a sample {X₁, ..., Xₙ} with n observations of the same population distribution with finite mean and variance. The sample mean X̄ and sample standard deviation S are defined by:
  > X̄ = (1/n)(X₁ + ... + Xₙ) [Eq. 1]
  > S = sqrt( (1/(n-1)) * Σᵢ₌₁ⁿ (Xᵢ - X̄)² ) [Eq. 2]" (p. 1444)

- **Paráfrase (Citação Indireta Acadêmica):**
  Para uma amostra de $n$ observações de desempenho $\{X_1, \ldots, X_n\}$ extraídas de uma mesma distribuição populacional com média e variância finitas, Chen et al. (2015, p. 1444) definem a média aritmética amostral $\bar{X}$ e o desvio padrão amostral $S$ conforme as equações clássicas da estatística inferencial. A utilização de $n-1$ no denominador de $S$ — em vez de $n$ — corresponde à **correção de Bessel**, que produz um estimador não viesado da variância populacional a partir de amostras finitas, aspecto particularmente relevante em nosso contexto, onde cada máquina foi avaliada com apenas 20 rodadas do Geekbench 6.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** — bloco de equações LaTeX com as definições formais de $\bar{X}$ e $S$, com citação direta a (Chen et al. 2015).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: são os vetores $\{X_1, \ldots, X_{20}\}$ sobre os quais calculamos $\bar{X}$ e $S$ para cada máquina em cada modalidade de teste (núcleo único e multinúcleo).
  - `maq*_rodada_*.CSV` → todas as colunas numéricas de telemetria (ex.: `Potência total da CPU (W)`, `CPU Inteira (°C)`, `Relógios efetivos núcleo (avg) (MHz)`): para cada coluna, calcula-se $\bar{X}$ e $S$ sobre as 20 rodadas, gerando perfis estatísticos das variáveis de hardware por máquina.

---

### 3.4 — Teste t e suas Precondições (Distribuição Normal)

- **Conceito/Teoria:** Precondições do teste t paramétrico para comparações de desempenho

- **Citação Direta (Ipsis Litteris):**
  > "Statistically, if X̄ obeys a normal distribution, then T = (√n · (X̄ - μ)) / S obeys the student's t-distribution with n-1 degrees of freedom." (p. 1444)

- **Citação Direta (Ipsis Litteris) — Precondição de Grande Amostra:**
  > "The sample mean of performance gaps between two computers, D̄, must obey a normal distribution in order to apply t-statistics. [...] Large-sample precondition. When performance distributions of one or both computers are non-normal but are with finite means and variances, the Central Limit Theorem (CLT) states that the sample mean performance of both computers approximately obeys normal distributions when the sample size n [...] is sufficiently large." (p. 1444)

- **Paráfrase (Citação Indireta Acadêmica):**
  A validade do teste t paramétrico pressupõe que a média amostral das diferenças de desempenho entre dois sistemas siga distribuição normal. Esta condição pode ser satisfeita por duas vias: pela **precondição de pequena amostra**, que exige que as próprias distribuições de desempenho dos sistemas sejam normais; ou pela **precondição de grande amostra**, segundo a qual o Teorema Central do Limite (TCL) garante a aproximação normal da média amostral quando o número de observações é suficientemente grande. Chen et al. (2015, p. 1444) demonstram empiricamente que nenhuma dessas condições é facilmente verificada na prática de benchmarking computacional, especialmente com 20 a 30 rodadas — tamanho amostral característico de estudos como o nosso.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** (subseção de Análise Estatística), para contextualizar as limitações das 20 rodadas e justificar a escolha de análise por Desvio Padrão em vez de inferência por teste t.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: com $n=20$ rodadas, nosso tamanho amostral está na faixa considerada pelos autores como insuficiente para a aplicação do TCL — o que reforça a necessidade de reportar $S$ com cautela interpretativa, sem afirmar diferenças estatisticamente significativas entre máquinas sem ressalvas.

---

### 3.5 — Distribuições de Desempenho Não Normais (Cauda Longa à Direita)

- **Conceito/Teoria:** Distribuições empíricas de desempenho com assimetria positiva (*right-skewed*)

- **Citação Direta (Ipsis Litteris):**
  > "According to the experimental results [...], the normality does not hold for the performance score of the computer on all three benchmarks, as evidenced by the remarkably long right tails and short left tails of the estimated performance distributions [...] it is hard for a program to execute faster than a threshold, but easy to be slowed down by various events, especially for multi-threaded programs which are affected by data races, thread scheduling, synchronization order, and contentions of shared resources." (p. 1445)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, p. 1445) demonstram empiricamente, por meio do estimador não paramétrico Kernel Parzen Window (KPW), que as distribuições de desempenho de programas — tanto mono quanto multithreaded — apresentam sistematicamente **cauda longa à direita** (assimetria positiva), contrariando a hipótese de normalidade. A assimetria é explicada pela natureza dos fatores de degradação: enquanto existem limites físicos para a aceleração de execução (impostos pela microarquitetura e pelos limites térmicos e de frequência do processador), não há barreira simétrica para a desaceleração causada por eventos como escalonamento de threads, disputas por cache compartilhada e interrupções do sistema operacional. Essa constatação é particularmente relevante para a interpretação dos nossos dados, uma vez que eventos de **Thermal Throttling** — registrados na coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)` dos CSVs do HWiNFO64 — constituem exatamente o tipo de evento de degradação assimétrica descrito pelos autores, gerando outliers negativos nos scores de desempenho.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Resultados e Discussão**, para justificar a assimetria observada nos Desvios Padrão das máquinas com maior incidência de throttling térmico (especialmente a Máquina D, com HD SATA e RAM Single Channel 1333 MHz, cujos gargalos de I/O e memória podem introduzir eventos de latência adicionais).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: eventuais rodadas com scores anormalmente baixos (outliers negativos) em qualquer máquina correspondem a eventos de desaceleração estocástica — o fenômeno de cauda longa descrito pelos autores.
  - `maqD_rodada_*.CSV` → coluna `Estrangulamento térmico do núcleo (avg) (Yes/No)`: rodadas com valor `Yes` nesta coluna são candidatas diretas a outliers negativos nos scores do Geekbench 6 da Máquina D.
  - `maq*_rodada_*.CSV` → coluna `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: quedas abruptas nessas métricas (especialmente em máquinas com HD SATA) geram atrasos de I/O que desaceleram o benchmark de forma assimétrica.

---

### 3.6 — Tamanho Amostral Necessário para o TCL: Por que 20 Rodadas São Insuficientes para Testes t

- **Conceito/Teoria:** Grande amostra necessária para a convergência do TCL em distribuições de desempenho

- **Citação Direta (Ipsis Litteris):**
  > "The common insight gained from the above experiments is that the number of performance observations (i.e., sample size) for approximating normal/log-normal distributions with the CLT is very large (e.g., several hundreds), thus can rarely be collected in day-to-day practices using only 20-30 benchmarks (with one to a few data sets each)." (p. 1448)

- **Paráfrase (Citação Indireta Acadêmica):**
  A partir de experimentos com o dataset KDataSets (32.000 execuções de benchmarks MiBench), Chen et al. (2015, p. 1448) verificam que a convergência do TCL para distribuições de desempenho computacional requer amostras de **várias centenas de observações** — chegando a 1.000 para distribuições log-normais. Com amostras de tamanho 20, o percentual de aproximações normais bem-sucedidas é inferior a 10%, tornando inapropriado o uso de testes t paramétricos nesse regime amostral. Este resultado tem implicação direta no nosso projeto: com 20 rodadas por máquina no Geekbench 6, não podemos afirmar com confiança estatística formal (nível 0,95) que as diferenças observadas entre máquinas são estatisticamente significativas no sentido do teste t. Nosso enfoque metodológico, portanto, concentra-se na análise descritiva (médias e desvios padrão) complementada pela interpretação arquitetural das diferenças observadas.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** — parágrafo de limitações metodológicas, como nota de rigor científico sobre o escopo inferencial das análises.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → 20 linhas de dados por arquivo: nosso $n=20$ está exatamente no regime identificado pelos autores como insuficiente para normalidade amostral. Isso deve ser explicitado como limitação no artigo.

---

### 3.7 — Outliers de Desempenho e Quebra da Normalidade em Benchmarks Cruzados

- **Conceito/Teoria:** Outliers de desempenho em benchmarks reais comprometem premissas de normalidade

- **Citação Direta (Ipsis Litteris):**
  > "Performance outliers have already been quite common in performance reports of latest commodity computers, and have been significant enough to break the normality/log-normality of computer performance. [...] In the era of dark silicon, this trend will become even more distinct, as specialized hardware accelerators designed for specific applications may produce more significant performance outliers." (p. 1448)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, p. 1448) alertam que outliers de desempenho são cada vez mais comuns em computadores de propósito geral modernos, a ponto de comprometerem sistematicamente as premissas de normalidade e log-normalidade das distribuições de desempenho. No contexto da chamada *era do silício escuro* (dark silicon), em que processadores incorporam aceleradores heterogêneos especializados (como as GPUs integradas Intel UHD 620 e MX130 presentes na Máquina D), essa tendência se intensifica: cargas de trabalho que ativam ou desativam esses aceleradores podem gerar picos e vales de desempenho consideravelmente mais acentuados do que em arquiteturas homogêneas convencionais.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (subseção de Benchmarks e Métricas de Desempenho), ao discutir as limitações dos benchmarks sintéticos como o Geekbench 6 em arquiteturas heterogêneas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → colunas `Carga do núcleo da GPU (%)` e `GPU D3D Uso (avg) (%)`: rodadas do Geekbench 6 que ativam significativamente a GPU da Máquina D (MX130 ou UHD 620) podem gerar scores anormalmente altos (outliers positivos), enquanto rodadas em que a GPU permanece inativa ficam abaixo da média — padrão de outlier descrito pelos autores.
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: valores discrepantes (mais de 2 desvios padrão acima ou abaixo da média) em qualquer das 20 rodadas devem ser tratados com os cuidados metodológicos descritos por Chen et al.

---

### 3.8 — Erro da Média Geométrica como Estimador de Speedup (GM-Speedup)

- **Conceito/Teoria:** Imprecisão da média geométrica como estimador de speedup entre sistemas

- **Citação Direta (Ipsis Litteris):**
  > "Compared with the HPT, the common practice which uses geometric mean performance scores to estimate the performance speedup of one computer over another has errors of 8:0 to 56:3 percent on SPEC CPU2006 or SPEC MPI2007." (p. 1443)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, p. 1443) demonstram que a prática consolidada de estimar o speedup entre computadores pela razão entre suas médias geométricas de desempenho — adotada pelo consórcio SPEC e por grande parte da literatura de Arquitetura de Computadores — pode introduzir erros que variam de 8,0% a 56,3% em relação ao speedup real estimado com confiança de 0,95 pelo framework HPT. Este resultado tem implicação direta para a interpretação dos nossos dados: ao comparar os scores médios do Geekbench 6 entre as Máquinas A, B, C e D, os valores de speedup relativo calculados devem ser apresentados como estimativas descritivas, não como medidas precisas de superioridade arquitetural absoluta.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Resultados e Discussão**, como nota metodológica ao apresentar as tabelas comparativas de scores médios entre máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: ao calcular a razão $\bar{X}_{\text{Maq}_i} / \bar{X}_{\text{Maq}_j}$ para estimar o speedup relativo entre máquinas, aplica-se diretamente a limitação descrita pelos autores — o valor obtido é uma estimativa pontual sem garantia de confiança, devendo ser apresentado com o Desvio Padrão correspondente.

---

### 3.9 — Uso Incorreto do Teste t com Amostras Pequenas e Não Normais

- **Conceito/Teoria:** Falha do teste t paramétrico na presença de outliers e amostras insuficientes

- **Citação Direta (Ipsis Litteris):**
  > "Voluntarily ignoring that fact, we incorrectly use the paired t-test, and get the conclusion 'BL265+ does not significantly outperform CELSIUS R550 at the significance level 0.05 (the confidence level 0.95)'. This conclusion apparently contradicts the straightforward fact that BL265+ outperforms CELSIUS R550 on all 12 benchmarks of SPECint2006." (p. 1448–1449)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, pp. 1448–1449) apresentam um caso exemplar em que a aplicação inadequada do teste t paramétrico — desconsiderando a não normalidade da distribuição de desempenho causada por outliers — gerou uma conclusão **contraditória com a evidência empírica direta**: o teste t indicou ausência de diferença significativa entre dois sistemas, quando na realidade um deles superava o outro em todos os benchmarks avaliados. O mecanismo de falha é claro: o teste t aplica um ajuste simétrico à distribuição de desempenho real (assimétrica à direita), estendendo artificialmente a cauda esquerda e diluindo o poder discriminativo do teste. Este resultado serve como advertência metodológica para nosso projeto: a simples inspeção das médias dos scores Geekbench, sem consideração da variabilidade amostral e da distribuição subjacente, pode levar a interpretações incorretas sobre a superioridade arquitetural de uma máquina sobre outra.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** (subseção de Análise Estatística e Limitações), como justificativa para a adoção de análise descritiva robusta em vez de testes de hipótese paramétricos.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: diferenças de score entre máquinas que parecem expressivas pela comparação de médias podem não ser estatisticamente significativas com $n=20$ e distribuições potencialmente não normais — limitação que deve ser explicitada nos Resultados.

---

### 3.10 — Framework HPT: Teste Não Paramétrico Hierárquico de Desempenho

- **Conceito/Teoria:** Framework HPT baseado nos testes de Wilcoxon para comparações de desempenho com confiança formal

- **Citação Direta (Ipsis Litteris):**
  > "We propose a non-parametric hierarchical performance testing (HPT) framework for performance comparison, which is significantly more practical than standard t-statistics because it does not require to collect a large number of performance observations in order to achieve a normal distribution of sample mean." (p. 1442)

- **Paráfrase (Citação Indireta Acadêmica):**
  O framework HPT proposto por Chen et al. (2015, p. 1442) combina, em dois níveis hierárquicos, testes estatísticos não paramétricos da família Wilcoxon: (1) o **Wilcoxon Rank-Sum Test** para comparação de desempenho por aplicação individual (nível uni-aplicação), e (2) o **Wilcoxon Signed-Rank Test** para síntese da comparação cruzada sobre múltiplos benchmarks (nível cross-aplicação). A principal vantagem do HPT em relação ao teste t reside na **ausência de pressupostos distributivos**: o framework produz estimativas de confiança válidas mesmo quando as distribuições de desempenho são não normais e o número de observações é pequeno, tornando-o especialmente adequado para cenários como o nosso, com apenas 20 rodadas por máquina.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** ou **Fundamentação Teórica**, como referência ao estado da arte em metodologia de comparação estatística de desempenho. Pode ser citado também no parágrafo de trabalhos relacionados.

  > ⚠️ **NOTA PREDITIVA:** O framework HPT não será implementado em nosso projeto (requer dados adicionais e software especializado). Sua citação serve para contextualizar as limitações metodológicas da nossa abordagem de análise descritiva e justificar trabalhos futuros. Esta referência foi fichada de forma preditiva e **sua utilização na redação final deve ser validada pelo grupo conforme o escopo final do artigo**.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: em um cenário de expansão futura, as 20 observações por máquina poderiam ser submetidas ao teste Wilcoxon Rank-Sum para comparação par a par entre máquinas, produzindo comparações com confiança formal mesmo sem normalidade amostral.

---

### 3.11 — Speedup com Confiança Garantida (r-Speedup)

- **Conceito/Teoria:** r-Speedup como métrica de desempenho relativo com garantia probabilística

- **Citação Direta (Ipsis Litteris):**
  > "The r-Speedup of computer A over computer B is the largest speedup of A over B having a confidence above r. [...] Given the confidence level r (e.g., r = 0:95), the r-Speedup can be viewed as a quantitative indicator of performance speedup with the guarantee of confidence r." (p. 1451)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, p. 1451) introduzem o conceito de **r-Speedup** como a alternativa estatisticamente rigorosa à comparação por média geométrica: trata-se do maior speedup de um sistema A sobre um sistema B para o qual é possível garantir um nível de confiança igual a $r$ (tipicamente $r = 0{,}95$). Diferentemente do speedup pela média geométrica — que é um escalar pontual sem garantia probabilística —, o $r$-Speedup encapsula a variabilidade amostral e entrega um resultado conservador, porém confiável. No contexto do nosso projeto, onde comparamos os scores Single_Core e Multi_Core do Geekbench 6 entre quatro máquinas com arquiteturas distintas, o conceito do $r$-Speedup serve como referência teórica para qualificar nossas afirmações de superioridade: ao dizer que "a Máquina X obteve score Y% superior à Máquina Z", deve-se explicitar que se trata de estimativa pela média amostral, sujeita às limitações de tamanho amostral discutidas por Chen et al.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Resultados e Discussão**, ao comentar as diferenças de desempenho relativo entre as máquinas com base nos scores médios do Geekbench.

  > ⚠️ **NOTA PREDITIVA:** Este conceito foi fichado de forma preditiva. Sua utilização depende da disponibilidade das especificações das Máquinas A, B e C, que ainda não foram formalizadas pelo grupo. Após o preenchimento dessas informações, poderá ser incorporado à discussão comparativa de resultados se os dados suportarem tal análise.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: ao calcular e apresentar a razão entre médias de scores de pares de máquinas, a citação de Chen et al. (2015) fornece o embasamento teórico para reconhecer as limitações estatísticas dessas estimativas de speedup relativo.

---

### 3.12 — Benchmark Suite como Amostra da Distribuição de Aplicações

- **Conceito/Teoria:** Benchmark suite como amostra representativa da distribuição de aplicações reais

- **Citação Direta (Ipsis Litteris):**
  > "The benchmark suite (e.g, SPECint2006 and SPECfp2006) utilized to evaluate the performance of the computer can be viewed as a representative sample of the application distribution." (p. 1444)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, p. 1444) conceituam uma suíte de benchmarks como uma amostra representativa da distribuição de aplicações reais que um sistema computacional pode executar. Essa perspectiva é transferível para o Geekbench 6: seus subtestes (criptografia, compressão, renderização, inferência de ML, entre outros) representam amostras de diferentes classes de carga de trabalho, e os scores Single-Core e Multi-Core sintetizam o desempenho do sistema nessa amostra específica. Consequentemente, a validade dos scores como indicadores de desempenho geral depende da representatividade dos subtestes em relação à carga de trabalho de interesse.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (subseção de Benchmarks Sintéticos), ao apresentar o Geekbench 6 e contextualizar o que seus scores representam e quais são seus limites de generalização.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: os scores do Geekbench 6 são a *performance measure* (métrica de desempenho) que aproxima a *quantitative feature* (característica quantitativa) da distribuição de desempenho de cada máquina para a distribuição de aplicações emulada pelo benchmark.

---

### 3.13 — Aceleradores Heterogêneos e Outliers Acentuados em Microarquiteturas P+E (Atualização: Tabela de Hardware com Núcleos Híbridos)

> ⚠️ **NOTA DE ATUALIZAÇÃO:** Este item foi acrescentado após o detalhamento completo da tabela de hardware (Máquinas A, B, E e F), que revelou processadores com arquitetura híbrida de núcleos *Performance* (P-cores) e *Efficient* (E-cores) — Intel Core i5-13420H (4P+4E), i5-1334U (2P+8E) e i5-14600KF (6P+8E). Este fichamento reutiliza a fundamentação já apresentada no item 3.7, agora aplicada de forma específica e mais precisa a este tipo de heterogeneidade microarquitetural.

- **Conceito/Teoria:** Outliers de desempenho intensificados por aceleradores/núcleos heterogêneos especializados ("dark silicon")

- **Citação Direta (Ipsis Litteris) — mesma citação do item 3.7, reaplicada a um contexto mais específico:**
  > "Performance outliers have already been quite common in performance reports of latest commodity computers, and have been significant enough to break the normality/log-normality of computer performance. [...] In the era of dark silicon, this trend will become even more distinct, as specialized hardware accelerators designed for specific applications may produce more significant performance outliers." (p. 1448)

- **Paráfrase (Citação Indireta Acadêmica):**
  A previsão de Chen et al. (2015, p. 1448) sobre o agravamento de outliers de desempenho em arquiteturas com **aceleradores especializados heterogêneos** encontra correspondência direta nas Máquinas A (Intel Core i5-13420H, 4P+4E), B (Intel Core i5-1334U, 2P+8E) e F (Intel Core i5-14600KF, 6P+8E) de nosso conjunto de dados. Nessas CPUs, o escalonador de threads do Windows 11 (Intel Thread Director) decide dinamicamente, rodada a rodada, se uma carga de trabalho do Geekbench 6 é despachada para um núcleo de Performance (maior clock, maior IPC) ou para um núcleo de Efficient (menor clock, maior eficiência energética). Essa decisão de escalonamento — não inteiramente determinística e sensível ao estado térmico e de ocupação do sistema no instante da execução — constitui exatamente o tipo de fator estocástico que, segundo os autores, produz distribuições de desempenho com **maior dispersão e outliers mais acentuados** em comparação a arquiteturas homogêneas (como a Máquina C, AMD Ryzen 5 3500U, 4 núcleos simétricos, ou a Máquina D, Intel Core i5-8265U, 4 núcleos simétricos). Espera-se, portanto, que o Desvio Padrão Amostral $S$ dos scores Multi_Core das Máquinas A, B e F seja proporcionalmente mais elevado do que o das máquinas com núcleos homogêneos, não necessariamente por instabilidade térmica, mas pela própria natureza do escalonamento heterogêneo.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Resultados e Discussão**, na subseção que compara o Desvio Padrão dos scores Multi_Core entre máquinas com CPUs híbridas (A, B, F) e máquinas com CPUs homogêneas (C, D, E).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqF.txt` → coluna `Multi_Core`: candidatas a apresentar Desvio Padrão $S$ relativamente mais elevado em razão da alternância de escalonamento entre P-cores e E-cores entre rodadas.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → colunas `Core 0 T0 Relógio efetivo (MHz)` até `Core 3 T1 Relógio efetivo (MHz)` (e, quando disponíveis para mais núcleos, as colunas equivalentes): permitem identificar, rodada a rodada, se a carga de trabalho foi predominantemente executada em núcleos com clock mais alto (P-cores) ou mais baixo (E-cores), evidenciando empiricamente a fonte da variabilidade.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna `Uso do núcleo (avg) (%)`: picos desbalanceados de utilização entre núcleos ao longo da rodada sustentam a hipótese de escalonamento heterogêneo como fonte de variabilidade.

  > ⚠️ **NOTA DE LIMITAÇÃO DE COLUNAS:** A lista de colunas do CSV fornecida no escopo do projeto contempla explicitamente apenas 4 núcleos (`Core 0` a `Core 3`). Como as Máquinas A, B, E e F possuem 6, 10, 6 e 14 núcleos físicos respectivamente, **pode ser necessário solicitar ao grupo a confirmação de colunas adicionais** (`Core 4` em diante) presentes nos arquivos CSV reais dessas máquinas, caso o HWiNFO64 as tenha registrado. Caso essas colunas não existam nos arquivos coletados, a análise por núcleo individual deve se limitar aos núcleos 0–3 disponíveis, e este fato deve ser declarado como limitação na Metodologia.

---

### 3.14 — Diversidade de Fator de Forma (Desktop vs. Notebook) e Implicações no TDP/Confiança da Amostra

> ⚠️ **NOTA DE ATUALIZAÇÃO:** Este item foi acrescentado após a inclusão das Máquinas E (Desktop, AMD Ryzen 5 5500, TDP 65 W) e F (Desktop, Intel Core i5-14600KF, TDP 125 W) na tabela de hardware, ampliando o escopo do estudo de notebooks ultrafinos/gamer para também incluir desktops montados.

- **Conceito/Teoria:** Generalização da comparação de desempenho exige cautela quando a "distribuição de aplicações" amostrada (benchmark) é executada em populações de hardware com características físicas (TDP, dissipação térmica, fator de forma) substancialmente distintas

- **Citação Direta (Ipsis Litteris):**
  > "The application distribution specifies how likely an application is executed on the computer. [...] the benchmark suite [...] utilized to evaluate the performance of the computer can be viewed as a representative sample of the application distribution." (p. 1443–1444)

- **Paráfrase (Citação Indireta Acadêmica):**
  Chen et al. (2015, pp. 1443–1444) definem a distribuição de aplicações como a frequência com que diferentes cargas de trabalho são executadas em um dado computador, e o benchmark como amostra dessa distribuição. Esse arcabouço conceitual reforça uma ressalva metodológica importante para a nova composição do nosso conjunto de máquinas: as Máquinas E e F (desktops montados, TDP de 65 W e 125 W) e as Máquinas A, B, C e D (notebooks, com TDP de 15 W a 45 W) não compartilham o mesmo envelope térmico nem o mesmo regime de dissipação de calor, ainda que executem exatamente a mesma suíte de benchmark (Geekbench 6). Isso significa que, embora a *distribuição de aplicações* amostrada seja idêntica entre os dois grupos, a *distribuição de desempenho* resultante pode divergir não apenas pela microarquitetura da CPU, mas pelo próprio fator de forma do sistema — um desktop com TDP de 125 W (Máquina F) tem folga térmica para sustentar o boost máximo por mais tempo do que um notebook ultrafino de 15 W (Máquinas B, C, D), introduzindo um viés sistemático (não aleatório) na comparação entre os dois grupos que deve ser explicitamente reconhecido, e não absorvido implicitamente no Desvio Padrão amostral de cada máquina individual.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia**, no parágrafo que apresenta a Tabela de hardware comparativo, como ressalva sobre a heterogeneidade de TDP/fator de forma entre os seis sistemas avaliados; pode ser retomado na **Discussão** ao comparar Notebooks vs. Desktops.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna `Potência total da CPU (W)`: espera-se que os desktops sustentem valores médios de potência mais próximos do TDP nominal (65 W e 125 W) por períodos mais longos, sem a contenção agressiva observada em notebooks.
  - `maqA_rodada_*.CSV` a `maqD_rodada_*.CSV` → coluna `CPU Inteira (°C)` e `Estrangulamento térmico do núcleo (avg) (Yes/No)`: notebooks (TDP 15–45 W) são candidatos mais prováveis a apresentar throttling térmico recorrente, dado o menor volume de dissipação em relação aos desktops.
  - `scores_maqE.txt`, `scores_maqF.txt` → coluna `Multi_Core`: espera-se Desvio Padrão $S$ proporcionalmente menor nos desktops, pela maior estabilidade térmica/elétrica do fator de forma, em contraste com a maior variabilidade potencialmente observada nos notebooks.

  > ⚠️ **NOTA PREDITIVA:** Os campos `[Preencher Gabinete]*` (modelo do gabinete das Máquinas E e F) ainda não foram preenchidos pelo grupo. Esta lacuna não compromete o fichamento teórico acima, mas deve ser solicitada ao grupo antes da redação final da Tabela de Hardware no `main.tex`, pois o modelo do gabinete/fonte de alimentação pode influenciar a capacidade de dissipação térmica e, consequentemente, a sustentação do boost de clock discutida neste item.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 — Equações LaTeX das Definições Estatísticas Fundamentais

As seguintes equações são extraídas textualmente de Chen et al. (2015, p. 1444) e devem ser incluídas na seção de **Metodologia** do `main.tex` com a citação correspondente:

```latex
% Média Aritmética Amostral
\begin{equation}
    \bar{X} = \frac{1}{n}\left(X_1 + \cdots + X_n\right)
    \label{eq:media_amostral}
\end{equation}

% Desvio Padrão Amostral (com Correção de Bessel)
\begin{equation}
    S = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}\left(X_i - \bar{X}\right)^2}
    \label{eq:desvio_padrao}
\end{equation}
```

**Texto de apoio para o `main.tex`:**
> "Para a análise estatística dos scores de desempenho e das métricas de telemetria, adota-se a Média Aritmética Amostral $\bar{X}$ (Equação~\ref{eq:media_amostral}) e o Desvio Padrão Amostral $S$ (Equação~\ref{eq:desvio_padrao}), conforme as definições formais estabelecidas por \cite{chen:15}. O fator $n-1$ no denominador de $S$ corresponde à correção de Bessel, que garante a estimação não viesada da variância populacional a partir de amostras finitas."

---

### 4.2 — Equação da Estatística t (Contexto de Limitações Metodológicas)

```latex
% Estatística T de Student (referenciada como limitação metodológica)
\begin{equation}
    T = \frac{\sqrt{n}\left(\bar{X} - \mu\right)}{S}
    \label{eq:t_student}
\end{equation}
```

**Nota de uso:** Esta equação deve ser referenciada na subseção de limitações estatísticas, citando Chen et al. (2015), para explicar por que o teste t **não é aplicável** diretamente à nossa análise com $n=20$ e distribuições possivelmente não normais.

---

### 4.3 — Sugestões de Gráficos e Tabelas Correspondentes no Matplotlib/LaTeX

**Gráfico 1 — Barplot de Scores com Hastes de Erro (Desvio Padrão):**
Gráfico de barras com 4 grupos (Máquinas A, B, C, D), duas barras por grupo (Single_Core e Multi_Core), com hastes de erro representando $S$ (Desvio Padrão Amostral das 20 rodadas). Fundamentação direta nas Equações 1 e 2 de Chen et al. (2015). No `main.tex`, referenciar como:
```
como observado na Figura~\ref{fig:barplot_scores}
```

**Gráfico 2 — Histograma de Distribuição dos Scores por Máquina:**
Para evidenciar a assimetria positiva discutida pelos autores (Seção 3.1 do artigo), plotar histogramas dos 20 scores Single_Core e Multi_Core por máquina, com curva de ajuste normal sobreposta (equivalente ao método NNF dos autores). Isso visualizará se há outliers e assimetria nas distribuições das nossas máquinas.

**Código Python sugerido para o histograma:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
maquinas = ['A', 'B', 'C', 'D']

for idx, maq in enumerate(maquinas):
    df = pd.read_csv(f'scores_maq{maq}.txt', sep=';')
    for row, col in enumerate(['Single_Core', 'Multi_Core']):
        ax = axes[row][idx]
        data = df[col].values
        ax.hist(data, bins=8, color='gray', edgecolor='black',
                density=True, alpha=0.7)
        mu, std = data.mean(), data.std(ddof=1)
        x = np.linspace(data.min(), data.max(), 100)
        ax.plot(x, norm.pdf(x, mu, std), 'k--', lw=1.5,
                label=f'Normal ajustada\n$\\bar{{X}}$={mu:.0f}, S={std:.0f}')
        ax.set_title(f'Máq. {maq} — {col}', fontsize=9)
        ax.legend(fontsize=7)
        ax.set_xlabel('Score', fontsize=8)
        ax.set_ylabel('Densidade', fontsize=8)

plt.suptitle('Distribuição dos Scores Geekbench 6 por Máquina\n'
             'Fonte: Os autores (2026)', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('fig_histogramas_scores.pdf', dpi=300, bbox_inches='tight',
            facecolor='white')
plt.savefig('fig_histogramas_scores.png', dpi=300, bbox_inches='tight',
            facecolor='white')
```

**Tabela LaTeX — Estatísticas Descritivas dos Scores:**
```latex
\begin{table}[ht]
\caption{Estatísticas descritivas dos scores do Geekbench 6 (20 rodadas por máquina)}
\label{tab:estatisticas_scores}
\centering
\begin{tabular}{lcccc}
\hline
\textbf{Máquina} & \textbf{$\bar{X}$ Single} & \textbf{$S$ Single} & \textbf{$\bar{X}$ Multi} & \textbf{$S$ Multi} \\
\hline
Máquina A & -- & -- & -- & -- \\
Máquina B & -- & -- & -- & -- \\
Máquina C & -- & -- & -- & -- \\
Máquina D & -- & -- & -- & -- \\
\hline
\end{tabular}
\medskip

{\small Fonte: Dados da pesquisa (2026). $\bar{X}$: Média Aritmética Amostral; $S$: Desvio Padrão Amostral \cite{chen:15}.}
\end{table}
```

---

## 5. SUGESTÕES DE KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

### Em inglês (Google Scholar):
1. `"benchmark performance variability" "standard deviation" computer architecture`
2. `"non-deterministic performance" benchmark reproducibility CPU`
3. `"statistical performance comparison" computers benchmark`
4. `"performance distribution" benchmark "normal distribution" test`
5. `"Geekbench" "statistical analysis" CPU performance variance`
6. `"sample size" performance benchmarking confidence interval`
7. `"Wilcoxon test" performance comparison computer systems`
8. `"thermal throttling" performance variability benchmark`
9. `"performance measurement methodology" CPU benchmark repeated runs`
10. `"SPEC benchmark" variability "standard deviation" performance`

### Em português (Google Acadêmico):
1. `"variabilidade de desempenho" benchmark processador estatística`
2. `"desvio padrão" benchmark CPU análise estatística comparação`
3. `"comparação de desempenho" computadores estatística intervalo confiança`
4. `"benchmark sintético" análise estatística processador`
5. `"estrangulamento térmico" variabilidade desempenho benchmark`

---

## 6. NOTAS FINAIS DE UTILIZAÇÃO NO ARTIGO

1. **Citação na Metodologia (Fórmulas):** Inserir `\cite{chen:15}` imediatamente após as Equações de $\bar{X}$ e $S$, indicando que as definições formais adotadas seguem Chen et al. (2015).

2. **Citação nas Limitações:** Usar paráfrase da Seção 3.6 (item 3.6 deste fichamento) para justificar que $n=20$ é insuficiente para testes t formais, e que os resultados devem ser interpretados como análise descritiva.

3. **Citação na Discussão (Variabilidade e Throttling):** Usar paráfrase da Seção 3.1 (item 3.5 deste fichamento) para interpretar Desvios Padrão mais elevados em máquinas com maior incidência de throttling térmico — remetendo ao conceito de distribuições com cauda longa à direita.

4. **Chave BibTeX para uso em `main.tex`:** `\cite{chen:15}`

5. **Acesso ao artigo:** Autorizado para a UNIVERSIDADE FEDERAL DO PARÁ via IEEE Xplore (baixado em 16 de junho de 2026).
