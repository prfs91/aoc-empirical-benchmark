# FICHAMENTO CIENTÍFICO COMPLETO
**Arquivo:** `fichamento_CompartilhamentoCacheMultiCore_Alves.md`
**Gerado para:** Disciplina de Arquitetura e Organização de Computadores — UFPA/Campus Tucuruí
**Prof. Orientador:** Prof. Dr. Iago Medeiros

---

## ✅ VEREDITO DE RELEVÂNCIA

**O artigo será útil para o nosso projeto de AOC? SIM.**

A dissertação é **altamente relevante** para o projeto do grupo. Ela aborda diretamente: hierarquia de memória cache (L1/L2/L3), desempenho de processadores multi-core, métricas de benchmarking (MPKI, Speedup, MFLOPS, IPC), consumo de potência energética, coerência de memória em arquiteturas compartilhadas, e metodologia estatística rigorosa com média, desvio padrão, coeficiente de variação e intervalo de confiança. Todos esses temas mapeiam diretamente nossas colunas de telemetria do HWiNFO64 e nos scores do Geekbench 6.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

ALVES, Marco Antonio Zanata. **Avaliação do Compartilhamento das Memórias Cache no Desempenho de Arquiteturas Multi-Core.** 2009. 175 f. Dissertação (Mestrado em Ciência da Computação) — Programa de Pós-Graduação em Computação, Instituto de Informática, Universidade Federal do Rio Grande do Sul (UFRGS), Porto Alegre, 2009. Orientador: Prof. Dr. Philippe O. A. Navaux.

- **Código BibTeX Completo (.bib):**

```bibtex
@MastersThesis{alves:09,
  author      = {Marco Antonio Zanata Alves},
  title       = {Avalia{\c{c}}{\~a}o do Compartilhamento das
                 Mem{\'o}rias Cache no Desempenho de
                 Arquiteturas Multi-Core},
  school      = {Programa de P{\'o}s-Gradua{\c{c}}{\~a}o em
                 Computa{\c{c}}{\~a}o ({PPGC}), Instituto de
                 Inform{\'a}tica, Universidade Federal do Rio
                 Grande do Sul ({UFRGS})},
  year        = {2009},
  address     = {Porto Alegre, Brasil},
  type        = {Disserta{\c{c}}{\~a}o de Mestrado},
  note        = {Orientador: Prof. Dr. Philippe O. A. Navaux.
                 175 f.}
}
```

> ⚠️ **Nota editorial:** O documento é uma Dissertação de Mestrado defendida em março de 2009 na UFRGS/PPGC. Não possui DOI público identificado. A referência acima está completa para uso no `sbc-template.bib`. O comando de citação no `main.tex` deverá ser `\cite{alves:09}`.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Dissertação de Mestrado em Ciência da Computação
- **Instituição/Editora:** Programa de Pós-Graduação em Computação (PPGC) — Instituto de Informática — Universidade Federal do Rio Grande do Sul (UFRGS) — Porto Alegre, RS, Brasil
- **Ano:** 2009 (Porto Alegre, Março de 2009)
- **Autor:** Marco Antonio Zanata Alves
- **Orientador:** Prof. Dr. Philippe Olivier Alexandre Navaux
- **Palavras-Chave Originais:** Memória cache; Processador multi-core; Arquitetura de computadores; Processamento de alto desempenho
- **Número de Páginas:** 175
- **Ferramentas Utilizadas:** Simulador Simics (Virtutech AB); Ferramenta Cacti (modelagem física de latência, potência e área de memória cache); Benchmark NAS-NPB (Numerical Aerodynamic Simulation — NASA Parallel Benchmarks)

**Resumo do Escopo Geral:**
A dissertação avalia experimentalmente diferentes configurações de compartilhamento de memória cache L2 em processadores multi-core e many-core, utilizando simulação por conjunto de instruções no ambiente Simics. O autor propõe e executa seis experimentos distintos, variando o grau de compartilhamento da cache L2 (de 1 a 32 núcleos por banco), o tamanho da cache, a associatividade, o tamanho da linha de dados, os níveis hierárquicos (L2/L3) e a contenção por portas de acesso. As latências físicas de memória são modeladas pela ferramenta Cacti, tornando as comparações próximas de sistemas reais. Os resultados demonstram que o equilíbrio entre tamanho do banco, latência de acesso e grau de compartilhamento é crítico para o desempenho: as organizações **1Core/L2** e **2Cores/L2** com bancos de 2 MB e linha de 128 bytes se mostraram as melhores escolhas para sistemas de propósito geral.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 Hierarquia de Memória e o Gap Processador–DRAM

- **Conceito/Teoria:** Distanciamento histórico de desempenho entre processador e memória DRAM; motivação para a hierarquia de memória.

- **Citação Direta (Ipsis Litteris):**
> "Com os agressivos crescimentos de velocidade dos processadores a cada ano, e a velocidade de memória apresentando crescimentos bem inferiores, fez-se necessário a criação de hierarquias de memórias que tiram proveito do custo/desempenho de tecnologias de memória." (Apêndice A, p. 137)

- **Paráfrase (Citação Indireta Acadêmica):**
Em decorrência do crescimento assimétrico entre as velocidades de processamento e de acesso à memória DRAM ao longo das décadas, tornou-se imprescindível a organização hierárquica dos sistemas de memória, de forma que os níveis mais rápidos — e consequentemente mais caros — fiquem próximos das unidades de processamento, enquanto os níveis mais lentos, de maior capacidade e menor custo, atuam como repositórios intermediários (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Hierarquia de Memória. Este trecho introduz o problema central que justifica a existência das caches L1, L2 e L3 em todos os processadores das nossas Máquinas A, B, C e D.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: o score reflete indiretamente a eficácia da hierarquia de cache no tempo de execução dos kernels do Geekbench 6.
  - `maq*_rodada_*.CSV` → `Relógio da memória (MHz)`: operando a 1333 MHz na Máquina D (Single Channel), o subsistema de memória representa o gargalo mais crítico no contexto do gap processador–DRAM discutido pelo autor.
  - `maq*_rodada_*.CSV` → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: evidenciam empiricamente a largura de banda do subsistema de memória em operação real.

---

### 3.2 Princípios de Localidade Temporal e Espacial

- **Conceito/Teoria:** Localidade Temporal e Localidade Espacial — fundamentos do funcionamento eficiente das memórias cache.

- **Citação Direta (Ipsis Litteris):**
> "• Localidade Temporal: Essa localidade diz respeito à necessidade temporal dos dados: se um item é referenciado, ele tende a ser referenciado novamente em breve. [...] • Localidade Espacial: Essa localidade é referente ao local de armazenamento da memória: se um item é referenciado, os itens de endereços próximos tendem a ser referenciados em breve." (Apêndice A, p. 139)

- **Paráfrase (Citação Indireta Acadêmica):**
O funcionamento eficiente das hierarquias de memória cache fundamenta-se em dois princípios complementares de localidade: a localidade temporal, segundo a qual dados acessados recentemente tendem a ser reutilizados em curto intervalo de tempo, e a localidade espacial, pela qual o acesso a um endereço de memória prediz acessos imediatos a posições adjacentes. Esses princípios motivam tanto as estratégias de pré-busca quanto as políticas de substituição de blocos nas memórias cache modernas (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Hierarquia de Memória / Memórias Cache.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Relógio da memória (MHz)`: frequências mais altas de memória ampliam a largura de banda, reduzindo a penalidade de falta (miss penalty) em casos onde a localidade espacial não é explorada a contento.
  - `maq*_rodada_*.CSV` → `Carga da memória física (%)`: elevada carga da memória física indica que os dados ativos excedem o que a cache consegue reter, comprometendo a localidade temporal.

---

### 3.3 Classificação das Faltas de Cache (os 4 Cs)

- **Conceito/Teoria:** Taxonomia das origens das faltas de dados na cache: Compulsórias, Capacidade, Conflito e Coerência.

- **Citação Direta (Ipsis Litteris):**
> "• Compulsórios – O primeiro acesso a qualquer bloco não pode ser realizado pois a cache está vazia [...] • Capacidade – Se a cache não puder conter todos os blocos de dados necessários durante a execução de um programa [...] • Conflito – Se a cache não puder manter mais dados de mesmo endereçamento [...] • Coerência – Quando a cache precisa remover ou limpar alguns blocos de dados a fim de manter em um estado coerente um sistema com múltiplas caches." (Apêndice A, p. 140)

- **Paráfrase (Citação Indireta Acadêmica):**
As faltas de dados em memórias cache são classificadas em quatro categorias fundamentais: faltas compulsórias, inevitáveis no primeiro acesso a qualquer bloco; faltas de capacidade, decorrentes da insuficiência do tamanho total da cache para conter o conjunto de trabalho ativo da aplicação; faltas de conflito, provocadas por colisões de endereçamento em caches de mapeamento direto ou de baixa associatividade; e faltas de coerência, exclusivas de sistemas multiprocessados com múltiplas cópias do mesmo bloco em caches distintas (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Memórias Cache; pode ser referenciado também em **Resultados e Discussão** para explicar variações de desempenho entre máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - **Máquina D (Roberta):** com apenas 6 MB de cache L3, aplicações que demandam conjuntos de trabalho maiores induzem faltas de **capacidade** — justificando scores mais baixos de Multi-Core no Geekbench 6 (`scores_maqD.txt` → `Multi_Core`).
  - `maq*_rodada_*.CSV` → `Carga da memória física (%)`: valores acima de 80% indicam alta pressão sobre a cache, correlacionando-se com maior taxa de faltas de capacidade.

> ⚠️ **Nota Preditiva:** Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário. Máquinas com caches L3 maiores ou com maior associatividade deverão apresentar menor taxa de faltas de capacidade e de conflito, resultando em scores Multi-Core superiores.

---

### 3.4 Memórias Cache para Processadores Multi-Core

- **Conceito/Teoria:** Demanda de suporte à vazão de dados para múltiplas threads simultâneas em arquiteturas multi-core; diferença entre caches privadas e compartilhadas.

- **Citação Direta (Ipsis Litteris):**
> "As memórias cache para processadores multi-core devem acompanhar o ritmo de inovações onde os novos projetos devem planejar o acesso a dados de múltiplas threads ao invés de apenas uma thread como acontecia nos processadores superescalares." (Capítulo 1, p. 23)

- **Paráfrase (Citação Indireta Acadêmica):**
Com a consolidação das arquiteturas multicore no mercado de processadores de propósito geral, o subsistema de memória cache passa a enfrentar um novo paradigma: ao invés de atender ao fluxo de dados de uma única thread, as memórias cache devem garantir alta vazão para múltiplos fluxos de instrução concorrentes, minimizando faltas, reduzindo latências de acesso e gerenciando eficientemente os protocolos de coerência entre núcleos (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Introdução** (motivação) ou **Fundamentação Teórica** (subseção sobre paralelismo e cache multi-core).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Uso total da CPU (%)` e `Utilização total da CPU (%)`: refletem o quanto os núcleos disponíveis estão sendo utilizados em paralelo durante o benchmark.
  - `maq*_rodada_*.CSV` → `Relógios efetivos núcleo (avg) (MHz)` e `Relógio da memória (MHz)`: a relação entre esses dois valores indica se o processador está aguardando dados da memória (subsistema sendo o gargalo) ou se os núcleos estão efetivamente em processamento.
  - `scores_maq*.txt` → `Multi_Core`: score diretamente impactado pela eficiência da cache em servir threads paralelas.

---

### 3.5 Métricas de Desempenho: Média, Desvio Padrão, COV e Intervalo de Confiança

- **Conceito/Teoria:** Metodologia estatística rigorosa para avaliação de sistemas computacionais; métricas utilizadas para garantir confiabilidade dos resultados.

- **Citação Direta (Ipsis Litteris) — Fórmulas extraídas do texto original:**

> "A média é a métrica básica para agrupar os dados de forma a gerar um valor significativo de toda amostra." (Cap. 3, p. 43)
>
> "O desvio padrão é obtido pela raiz quadrada da variância. Este valor é o mais comum para denotar a dispersão estatística." (Cap. 3, p. 43)
>
> "O coeficiente de variação ou apenas COV (Coefficient Of Variation) representa a taxa entre o desvio padrão e a média." (Cap. 3, p. 43)
>
> "Nas medições foi utilizado a métrica de um desvio padrão, para avaliar a confiança do resultado, sendo que o erro igual a um desvio padrão representa 81,30% em uma distribuição T Student." (Cap. 4, p. 76)

- **Fórmulas LaTeX extraídas do texto original (Seção 3.1.2, p. 43):**

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

$$\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

$$\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

$$\text{C.O.V.} = \frac{\sigma}{\bar{x}}$$

$$\bar{x} - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}} \;\leq\; \mu \;\leq\; \bar{x} + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}$$

**Código LaTeX puro para o `main.tex`:**

```latex
% Média Aritmética Amostral
\begin{equation}
    \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
    \label{eq:media}
\end{equation}

% Desvio Padrão Amostral
\begin{equation}
    \sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
    \label{eq:desvio_padrao}
\end{equation}

% Coeficiente de Variação
\begin{equation}
    \text{C.O.V.} = \frac{\sigma}{\bar{x}}
    \label{eq:cov}
\end{equation}
```

- **Paráfrase (Citação Indireta Acadêmica):**
A metodologia estatística adotada por Alves (2009) fundamenta-se em métricas clássicas de análise descritiva: a média aritmética, representada pela Equação~\ref{eq:media}, agrega as medições em um valor representativo; o desvio padrão amostral, dado pela Equação~\ref{eq:desvio_padrao}, quantifica a dispersão das medições em torno da média, sendo utilizado como intervalo de confiança de 81,30\% segundo a distribuição \textit{t} de Student; e o coeficiente de variação (C.O.V.), da Equação~\ref{eq:cov}, normaliza o desvio padrão pela média, permitindo comparações entre amostras de escalas distintas. O autor demonstrou que, para uma variação menor que 1\% nos resultados de ciclos de execução, foram necessárias apenas 5,15 repetições por experimento, validadas por 20 execuções iniciais.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** — subseção de Análise Estatística. As fórmulas devem ser incluídas no `main.tex` justificando nossa análise dos 20 dados do Geekbench 6 por máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → `Single_Core` e `Multi_Core`: as 20 rodadas por máquina permitem calcular $\bar{x}$ e $\sigma$ para cada métrica de desempenho, exatamente como proposto pelo autor.
  - `maq*_rodada_*.CSV` → TODAS as colunas críticas: a média temporal de cada rodada (ex.: `Relógios efetivos núcleo (avg) (MHz)`, `CPU Inteira (°C)`, `Potência total da CPU (W)`) deve ser calculada linha por linha no script Python antes de calcular $\sigma$ inter-rodadas.
  - **Desvio padrão alto** em uma máquina (ex.: alta variação em `Núcleo máximo (°C)`) indica instabilidade térmica — fenômeno diretamente discutido pelo autor em termos de variação não-determinística nos resultados.

---

### 3.6 Speedup e MPKI como Métricas de Comparação

- **Conceito/Teoria:** Definição formal de Speedup entre sistemas e de MPKI (Misses Per Kilo Instructions) como métrica normalizada de faltas de cache.

- **Citação Direta (Ipsis Litteris):**
> "O speedup de um sistema nada mais é que uma comparação de desempenho. [...] a primeira organização de memória cache avaliada [...] mostrando dessa maneira, os eventuais ganhos obtidos com cada abordagem." (Cap. 3, p. 43)
>
> "A métrica MPKI (misses per kilo instructions) de uma memória cache nada mais é que a taxa de faltas de dados a cada mil instruções executadas." (Cap. 3, p. 43)

- **Fórmulas LaTeX (Seção 3.1.2, p. 43–44):**

```latex
\begin{equation}
    \text{Speedup} = \frac{\text{Tempo no sistema base}}{\text{Tempo no sistema melhorado}}
    \label{eq:speedup}
\end{equation}

\begin{equation}
    \text{MPKI} = \frac{\text{Faltas de Dados}}{\text{Instruções Executadas} / 1000}
    \label{eq:mpki}
\end{equation}
```

- **Paráfrase (Citação Indireta Acadêmica):**
O speedup, conforme definido pela Equação~\ref{eq:speedup}, expressa o ganho relativo de desempenho de um sistema em relação a uma configuração de referência, sendo amplamente utilizado em avaliações de arquiteturas paralelas. Já o MPKI, apresentado na Equação~\ref{eq:mpki}, normaliza a contagem de faltas de cache pelo número de instruções executadas, permitindo comparações justas entre aplicações de diferentes densidades computacionais (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (definições de métricas) e **Resultados e Discussão** (ao comparar scores entre as quatro máquinas).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → `Multi_Core`: o speedup relativo entre máquinas pode ser calculado usando os scores como proxy de tempo de execução: $\text{Speedup}_{B/D} = \text{Score}_{B} / \text{Score}_{D}$.
  - O MPKI em si não é diretamente medido pelo HWiNFO64, mas a coluna `Carga da memória física (%)` e `Relógio da memória (MHz)` são os indicadores mais próximos disponíveis.

---

### 3.7 Potência Dinâmica, Estática e Energia Total do Sistema de Memória

- **Conceito/Teoria:** Definições formais de energia dinâmica, potência dinâmica, energia estática e potência total — métricas de eficiência energética arquitetural.

- **Citação Direta (Ipsis Litteris):**
> "A energia dinâmica de um sistema de memória é aquela necessária para efetuar cada operação de leitura ou escrita. [...] A potência dinâmica [...] é variável de acordo com a aplicação executada, assim, é dada pela energia dinâmica dividida pelo tempo de execução da aplicação." (Cap. 3, p. 44)

- **Fórmulas LaTeX (Seção 3.1.2, p. 44):**

```latex
\begin{equation}
    E_{\text{din}}(J) = E_{\text{op}}(J) \cdot N_{\text{op}}
    \label{eq:energia_din}
\end{equation}

\begin{equation}
    P_{\text{din}}(W) = \frac{E_{\text{din}}(J)}{t_{\text{ligado}}(s)}
    \label{eq:potencia_din}
\end{equation}

\begin{equation}
    E_{\text{total}}(J) = \sum_{i=1}^{n} \left( E_{\text{est},i} + E_{\text{din},i} \right)
    \label{eq:energia_total}
\end{equation}
```

- **Paráfrase (Citação Indireta Acadêmica):**
A avaliação energética de um sistema computacional desdobra-se em dois componentes fundamentais: a potência dinâmica, proporcional à frequência de operações realizadas sobre a memória, e a potência estática (ou de leakage), intrínseca à tecnologia de integração e independente das operações realizadas. A potência total do sistema é a soma de ambas as contribuições, e sua minimização representa um dos principais objetivos de projeto nas modernas arquiteturas multi-core, especialmente em cenários de uso intensivo com múltiplos núcleos compartilhando recursos de memória (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (consumo energético) e **Resultados e Discussão** (análise de Desempenho por Watt).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Potência total da CPU (W)`: métrica direta de potência do processador durante os benchmarks — análoga à potência dinâmica definida pelo autor.
  - `maq*_rodada_*.CSV` → `Potência de núcleos IA (W)` e `Potência de núcleo GT (W)`: decomposição da potência entre núcleos de processamento e gráficos integrados.
  - `maq*_rodada_*.CSV` → `Potência das linhas GPU (avg) (W)`: potência da GPU discreta (quando presente).
  - `maq*_rodada_*.CSV` → `Potência total do sistema (W)`: consumo agregado de todo o sistema computacional.
  - **Métrica derivada — Desempenho por Watt:** $\text{Perf/W} = \text{Score}_{\text{Geekbench}} / \overline{P_{\text{CPU}}}$, onde $\overline{P_{\text{CPU}}}$ é a média de `Potência total da CPU (W)` ao longo da rodada.

---

### 3.8 Compartilhamento de Cache L2 e Impacto no Desempenho

- **Conceito/Teoria:** Resultado central da dissertação — relação entre grau de compartilhamento da cache L2, latência de acesso, taxa de faltas e desempenho final do sistema.

- **Citação Direta (Ipsis Litteris):**
> "Com o aumento no compartilhamento dos blocos de memória cache, as aplicações tendem a usufruir de maior velocidade para o compartilhamento de dados entre os diversos fluxos de execução, reduzindo assim, a quantidade de faltas de dados. Por outro lado, o compartilhamento adotado nesse experimento manteve o total de memória cache do sistema, assim, ao aumentar o grau de compartilhamento, os bancos da memória cache formadas são maiores, influenciando no tempo de acesso a dados, consumo de potência e área ocupada." (Cap. 4, p. 78)

- **Citação Direta (Ipsis Litteris) — Conclusão sobre configuração ótima:**
> "apenas as organizações 1Core/L2 e 2Cores/L2 com tamanho total igual a 32MB (bancos de 2 MB compartilhados), com tamanho de linha igual a 128 B, permanecem como boa escolha de implementação física em sistemas de propósito geral." (Cap. 5, p. 135)

- **Paráfrase (Citação Indireta Acadêmica):**
Os experimentos demonstraram que o compartilhamento da cache L2 encerra um *trade-off* fundamental: enquanto bancos maiores compartilhados reduzem a taxa de faltas de dados ao permitir que múltiplos núcleos acessem um espaço de endereçamento comum, as maiores dimensões físicas desses bancos elevam a latência de acesso, o consumo de potência e a área de silício. Nas avaliações realizadas com cargas de trabalho científicas paralelas, a organização que combinou pequenos bancos de cache (2 MB por módulo L2) com compartilhamento limitado a dois núcleos mostrou o melhor equilíbrio entre redução de faltas, latência de acesso e custo físico (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Resultados e Discussão** — ao comparar o desempenho das quatro máquinas em função do tamanho de suas caches L3 e da organização de memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → `Multi_Core`: scores mais altos em máquinas com maior cache L3 ou Dual Channel (Máquinas A, B ou C) validam empiricamente o benefício do compartilhamento eficiente de memória descrito pelo autor.
  - `maq*_rodada_*.CSV` → `Carga da memória física (%)`: alta pressão sobre a memória física em máquinas com cache pequena (Máquina D: 6 MB L3, RAM Single Channel 1333 MHz) confirma a hipótese de faltas de capacidade.
  - `maq*_rodada_*.CSV` → `Relógio da memória (MHz)`: a Máquina D opera a 1333 MHz — abaixo do padrão DDR4 convencional de 2133+ MHz — amplificando a penalidade das faltas de cache, corroborando os resultados do autor sobre latência de acesso.

> ⚠️ **Nota Preditiva:** Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário. Máquinas com RAM Dual Channel e frequências mais altas deverão exibir comportamento mais próximo das organizações 2Cores/L2 avaliadas pelo autor.

---

### 3.9 Processadores Multi-Core: Arquitetura e Variantes Comerciais

- **Conceito/Teoria:** Caracterização técnica dos processadores Multi-Core; diferença entre SMT, IMT, BMT e CMP; estudo de casos AMD, Intel (Core2, Nehalem/i7), Sun (Niagara), IBM (Power).

- **Citação Direta (Ipsis Litteris):**
> "A família Nehalem representada pelo processador Core i7 [...] apresenta 4 núcleos de processamento, sendo que cada núcleo possui suporte à SMT de até 2 threads por núcleo, trabalhando assim com 8 threads ativas no total." (Cap. 2, p. 34)
>
> "A memória cache de primeiro e segundo nível desse processador Core i7 é privada para cada núcleo de processamento, possuindo uma memória cache de terceiro nível compartilhada entre todos os núcleos de processamento." (Cap. 2, p. 35)

- **Paráfrase (Citação Indireta Acadêmica):**
A arquitetura Nehalem, representada pelo processador Intel Core i7, inaugurou na linha Intel a presença de 4 núcleos nativos com suporte a Simultaneous Multithreading (SMT) de 2 threads por núcleo, totalizando 8 threads lógicas ativas. Sua organização de memória cache caracteriza-se por caches L1 e L2 privadas por núcleo — favorecendo o desempenho de cargas de trabalho com baixo compartilhamento de dados — e uma cache L3 compartilhada entre todos os núcleos, que funciona como repositório comum para dados de uso frequente em cargas paralelas (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Arquiteturas Multi-Core; pode ser usado para contextualizar o Intel Core i5-8265U da Máquina D (Whiskey Lake, descendente direto da arquitetura Skylake/Coffee Lake).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - **Máquina D:** Intel Core i5-8265U — 4 Cores / 8 Threads (SMT ativo) — reflete exatamente a configuração 4 núcleos com HT descrita pelo autor para a família Nehalem e seus sucessores.
  - `maqD_rodada_*.CSV` → `Core 0 T0 Uso (%)`, `Core 0 T1 Uso (%)`, ..., `Core 3 T1 Uso (%)`: os 8 campos de threads lógicas confirmam a estrutura 4C/8T do processador.
  - `maqD_rodada_*.CSV` → `Ring/LLC Relógio (MHz)`: frequência do barramento interno da cache L3 compartilhada (Ring Bus).
  - `maqD_rodada_*.CSV` → `Relação do relógio do núcleo (avg) (x)` e `Uncore Relação (x)`: distingue entre a frequência dos núcleos e da parte não-nuclear do chip (incluindo a L3 compartilhada).

---

### 3.10 Gargalo de Von Neumann e Contenção de Barramento

- **Conceito/Teoria:** Contenção de acesso à memória como gargalo de desempenho em sistemas multiprocessados; impacto do barramento compartilhado.

- **Citação Direta (Ipsis Litteris):**
> "Os resultados obtidos mostraram que, para um sistema multiprocessado de até oito processadores, as contenções geradas pelo barramento são responsáveis por grande parte do tempo total de execução." (Cap. 2, p. 37 — referenciando Nayfeh, Olukotun e Singht, 1996)

- **Paráfrase (Citação Indireta Acadêmica):**
O gargalo de memória, também denominado gargalo de Von Neumann, manifesta-se de forma especialmente crítica em sistemas multiprocessados, onde a contenção pelo barramento de acesso à memória compartilhada pode comprometer substancialmente o tempo total de execução. Estudos predecessores ao trabalho de Alves (2009) demonstraram que, em sistemas com até oito processadores compartilhando um barramento único, a latência de acesso à memória torna-se o fator dominante no desempenho global, sobrepondo-se inclusive ao aumento do número de núcleos (Alves 2009, citando Nayfeh, Olukotun e Singht 1996).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (gargalo de memória e barramento) e **Resultados e Discussão** (análise do impacto do Single Channel na Máquina D).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Relógio da memória (MHz)` = 1333 MHz (Single Channel): a largura de banda efetiva do barramento de memória da Máquina D é de aproximadamente 10,6 GB/s — significativamente inferior ao Dual Channel equivalente (~21,2 GB/s), configurando o gargalo descrito pelo autor.
  - `maqD_rodada_*.CSV` → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: valores empíricos da largura de banda de memória em operação real.
  - `maqD_rodada_*.CSV` → `Carga da memória física (%)` > 85%: indica que o processador frequentemente aguarda dados da memória principal, reproduzindo o fenômeno de contenção de barramento discutido.

---

### 3.11 Coerência de Cache e Protocolo MESI em Multi-Core

- **Conceito/Teoria:** Necessidade de protocolo de coerência de cache em sistemas multiprocessados; funcionamento do protocolo MESI (Modified, Exclusive, Shared, Invalid).

- **Citação Direta (Ipsis Litteris):**
> "Como em diversos projetos de multiprocessadores as memórias cache estão conectadas a uma única memória principal interconectadas por um barramento, os protocolos de coerência de memória cache mais populares são os baseados na técnica de snooping [...] Como exemplo desse tipo de protocolo pode-se citar o protocolo MESI [...] onde o nome MESI vêm das iniciais dos estados possíveis de um dado durante operação (modified, exclusive, shared, e invalid)." (Apêndice A, p. 149)

- **Paráfrase (Citação Indireta Acadêmica):**
Em arquiteturas multi-core, onde múltiplos núcleos mantêm cópias locais de dados em suas respectivas caches L1 e L2, a consistência entre essas cópias é garantida por protocolos de coerência. O protocolo MESI, amplamente adotado em processadores de propósito geral, baseia-se em snooping sobre o barramento compartilhado e classifica cada bloco de cache em um de quatro estados: Modificado (M), Exclusivo (E), Compartilhado (S) ou Inválido (I), determinando as ações necessárias quando ocorrem leituras ou escritas por diferentes núcleos sobre o mesmo endereço de memória (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Arquiteturas Multi-Core e Hierarquia de Memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` → `Estrangulamento térmico do núcleo (avg) (Yes/No)`: embora não seja diretamente MESI, situações de throttling afetam a frequência dos núcleos e, consequentemente, a taxa de operações de coerência por ciclo.
  - A análise de coerência é mais relevante para as Máquinas A, B e C — especialmente se possuírem processadores com maior número de núcleos, onde a contenção MESI torna-se mais visível.

> ⚠️ **Nota Preditiva:** Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de forma preditiva e só serão utilizados na redação final conforme as configurações reais de hardware das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.

---

### 3.12 Design of Experiments (DoE) e Metodologia de Avaliação

- **Conceito/Teoria:** Metodologia formal de projeto de experimentos (Design of Experiments — DoE) aplicada à avaliação de sistemas computacionais, seguindo Jain (1991).

- **Citação Direta (Ipsis Litteris):**
> "De acordo com (JAIN, 1991), a utilização de uma correta metodologia para avaliação de desempenho de sistemas computacionais evita diversos problemas, como a falta de objetivos, objetivos viciados, abordagem não sistemática, análise sem compreender o problema, métricas incorretas de desempenho, carga de trabalho não representativa [...]" (Cap. 3, p. 41)

- **Paráfrase (Citação Indireta Acadêmica):**
A adoção de uma metodologia formal de projeto de experimentos é condição necessária para a validade científica de avaliações de desempenho computacional, conforme sistematizado por Jain (1991) e aplicado por Alves (2009). Entre as etapas fundamentais dessa metodologia destacam-se: a definição clara dos objetivos e métricas de avaliação; a seleção de cargas de trabalho representativas; a repetição controlada de experimentos para isolamento de variações não-determinísticas; e o uso de técnicas estatísticas apropriadas para quantificar a confiabilidade dos resultados obtidos.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** — justificando as 20 rodadas por máquina, a padronização das condições de teste e o uso de média e desvio padrão.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → 20 linhas de dados por arquivo: as 20 rodadas do Geekbench 6 por máquina reproduzem a metodologia de múltiplas repetições descrita pelo autor, permitindo calcular intervalo de confiança segundo a distribuição *t* de Student com $n-1 = 19$ graus de liberdade.
  - `maq*_rodada_*.CSV` → Todos os 80 arquivos: cada arquivo corresponde a uma rodada completa com registros segundo a segundo, permitindo calcular médias e desvios de cada variável por rodada antes da análise inter-rodadas.

---

### 3.13 Resultados: Impacto da Associatividade e do Tamanho da Linha de Cache

- **Conceito/Teoria:** Efeito do aumento da associatividade e do tamanho da linha de dados sobre desempenho, potência e área.

- **Citação Direta (Ipsis Litteris):**
> "Sobre o aumento do tamanho de linha da memória cache [...] presente no quarto experimento, podemos concluir que essa técnica apresenta ganho de desempenho ao ser utilizada, apresentando sobrecusto em termos de consumo de potência e ocupação de área. Sendo que, foram obtidos ganhos nas organizações 1Core/L2 (+2,38%), 2Cores/L2 (+3,07%), 4Cores/L2 (+2,47%) e 8Cores/L2 (+2,55%)." (Cap. 5, p. 134)

- **Paráfrase (Citação Indireta Acadêmica):**
O aumento do tamanho da linha de cache — que determina a quantidade de dados trazidos da memória principal a cada falta — demonstrou ser a técnica com melhor relação custo-benefício dentre as avaliadas, gerando ganhos de desempenho consistentes entre 2,38\% e 3,07\% em organizações com até 8 núcleos por banco L2, ao custo de um moderado aumento no consumo de potência e na área de silício ocupada pela memória. Isso ocorre porque linhas maiores exploram mais eficientemente o princípio de localidade espacial, amortizando o custo de acesso à memória principal ao longo de múltiplas instruções (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** (parâmetros de projeto de cache) e **Resultados e Discussão** (ao discutir o impacto da configuração de memória na Máquina D vs. demais máquinas).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Relógio da memória (MHz)` e `Taxa de leituras (MB/s)`: frequências mais altas e maiores taxas de leitura indicam que o subsistema de memória consegue servir linhas de cache maiores com menor penalidade de falta.

---

### 3.14 Limitações e Conteúdo para Trabalhos Futuros (NUCA)

- **Conceito/Teoria:** Limitações das arquiteturas de cache uniforme (UCA) para processadores many-core; emergência das arquiteturas de cache não-uniforme (NUCA).

- **Citação Direta (Ipsis Litteris):**
> "Para processadores many-core as memórias cache de arquitetura uniforme deverão sofrer ainda mais os problemas associados a latência do fio. Neste cenário futuro, o uso de memórias NUCA (non-uniform cache architecture) podem ser consideradas [...]" (Cap. 5, p. 135)

- **Paráfrase (Citação Indireta Acadêmica):**
As arquiteturas de cache de acesso uniforme (UCA), predominantes nos processadores multi-core avaliados, tendem a enfrentar limitações crescentes com o aumento do número de núcleos, especialmente em decorrência da latência introduzida pelo atraso de propagação elétrica nos fios de interconexão de longa distância dentro do chip. As arquiteturas de cache não-uniforme (NUCA), nas quais a latência de acesso varia conforme a distância física entre o núcleo solicitante e o banco de cache acessado, apresentam-se como alternativa promissora para as gerações futuras de processadores many-core (Alves 2009).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Conclusões e Trabalhos Futuros** — contextualizando as tendências arquiteturais além do escopo deste trabalho.

---

### 3.15 Núcleos Heterogêneos (P-Cores/E-Cores) — Arquitetura Híbrida Raptor Lake

> **Atualização motivada pelos dados de hardware:** com o preenchimento completo da tabela de máquinas, identificamos que as Máquinas A (i5-13420H), B (i5-1334U) e F (i5-14600KF) utilizam arquitetura híbrida Intel (Raptor Lake / Raptor Lake-H / Raptor Lake-P) com núcleos de desempenho (P-cores) e núcleos eficientes (E-cores) em proporções distintas (4P+4E, 2P+8E e 6P+8E, respectivamente). Este tema não havia sido fichado anteriormente porque a dissertação de Alves (2009) trata exclusivamente de **núcleos homogêneos**, mas o próprio autor antecipa teoricamente a existência de núcleos heterogêneos em MPSoCs, o que justifica a citação abaixo.

- **Conceito/Teoria:** Processadores Multi-Core Heterogêneos — núcleos com propósitos e características distintas dentro do mesmo chip.

- **Citação Direta (Ipsis Litteris):**
> "No entanto, projetos de processadores multi-core para aplicações em sistemas embarcados, freqüentemente possuem núcleos heterogêneos (KUMAR et al., 2004) (KUMAR et al., 2005). Nesse caso, cada núcleo, ou conjunto de núcleos, é responsável por processamentos específicos e distintos dos demais." (Cap. 2, p. 30)

- **Paráfrase (Citação Indireta Acadêmica):**
Diferentemente da maioria dos processadores de propósito geral da década de 2000 — que adotavam núcleos homogêneos, ou seja, idênticos entre si em microarquitetura e capacidade —, alguns projetos voltados a sistemas embarcados já incorporavam núcleos heterogêneos, nos quais cada núcleo ou grupo de núcleos atende a uma finalidade computacional específica. Embora o autor não tivesse acesso, em 2009, a processadores híbridos de propósito geral, sua previsão teórica sobre heterogeneidade de núcleos antecipa exatamente o modelo adotado pela Intel a partir da 12ª geração (Alder Lake) e mantido nas gerações Raptor Lake utilizadas em nossas Máquinas A, B e F, nas quais núcleos de Desempenho (P-Cores, otimizados para IPC máximo via Hyper-Threading) coexistem com núcleos Eficientes (E-Cores, sem Hyper-Threading, otimizados para vazão por Watt) (Alves 2009, citando Kumar et al. 2004, 2005).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Arquiteturas Multi-Core (logo após a discussão de SMT/IMT/BMT/CMP, Seção 2.1.2 do autor); também pode ser referenciado em **Metodologia**, ao descrever as Máquinas A, B e F na tabela de hardware.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqA_rodada_*.CSV` e `maqB_rodada_*.CSV` e arquivos correspondentes à Máquina F → colunas `Core 0 Relógio (MHz)` a `Core 3 Relógio (MHz)`: nas arquiteturas híbridas, os primeiros núcleos endereçados pelo HWiNFO64 tendem a corresponder aos P-Cores, com clocks de boost mais altos (até 4,60 GHz na Máquina A e 5,3 GHz na Máquina F), enquanto os núcleos remanescentes (E-Cores) operam em faixas de clock mais baixas e constantes.
  - `maq*_rodada_*.CSV` → `Relação do relógio do núcleo (avg) (x)`: útil para diferenciar estatisticamente os multiplicadores de clock entre P-Cores e E-Cores dentro da mesma rodada.
  - `scores_maq*.txt` → `Multi_Core`: o Geekbench 6 distribui threads entre P-Cores e E-Cores via *Thread Director* do Windows 11 — máquinas com mais P-Cores (Máquina F: 6P) tendem a apresentar maior score Multi-Core por thread ativa, mesmo com menor contagem total de núcleos físicos do que arquiteturas homogêneas equivalentes.
  - **Justificativa de uso:** Esta citação permite ao grupo explicar, na seção de Resultados, por que a Máquina B (10 Cores / 12 Threads, mas apenas 2 P-Cores) pode apresentar score Single-Core inferior ao esperado para sua contagem nominal de núcleos — o desempenho de thread única depende do P-Core, não da soma total de núcleos heterogêneos.

---

### 3.16 Litografia e Escala de Integração — Comparativo 14nm vs. 12nm vs. 7nm vs. Intel 7

> **Atualização motivada pelos dados de hardware:** a tabela completa revela grande disparidade de processos litográficos entre as máquinas: Whiskey Lake-U a 14nm (Máquina D), Zen+ a 12nm (Máquina C), Zen 3 a 7nm (Máquina E) e Raptor Lake em "Intel 7" — equivalente a ~10nm aprimorado (Máquinas A, B, F). Esse espectro de gerações tecnológicas conecta-se diretamente ao tema de potência estática discutido pelo autor.

- **Conceito/Teoria:** Tecnologia de Integração (Litografia) e seu impacto sobre consumo de potência estática (leakage) e densidade de transistores.

- **Citação Direta (Ipsis Litteris):**
> "Porém, com novas tecnologias de integração, o tamanho das memórias cache tendem a continuar a crescer assim como a demanda por mais vazão de dados. [...] para futuras tecnologias de integração, as memórias cache que utilizam o modelo atual de arquitetura irão sofrer com problemas de atraso do fio, gerando assim grande contenção ao processamento." (Cap. 2, p. 32)

- **Citação Direta (Ipsis Litteris) — Potência Estática:**
> "A potência estática é a soma de todas taxas de leakage (vazamento) do sistema." (Cap. 3, p. 44)

- **Paráfrase (Citação Indireta Acadêmica):**
O avanço da tecnologia de integração (litografia) permite, por um lado, maior densidade de transistores por chip — possibilitando caches L3 maiores e mais núcleos no mesmo encapsulamento — mas, por outro, intensifica os efeitos de atraso de propagação no fio (*wire delay*) e o consumo de potência estática (leakage), fenômenos que se tornam progressivamente mais críticos à medida que o processo de fabricação encolhe (Alves 2009). Tecnologias de integração mais recentes e refinadas, como o processo "Intel 7" (~10nm classe avançada) e o processo de 7nm da TSMC empregado nos núcleos Zen 3, tendem a oferecer maior eficiência energética por transistor em comparação a processos mais antigos como os 14nm da família Whiskey Lake-U, ainda que o ganho real de desempenho por watt dependa também da microarquitetura e do gerenciamento dinâmico de frequência (DVFS) implementado.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Memórias Cache para Multi-Core (Seção 2.1.3 do autor); ideal também para a **Metodologia**, ao justificar a heterogeneidade tecnológica da amostra do grupo (4 gerações litográficas distintas: 14nm, 12nm, 7nm e Intel 7).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` (14nm) vs. `maqE_rodada_*.CSV` (7nm) → `Potência total da CPU (W)`: comparação direta do consumo de potência entre a litografia mais antiga (Whiskey Lake-U, Máquina D) e a mais recente entre os desktops (Zen 3, Máquina E), controlando-se pelo TDP de projeto (15W vs. 65W) declarado no datasheet.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqF_rodada_*.CSV` (Intel 7) → `Potência de núcleos IA (W)`: métrica de potência isolada dos núcleos, útil para isolar o ganho de eficiência por transistor do processo "Intel 7" frente ao 14nm da Máquina D.
  - `maq*_rodada_*.CSV` → métrica derivada **Desempenho por Watt** ($\text{Score}/\overline{P_{\text{CPU}}}$, Equação \ref{eq:potencia_din} já fichada na Seção 3.7): pode ser plotada em função da litografia de cada máquina para visualizar a correlação entre processo de fabricação e eficiência energética.
  - **Justificativa de uso:** Esta citação fundamenta teoricamente por que processadores mais antigos (Máquina D, 14nm) tendem a apresentar maior potência estática relativa e, consequentemente, pior relação desempenho/watt mesmo operando dentro de seu envelope térmico nominal — sem necessidade de invocar dados quantitativos de leakage não disponíveis em nossa telemetria (o HWiNFO64 não decompõe potência dinâmica de estática isoladamente, apenas o total agregado em `Potência total da CPU (W)`).

---

### 3.17 TDP, PL1/PL2 e Limites de Projeto de Potência (Desktop vs. Notebook)

> **Atualização motivada pelos dados de hardware:** a tabela revela um espectro de TDP de projeto extremamente amplo — de 15W (Máquinas B, C, D, notebooks ultrafinos) a 125W (Máquina F, desktop com i5-14600KF). Esse contraste de fator de forma (notebook vs. desktop montado) conecta-se diretamente à discussão do autor sobre o equilíbrio entre desempenho, consumo de potência e ocupação de área.

- **Conceito/Teoria:** Limites de Projeto de Potência (Power Limits PL1/PL2) e a relação entre fator de forma físico (notebook ultrafino vs. desktop) e o espaço de projeto disponível para dissipação térmica.

- **Citação Direta (Ipsis Litteris):**
> "De forma geral, os experimentos mostram a importância da integração do projeto de organização de memória cache e o projeto físico, a fim de obter a melhor troca entre desempenho e consumo de potência e ocupação de área." (Cap. 5, p. 133)

- **Paráfrase (Citação Indireta Acadêmica):**
A relação entre desempenho, consumo de potência e restrições físicas de projeto — central na conclusão de Alves (2009) para o subsistema de memória cache — estende-se naturalmente à comparação entre fatores de forma de sistemas completos. Processadores projetados para notebooks ultrafinos (TDP base de 15W, como nas Máquinas B, C e D) operam sob um envelope térmico deliberadamente restrito, priorizando eficiência energética e portabilidade em detrimento do desempenho sustentado de pico. Já processadores de desktop (TDP base de 65W a 125W, como nas Máquinas E e F) dispõem de maior margem física para dissipação de calor, permitindo sustentar frequências de boost por períodos mais longos sem incorrer em redução de clock por proteção térmica (Alves 2009, adaptado ao contexto de TDP de sistema completo).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Metodologia** (justificando a categorização das máquinas por fator de forma) e **Resultados e Discussão** (ao explicar diferenças de estabilidade de clock entre notebooks e desktops).

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maq*_rodada_*.CSV` → `Limite de potência PL1 (Static) (W)` e `Limite de potência PL1 (Dynamic) (W)`: para processadores Intel (Máquinas A, B, D, F), esses campos revelam o limite de potência sustentada configurado pelo fabricante — tipicamente próximo ao TDP base (15W para B e D; mais elevado para A e F).
  - `maq*_rodada_*.CSV` → `Limite de potência PL2 (Static) (W)` e `Limite de potência PL2 (Dynamic) (W)`: revela o limite de potência de pico (boost) — métrica crucial para notebooks ultrafinos, cujo PL2 geralmente excede o TDP base por curtos períodos antes do throttling.
  - `maq*_rodada_*.CSV` → `IA: Package-Level RAPL/PBM PL1 (Yes/No)` e `IA: Package-Level RAPL/PBM PL2 PL3 (Yes/No)`: flags binárias que confirmam, segundo a segundo, se o processador está sendo limitado pelo PL1 (sustentado) ou pelo PL2 (pico) durante o benchmark — diretamente relevante para notebooks de 15W como as Máquinas B, C e D.
  - `maq*_rodada_*.CSV` → `Limite de desempenho - Térmico (Yes/No)`: comparação direta entre notebooks (espera-se ativação frequente) e desktops (espera-se baixa ou nula ativação).
  - **Justificativa de uso:** Esta citação justifica teoricamente por que esperamos observar maior incidência de `Estrangulamento térmico do núcleo (avg) (Yes/No)` = "Yes" nas Máquinas B, C e D (notebooks ultrafinos com TDP 15W) do que nas Máquinas E e F (desktops com TDP 65W/125W), mesmo quando os scores absolutos do Geekbench 6 da Máquina F sejam superiores em valor nominal — o desvio padrão relativo das rodadas é a métrica mais sensível a essa diferença de fator de forma, não a média isolada.

---

### 3.18 GPU Dedicada e Barramento PCI Express — Acoplamento Processador-GPU

> **Atualização motivada pelos dados de hardware:** com a tabela completa, observamos que metade das máquinas possui GPU dedicada conectada via interface PCIe (Máquinas A, D, E e F), com gerações distintas do barramento (PCIe 3.0 x4 na Máquina D vs. PCIe 4.0 x8 nas demais). A dissertação de Alves (2009), embora focada em cache, trata extensamente de interconexões intra-chip e seus parâmetros de comparação, que se aplicam por analogia ao barramento PCIe externo.

- **Conceito/Teoria:** Interconexões e seus critérios de comparação (Escalabilidade, Desempenho, Custo) — aplicados ao barramento PCI Express que conecta a GPU dedicada ao restante do sistema.

- **Citação Direta (Ipsis Litteris):**
> "Algumas das principais características de comparação entre interconexões são (ROSE; NAVAUX, 2003): • Escalabilidade [...] • Desempenho – O desempenho desejável de uma interconexão é que essa consiga manipular e dar vazão a todos os dados em tempo hábil. Assim, o desempenho indica a capacidade e a velocidade da transferência de dados pela interconexão." (Apêndice A, p. 150)

- **Paráfrase (Citação Indireta Acadêmica):**
Embora o autor trate primariamente de interconexões intra-chip entre núcleos e bancos de memória cache, os critérios de avaliação por ele sistematizados — especialmente desempenho (capacidade e velocidade de vazão de dados) e custo (em área e potência) — aplicam-se diretamente à análise do barramento PCI Express que interliga a GPU dedicada ao processador e à memória principal em nossas máquinas. Gerações mais recentes do padrão PCIe (4.0) oferecem o dobro da taxa de transferência por linha (*lane*) em relação ao PCIe 3.0, para a mesma largura nominal de barramento, reduzindo a contenção de dados entre GPU e CPU em cargas de trabalho que demandam alta vazão de textura, geometria ou dados de computação geral em GPU (GPGPU) (Alves 2009, adaptado de Rose e Navaux 2003).

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — subseção sobre Interconexões (Apêndice A.3.2 do autor); pode ser referenciado também na **Metodologia**, ao descrever o subsistema gráfico das Máquinas A, D, E e F.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` (PCIe 3.0 x4, GPU MX130) → `Velocidade do link PCIe (GT/s)`: espera-se valor próximo a 8,0 GT/s por linha (padrão PCIe 3.0), resultando em largura de banda efetiva substancialmente menor do que nas máquinas com PCIe 4.0 x8.
  - `maqA_rodada_*.CSV`, `maqE_rodada_*.CSV`, arquivo correspondente à Máquina F (todos PCIe 4.0 x8, GPUs RTX 4050/RX 7600/RTX 3050) → `Velocidade do link PCIe (GT/s)`: espera-se valor próximo a 16,0 GT/s por linha, com o dobro de linhas (x8) em relação à Máquina D (x4), evidenciando uma largura de banda total muito superior.
  - `maq*_rodada_*.CSV` → `PCI Express Error Counters (avg)`, `Replay Count`, `Correctable Error Count`: contadores de erro de barramento PCIe — relevantes para investigar se a interface mais antiga (PCIe 3.0 x4 da Máquina D) apresenta maior incidência de retransmissões (*replays*) sob carga sustentada.
  - `maq*_rodada_*.CSV` → `Carga do barramento GPU (%)`: indica o quão saturado está o link PCIe durante a execução do benchmark gráfico do Geekbench 6 (Compute/OpenCL).
  - **Justificativa de uso:** Esta citação permite ao grupo explicar, na seção de Resultados, por que o subteste de *Compute* do Geekbench 6 na Máquina D (GPU MX130 via PCIe 3.0 x4) pode ser limitado tanto pela capacidade computacional modesta da própria GPU quanto pela menor largura de banda do barramento que a interliga ao restante do sistema — um efeito de gargalo de interconexão análogo, em escala, ao gargalo de barramento intra-chip discutido pelo autor para memórias cache compartilhadas.

---

### 3.19 Armazenamento: SSD NVMe vs. HDD SATA e o Tempo de Carregamento da Carga de Trabalho

> **Atualização motivada pelos dados de hardware:** a tabela evidencia o contraste mais extremo de toda a amostra: SSDs NVMe operando via PCIe Gen 3.0/4.0 (Máquinas A, B, F) contra o HDD mecânico SATA de 5400 RPM da Máquina D. Embora a dissertação de Alves (2009) não trate de armazenamento secundário (seu escopo é estritamente a hierarquia cache-memória principal), o princípio teórico de hierarquia de memória do Apêndice A se estende naturalmente ao nível de armazenamento não-volátil, justificando a citação por analogia.

- **Conceito/Teoria:** Extensão da Hierarquia de Memória ao nível de armazenamento secundário — o disco como último nível, mais lento e não-volátil, da hierarquia descrita pelo autor.

- **Citação Direta (Ipsis Litteris):**
> "O nível mais baixo de memória utiliza tecnologias de armazenamento magnético não voláteis. Para este nível o grande ponto chave é o tamanho total de armazenamento em que os dados se mantenham, mesmo quando a energia de alimentação for cortada. [...] Este nível de memória tradicionalmente utiliza meios magnéticos que são escritos e gravados por dispositivos mecânicos, tendo assim péssimo desempenho." (Apêndice A, p. 138)

- **Paráfrase (Citação Indireta Acadêmica):**
O nível mais baixo da hierarquia de memória, tradicionalmente ocupado por dispositivos de armazenamento magnético não-volátil, caracteriza-se historicamente pelo desempenho inferior em relação aos níveis superiores, em função da natureza mecânica de seus mecanismos de leitura e escrita (Alves 2009, citando Hennessy e Patterson 2007). Embora o autor não tivesse como objeto de estudo o armazenamento secundário, o mesmo princípio de hierarquização por custo/desempenho aplica-se à comparação entre tecnologias de disco: HDDs mecânicos como o Western Digital Blue de 5400 RPM (Máquina D) dependem de latência de busca (*seek time*) e tempo de rotação física do prato magnético, ao passo que SSDs NVMe conectados via PCIe (Máquinas A, B e F) eliminam completamente os componentes mecânicos, operando com latências de acesso ordens de grandeza menores e taxas de transferência sequencial substancialmente superiores.

- **Onde Encaixar no Artigo LaTeX:** Seção de **Fundamentação Teórica** — como extensão da subseção de Hierarquia de Memória (Apêndice A.1 do autor), explicitando que o conceito se estende ao armazenamento secundário; também essencial na seção de **Resultados e Discussão**, ao explicar diferenças no tempo de carregamento inicial do Geekbench 6 entre as máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `maqD_rodada_*.CSV` (HDD SATA 5400 RPM) → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: espera-se valores tipicamente na faixa de 80–160 MB/s em leitura sequencial, ordens de grandeza inferiores aos SSDs NVMe.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, arquivo correspondente à Máquina F (SSD NVMe) → `Taxa de leituras (MB/s)` e `Taxa de gravações (MB/s)`: espera-se valores na faixa de centenas a milhares de MB/s, refletindo a ausência de latência mecânica.
  - `maq*_rodada_*.CSV` → `Atividade de leitura (%)`, `Atividade de gravação (%)`, `Atividade total (%)`: indicam o percentual de tempo em que o disco está ocupado atendendo requisições — espera-se atividade total mais alta e mais prolongada na Máquina D durante a fase de carregamento do executável do Geekbench 6 e de seus arquivos de dados de teste.
  - `maq*_rodada_*.CSV` → `Temperatura do disco (°C)`: aplicável majoritariamente aos SSDs NVMe, que podem apresentar throttling térmico próprio sob carga sustentada de leitura/escrita — fenômeno distinto, mas conceitualmente análogo ao throttling de CPU discutido pelo autor.
  - **Justificativa de uso:** Esta citação fundamenta teoricamente a hipótese de que o tempo total de execução do Geekbench 6 na Máquina D pode incluir uma parcela não-desprezível de tempo de I/O em disco (carregamento de assets/dados de teste do benchmark), aumentando a variabilidade entre rodadas caso haja contenção de cache do sistema operacional (Windows 11) sobre um meio de armazenamento lento — efeito que se soma, mas é distinto, das faltas de cache de CPU/memória RAM já discutidas nas Seções 3.3 e 3.8 deste fichamento.

> ⚠️ **Nota sobre dados pendentes:** A Máquina C ainda não possui definição clara entre SSD ou HDD ("[SSD ou HD?]\*"), nem a interface exata do disco, nem a frequência da RAM. A Máquina E e a Máquina F também aguardam preenchimento de modelo de gabinete e geração exata da interface do disco, respectivamente. Os fichamentos das Seções 3.15 a 3.19 permanecem válidos independentemente desses dados pendentes, pois já dispomos de informações suficientes nas Máquinas A, B, D, E e F para sustentar as citações acima; os campos pendentes da Máquina C deverão ser incorporados como casos adicionais de comparação assim que disponibilizados pelo grupo.

---

## 4. ELEMENTOS VISUAIS, FÓRMULAS E EQUAÇÕES

### 4.1 Fórmulas Matemáticas/Físicas em LaTeX Puro

Bloco completo pronto para inclusão no `main.tex` (Seção de Metodologia):

```latex
% ============================================================
% BLOCO DE EQUAÇÕES ESTATÍSTICAS — FUNDAMENTADO EM ALVES (2009)
% ============================================================

A análise estatística dos resultados segue a metodologia
proposta por \cite{alves:09}, com base em \cite{jain:91}.
Para cada máquina avaliada e cada métrica de interesse,
foram calculadas as seguintes grandezas:

\begin{equation}
    \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
    \label{eq:media}
\end{equation}

\noindent onde $n = 20$ representa o número de rodadas do
benchmark Geekbench~6 por máquina avaliada.

\begin{equation}
    \sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
    \label{eq:desvio_padrao}
\end{equation}

\noindent O coeficiente de variação (C.O.V.) normaliza a
dispersão em relação à média, permitindo comparações
entre métricas de escalas distintas \cite{alves:09}:

\begin{equation}
    \text{C.O.V.} = \frac{\sigma}{\bar{x}}
    \label{eq:cov}
\end{equation}
```

### 4.2 Sugestão de Gráficos/Tabelas Correspondentes no Matplotlib

Com base nos experimentos apresentados na dissertação, sugerimos os seguintes gráficos para o artigo do grupo:

**Gráfico 1 — Barplot de Scores Geekbench 6 com hastes de erro (desvio padrão):**
- Eixo X: Máquinas (A, B, C, D)
- Eixo Y: Score Geekbench 6
- Séries: Single-Core e Multi-Core separadas em barras agrupadas
- Hastes de erro: ± 1 desvio padrão (análogo à Figura 4.2 do autor)

**Gráfico 2 — Barplot de Temperatura Média da CPU por Máquina:**
- Eixo X: Máquinas (A, B, C, D)
- Eixo Y: `CPU Inteira (°C)` e `Núcleo máximo (°C)` médios por rodada
- Fonte: `maq*_rodada_*.CSV`

**Gráfico 3 — Barplot de Potência da CPU e Eficiência (Score/Watt):**
- Eixo X: Máquinas (A, B, C, D)
- Eixo Y primário: `Potência total da CPU (W)` média
- Eixo Y secundário: Score Geekbench / Watt (Desempenho por Watt)

**Gráfico 4 — Barplot de Frequência Efetiva e Carga de CPU:**
- Eixo X: Máquinas (A, B, C, D)
- Eixo Y: `Relógios efetivos núcleo (avg) (MHz)` médio
- Hastes de erro: ± 1 σ — desvio alto indica throttling (análogo à Figura 4.1 do autor)

**Tabela LaTeX sugerida — Parâmetros de Memória das Máquinas (na seção de Metodologia):**

```latex
\begin{table}[ht]
\caption{Configuração do subsistema de memória das máquinas avaliadas.}
\label{tab:memoria}
\begin{center}
\begin{tabular}{lcccc}
\hline
\textbf{Parâmetro} & \textbf{Máq. A} & \textbf{Máq. B} & \textbf{Máq. C} & \textbf{Máq. D} \\
\hline
Cache L3 (MB)       & --  & --  & --  & 6   \\
RAM (GB)            & --  & --  & --  & 8   \\
Frequência (MHz)    & --  & --  & --  & 1333\\
Canal               & --  & --  & --  & Single \\
Armazenamento       & --  & --  & --  & HD SATA \\
\hline
\end{tabular}
\end{center}
{\footnotesize Fonte: Os autores (2026). Dados coletados via ferramenta HWiNFO64.}
\end{table}
```

> ⚠️ **Ação necessária do grupo:** Preencher os campos "--" com os dados reais das Máquinas A, B e C nas próximas interações.

> 🆕 **ATUALIZAÇÃO (dados completos de hardware recebidos):** com o preenchimento da tabela de especificações pelo grupo, a tabela acima (com placeholders "--" e escopo limitado a 4 máquinas) pode agora ser substituída/complementada pela versão real abaixo, já estendida para as 6 máquinas (A–F). Mantemos a tabela anterior como registro histórico da primeira versão do fichamento.

**Tabela LaTeX atualizada — Parâmetros Reais de Memória e Armazenamento das 6 Máquinas:**

```latex
\begin{table}[ht]
\caption{Configuração real do subsistema de memória e armazenamento das máquinas avaliadas.}
\label{tab:memoria_completa}
\begin{center}
\footnotesize
\begin{tabular}{lcccccc}
\hline
\textbf{Parâmetro} & \textbf{Máq. A} & \textbf{Máq. B} & \textbf{Máq. C} & \textbf{Máq. D} & \textbf{Máq. E} & \textbf{Máq. F} \\
\hline
Cache L3 (MB)     & 12        & 12        & 4          & 6          & 16        & 24        \\
RAM (GB/Tipo)     & 8 DDR5    & 16 DDR4   & 8 DDR4     & 8 DDR4     & 16 DDR4   & 32 DDR4   \\
Frequência (MHz)  & 5200 MT/s & 2666      & [Indef.]*  & 2400       & [Indef.]* & 3600      \\
Canal             & Dual      & Dual      & Single     & Single     & Dual      & Dual      \\
Armazenamento     & SSD NVMe  & SSD NVMe  & [Indef.]*  & HDD SATA   & SSD+HDD   & 2x SSD NVMe \\
Interface Disco   & PCIe 4.0 x4 & PCIe 3.0 x4 & [Indef.]* & SATA III  & SATA III  & [Indef.]* \\
\hline
\end{tabular}
\end{center}
{\footnotesize Fonte: Os autores (2026). Especificações declaradas pelo grupo e validadas via HWiNFO64.\\
*Campos pendentes de confirmação para a Máquina C (frequência RAM, tipo e interface de disco) e parcialmente para a Máquina E (frequência RAM) e Máquina F (geração da interface do disco).}
\end{table}
```

- **Justificativa de uso desta tabela atualizada:** Diferentemente da tabela anterior (que cobria apenas as 4 primeiras máquinas com dados de memória ainda incompletos), esta versão consolida o panorama real de **topologia de canal** (Dual vs. Single Channel) e **tecnologia de armazenamento** (SSD NVMe vs. HDD mecânico) para as 6 máquinas do grupo. Ela deve ser inserida na seção de **Metodologia** do `main.tex`, imediatamente após a tabela de especificações de CPU, servindo de base direta para as discussões fichadas nas Seções 3.16 (litografia/potência), 3.18 (barramento PCIe/GPU) e 3.19 (armazenamento) deste documento. As células marcadas com `[Indef.]*` devem ser preenchidas pelo grupo antes da submissão final, conforme indicado na nota de rodapé da própria tabela.

---

## 5. KEYWORDS PARA PESQUISA NO GOOGLE ACADÊMICO

As buscas abaixo devem ser realizadas no **Google Acadêmico** (scholar.google.com) para encontrar artigos que complementem e sustentem nossa discussão no `main.tex`:

### 5.1 Keywords em Inglês
1. `"L3 cache" "multi-core" "benchmark performance" "single channel" "dual channel" memory`
2. `"cache miss rate" "multicore processor" "benchmark" "Geekbench" performance evaluation`
3. `"memory hierarchy" "cache sharing" "chip multiprocessor" performance throughput`
4. `"thermal throttling" "CPU frequency" "benchmark variability" standard deviation`
5. `"performance per watt" "energy efficiency" "multicore" "cache" benchmark`
6. `"MPKI" "cache miss" "memory bandwidth" "performance evaluation" multicore`
7. `"cache associativity" "cache line size" "multi-core" performance tradeoff`
8. `"DDR4 single channel dual channel" memory bandwidth performance impact`
9. `"Geekbench" "CPU benchmark" "architecture comparison" "memory subsystem"`
10. `"IPC" "instructions per cycle" "effective clock" benchmark "multicore"`

### 5.2 Keywords em Português
1. `"hierarquia de memória cache" "processadores multi-core" desempenho benchmark`
2. `"estrangulamento térmico" "throttling" "variabilidade" benchmark processador`
3. `"memória single channel" "dual channel" impacto desempenho processador`
4. `"consumo de energia" "desempenho por watt" processador multi-core benchmark`
5. `"avaliação de desempenho" "arquitetura de computadores" benchmark "desvio padrão"`
6. `"cache L3" "desempenho" "multi-core" "Intel" avaliação experimental`
7. `"gargalo de memória" "Von Neumann" "barramento" desempenho computacional`

### 5.3 Keywords Adicionais — Núcleos Híbridos, Litografia, PCIe e Armazenamento
*(Acrescentadas em função da disponibilização completa dos dados de hardware das 6 máquinas — Seções 3.15 a 3.19)*

**Em inglês:**
1. `"hybrid architecture" "P-cores" "E-cores" "performance cores" "efficiency cores" benchmark`
2. `"Raptor Lake" OR "Alder Lake" "heterogeneous cores" performance evaluation`
3. `"Thread Director" Windows scheduling "hybrid CPU" performance`
4. `"process node" "7nm" "10nm" "14nm" CPU power efficiency comparison`
5. `"PCIe 3.0" "PCIe 4.0" bandwidth comparison GPU performance impact`
6. `"NVMe SSD" "HDD" storage benchmark loading time comparison`
7. `"power limit" "PL1" "PL2" "RAPL" CPU sustained performance throttling`
8. `"TDP" "form factor" notebook desktop CPU performance comparison`

**Em português:**
1. `"núcleos heterogêneos" "P-Core" "E-Core" desempenho processador híbrido`
2. `"litografia" "nanômetros" "processo de fabricação" eficiência energética processador`
3. `"barramento PCI Express" "PCIe" desempenho GPU dedicada notebook`
4. `"SSD NVMe" "HDD SATA" "tempo de carregamento" benchmark armazenamento`
5. `"limite de potência" "PL1 PL2" "RAPL" sustentação de clock processador`
6. `"TDP" "fator de forma" notebook desktop comparação desempenho`

---

## 6. INTERPRETAÇÃO ARQUITETURAL DO DESVIO PADRÃO ALTO

Com base na metodologia estatística do autor (Seção 4.1, p. 76–78), um **desvio padrão alto** nas métricas de desempenho de uma máquina possui interpretação arquitetural direta:

| Coluna HWiNFO64 com σ alto | Interpretação Arquitetural (fundamentada em Alves 2009) |
|---|---|
| `Relógios efetivos núcleo (avg) (MHz)` | **Thermal Throttling:** o processador reduz dinamicamente a frequência para proteger componentes do superaquecimento — causa direta de instabilidade nos scores do Geekbench 6 |
| `CPU Inteira (°C)` | Alta variância térmica indica dissipação inadequada de calor; cooling insuficiente para sustentar clock de boost contínuo |
| `Núcleo máximo (°C)` | Pico térmico acima do TjMAX força `Estrangulamento térmico` = Yes — evento de alta latência similar ao Block Multithreading descrito pelo autor |
| `Potência total da CPU (W)` | Variação na potência durante benchmark indica que o processador não consegue sustentar o PL2 (Power Limit 2) e cai para PL1, reduzindo desempenho |
| `Carga da memória física (%)` | Variação indica que o conjunto de trabalho ativo alterna entre caber e não caber na cache — confirmando faltas de capacidade (Classificação dos 4 Cs, Seção 3.3 deste fichamento) |
| `Taxa de leituras (MB/s)` | Alta variabilidade na taxa de leitura em disco indica que o HD SATA (Máquina D) é gargalo de I/O durante o carregamento dos kernels do benchmark |
| `Core 0...3 Relógio (MHz)` *(em CPUs híbridas A, B, F)* | Alto desvio entre núcleos individuais pode refletir a alternância do *Thread Director* do Windows 11 entre P-Cores e E-Cores, e não necessariamente instabilidade térmica — deve ser diferenciado do throttling propriamente dito (Seção 3.15) |
| `Velocidade do link PCIe (GT/s)` *(Máquinas A, D, E, F)* | Variação aqui é atípica e, se ocorrer, pode indicar renegociação dinâmica do link PCIe (ASPM) durante o benchmark gráfico, afetando a taxa de transferência GPU-CPU (Seção 3.18) |

> **Conclusão analítica:** Em máquinas com armazenamento HD SATA e cooling limitado (como a Máquina D), o desvio padrão dos scores de Single-Core tenderá a ser maior que em máquinas com SSD NVMe e sistema de resfriamento mais eficiente — fenômeno diretamente previsto pela metodologia de análise de variação de Alves (2009) e pela classificação de faltas de cache.

> **Conclusão analítica complementar (núcleos híbridos):** Nas Máquinas A, B e F, o desvio padrão do score *Single-Core* deve ser interpretado com cautela adicional: caso o sistema operacional não atribua consistentemente a thread do benchmark a um P-Core, rodadas podem ser eventualmente executadas (parcial ou totalmente) em um E-Core, gerando uma dispersão de resultados que não decorre de instabilidade térmica ou elétrica, mas sim de escalonamento de threads pelo *Thread Director*. Recomenda-se ao grupo, no script Python de análise, verificar a coluna `Core 0 Relógio (MHz)` (tipicamente o primeiro P-Core) momento a momento durante o subteste Single-Core, a fim de confirmar se a thread permaneceu de fato alocada a um núcleo de desempenho durante toda a rodada.

---

*Fichamento gerado em: Junho de 2026*
*Grupo — Disciplina AOC — UFPA Campus Tucuruí*
*Autores: Pamella Roberta, Cinara Oliveira, Nicolas Martins, Leandro Vitório, Raony Dias, Nauan Christo*
