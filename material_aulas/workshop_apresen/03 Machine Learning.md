[[Índice]] | [[02.1 O Que é IA|← Anterior]] | [[04 Modelos Fundacionais|Próximo →]]

# 03 Machine Learning

[[#A pergunta central]]
[[#Programação tradicional vs aprendizado de máquina]]
[[#O que significa aprender]]
[[#Tipos de aprendizado]]
[[#Como o modelo aprende — a intuição do gradiente]]

---

## A pergunta central

Antes de definir Machine Learning, vale fazer uma pergunta:

> *Como você reconhece um gato?*

Você não consulta uma lista de regras. Você já viu gatos. Muitos. E seu cérebro aprendeu — a partir de exemplos — o que é e o que não é um gato.

Machine Learning é a ideia de que computadores podem fazer o mesmo: **aprender a partir de exemplos**, sem que ninguém escreva explicitamente as regras.

---

## Programação tradicional vs aprendizado de máquina

Na programação tradicional, o programador escreve as regras. O computador aplica essas regras aos dados e produz respostas.

```
Dados + Regras → Respostas
```

No aprendizado de máquina, a lógica se inverte. Você fornece os dados *e* as respostas corretas. O sistema descobre as regras sozinho.

```
Dados + Respostas → Regras (= o modelo)
```

Isso muda tudo. Tarefas que seriam impossíveis de programar manualmente — reconhecer faces, traduzir idiomas, detectar tumores em imagens — tornam-se tratáveis quando há dados suficientes.

---

## O que significa aprender

No coração de qualquer sistema de ML existe uma **equação probabilística**:

$$\arg\max_X \; P(X \mid y_1, y_2, \ldots, y_n)$$

Leia assim:

> *Encontre o X que tem a maior probabilidade de ocorrer, dado que observamos $y_1, y_2, \ldots, y_n$.*

Em termos concretos: dado o que você sabe (os dados observados $y_i$), qual é a explicação mais provável ($X$)?

Alguns exemplos de como isso se aplica:

| Contexto | Os $y_i$ (observações) | O $X$ procurado |
|----------|------------------------|-----------------|
| Detector de spam | Palavras do e-mail | É spam ou não? |
| Diagnóstico médico | Sintomas do paciente | Qual doença? |
| Completar texto | Palavras anteriores | Qual palavra vem a seguir? |
| Reconhecimento de voz | Sinal de áudio | Qual palavra foi dita? |

> 💡 O exemplo Completar texto — *"dado o que veio antes, qual palavra vem a seguir?"* — é exatamente o que um LLM faz. Voltaremos a isso com profundidade nas seções [[06 Como os LLMs Aprendem#Tokenização — as unidades do aprendizado|06 — Tokenização]] e [[06 Como os LLMs Aprendem#Completando palavras — geração token a token|06 — Próximo Token]].

---

## Tipos de aprendizado

![[figs/tipos_aprendizado.svg|656]]

Os três tipos diferem em *como* os dados de treinamento são fornecidos:

No **aprendizado supervisionado**, cada exemplo vem com a resposta correta — o rótulo. O modelo aprende a mapear entradas para saídas a partir desses pares. É o tipo mais comum: classificação de e-mails, previsão de preços, diagnóstico por imagem.

No **aprendizado não-supervisionado**, os dados não têm rótulos. O modelo descobre estrutura por conta própria — grupos naturais, compressões, anomalias. Útil quando não sabemos de antemão quais categorias existem.

No **aprendizado por reforço**, o modelo aprende através de interação com um ambiente: toma ações, recebe recompensas ou penalidades, e ajusta seu comportamento. É o paradigma por trás de sistemas como o AlphaGo e de parte do treinamento dos LLMs modernos — voltaremos a isso na seção [[08 Chatbots]].

---

## Como o modelo aprende — a intuição do gradiente

Imagine que você está atirando flechas em um alvo, mas há um **vento** que você não vê e não sabe medir. Você mira, atira, e observa **quanto o vento desviou a flecha** do centro. Então corrige a mira na direção contrária ao desvio e atira de novo. Vê o novo desvio, corrige de novo. Com o tempo, as flechas passam a cair cada vez mais perto do centro — sem que você precise saber a força do vento, só **medir o erro e corrigir**.

Esse é o processo básico de treinamento em ML:

1. **Previsão** — o modelo recebe uma entrada e produz uma saída
2. **Erro** — compara-se a saída com a resposta correta através de uma *função de perda* (*loss function*), que mede o quão longe o modelo está
3. **Ajuste** — calcula-se o *gradiente* — a direção em que os parâmetros do modelo devem se mover para reduzir o erro
4. **Repetição** — repete-se com milhões de exemplos, até o erro convergir

O gradiente é como uma bússola que aponta na direção do erro crescente. Movendo-se na direção *oposta* ao gradiente (*descida do gradiente*), o modelo encontra progressivamente configurações de parâmetros que erram menos.

> 🛠️ **Demo:** [https://teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/) — veja esse ciclo acontecendo em tempo real, com a sua webcam como dado de entrada.

---

[[Índice]] | [[02.1 O Que é IA|← Anterior]] | [[04 Modelos Fundacionais|Próximo →]]

[[#03 Machine Learning|↑ Topo]]
