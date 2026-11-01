[[Índice]] | [[05 LLMs e Como Surgiram|← Anterior]] | [[07 Como o Modelo Decide|Próximo →]]

# 06 Como os LLMs Aprendem

[[#Aprendizado supervisionado vs auto-supervisionado]]
[[#Next Token Prediction — o caminho do GPT]]
[[#Masked Language Modeling — o caminho do BERT]]
[[#Por que isso permite escalar sem rótulos humanos]]
[[#Tokenização — as unidades do aprendizado]]
[[#Completando palavras — geração token a token]]

---

## Aprendizado supervisionado vs auto-supervisionado

No aprendizado supervisionado clássico, cada exemplo de treinamento precisa de um **rótulo** produzido por um humano: esta foto é um gato, este e-mail é spam, este tumor é maligno. O rótulo é o sinal que guia o modelo — sem ele, não há aprendizado.

Isso funciona bem em escala pequena. Mas para treinar um modelo sobre toda a linguagem humana — bilhões de documentos, dezenas de idiomas, código, ciência, literatura — seria necessário um exército de anotadores trabalhando por décadas. O custo é proibitivo.

O **aprendizado auto-supervisionado** contorna esse problema com uma ideia elegante:

> *O próprio texto é o rótulo.*

Não é necessário nenhum trabalho humano de anotação. O sinal de treinamento está escondido dentro dos dados — basta saber onde procurar.

---

## Next Token Prediction — o caminho do GPT

A estratégia do GPT é direta: **ocultar o fim da sequência e pedir ao modelo que o preveja**.

Dado o texto:

```
A Torre Eiffel fica em ___
```

O modelo deve prever: `Paris`. Dado:

```
Paris é a capital da ___
```

Deve prever: `França`. E assim por diante, sobre trilhões de sequências.

A cada previsão, o modelo compara sua resposta com a resposta correta (que estava no texto original) e ajusta seus pesos na direção certa. Sem nenhum rótulo externo — o próprio corpus é o professor.

O resultado é um modelo que internalizou uma enorme quantidade de estrutura sobre linguagem, fatos, relações e raciocínio — não porque foi ensinado explicitamente sobre esses tópicos, mas porque prever bem o próximo token *exige* modelar tudo isso.

---

## Masked Language Modeling — o caminho do BERT

O BERT usa uma variação: em vez de prever o que vem *depois*, ele **mascara palavras no meio da sequência** e pede ao modelo que as recupere a partir do contexto bidirecional.

Dado:

```
A Torre Eiffel fica em [MASK], capital da França.
```

O modelo deve prever: `Paris` — mas agora pode usar tanto o que vem antes quanto o que vem depois do token mascarado.

Isso força o modelo a construir representações ricas de significado contextual, o que o torna excelente para tarefas de *compreensão*. A desvantagem é que o modelo bidirecional não gera texto de forma natural — ele não foi treinado para escrever, mas para entender.

| | Next Token Prediction | Masked Language Modeling |
|---|---|---|
| Modelo | GPT | BERT |
| O que é ocultado | O fim da sequência | Tokens aleatórios no meio |
| Direção de leitura | Esquerda → direita | Bidirecional |
| Ponto forte | Geração de texto | Compreensão e classificação |

---

## Por que isso permite escalar sem rótulos humanos

A consequência prática é enorme. Todo texto que já foi escrito — livros, artigos, código, fóruns, notícias, legislação, receitas, enciclopédias — se torna automaticamente dado de treinamento, sem custo adicional de anotação.

A internet inteira é um conjunto de treinamento auto-supervisionado.

Isso explica a trajetória de escala dos LLMs. O GPT-2 foi treinado em ~40 GB de texto. O GPT-3 em ~570 GB. Modelos posteriores ultrapassaram trilhões de tokens. Cada incremento foi possível porque não havia gargalo humano no processo de anotação — bastava coletar mais texto e mais GPUs.

O aprendizado auto-supervisionado transformou um problema de *custo de anotação* num problema de *custo computacional*. E o custo computacional, diferente do custo humano, escala com dinheiro e hardware.

---

## Tokenização — as unidades do aprendizado

Antes de qualquer aprendizado, o texto precisa ser convertido numa forma que o modelo possa processar: uma sequência de números. Esse processo é a **tokenização**.

Um token não é necessariamente uma palavra. É um fragmento de texto — pode ser uma palavra inteira, uma sílaba, um prefixo, um sufixo, ou até um único caractere. A granularidade depende do algoritmo de tokenização e do vocabulário do modelo.

Por exemplo, a frase `"tokenização"` pode ser dividida como:

```
["token", "iza", "ção"]  →  [15432, 7891, 234]
```

Cada fragmento recebe um número inteiro — seu ID no vocabulário do modelo. É sobre essa sequência de IDs que todo o aprendizado acontece.

Algumas consequências não óbvias da tokenização:

**Palavras raras ou técnicas são divididas em mais tokens** — e portanto "custam mais" ao modelo processar e gerar. Uma palavra comum em inglês é frequentemente 1 token; uma palavra técnica em português pode ser 3 ou 4.

**O modelo não vê letras, vê tokens** — erros de ortografia, variações de capitalização e palavras compostas podem ser tokenizados de formas inesperadas, afetando o comportamento do modelo.

**Idiomas diferentes têm eficiências diferentes** — modelos treinados majoritariamente em inglês tokenizam inglês de forma mais compacta do que outros idiomas. Um texto em português pode exigir 20–30% mais tokens do que o equivalente em inglês.

**Números e código têm tokenizações próprias** — `12345` pode virar `["123", "45"]` dependendo do modelo, o que explica parte da dificuldade de LLMs com aritmética.

> 🛠️ **Demo — faça agora:**
>
> ** [HuggingFace Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground)** — escolha diferentes modelos (GPT-4, LLaMA, Mistral) e veja como o mesmo texto é dividido de formas distintas. Tente palavras técnicas, números, emojis e código.
>
> *Pergunta para a audiência: quantos tokens vocês acham que tem a frase "Inteligência Artificial Generativa"?*
>
> 🧪 **Experimento sugerido:** cole o mesmo trecho de uma norma tributária em português e uma tradução em inglês, com o tokenizador do GPT-4 e depois com o de outro modelo. O português gasta mais tokens? Quanto? (Tokens são a unidade de **custo e de limite de contexto** — o mesmo texto custa mais ou menos conforme o idioma e o modelo.) Confira o número com os seus próprios textos antes de citar a regra de "20–30%".
>
> 🔐 **Nota de privacidade:** o Tokenizer Playground diz executar *localmente no navegador*  mas, por regra do workshop, cole **apenas texto público ou fictício** em qualquer site.

---
# Tokens não são palavras e nem necessariamente possuem significado linguístico

## O que é uma palavra?

Para nós, falantes de português, a palavra

> infelizmente

é uma palavra com significado relativamente claro, composto por uma raiz *feliz* e morfemas derivacionais.

in + feliz + mente

Mas um sistema computacional pode representá-la de várias maneiras e não necessariamente precisa se adequar aos morfemas reais da língua.

---

## Primeira possibilidade

O tokenizador pode armazenar:

```

infelizmente

```

como um único token.

Nesse caso, basta um símbolo para representar toda a palavra.

---

## Segunda possibilidade

Ele também pode quebrá-la em partes:

```

infeliz

mente

```

Agora temos dois tokens.

Curiosamente, essas partes fazem sentido para nós:

- infeliz = contrário de feliz, visto que possui os morfemas in (contrário) + feliz (radical)
- mente = transforma a palavra em advérbio de modo

---
## Terceira possibilidade

Dependendo do tokenizador, a divisão pode ser completamente diferente:

```

inf

eliz

mente

```


Não existe uma única resposta correta.

Cada modelo utiliza seu próprio vocabulário de tokens. Exemplo:

![[Pasted image 20260710151251.png]]

---
## Pergunta

Isso significa que o computador conhece:

- prefixos?
- sufixos?
- morfemas?

A resposta é:

# Não exatamente.

---
## Como o tokenizador decide?

O objetivo do tokenizador **não é fazer análise linguística**.

Ele procura divisões que sejam eficientes para representar grandes quantidades de texto, muitas vezes com base em frequência.

Isso significa que uma divisão útil para o modelo pode não coincidir com aquilo que aprendemos nas aulas de Português.

Portanto, um token pode coincidir com um morfema da língua, mas apenas porque a distribuição de sequência de caracteres analisados pelo sistema computacional culminou naquele padrão sequencial.

---
## Comparando Linguística e IA

| Linguística | Tokenizador |
|-------------|-------------|
| procura estrutura da língua | procura eficiência estatística |
| morfemas possuem significado | tokens não precisam possuir significado |
| regras linguísticas | frequência em grandes corpora |

---
## Um exemplo

Observe:

```

cachorros

```

Na Linguística podemos analisar:

```

cachorr

o

s

```

(radical + vogal temática + plural)

Já um tokenizador pode produzir:

```

cachorros

```

ou

```

cachorro

s

```

ou

```

cach

orros

```

Todas essas divisões podem funcionar.

---
## Então por que usar tokens?

Porque eles permitem representar praticamente qualquer texto.

Mesmo palavras muito raras podem ser formadas pela combinação de tokens menores.

Isso evita que o modelo precise memorizar milhões de palavras completas.

Portanto,
Quando dizemos que um LLM prevê o "próximo token", isso **NÃO** significa que ele prevê a próxima palavra.
**Na prática, ele prevê pedaços de texto, conjuntos de caracteres.**

---
# A questão da eficiência

E por que conjuntos, e não caracteres únicos?

A resposta está no custo computacional.

### Uma palavra por símbolo?

Imagine que o modelo tivesse um símbolo diferente para cada palavra da língua portuguesa.

Teríamos símbolos distintos para:

- gato
- gata
- gatos
- gatas
- gatinho
- gatinha
- gatões
- gatinhas

E o mesmo aconteceria para milhões de outras palavras.

Além disso, sempre surgem palavras novas:

- nomes próprios;
- gírias;
- abreviações;
- neologismos;
- palavras de outros idiomas.

O vocabulário precisaria crescer continuamente, tornando o modelo muito maior e mais caro de treinar.
### Um caractere por símbolo?

Podemos pensar no extremo oposto.

E se cada símbolo fosse apenas um caractere?

```
g
a
t
o
```

Agora qualquer palavra poderia ser construída.

Mas surge outro problema.

Uma palavra simples como

```
computador
```

seria dividida em:

```
c
o
m
p
u
t
a
d
o
r
```

O modelo precisaria prever um caractere de cada vez.

As sequências ficariam muito maiores, tornando o treinamento e a geração de texto muito mais lentos.

Além disso, seria muito mais difícil aprender padrões linguísticos, já que palavras e partes de palavras seriam "quebradas" em unidades muito pequenas.
### Tokens: um meio-termo

Os modelos modernos, de modo geral, optam por um equilíbrio entre ambas as perspectivas.

> 💡 **Resumo:** Os tokens representam um equilíbrio entre flexibilidade e eficiência. Palavras inteiras exigiriam um vocabulário enorme; caracteres individuais produziriam sequências muito longas. Os tokens ficam exatamente no meio desses dois extremos, permitindo que os modelos representem a linguagem de forma eficiente sem perder capacidade de generalização.

---
## Completando palavras — geração token a token

Quando um LLM gera texto, ele não produz a resposta inteira de uma vez. Ele a constrói **um token por vez**, de forma autorregressiva:

1. Recebe a sequência de tokens até o momento
2. Calcula a distribuição de probabilidade sobre todos os tokens do vocabulário
3. Seleciona o próximo token (por argmax ou amostragem)
4. Acrescenta esse token à sequência
5. Repete — agora com a sequência um token mais longa

É por isso que os chatbots "escrevem" na sua frente em tempo real: cada token que aparece na tela é uma iteração desse ciclo. O modelo não estava "pensando" e depois "digitou" — ele foi construindo a resposta token a token, cada escolha condicionada em tudo que veio antes.

Isso tem uma implicação importante: **o modelo não pode "corrigir" um token que já emitiu**. Uma vez que um token foi gerado, ele entra no contexto e influencia todos os tokens seguintes. Se o modelo "errou" cedo numa resposta, os tokens seguintes foram condicionados nesse erro — o que pode amplificar o problema em vez de corrigi-lo.

Esse mecanismo também explica por que **o prompt importa tanto**: os tokens do prompt são o contexto inicial sobre o qual toda a geração é condicionada. Mudar uma palavra no prompt pode mudar completamente a direção da resposta — porque muda a distribuição de probabilidade do primeiro token gerado, que muda a do segundo, e assim por diante.

> 🛠️ **Demo — faça agora:**
>
> **1. [Next Token Prediction](https://alonsosilva-nexttokenprediction.hf.space)** — veja ao vivo as probabilidades dos candidatos ao próximo token para qualquer sequência que você digitar. *(Usa o GPT-2 de 124M parâmetros: ótimo para inglês, fraco em português. É um Space gratuito do Hugging Face — pode estar lento ou "dormindo" na hora; abra com antecedência.)*
>
> **2. Plano B local, em português — [`proximo_token.py`](../codigos_uteis/proximo_token.py)** — mesma ideia, usando os modelos do Ollama, sem internet. Exemplos: `python proximo_token.py "A capital do Brasil é"` e `python proximo_token.py --gerar 12 --temperatura 1 "O ICMS é um imposto"`. Rode algumas vezes com temperatura 1: em algum momento o modelo vai completar com algo **plausível e errado** (por exemplo, "O ICMS é um imposto *federal*" — ele é estadual). É a alucinação da seção [[07 Como o Modelo Decide]] acontecendo diante dos olhos da turma.


---
# Como computadores representam palavras?

---
## Até agora...

Aprendemos que modelos transformam textos em tokens.

Mas surge uma nova pergunta:

> Como representar o significado desses tokens?

Isso é feito através de valores numéricos atribuídos aos tokens: os **embeddings**

---
# Palavras diferentes...

Observe estas palavras:

• cachorro

• dog

• perro

• 犬

São escritas de maneiras completamente diferentes.

Mesmo assim, todas se referem aproximadamente ao mesmo conceito.

Como um sistema computacional percebe essa relação?

---
# A ideia principal

Os modelos de linguagem transformam cada token em um conjunto de números.

Esses conjuntos de números são chamados de **embeddings**.

Podemos imaginar um embedding como uma coordenada em um enorme mapa.

Palavras usadas em contextos parecidos acabam ficando próximas nesse mapa.

---
# Um mapa imaginário

Imagine um mapa onde palavras semelhantes aparecem próximas.

```
                gato

         cachorro

hamster


        leão
```

Animais aparecem agrupados.

Já palavras relacionadas à realeza aparecem em outro lugar.

```
            rei

        rainha

 príncipe

 princesa
```

Essas posições não foram definidas por especialistas.

Elas foram aprendidas automaticamente durante o treinamento.

Veja esse exemplo:

![[Pasted image 20260710160157.png]]

---
# O computador conhece significados?

Não exatamente.

O computador aprende que certas palavras aparecem em contextos semelhantes.

Por exemplo:

"O cachorro latiu."

"O gato miou."

Como essas palavras aparecem em contextos linguísticos parecidos, seus embeddings tendem a ficar próximos.

> "Palavras usadas em contextos semelhantes tendem a possuir significados semelhantes."

---
# Atenção!

Embeddings NÃO são dicionários.

Eles não armazenam definições.

Também não representam "o verdadeiro significado" das palavras.

Eles representam padrões aprendidos a partir do uso da linguagem.

---
# Para pensar

Para computadores palavras podem ser representadas como pontos em um espaço derivados de contextos semelhantes,
mas como seres humanos aprendem os significados de palavras?


[[Índice]] | [[05 LLMs e Como Surgiram|← Anterior]] | [[07 Como o Modelo Decide|Próximo →]]

[[#06 Como os LLMs Aprendem|↑ Topo]]
