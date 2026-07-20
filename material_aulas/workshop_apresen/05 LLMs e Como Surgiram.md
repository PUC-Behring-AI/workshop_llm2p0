[[Índice]] | [[04 Modelos Fundacionais|← Anterior]] | [[06 Como os LLMs Aprendem|Próximo →]]

# 05 LLMs — O que são e como surgiram

[[#O que é um LLM]]
[[#A arquitetura que mudou tudo — Transformer (2017)]]
[[#O primeiro uso — tradução automática]]
[[#BERT e GPT — dois caminhos a partir do Transformer (2018–2019)]]
[[#GPT-3 — a virada de escala (2020)]]
[[#ChatGPT — quando o mundo percebeu (2022)]]
[[#O que ficou para trás]]

---

## O que é um LLM

Um **Modelo de Linguagem Grande** (*Large Language Model*, LLM) é um modelo fundacional especializado em linguagem — treinado para modelar a distribuição de probabilidade de sequências de texto.

Na prática, isso significa que o modelo aprendeu a responder a pergunta:

> *Dado tudo que veio antes, qual é o token mais provável a seguir?*

$$\arg\max_{x} \; P(x \mid t_1, t_2, \ldots, t_n)$$

Essa pergunta não é nova. Em 1951, Claude Shannon — o pai da teoria da informação — publicou um experimento simples e profundo: ele mostrava a pessoas fragmentos de texto em inglês e pedia que adivinhassem a letra seguinte. A partir das taxas de acerto, estimou a entropia do inglês escrito — o quanto de "surpresa" cada novo caractere carrega dado o contexto anterior.

> Shannon, C. E., [*Prediction and Entropy of Printed English*](https://doi.org/10.1002/j.1538-7305.1951.tb01366.x), Bell System Technical Journal, 1951.


A conclusão de Shannon foi que o inglês é altamente redundante — conhecendo o contexto, um leitor humano consegue prever a próxima letra com acerto surpreendente. Os LLMs fazem exatamente isso, mas em escala computacional e com tokens em vez de letras: aprendem a distribuição de probabilidade do que vem a seguir, sobre trilhões de exemplos de texto.

A ideia central tem mais de 70 anos. O que mudou foi a escala.

Essa é a mesma equação que vimos em [[03 Machine Learning]] — mas aplicada a linguagem, em escala de bilhões de parâmetros e trilhões de palavras de treinamento.

Para entender o que são os $t_i$ nessa equação — as unidades sobre as quais o modelo opera — veja [[06 Como os LLMs Aprendem#Tokenização — as unidades do aprendizado|06 — Tokenização]]. Para ver ao vivo como o modelo calcula as probabilidades do próximo token, use os demos em [[Recursos e Demos#06. Como os LLMs Aprendem — auto-supervisão, tokens e geração|Recursos e Demos]].

O "Grande" no nome não é marketing. Ele descreve uma descontinuidade real: modelos acima de certos limiares de escala desenvolvem **capacidades emergentes** que modelos menores simplesmente não têm — raciocínio em múltiplos passos, aprendizado a partir de exemplos no prompt, tradução sem treinamento explícito para o par de idiomas.

---

## A arquitetura que mudou tudo — Transformer (2017)

Em 2017, pesquisadores do Google publicaram um artigo cujo título virou slogan:

> Vaswani et al., [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762), NeurIPS 2017


Antes do Transformer, os modelos de linguagem processavam texto de forma sequencial — palavra por palavra, acumulando contexto numa memória que inevitavelmente degradava com a distância. Sequências longas eram um problema estrutural.

O Transformer introduziu o **mecanismo de atenção**: em vez de processar sequencialmente, o modelo calcula diretamente o quanto cada token deve "prestar atenção" a cada outro token na sequência — em paralelo, sem importar a distância entre eles.

Três consequências imediatas:

**Paralelismo** — o processamento pode ser distribuído em hardware massivo (GPUs/TPUs), o que tornou possível treinar em escalas impensáveis anteriormente.

**Contexto global** — qualquer token pode influenciar diretamente qualquer outro, independente de quantas palavras os separam.

**Transferência de escala** — a arquitetura cresce de forma previsível: mais parâmetros, mais dados, melhor desempenho. Isso abriu caminho para a corrida de escala dos anos seguintes.

---
## Na prática, por que atenção foi importante?

Na linguagem humana, muitas interpretações dependem de palavras que estão bastante distantes umas das outras. 

Por exemplo:

> Qual livro a Maria disse que João comprou ontem?

Para responder à pergunta, precisamos perceber que:

> **qual livro**

está relacionado, como complemento, ao verbo

> **comprou**

mesmo havendo várias palavras entre eles.

Nós fazemos isso naturalmente durante a leitura.

Os Transformers foram projetados justamente para tentarem estabelecer esse tipo de relação entre palavras distantes com mais eficiência.

**E ambiguidades?**

Considere a frase:

> A menina carregou o grande livro na mochila mesmo sendo pequena.

Quem era pequena?

- a menina?
- a mochila?

Não existe nenhuma regra simples que responda essa pergunta.

O modelo precisa considerar o restante da frase para decidir qual interpretação parece mais provável.

É justamente esse tipo de problema que o mecanismo de atenção ajuda a resolver.

---
## Como funciona?

Ao processar a palavra

> pequena

o modelo pode atribuir diferentes níveis de atenção às demais palavras da frase.

Por exemplo:

```
A menina carregou o livro na mochila mesmo sendo pequena.

        ↑
     menina

                    ↑
                 mochila

             ↑
           livro
```

Essas relações recebem pesos diferentes durante o processamento.

Palavras mais relevantes exercem maior influência na representação da palavra atual.

---
## Atenção não significa compreensão

Mesmo utilizando atenção, os modelos ainda cometem erros.

Algumas ambiguidades continuam difíceis até mesmo para seres humanos.

Além disso, muitas interpretações dependem de informações que não aparecem no texto.

Por exemplo:

> Maria colocou o grande livro na mochila porque ela era pequena.

Um modelo de linguagem normalmente escolhe a interpretação que parece **mais provável**, considerando os bilhões de exemplos observados durante o treinamento.

Já um ser humano pode utilizar diversas outras fontes de informação, como:

- conhecimento de mundo;
- experiências anteriores;
- contexto da conversa;
- intenções do falante;
- tom do falante.

Em outras palavras, um LLM resolve muitos casos de ambiguidade porque aprendeu padrões estatísticos extremamente complexos da linguagem. Já os seres humanos combinam esses padrões com processos cognitivos mais amplos relacionados à linguagem, percepção, memória, raciocínio, dentre outros.

> 💡 A atenção permite que o modelo relacione palavras distantes e utilize o contexto global da sentença. Isso melhora significativamente a interpretação da linguagem, mas não elimina todas as ambiguidades nem substitui o conhecimento de mundo humano.

---

## O primeiro uso — tradução automática

O Transformer não nasceu para ser um chatbot. Nasceu para **traduzir**.

O problema que motivou o artigo de 2017 era clássico em NLP: dado um texto em inglês, gerar o equivalente em francês. O modelo aprende a fazer isso processando milhões de pares de frases traduzidas — e internamente precisa resolver um problema profundo: palavras em idiomas diferentes não se correspondem uma a uma, a ordem gramatical muda, e o significado de uma palavra frequentemente depende de tokens distantes na frase.

O mecanismo de atenção foi a solução elegante para esse problema. Ao traduzir *"The animal didn't cross the street because it was too tired"*, o modelo precisa saber que *"it"* se refere a *"animal"* e não a *"street"* — algo que só é possível consultando o contexto global da frase inteira, não apenas os tokens adjacentes.

O resultado foi imediato: o Transformer superou todos os modelos anteriores de tradução e se tornou a base do Google Translate moderno.

O que ninguém previu em 2017 é que a mesma arquitetura — com variações — dominaria não apenas tradução, mas linguagem em geral, depois visão computacional, geração de código, estrutura de proteínas e música. A solução para tradução se revelou uma solução geral para *sequências* de qualquer tipo.

> 💡 **Demo ao vivo:** A tradução ainda é uma das formas mais intuitivas de ver um LLM em ação. Abra qualquer chatbot da lista em [[Recursos e Demos#11. Antropomorfização|Recursos: Chatbots]] e peça uma tradução técnica — depois pergunte por que escolheu certas palavras. A resposta vai ilustrar exatamente o mecanismo de atenção contextual que o Transformer resolveu.

---

## BERT e GPT — dois caminhos a partir do Transformer (2018–2019)

A partir da mesma arquitetura, o Google e a OpenAI tomaram direções opostas — e ambas se provaram frutíferas.

### BERT — Google, 2018

> Devlin et al., [*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*](https://arxiv.org/abs/1810.04805) (2018)


O BERT é um modelo **bidirecional**: para prever uma palavra mascarada, ele lê o contexto inteiro — tanto o que vem antes quanto o que vem depois. Isso o torna excelente para tarefas de *compreensão* — classificação, extração de informação, perguntas e respostas.

O BERT quebrou praticamente todos os benchmarks de NLP de 2018 e estabeleceu o paradigma de **pré-treinar e depois fazer fine-tuning** para tarefas específicas.

### GPT-1 e GPT-2 — OpenAI, 2018–2019

> Radford et al., [*Language Models are Unsupervised Multitask Learners*](https://openai.com/research/language-models-are-unsupervised-multitask-learners) (GPT-2, 2019)

O GPT usa apenas a metade *gerativa* do Transformer — processa texto da esquerda para a direita e aprende a prever o próximo token. Isso o torna naturalmente adequado para **geração** de texto.

O GPT-2 (2019, 1,5 bilhão de parâmetros) gerou tal preocupação com desinformação que a OpenAI inicialmente recusou publicar os pesos completos — um momento que marcou o início do debate público sobre riscos de LLMs. O texto que ele gerava era fluente o suficiente para enganar.

| | BERT | GPT |
|---|---|---|
| Direção | Bidirecional | Esquerda → direita |
| Tarefa primária | Compreensão | Geração |
| Treinamento | Mascaramento de tokens | Próximo token |
| Ponto forte | Classificação, QA | Completar texto, diálogo |

> 💡 **Demo ao vivo — tokenização:** O treinamento por "mascaramento de tokens" e "próximo token" só faz sentido quando você vê o que é um token. Use os demos em [[Recursos e Demos#06. Como os LLMs Aprendem — auto-supervisão, tokens e geração|Recursos: Tokenização]] — [Runcell Token Counter](https://www.runcell.dev/tool/token-counter#counter) e [HuggingFace Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) — para mostrar como o mesmo texto é dividido de formas diferentes por diferentes modelos.

---

## GPT-3 — a virada de escala (2020)

> Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020
> [https://arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165)

O GPT-3 não foi apenas maior que o GPT-2 — foi **cem vezes maior**, com 175 bilhões de parâmetros. E a diferença de escala produziu algo qualitativamente diferente.

O fenômeno central foi o **aprendizado em contexto** (*in-context learning*): o modelo conseguia executar tarefas novas simplesmente lendo alguns exemplos no prompt — sem qualquer atualização de pesos, sem fine-tuning. Você mostrava dois ou três exemplos de tradução e ele traduzia. Dois exemplos de código e ele programava.

Isso era emergência em ação: uma capacidade que o GPT-2 não tinha, que não foi treinada explicitamente, e que surgiu da escala.

O artigo tem um subtítulo que define uma era: *"Language models are few-shot learners"* — modelos de linguagem são aprendizes de poucos exemplos. A fronteira entre "modelo" e "sistema que pode ser instruído" começou a se dissolver.

> 💡 **Demo ao vivo — próximo token:** Para ver de perto como o modelo "decide" o que vem a seguir — as distribuições de probabilidade por token — use os demos em [[Recursos e Demos#06. Como os LLMs Aprendem — auto-supervisão, tokens e geração|Recursos: Predição do Próximo Token]]: [Next Token Prediction](https://alonsosilva-nexttokenprediction.hf.space) mostra as probabilidades de cada candidato.

---

## ChatGPT — quando o mundo percebeu (2022)

Em novembro de 2022, a OpenAI lançou o ChatGPT — uma interface de chat construída sobre o GPT-3.5, ajustada com uma técnica chamada **RLHF** (Reinforcement Learning from Human Feedback, que veremos em detalhes na seção [[08 Chatbots]]).

A diferença do ChatGPT para os modelos anteriores não era apenas técnica. Era de **experiência**: uma interface de conversa natural, respostas coerentes e úteis, disponível gratuitamente no navegador.

Em 5 dias, 1 milhão de usuários. Em 2 meses, 100 milhões — o produto de consumo de crescimento mais rápido da história até então.

O que o ChatGPT fez não foi inventar uma tecnologia nova — foi tornar acessível o que já existia em laboratórios. E ao fazer isso, colocou LLMs na agenda de todos: executivos, legisladores, educadores, jornalistas e o público geral.

> *"O GPT-3 mostrou que era possível. O ChatGPT mostrou que era real."*

---

## O que ficou para trás

A história que contamos aqui é a história dos marcos públicos. O que ela não conta:

Décadas de pesquisa em redes neurais recorrentes (RNNs, LSTMs) que estabeleceram as bases. O trabalho de Yoshua Bengio, Geoffrey Hinton e Yann LeCun em aprendizado profundo nos anos 2000 — premiado com o Turing Award em 2018. A infraestrutura de hardware (GPUs da NVIDIA) e de dados (a internet inteira) sem a qual nada disso seria possível.

Os LLMs são o resultado visível de décadas de acumulação invisível. A descontinuidade de 2017–2022 foi real — mas foi construída sobre fundações muito mais antigas.

---

[[Índice]] | [[04 Modelos Fundacionais|← Anterior]] | [[06 Como os LLMs Aprendem|Próximo →]]

[[#05 LLMs — O que são e como surgiram|↑ Topo]]
