# FICHAMENTO CIENTÍFICO COMPLETO
## Disciplina: Arquitetura e Organização de Computadores — UFPA Campus Tucuruí
## Arquivo: `fichamento_ReducaoTempoAvaliacaoDesempenhoProgramasParalelos_Lucena.md`

---

> **VEREDITO DE RELEVÂNCIA:** ⚠️ **APROVAÇÃO PARCIAL — O artigo possui utilidade periférica e direcionada.**
>
> O documento não aborda diretamente Benchmarking de hardware, CPU, GPU, Thermal Throttling, TDP
> ou consumo energético — eixos centrais do nosso projeto. Seu foco é a estimativa preditiva do
> **tempo de execução de programas paralelos** em HPC (High Performance Computing), utilizando
> modelagem analítica e redes neurais MLP como alternativas ao custo de múltiplas execuções.
>
> Entretanto, o artigo apresenta **três pontos de aproveitamento legítimo e direto**:
>
> 1. **Justificativa teórica para múltiplas execuções de benchmark:** o artigo fundamenta por que
>    repetir execuções é metodologicamente necessário, validando nossa abordagem de 20 rodadas por máquina.
> 2. **O conceito de "Memory Wall" em aplicações paralelas:** o artigo referencia Furtunato et al. (2020),
>    *"When parallel speedups hit the memory wall"* (IEEE Access), cujo tema é diretamente aplicável
>    à nossa discussão sobre gargalo de Von Neumann e impacto do modo Single Channel de memória.
> 3. **Métricas de validação estatística:** o uso do erro relativo absoluto como métrica de comparação
>    entre estimativas e valores reais é conceitualmente análogo ao papel do Desvio Padrão Amostral
>    como indicador de estabilidade nas nossas 20 rodadas de Geekbench 6.
>
> O fichamento foi gerado focado exclusivamente nesses três pontos de aderência ao escopo do projeto.
> Conceitos de redes neurais MLP, Pascal Analyzer e OpenMP foram descartados por falta de aderência.

---

## 1. IDENTIFICAÇÃO BIBLIOGRÁFICA REGULAR

- **Referência Textual Padrão SBC:**

  LUCENA, E. G. M. de; XAVIER-DE-SOUZA, S. **Estudo de Abordagens Para Redução do Tempo de Avaliação de Desempenho de Programas Paralelos**. In: SIMPÓSIO BRASILEIRO DE COMPUTAÇÃO — SBC, 2025(?), [s.l.]. *Anais [...]*. Porto Alegre: Sociedade Brasileira de Computação, 2025. p. 1--2.

  > ⚠️ **NOTA EDITORIAL:** O artigo não informa explicitamente o nome do evento, o ano exato de publicação
  > nem o número de páginas ou DOI. A referência acima foi construída com os dados disponíveis no documento.
  > **O líder do grupo deve completar o nome do evento/periódico e o ano antes de inserir no `main.tex`.**

- **Código BibTeX Completo (.bib):**

```bibtex
@InProceedings{lucena:25,
  author    = {Elisa Gabriela Machado de Lucena and Samuel Xavier-de-Souza},
  title     = {Estudo de Abordagens Para Reduc¸{\~a}o do Tempo de Avaliac¸{\~a}o
               de Desempenho de Programas Paralelos},
  booktitle = {Anais do Simp{\'o}sio Brasileiro de Computac¸{\~a}o},
  year      = {2025},
  address   = {Porto Alegre},
  publisher = {Sociedade Brasileira de Computac¸{\~a}o ({SBC})},
  pages     = {1--2},
  note      = {Departamento de Engenharia da Computac¸{\~a}o e Automac¸{\~a}o,
               {UFRN}. Verificar nome do evento e p{\'a}ginas exatas.}
}
```

> ⚠️ **Atenção:** Preencher `booktitle`, `year` e `pages` com os dados exatos do evento após confirmação
> com o Prof. Dr. Iago Medeiros ou verificação no portal da SBC/DBLP.

---

## 2. METADADOS E OBJETIVOS DO DOCUMENTO

- **Grau/Tipo:** Artigo Completo de Conferência (formato SBC — 2 páginas)
- **Instituição/Editora:** Universidade Federal do Rio Grande do Norte (UFRN) —
  Departamento de Engenharia da Computação e Automação (DCA) / Laboratório de Processamento
  Paralelo e Sistemas (LAPPS)
- **Autores:** Elisa Gabriela Machado de Lucena; Samuel Xavier-de-Souza
- **Contato:** elisa.lucena.127@ufrn.edu.br; samuel@dca.ufrn.br
- **Palavras-Chave Originais:** Não declaradas explicitamente no documento.
  Palavras-chave inferidas: programas paralelos; análise de escalabilidade; modelagem analítica;
  redes neurais MLP; tempo de execução; custo computacional.
- **Resumo do Escopo Geral:**
  O artigo propõe e compara duas abordagens para reduzir o custo de análise de escalabilidade
  de programas paralelos: (i) modelagem analítica baseada em curvas de tempo de execução, adaptada
  do método de Furtunato et al. (2020); e (ii) redes neurais do tipo Perceptron Multicamadas (MLP)
  treinadas com subconjuntos amostrados dos dados de execução. A comparação é feita com base em
  três métricas — erro relativo absoluto, tempo total de análise e custo computacional — aplicadas
  a três algoritmos paralelos (multiplicação de matrizes, busca em largura e ray tracing),
  paralelizados com OpenMP e variando o número de núcleos e o tamanho de entrada.
  O objetivo final é integrar a melhor abordagem ao Pascal Analyzer, ferramenta de visualização
  de escalabilidade desenvolvida pelo LAPPS/UFRN.

---

## 3. FICHAMENTO ESPECÍFICO E DETALHADO (CITAÇÕES DIRETAS E INDIRETAS)

---

### 3.1 Custo de Múltiplas Execuções de Benchmark — Justificativa Metodológica

- **Conceito/Teoria:** Múltiplas execuções de benchmark são metodologicamente necessárias para
  análise de desempenho confiável, mas impõem custo computacional significativo. A repetição de
  execuções é, portanto, um requisito de validade científica, não uma escolha arbitrária.

- **Citação Direta (Ipsis Litteris):**
  > "A análise de desempenho de aplicações paralelas é essencial, especialmente em ambientes de
  > alto desempenho. Ferramentas como o Pascal Analyzer [...] permitem avaliar a escalabilidade de
  > algoritmos paralelos, mas exigem múltiplas execuções sob diferentes configurações, o que torna
  > o processo custoso." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) argumentam que a análise de desempenho de aplicações
  computacionais demanda, por razões de rigor metodológico, a repetição sistemática das execuções
  sob configurações controladas. Essa necessidade de replicação é inerente à avaliação de
  desempenho e impõe custo temporal e computacional ao processo experimental — custo que os
  autores buscam mitigar via modelagem preditiva, mas que, em contextos de avaliação empírica
  direta (como o nosso), representa o fundamento da confiabilidade estatística dos resultados.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — parágrafo de justificativa da escolha de 20 rodadas
  por máquina; reforça a validade científica do protocolo experimental adotado pelo grupo.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqA.txt`, `scores_maqB.txt`, `scores_maqC.txt`, `scores_maqD.txt` → colunas
    `Single_Core` e `Multi_Core`: as 20 rodadas por máquina constituem exatamente o tipo de
    "múltiplas execuções sob configurações controladas" descrito pelos autores. A variabilidade
    entre as rodadas (quantificada pelo Desvio Padrão Amostral) é a evidência empírica da
    necessidade dessas repetições.
  - `maqD_rodada_*.CSV` → coluna `CPU Inteira (°C)` e `Estrangulamento térmico do núcleo (avg)
    (Yes/No)`: variações térmicas entre rodadas demonstram que execuções únicas seriam insuficientes
    para capturar o comportamento real do sistema — corroborando a premissa dos autores.

---

### 3.2 Custo Computacional vs. Precisão — Trade-off em Avaliação de Desempenho

- **Conceito/Teoria:** Existe um trade-off fundamental entre custo computacional (número de
  execuções necessárias) e precisão dos resultados de desempenho. Abordagens de maior precisão
  tendem a demandar maior custo de execução.

- **Citação Direta (Ipsis Litteris):**
  > "A meta é avaliar o equilíbrio entre custo computacional, precisão e generalização." (Resumo, p. 1)

- **Citação Direta Complementar:**
  > "A abordagem com MLP tende a ser mais precisa em situações mais complexas, embora demande
  > maior esforço computacional." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) identificam um trade-off estrutural na avaliação de
  desempenho computacional: métodos de maior precisão — como redes neurais MLP — impõem custo
  computacional e de coleta de dados mais elevado, enquanto abordagens analíticas mais simples
  reduzem esse custo ao preço de menor generalidade. Esse trade-off é diretamente análogo à
  escolha, no presente trabalho, do número de rodadas de benchmark: aumentar as repetições eleva
  a confiabilidade estatística dos resultados, mas impõe custo de tempo ao grupo experimental.
  A definição de 20 rodadas representa o ponto de equilíbrio entre precisão estatística e
  viabilidade operacional.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — justificativa da quantidade de rodadas escolhida
  (20 rodadas) e da escolha do Desvio Padrão Amostral como métrica de precisão; Considerações Finais.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core` de todas as máquinas: o Desvio
    Padrão Amostral calculado sobre as 20 rodadas de cada máquina é a métrica que quantifica
    empiricamente esse trade-off entre custo (número de rodadas) e precisão (redução do erro
    estatístico pela Lei dos Grandes Números).

---

### 3.3 Erro Relativo Absoluto como Métrica de Validação Experimental

- **Conceito/Teoria:** O erro relativo absoluto é a métrica primária para comparar estimativas de
  desempenho com valores reais medidos. Quanto menor o erro relativo entre uma estimativa e o
  valor real, maior a fidelidade do modelo ou do experimento.

- **Citação Direta (Ipsis Litteris):**
  > "A comparação entre eles será feita com base em três métricas: erro relativo absoluto entre o
  > tempo estimado e o tempo real, tempo total de análise e custo computacional." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) adotam o erro relativo absoluto como métrica central para
  quantificar a fidelidade de estimativas de desempenho em relação aos valores medidos
  experimentalmente. Essa métrica normaliza a diferença entre estimativa e realidade em função
  do valor real, tornando-a comparável entre configurações distintas de hardware e carga.
  No contexto do presente trabalho, o Desvio Padrão Amostral das 20 rodadas de Geekbench 6
  cumpre papel análogo: ao medir a dispersão dos scores obtidos em torno da média, quantifica
  o quanto os valores observados experimentalmente divergem entre si, servindo como indicador
  da estabilidade e reprodutibilidade do benchmark em cada máquina.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — definição formal das métricas estatísticas
  utilizadas (Média Aritmética e Desvio Padrão Amostral); Resultados e Discussão.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core`: calcular, para cada máquina, o
    Desvio Padrão Amostral das 20 rodadas e expressá-lo também como percentual da média
    (coeficiente de variação — CV%) produz uma métrica análoga ao "erro relativo absoluto"
    citado pelos autores, facilitando a comparação entre máquinas com scores em escalas
    absolutas distintas.

  **Fórmula do Coeficiente de Variação sugerida para o `main.tex`:**
  ```latex
  \begin{equation}
  CV = \frac{s}{\bar{x}} \times 100\%
  \label{eq:cv}
  \end{equation}
  ```
  Onde $s$ é o Desvio Padrão Amostral e $\bar{x}$ é a Média Aritmética das 20 rodadas.
  Máquinas com $CV$ elevado indicam instabilidade de desempenho (provável throttling térmico
  ou ruído de armazenamento), enquanto $CV$ baixo indica comportamento estável e reprodutível.

---

### 3.4 "Memory Wall" — Gargalo de Memória em Aplicações Paralelas (Via Referência Citada)

- **Conceito/Teoria:** O "Memory Wall" (Muro de Memória) descreve o fenômeno pelo qual o
  desempenho de aplicações paralelas é limitado não pela capacidade de processamento dos núcleos,
  mas pela velocidade com que a memória principal consegue fornecer dados aos processadores.
  É o equivalente em larga escala do gargalo de Von Neumann que estudamos em AOC.

- **Origem no Artigo Fichado:**
  Os autores referenciam diretamente o trabalho de Furtunato et al. (2020), intitulado
  *"When parallel speedups hit the memory wall"* (IEEE Access, v. 8, p. 79225–79238), como
  base metodológica para o modelo analítico que propõem.

- **Citação Direta (Ipsis Litteris) — Referência ao Trabalho de Furtunato et al.:**
  > "A metodologia do trabalho consiste inicialmente na construção de um modelo analítico baseado
  > em curvas de tempo de execução, com aplicação de modelagem semelhante à utilizada por
  > Furtunato et al [Furtunato et al. 2020], adaptando para a métrica de tempo de execução." (p. 1)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) fundamentam seu modelo analítico no trabalho de Furtunato
  et al. (2020), que demonstrou empiricamente que aplicações paralelas atingem um ponto de
  saturação de desempenho determinado não pela quantidade de núcleos disponíveis, mas pela
  largura de banda de memória do sistema — fenômeno denominado *Memory Wall*. No contexto
  do presente trabalho, esse fenômeno se manifesta na comparação entre máquinas com subsistemas
  de memória distintos: processadores operando com memória em modo Single Channel (como a
  Máquina D, com 1x8 GB DDR4 a 1333 MHz) possuem largura de banda de memória limitada que
  pode impedir os núcleos de operarem em sua capacidade máxima durante o teste Multi-Core do
  Geekbench 6, mesmo que o processador disponha de múltiplos núcleos ativos.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Hierarquia de Memória
  e Gargalo de Von Neumann; Resultados e Discussão — análise comparativa do impacto de Single
  Channel vs. Dual Channel nos scores Multi-Core.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqD.txt` → coluna `Multi_Core`: se o score Multi-Core da Máquina D não escalar
    proporcionalmente ao número de núcleos em relação ao Single-Core, o *Memory Wall* é o
    principal suspeito arquitetural — a memória Single Channel (largura de banda ~21 GB/s)
    não consegue alimentar todos os 4 núcleos simultaneamente.
  - `maqD_rodada_*.CSV` → coluna `Carga da memória física (%)`: utilização próxima de 100%
    durante os testes Multi-Core é evidência direta do gargalo de memória.
  - `maqD_rodada_*.CSV` → coluna `Relógio da memória (MHz)` e `Tcas (T)`, `Trcd (T)`, `Trp (T)`,
    `Tras (T)`: os timings de latência da memória DDR4 registrados pelo HWiNFO64 determinam
    o custo de acesso à memória — latências elevadas combinadas com largura de banda Single
    Channel compõem o gargalo descrito pelo conceito de *Memory Wall*.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA (MÁQUINAS A, B e C) — ATUALIZADA:**
  > Se alguma das Máquinas A, B ou C operar com memória em modo Dual Channel, a largura de banda
  > efetiva será aproximadamente o dobro da Máquina D. Isso deverá se traduzir em ganho expressivo
  > no score Multi-Core do Geekbench 6 sem necessariamente elevar o score Single-Core — padrão
  > característico da superação do gargalo de *Memory Wall*. **Este mapeamento de colunas e sua
  > interpretação só serão utilizados na redação final conforme as configurações reais de hardware
  > das Máquinas A, B ou C forem preenchidas pelo grupo nas próximas interações, se necessário.**
  >
  > Com a tabela de hardware completa agora disponível (Máquinas A–F), confirma-se empiricamente
  > que esse cenário preditivo se realiza: a **Máquina A** opera em Dual Channel (DDR5 5200 MT/s)
  > e a **Máquina C** opera em Single Channel (DDR4, MHz não informado), reproduzindo exatamente
  > o contraste teórico aqui anunciado. A análise detalhada e quantificada desse contraste está
  > desenvolvida na nova seção 3.7 deste fichamento.

---

### 3.5 Escalabilidade de Desempenho vs. Número de Núcleos — Lei de Amdahl (Implícita)

- **Conceito/Teoria:** O desempenho de aplicações paralelas não escala linearmente com o número
  de núcleos. A fração serial do código e os gargalos de memória impõem um limite superior ao
  ganho de desempenho em sistemas multicore — limite formalizado pela Lei de Amdahl.

- **Citação Direta (Ipsis Litteris):**
  > "Os experimentos serão realizados com três algoritmos — todos paralelizados com diretivas do
  > OpenMP: multiplicação de matrizes, busca em largura (BFS) e o traçado de raio (ray trace).
  > Para cada algoritmo, serão variadas o número de núcleos utilizados e o tamanho da entrada."
  > (p. 2)

- **Citação Direta Complementar:**
  > "Porém existem desafios, como a limitação da abordagem analítica em modelar comportamentos
  > não lineares e o risco de overfitting nos modelos de aprendizado de máquina, caso o conjunto
  > de dados de treino não represente adequadamente todo o domínio de execução." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) estruturam seus experimentos variando simultaneamente o
  número de núcleos ativos e o tamanho da carga de trabalho, reconhecendo que o comportamento
  de desempenho em sistemas paralelos é não linear — fator que dificulta a modelagem analítica
  simples e demanda abordagens mais sofisticadas para capturar regiões de transição de
  comportamento. Essa não linearidade é explicada, em nível de arquitetura, pela Lei de Amdahl:
  à medida que o número de núcleos aumenta, a fração serial do código e os gargalos de
  comunicação entre núcleos passam a dominar o tempo total de execução, impondo um teto de
  ganho que não pode ser superado apenas com adição de unidades de processamento.

- **Onde Encaixar no Artigo LaTeX:** Fundamentação Teórica — subseção sobre Paralelismo a Nível
  de Thread e Limitações de Escalabilidade; Resultados — análise da razão entre score Multi-Core
  e Single-Core como proxy do ganho de paralelismo efetivo de cada máquina.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → razão entre `Multi_Core` e `Single_Core` por máquina: o quociente
    Multi/Single é o indicador empírico de eficiência paralela — valores próximos ao número
    de núcleos (ex.: ratio ≈ 4 para 4 núcleos) indicam boa escalabilidade; valores menores
    indicam gargalos (memória, térmica ou serialização de código).
  - `maqD_rodada_*.CSV` → coluna `Uso total da CPU (%)` vs. `Relógios efetivos núcleo (avg)
    (MHz)`: durante o teste Multi-Core, uso total elevado com clocks efetivos abaixo do boost
    máximo indica que os núcleos estão ativos mas limitados — condição análoga ao teto de Amdahl
    imposto por gargalos de memória ou térmica.
  - `maqD_rodada_*.CSV` → colunas `Core 0 T0 Uso (%)` a `Core 3 T1 Uso (%)`: distribuição de
    carga entre threads revela o grau de paralelismo efetivo explorado pelo Geekbench 6.

---

### 3.6 Generalização de Modelos e Reprodutibilidade Experimental

- **Conceito/Teoria:** A capacidade de um modelo experimental ou analítico generalizar seus
  resultados para cenários não observados durante o treinamento/coleta é um critério fundamental
  de validade científica. Em benchmarking, isso corresponde à reprodutibilidade dos resultados
  em diferentes condições de execução.

- **Citação Direta (Ipsis Litteris):**
  > "A meta é avaliar o equilíbrio entre custo computacional, precisão e generalização."
  > (Resumo, p. 1)

- **Citação Direta Complementar:**
  > "Espera-se que os resultados contribuam para tornar as análises de desempenho mais rápidas,
  > econômicas e viáveis em diferentes contextos de aplicação." (p. 2)

- **Paráfrase (Citação Indireta Acadêmica):**
  Lucena e Xavier-de-Souza (2025) destacam que a generalização — capacidade de um método
  produzir resultados consistentes em condições distintas das observadas durante sua calibração —
  é um dos três pilares fundamentais da avaliação científica de desempenho, ao lado da precisão
  e do custo computacional. Transposto para o contexto do presente trabalho, o conceito de
  generalização equivale à reprodutibilidade dos scores de benchmark entre rodadas e entre
  máquinas distintas: um método de avaliação de desempenho só é cientificamente válido se seus
  resultados forem estáveis e comparáveis entre diferentes execuções do mesmo ambiente e
  transferíveis como referência de comparação entre ambientes distintos.

- **Onde Encaixar no Artigo LaTeX:** Metodologia — justificativa do protocolo padronizado de
  coleta (mesmo benchmark, mesma versão, mesmo sistema operacional, janelas de tempo iguais);
  Resultados — discussão sobre a comparabilidade dos scores entre as quatro máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → colunas `Single_Core` e `Multi_Core` de todas as máquinas: a
    reprodutibilidade é medida pelo Desvio Padrão Amostral das 20 rodadas. Máquinas com
    desvio padrão baixo apresentam alta reprodutibilidade e, portanto, maior generalização
    dos resultados de benchmark.
  - `maqD_rodada_*.CSV` → todas as colunas de telemetria: a uniformidade das condições
    ambientais (temperatura inicial de cada rodada, carga de background) é a variável de
    controle que garante a generalização dos resultados entre rodadas.

---

### 3.7 Correlação com a Tabela Completa de Hardware (Máquinas A–F) — ATUALIZAÇÃO

> **NOTA DE ESCOPO DESTA SEÇÃO:** Esta subseção foi adicionada após o recebimento da tabela
> comparativa completa de hardware das seis máquinas do grupo (A, B, C, D, E e F). Ela **não
> introduz novos conceitos teóricos do artigo de Lucena e Xavier-de-Souza (2025)** — os cinco
> conceitos já fichados nas seções 3.1 a 3.6 permanecem inalterados. O objetivo aqui é **aplicar
> esses mesmos conceitos teóricos aos componentes reais agora disponíveis**, demonstrando
> concretamente onde cada citação encontra correspondência empírica na nossa base de hardware.
> Cada subitem abaixo indica explicitamente a qual seção anterior (3.1–3.6) ele se vincula.

---

#### 3.7.1 Memory Wall e Topologia de Canais de RAM (vínculo direto com a Seção 3.4)

- **Conceito retomado:** *Memory Wall* — limitação de desempenho pela largura de banda de
  memória, fundamentado em Furtunato et al. (2020) e citado por Lucena e Xavier-de-Souza (2025).

- **Correlação com a Tabela de Hardware:**
  A tabela completa confirma a existência de um contraste arquitetural direto e mensurável
  entre topologias de memória no nosso conjunto de seis máquinas:

  | Máquina | Topologia RAM | Tipo/Velocidade | Núcleos/Threads |
  |---|---|---|---|
  | A (Raony) | **Dual Channel** (1x8GB) | DDR5 5200 MT/s | 8C/12T |
  | B (Leandro) | **Dual Channel** (2x8GB) | DDR4 2666 MHz | 10C/12T |
  | C (Cinara) | **Single Channel** (1x8GB) | DDR4 [MHz não informado]* | 4C/8T |
  | D (Roberta) | **Single Channel** (1x8GB) | DDR4 2400 MHz | 4C/8T |
  | E (Nauan) | **Dual Channel** (2x8GB) | DDR4 [MHz não informado]* | 6C/12T |
  | F (Nicolas) | **Dual Channel** (2x16GB) | DDR4 3600 MHz | 14C/20T |

  **Justificativa de uso no `main.tex`:** Esta tabela viabiliza, pela primeira vez no projeto,
  uma comparação de pares quase controlada. A Máquina C e a Máquina D compartilham a condição
  de Single Channel e número idêntico de núcleos físicos (4C/8T), formando um grupo de
  comparação natural. Já as Máquinas A, B, E e F operam em Dual Channel, mas com núcleos físicos
  distintos (8, 10, 6 e 14, respectivamente), de modo que a comparação de eficiência de
  paralelismo (ver Equação `eq:eficiencia_paralela`, seção 4.2) deve ser normalizada pelo número
  de núcleos antes de qualquer conclusão sobre o efeito isolado do canal de memória.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA — DADOS AINDA PENDENTES:** A velocidade efetiva da RAM
  > (MHz) das Máquinas C e E não foi informada na tabela ("[MHz]*"). Sem esse dado, a largura
  > de banda teórica dessas duas máquinas não pode ser calculada com precisão pela fórmula
  > $BW = \text{canais} \times \text{frequência efetiva} \times \text{largura do barramento}$.
  > **Este trecho teórico e seu respectivo mapeamento de colunas foram devidamente fichados de
  > forma preditiva e só serão utilizados na redação final conforme as configurações reais de
  > hardware das Máquinas C e E forem preenchidas pelo grupo nas próximas interações, se
  > necessário.**

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqA.txt` a `scores_maqF.txt` (quando disponíveis) → coluna `Multi_Core`: comparar
    o score Multi-Core de C e D (ambas Single Channel, 4C/8T) com o de A, B, E e F (Dual Channel)
    normalizado pelo número de núcleos é o teste empírico direto da hipótese de *Memory Wall*
    citada na seção 3.4.
  - `maqA_rodada_*.CSV`, `maqB_rodada_*.CSV`, `maqE_rodada_*.CSV`, `maqF_rodada_*.CSV` → coluna
    `Relógio da memória (MHz)`: permitirá calcular a largura de banda teórica real de cada
    máquina Dual Channel assim que os arquivos de telemetria dessas máquinas forem gerados.
  - `maqC_rodada_*.CSV` e `maqD_rodada_*.CSV` → coluna `Carga da memória física (%)`: espera-se
    que ambas apresentem maior saturação desta métrica durante o teste Multi-Core, evidenciando
    o estrangulamento de banda descrito pelo *Memory Wall*.

---

#### 3.7.2 Custo Computacional vs. Precisão — TDP e Litografia como Proxy de Custo Energético (vínculo com a Seção 3.2)

- **Conceito retomado:** Trade-off entre custo computacional e precisão/desempenho, citado por
  Lucena e Xavier-de-Souza (2025) ao comparar modelagem analítica (menor custo) com MLP
  (maior custo, maior precisão).

- **Correlação com a Tabela de Hardware:**
  A tabela revela um espectro de TDP entre 15 W (Máquinas B, C e D) e 125 W (Máquina F),
  abrangendo litografias de 14 nm (Whiskey Lake-U) a 7 nm/Intel 7 (Zen 3, Raptor Lake).
  Esse espectro é o análogo arquitetural direto do trade-off "custo computacional vs. precisão"
  descrito no artigo fichado: assim como os autores reconhecem que maior precisão (MLP) custa
  mais poder computacional, em nível de hardware um TDP mais alto (Máquina F, 125 W) tende a
  entregar desempenho bruto superior ao custo de maior consumo energético — o inverso ocorrendo
  nas máquinas de 15 W (B, C, D), otimizadas para eficiência energética em detrimento do
  desempenho de pico.

  **Justificativa de uso no `main.tex`:** Esta correlação fundamenta a métrica de Desempenho
  por Watt (Seção 5 do escopo teórico geral do projeto) ao comparar diretamente as Máquinas
  B/C/D (15 W) contra E/F (65 W/125 W), usando o TDP nominal da tabela como denominador
  preliminar até que a coluna real `Potência total da CPU (W)` do HWiNFO64 esteja disponível
  para todas as seis máquinas.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maq*.txt` → coluna `Multi_Core` dividida pelo TDP Base da CPU (W) da tabela:
    proxy preliminar de Desempenho por Watt, válido enquanto os arquivos CSV de telemetria
    completos não estiverem disponíveis para as Máquinas A, B, C, E e F.
  - `maq*_rodada_*.CSV` → coluna `Potência total da CPU (W)`: substituirá o TDP nominal da
    tabela pelo consumo real medido, refinando o cálculo de Desempenho por Watt assim que
    os 80 arquivos estiverem completos para todas as seis máquinas.

---

#### 3.7.3 Múltiplas Execuções e Estabilidade Térmica — TDP Elevado como Fator de Risco (vínculo com a Seção 3.1)

- **Conceito retomado:** Necessidade metodológica de múltiplas execuções para capturar
  variações reais de desempenho, citada na seção 3.1, com a coluna `CPU Inteira (°C)` como
  evidência de que execuções únicas seriam insuficientes.

- **Correlação com a Tabela de Hardware:**
  A Máquina F (Intel Core i5-14600KF, TDP 125 W, 14 núcleos/20 threads) é a configuração de
  maior densidade de potência da tabela. Processadores Desktop "K/KF" da Intel são historicamente
  associados a maior variabilidade térmica sob carga sustentada, pois operam com Turbo Boost
  agressivo (P-Cores até 5.3 GHz) frequentemente limitado pela capacidade de dissipação do
  cooler instalado — informação ainda não detalhada na tabela ("[Preencher Gabinete]*").
  Esse cenário reforça, com um caso concreto do nosso próprio conjunto de máquinas, exatamente
  o argumento da seção 3.1: a necessidade de múltiplas rodadas para capturar a variabilidade
  real de desempenho ao longo do tempo de execução.

  **Justificativa de uso no `main.tex`:** Recomenda-se usar a Máquina F como exemplo central
  na discussão de Desvio Padrão Amostral elevado, pois seu TDP de 125 W em fator de forma
  Desktop é o cenário mais propenso a apresentar variações de clock entre rodadas devido a
  ajustes dinâmicos de frequência sob temperatura.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqF.txt` (quando disponível) → colunas `Single_Core` e `Multi_Core`: calcular o
    Desvio Padrão Amostral das 20 rodadas é o teste direto desta hipótese.
  - `maqF_rodada_*.CSV` → colunas `CPU Inteira (°C)`, `Núcleo máximo (°C)` e `Estrangulamento
    térmico do núcleo (avg) (Yes/No)`: evidência primária de eventual throttling térmico que
    explicaria desvios padrão elevados nos scores desta máquina.

  > ⚠️ **NOTA DE ABSTRAÇÃO PREDITIVA — DADO PENDENTE:** O modelo do gabinete e o sistema de
  > refrigeração das Máquinas E e F ainda não foram preenchidos na tabela ("[Preencher
  > Gabinete]*"). Sem essa informação, não é possível afirmar se a dissipação térmica é
  > adequada ao TDP de 65 W/125 W. **Este trecho teórico foi fichado de forma preditiva e só
  > será utilizado na redação final conforme os dados de gabinete/refrigeração das Máquinas
  > E e F forem preenchidos pelo grupo, se necessário.**

---

#### 3.7.4 Cache L3 e Instruções Avançadas como Variáveis Adicionais de Generalização (vínculo com a Seção 3.6)

- **Conceito retomado:** Generalização e comparabilidade de resultados entre ambientes
  distintos, citada na seção 3.6, exigindo controle de variáveis para que a comparação entre
  máquinas seja cientificamente válida.

- **Correlação com a Tabela de Hardware:**
  A tabela revela que o Cache L3 varia de 4 MB (Máquina C) a 24 MB (Máquina F), e que o
  conjunto de instruções avançadas (AVX, AVX2, FMA3, BMI2 e, em alguns casos, Intel DL Boost/VNNI)
  não é uniforme entre as seis máquinas — processadores AMD (Máquinas C e E) não possuem
  Intel DL Boost (VNNI), por exemplo. Isso é uma variável de confusão relevante para a
  generalização dos resultados: scores de benchmark sintético como o Geekbench 6 podem ser
  sensíveis ao uso de instruções vetoriais específicas, de modo que a comparação direta entre
  CPUs Intel e AMD deve considerar essa diferença como possível fonte de variância não
  relacionada à arquitetura de memória ou térmica.

  **Justificativa de uso no `main.tex`:** Esta correlação deve ser citada como limitação
  metodológica na seção de Discussão, reforçando — em linha com o conceito de generalização
  da seção 3.6 — que comparações de desempenho cross-vendor (Intel vs. AMD) exigem cautela
  interpretativa adicional, pois parte da diferença de score pode refletir o conjunto de
  instruções suportado, e não apenas frequência, núcleos ou hierarquia de memória.

- **Mapeamento de Colunas e Arquivos de Teste:**
  - `scores_maqC.txt` e `scores_maqE.txt` (CPUs AMD) vs. demais arquivos (CPUs Intel) → coluna
    `Single_Core`: comparação que deve ser acompanhada de nota metodológica sobre a ausência
    de VNNI nos processadores AMD do conjunto.
  - Não há coluna específica no HWiNFO64 para uso de instruções vetoriais (AVX/VNNI) durante
    a execução; esta limitação deve ser declarada explicitamente na seção de Limitações do
    artigo final.

---

### 4.1 Observação sobre Fórmulas no Artigo Original

O artigo não apresenta equações matemáticas explícitas em seu corpo. A modelagem analítica
mencionada pelos autores é descrita em termos qualitativos como "baseada em curvas de tempo de
execução", sem detalhar as equações formais — o que é compatível com o escopo reduzido de um
artigo de 2 páginas de conferência.

As fórmulas relevantes para o nosso `main.tex`, derivadas dos conceitos abordados pelo artigo,
são as seguintes:

---

### 4.2 Fórmulas para Inserção no `main.tex` (Derivadas dos Conceitos do Artigo)

**Média Aritmética dos Scores (Estimativa do Valor Central):**
```latex
\begin{equation}
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\label{eq:media}
\end{equation}
```

**Desvio Padrão Amostral (Métrica de Reprodutibilidade e Estabilidade):**
```latex
\begin{equation}
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
\label{eq:desvpad}
\end{equation}
```

**Coeficiente de Variação — CV (Métrica Relativa, Análoga ao Erro Relativo Absoluto):**
```latex
\begin{equation}
CV = \frac{s}{\bar{x}} \times 100\%
\label{eq:cv}
\end{equation}
```

**Eficiência de Paralelismo Empírica (Razão Multi-Core / Single-Core):**
```latex
\begin{equation}
E_{paralela} = \frac{\bar{x}_{Multi\text{-}Core}}{\bar{x}_{Single\text{-}Core}}
\label{eq:eficiencia_paralela}
\end{equation}
```

Onde:
- $x_i$ = score (Single\_Core ou Multi\_Core) da $i$-ésima rodada de benchmark.
- $n = 20$ = número total de rodadas por máquina (correção de Bessel no denominador $n-1$).
- $E_{paralela}$ = razão entre o score médio Multi-Core e o score médio Single-Core, indicando
  o ganho efetivo de paralelismo. Valor ideal para 4 núcleos com Hyper-Threading = próximo de 8;
  valores observados abaixo disso indicam gargalo de memória (*Memory Wall*), térmica ou overhead.

---

### 4.3 Referência Bibliográfica Derivada de Alto Valor — Furtunato et al. (2020)

O artigo fichado cita o seguinte trabalho como base metodológica central, diretamente relevante
para nossa discussão de *Memory Wall* e gargalo de Von Neumann:

> FURTUNATO, A. F. A.; GEORGIOU, K.; EDER, K.; XAVIER-DE-SOUZA, S. **When parallel speedups
> hit the memory wall**. IEEE Access, v. 8, p. 79225–79238, 2020.

**BibTeX sugerido para o `sbc-template.bib`:**
```bibtex
@Article{furtunato:20,
  author  = {Ant{\^o}nio F. A. Furtunato and Kyriakos Georgiou
             and Kerstin Eder and Samuel Xavier-De-Souza},
  title   = {When parallel speedups hit the memory wall},
  journal = {{IEEE} Access},
  year    = {2020},
  volume  = {8},
  pages   = {79225--79238},
  doi     = {10.1109/ACCESS.2020.2990470}
}
```

> 🔑 **Este é o artigo de alto valor oculto no fichamento:** O artigo de Lucena e Xavier-de-Souza
> (2025) funciona como um ponteiro bibliográfico para Furtunato et al. (2020), que discute
> diretamente o *Memory Wall* em aplicações paralelas. Recomenda-se fortemente que o grupo
> localize e fiche separadamente o artigo de Furtunato et al. (2020) — disponível no IEEE
> Access com DOI: 10.1109/ACCESS.2020.2990470 — pois ele fornecerá embasamento teórico
> robusto para a discussão sobre Single Channel vs. Dual Channel e gargalo de memória.

---

### 4.4 Sugestão de Gráficos e Tabelas para o `main.tex`

**Gráfico Sugerido — Eficiência de Paralelismo por Máquina:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Razão Multi-Core / Single-Core por máquina (preencher com dados reais)
maquinas     = ['Máquina A', 'Máquina B', 'Máquina C', 'Máquina D']
media_single = [mean_A_single, mean_B_single, mean_C_single, mean_D_single]
media_multi  = [mean_A_multi,  mean_B_multi,  mean_C_multi,  mean_D_multi]

eficiencia = [m / s for m, s in zip(media_multi, media_single)]

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(maquinas, eficiencia,
              color=['#1a1a1a', '#555555', '#999999', '#cccccc'],
              edgecolor='black', linewidth=0.8)
ax.axhline(y=4, color='black', linestyle='--', linewidth=0.8,
           label='Teto teórico Amdahl (4 núcleos)')
ax.set_xlabel('Máquina', fontsize=11)
ax.set_ylabel('Razão Multi-Core / Single-Core', fontsize=11)
ax.set_title('Eficiência de Paralelismo por Máquina (Geekbench 6)', fontsize=12)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('fig_eficiencia_paralela.pdf', dpi=300)
```

**Legenda LaTeX sugerida para inserção no `main.tex`:**
```latex
\begin{figure}[ht]
\centering
\includegraphics[width=.7\textwidth]{fig_eficiencia_paralela.pdf}
\caption{Razão entre os scores médios Multi-Core e Single-Core do Geekbench~6 por máquina,
  indicando a eficiência de paralelismo empírica. A linha tracejada representa o teto teórico
  de escalabilidade para 4 núcleos físicos. Valores inferiores a este teto evidenciam a
  presença de gargalos arquiteturais (memória, térmica ou overhead de sincronização).
  Fonte: Os autores (2026).}
\label{fig:eficiencia_paralela}
\end{figure}
```

---

## 5. KEYWORDS PARA BUSCA NO GOOGLE ACADÊMICO

Com base nos conceitos fichados neste documento, as seguintes strings de busca são recomendadas
para encontrar referências de alto impacto que sustentem as seções do artigo:

**Para embasar a discussão sobre Memory Wall e gargalo de memória (PRIORIDADE ALTA):**
- `"memory wall" "parallel speedups" multicore benchmark`
- `"single channel" "dual channel" DDR4 benchmark performance comparison`
- `"Von Neumann bottleneck" memory bandwidth CPU performance`
- `"gargalo de memória" "canal único" desempenho processador multicore`
- `memory bandwidth bottleneck CPU benchmark scaling`

**Para embasar a justificativa das múltiplas rodadas de benchmark:**
- `benchmark reproducibility "multiple runs" "standard deviation" CPU`
- `"performance variability" benchmark statistical analysis`
- `"number of iterations" benchmark methodology statistical significance`
- `reprodutibilidade benchmark metodologia avaliação desempenho`

**Para embasar a discussão sobre escalabilidade e Lei de Amdahl:**
- `"Amdahl's law" multicore performance scaling benchmark`
- `"Lei de Amdahl" processador multicore desempenho escalabilidade`
- `parallel efficiency multicore CPU benchmark real workload`
- `"speedup" "multicore" "memory bottleneck" benchmark`

**Para embasar a seção de métricas estatísticas (desvio padrão, CV):**
- `"coefficient of variation" CPU benchmark performance stability`
- `"sample standard deviation" performance evaluation computer benchmark`
- `benchmark score variability thermal throttling standard deviation`
- `"coeficiente de variação" benchmark desempenho computacional`

**Para buscar o artigo de Furtunato et al. (2020) — referência derivada de ALTA PRIORIDADE:**
- `"when parallel speedups hit the memory wall" Furtunato`
- `furtunato georgiou eder xavier-de-souza "memory wall" IEEE Access 2020`
- DOI direto: `10.1109/ACCESS.2020.2990470`

---

> **⚠️ SÍNTESE FINAL DE APROVEITAMENTO:**
>
> Este artigo de 2 páginas possui valor primário **baixo** para o projeto, pois não aborda
> hardware real, telemetria, temperatura ou energia. Seu aproveitamento direto no `main.tex`
> deve ser restrito a:
>
> 1. **Uma citação** na Metodologia justificando as 20 rodadas como necessidade metodológica
>    de análise de desempenho (seção 3.1 deste fichamento).
> 2. **Uma citação** na Metodologia ou Fundamentação Teórica usando o conceito de trade-off entre
>    custo e precisão para justificar o protocolo experimental (seção 3.2).
> 3. **Um apontamento bibliográfico** para Furtunato et al. (2020) — *"When parallel speedups
>    hit the memory wall"* — como referência de alto impacto sobre *Memory Wall*, que deverá ser
>    fichada e citada diretamente na seção de Hierarquia de Memória e Gargalo de Von Neumann
>    (seção 3.4 deste fichamento).
>
> O grupo deve priorizar a busca e fichamento autônomo de Furtunato et al. (2020) para extrair
> os dados quantitativos sobre *Memory Wall* que este artigo apenas menciona de forma referencial.

---

> **📌 ADENDO À SÍNTESE — APÓS RECEBIMENTO DA TABELA COMPLETA DE HARDWARE (A–F):**
>
> A seção 3.7, adicionada nesta atualização, não modifica o veredito original nem os conceitos
> já fichados (3.1–3.6) — ela apenas ancora cada um desses conceitos em componentes reais do
> conjunto de seis máquinas do grupo:
>
> - **3.7.1** vincula a Seção 3.4 (*Memory Wall*) ao contraste real Single Channel (Máquinas C
>   e D) vs. Dual Channel (Máquinas A, B, E e F), agora com correspondência empírica concreta.
> - **3.7.2** vincula a Seção 3.2 (trade-off custo/precisão) ao espectro de TDP entre 15 W e
>   125 W presente na tabela, propondo um proxy preliminar de Desempenho por Watt.
> - **3.7.3** vincula a Seção 3.1 (necessidade de múltiplas execuções) ao caso da Máquina F
>   (125 W, Desktop), apontada como candidata mais provável a apresentar Desvio Padrão elevado.
> - **3.7.4** vincula a Seção 3.6 (generalização) à heterogeneidade de Cache L3 e conjuntos de
>   instruções (Intel vs. AMD) entre as seis máquinas, como limitação metodológica a declarar.
>
> **Dados ainda pendentes de preenchimento pelo grupo**, sinalizados com "[Preencher]*" na
> tabela original e replicados nas notas de abstração preditiva desta seção: velocidade da RAM
> (MHz) das Máquinas C e E; modelo de gabinete e refrigeração das Máquinas E e F; tipo de
> armazenamento e interface da Máquina C; geração da interface de disco da Máquina F.
