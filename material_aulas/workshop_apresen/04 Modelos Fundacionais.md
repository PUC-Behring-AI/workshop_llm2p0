[[Índice]] | [[03 Machine Learning|← Anterior]] | [[05 LLMs e Como Surgiram|Próximo →]]

# 04 Modelos Fundacionais

[[#A definição — Stanford 2021]]
[[#A história da IA é uma história de representações]]
[[#O que muda com os modelos fundacionais]]
[[#Emergência e homogeneização]]
[[#Oportunidades e riscos]]

---

## A definição — Stanford 2021

Em agosto de 2021, pesquisadores da Stanford publicaram um artigo que cunhou o termo e definiu o campo:

> Bommasani et al., [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258), arXiv:2108.07258

A definição formal do artigo:

> *"Models trained on broad data (generally using self-supervision at scale) that can be adapted (e.g., fine-tuned) to a wide range of downstream tasks."*

Em português:

> *Modelos treinados em dados amplos — geralmente via auto-supervisão em escala — que podem ser adaptados a uma grande variedade de tarefas.*

Três elementos essenciais nessa definição: **dados amplos** (não específicos de uma tarefa), **auto-supervisão em escala** (sem necessidade de rotulação manual massiva), e **adaptabilidade** (o mesmo modelo serve como base para muitas aplicações).

---

## A história da IA é uma história de representações

*Figura retirada de [Bommasani et al.](https://arxiv.org/pdf/2108.07258), Fig. 1*

![[figs/machine_learning_evolution.png]]

A evolução não é linear — é uma série de mudanças de paradigma, cada uma habilitada por mais dados e mais poder computacional:

Na era das **representações manuais**, especialistas codificavam o conhecimento diretamente em regras e features. O sistema era tão bom quanto o conhecimento do programador — e escalava mal.

No **ML por tarefa**, os sistemas aprendiam padrões a partir de dados, mas precisavam de dados rotulados e eram treinados separadamente para cada problema. Um modelo de detecção de spam não sabia nada sobre tradução.

Com o **aprendizado profundo**, redes neurais com muitas camadas passaram a aprender representações hierárquicas diretamente dos dados brutos. A necessidade de features manuais desapareceu em muitos domínios — e o desempenho disparou em visão, fala e linguagem.

Os **modelos fundacionais** representam a fase atual: treinados em escala incomparável, em dados de múltiplas modalidades, capazes de ser adaptados a tarefas que nem existiam quando foram criados.

---

## O que muda com os modelos fundacionais

*Figura retirada de [Bommasani et al.](https://arxiv.org/pdf/2108.07258),Fig. 2*

![[figs/foundation_model.png]]

O modelo fundacional funciona como um **centro de gravidade**: absorve dados de múltiplas modalidades durante o pré-treino, e depois pode ser adaptado — via fine-tuning ou prompting — para uma enorme variedade de tarefas downstream.

Isso inverte a lógica anterior. Em vez de treinar um modelo por tarefa, você treina **um** modelo massivo e o adapta. O custo do pré-treino é amortizado por todas as aplicações que se constroem sobre ele.

---

## Emergência e homogeneização

O artigo da Stanford identifica dois fenômenos que definem o paradigma:

**Emergência** — capacidades que surgem espontaneamente da escala, sem terem sido treinadas explicitamente. O GPT-3, com 175 bilhões de parâmetros, desenvolveu a capacidade de aprender novas tarefas apenas a partir de exemplos no prompt (*in-context learning*) — algo que não foi programado nem antecipado.

**Homogeneização** — à medida que todos os produtos e aplicações são construídos sobre os mesmos poucos modelos fundacionais, o ecossistema converge. Isso é uma faca de dois gumes: os esforços para melhorar robustez e reduzir vieses se concentram em poucos modelos e beneficiam todos — mas os problemas e vieses desses modelos também se propagam por toda a cadeia.

> *"Foundation models incentivize homogenization: the same few models are repeatedly reused as the basis for many applications."*
> — [Bommasani et al.](https://arxiv.org/pdf/2108.07258), 2021

---

## Oportunidades e riscos

O título do artigo não é por acaso. Os autores identificaram explicitamente os dois lados:

**Oportunidades** — menor barreira para construir aplicações de IA, capacidades emergentes que nenhum modelo específico por tarefa teria, e a possibilidade de concentrar esforços de segurança e alinhamento num número pequeno de modelos.

**Riscos** — centralização de poder em poucos laboratórios e empresas, pontos únicos de falha que podem irradiar danos em escala, vieses e problemas do modelo base herdados por todas as aplicações construídas sobre ele, e impacto ambiental do treinamento massivo.

> 💡 Esses riscos não são abstratos — voltaremos a eles nas seções [[09 System Prompt e Guard Rails]] e [[11 Antropomorfização]], quando discutirmos como esses modelos moldam comportamentos e como tentamos limitá-los. A **centralização** em poucos laboratórios, nuvens e fabricantes de chips ganha uma seção própria, do ponto de vista de quem gere informação sensível, em [[09.2 Soberania da Informação]].

---

[[Índice]] | [[03 Machine Learning|← Anterior]] | [[05 LLMs e Como Surgiram|Próximo →]]

[[#04 Modelos Fundacionais|↑ Topo]]
