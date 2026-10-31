[[Índice]] | [[01.1 IA Hoje — Agentes e Engenharia|Próximo →]]

# 01 Apresentação

[[#O que esperar deste workshop]]
[[#Como este workshop foi feito]]
[[#Quem somos nós?]]
[[#Por que estou aqui hoje?]]
[[#Vocabulário — As Palavras que a IA Tomou Emprestado]]
[[#O que é um computador?]]
[[#Antes de Começar — Sua Vez de Falar]]
[[#Quebra Gelo — Experimente Agora]]

---

## O que esperar deste workshop

Este é um workshop de **4 horas** em que conceito e prática andam juntos. Não há um bloco só de teoria seguido de um bloco só de demonstrações: sempre que possível, **cada ideia é apresentada e logo em seguida experimentada ao vivo**, com ferramentas na tela, no seu navegador ou rodando na máquina do instrutor.

O ritmo é sempre o mesmo:

> **ideia → demonstração → o que isso significa para o nosso trabalho**

| Quando falarmos de…        | Vamos ver, na prática…                                                          |
| -------------------------- | ------------------------------------------------------------------------------- |
| 🧰 IA hoje: agentes e ferramentas | O mesmo modelo respondendo com e sem ferramentas, passo a passo no terminal |
| 🔤 Tokens                   | Um texto em português sendo dividido por diferentes tokenizadores               |
| 🎲 Próximo token e alucinação | As probabilidades de cada candidato e uma resposta plausível e errada surgindo |
| 🧭 System prompt e guard rails | Um personagem construído só com texto, e as tentativas de fazê-lo "sair do papel" |
| 🔐 Segurança e soberania    | Dados mascarados antes de chegar ao modelo, e um modelo rodando sem internet    |

Não é preciso conhecimento técnico prévio. Vamos construir o entendimento camada por camada — de *"o que é IA"* até *"por que o modelo responde de forma diferente dependendo de como você pergunta"* e *"o que acontece com os dados que eu entrego a ele"*.

As demonstrações foram preparadas especificamente para este workshop. Você vai interagir com um LLM de forma estruturada, ver o efeito de diferentes prompts e entender, na prática, o que cada conceito explica. Em alguns momentos haverá uma pausa maior para você mesmo experimentar; em outros, será só uma olhada de poucos minutos.

> 💡 **Ao final, você deve sair com uma intuição clara** sobre o que esses sistemas fazem, o que eles *não* fazem, e como usá-los sem se iludir sobre o que são.

Três fios atravessam o workshop inteiro:

1. **O motor** — como um LLM funciona por dentro (seções 02–08).
2. **O sistema** — que, hoje, a IA útil é um modelo *mais* ferramentas, dados e engenharia em volta dele ([[01.1 IA Hoje — Agentes e Engenharia]]).
3. **O controle** — o que acontece com os dados que entregamos a esses sistemas, e quem controla a infraestrutura onde eles rodam ([[09.1 Segurança de Dados em Sistemas de IA]] e [[09.2 Soberania da Informação]]).

---

## Como este workshop foi feito

Este workshop é em si um exemplo do que vamos discutir.

**A apresentação e o demo foram construídos com a assistência do Claude** — o modelo de linguagem da Anthropic — como ferramenta de desenvolvimento. Isso incluiu:

- 📝 **Esta apresentação** — estrutura, textos e figuras desenvolvidos em conversa com o Claude, iterando seção por seção
- 💻 **O código do demo interativo** — gerado com o Claude como assistente de programação, revisado e ajustado pelo instrutor
- 🗂️ **Os arquivos Markdown** — formatados e organizados com auxílio do Claude para leitura no Obsidian

Isso não é uma confissão — é um ponto didático intencional.

Usar uma ferramenta de IA para preparar um workshop *sobre* ferramentas de IA cria uma oportunidade única: **você está vendo o produto enquanto aprende sobre o processo**. Ao longo da apresentação, vou apontar momentos em que o comportamento do Claude durante a preparação ilustra exatamente o que estamos discutindo — seus acertos, seus limites, e as decisões que precisaram de julgamento humano.

> *A IA foi o assistente. O workshop é nosso.*
---

## Quem somos nós?

![[talker.png]]

---

## O que é um computador?

Antes de falar de Inteligência Artificial, vale relembrar algo básico — e fácil de esquecer no meio de tanto termo sofisticado: **um computador é, no fundo, uma máquina que calcula 0 e 1.**

Todo processador, por mais moderno que seja, opera sobre **bits** — dígitos binários que só podem valer `0` ou `1`. Fisicamente, isso é implementado como um transistor ligado ou desligado, uma tensão alta ou baixa, um pulso presente ou ausente. Não existe "meio termo": é sempre uma escolha entre dois estados.

- 🔢 **Números** viram sequências de 0s e 1s (binário).
- 🔤 **Texto** vira números, que viram 0s e 1s (codificação, como UTF-8).
- 🖼️ **Imagens, áudio e vídeo** também viram números — e, no fim, 0s e 1s.

Um computador não "entende" letras, cores ou sons. Ele manipula bits em altíssima velocidade, seguindo instruções também escritas em 0 e 1, e o resultado dessa manipulação é reconstruído em algo que faz sentido para nós — uma imagem na tela, um som no alto-falante, uma frase de resposta.

> 💡 *Tudo que um computador "faz" — de uma planilha a um modelo de linguagem gerando texto — é, no nível mais fundamental, uma quantidade absurda de operações com 0 e 1. Isso vai importar quando falarmos sobre o que significa uma IA "pensar" ou "entender".*

Atividade: https://www.advanced-ict.info/interactive/binary.html


---

## Vocabulário — As Palavras que a IA Tomou Emprestado

Antes de entrar nos conceitos técnicos, vale pausar num detalhe que passa despercebido: **o campo de Inteligência Artificial usa, quase inteiramente, palavras emprestadas do vocabulário humano**.

Não são metáforas acidentais. São escolhas deliberadas — e têm consequências. Quando ouvimos essas palavras referidas a uma máquina, algo sutil acontece: o cérebro as processa com as mesmas associações que carregam quando falamos de gente. E aí o terreno começa a escorregar.

Veja os exemplos abaixo. Para cada termo, o significado técnico em IA é radicalmente diferente do significado quando aplicado a um ser humano.

---

### Aprender (*learning*)

**Em IA:** O modelo é exposto a uma quantidade de dados (exemplos) e ajusta seus parâmetros internos (de dezenas a bilhões de números) para minimizar o erro nas suas previsões. Não há compreensão, não há memória persistente, não há curiosidade. É uma operação matemática de otimização.

**Em um humano:** Envolve experiência, emoção, contexto, esquecimento seletivo, generalização criativa, e uma história de vida que dá sentido ao que é aprendido. Aprender muda quem você é.

> *O modelo "aprendeu" a escrever poesia da mesma forma que uma calculadora "aprendeu" a somar: ajustando o que faz até acertar. Nem mais, nem menos.*

---

### Treinar (*training*)

**Em IA:** O processo de passar os dados pelo modelo repetidamente, ajustando os pesos da rede neural a cada iteração. "Treinar" um modelo pode levar horas ou semanas em clusters de GPUs consumindo energia equivalente à de cidades inteiras.

**Em um humano:** Treinar implica esforço, dor, motivação, fracasso, superação. O atleta que treina carrega consigo a experiência de cada sessão. Há intenção, há propósito, há uma narrativa de progresso.

> *Dizer que um modelo foi "treinado" não diz nada sobre o que ele viveu — porque ele não viveu nada.*

---

### Refinar (*fine-tuning*)

**Em IA:** Pegar um modelo já treinado e ajustá-lo com um conjunto menor de dados especializados — para que responda melhor a um domínio específico (medicina, direito, atendimento ao cliente). O modelo não "muda de opinião": ele recalibra probabilidades.

**Em um humano:** Refinar-se é um processo de maturidade. Significa reconhecer falhas, buscar crescimento, integrar críticas ao longo do tempo. É profundamente pessoal e voluntário.

> *Um modelo "refinado" para ser educado não é mais gentil. Ele agora tem maior probabilidade estatística de gerar tokens associados a respostas educadas.*

---

### Destilar (*distillation*)

**Em IA:** Uma técnica em que um modelo menor ("aluno") é treinado para imitar o comportamento de um modelo maior ("professor"), comprimindo o conhecimento em menos parâmetros. O objetivo é eficiência: um modelo menor (mais barato) que se comporta como um grande.

**Em um humano:** Destilar conhecimento é o trabalho de uma vida — ou de gerações. É sintetizar experiências, filtrar o essencial, transmitir sabedoria de forma que transcenda o detalhe e alcance o princípio.

> *A destilação em IA é uma compressão estatística. A destilação humana é uma obra de interpretação e julgamento.*

---

### Aprendizado por Reforço (*Reinforcement Learning / RLHF*)

**Em IA:** O modelo recebe sinais de recompensa baseados em avaliações humanas de suas respostas. Com o tempo, aprende a gerar respostas que maximizam essa recompensa. No caso do RLHF (*Reinforcement Learning from Human Feedback*), avaliadores humanos classificam respostas e esse sinal guia o ajuste do modelo.

**Em um humano:** Aprendizado por reforço é como crescemos. Elogio, punição, consequência, arrependimento — moldamos comportamentos ao longo de anos, com toda a complexidade emocional e moral que isso implica. Há culpa, há orgulho, há valores sendo formados.

> *O RLHF não ensina o modelo a querer agradar. Otimiza os parâmetros para o que os avaliadores classificariam bem. A diferença importa muito.*

---

### Memória (*memory / context window*)

**Em IA:** O modelo não tem memória entre conversas. O que chamamos de "memória" é, na verdade, o contexto atual — o texto visível dentro de uma janela de tokens. Quando a conversa termina, tudo some. Não há reconhecimento, não há saudade, não há continuidade.

**Em um humano:** Memória é identidade. É o fio que conecta quem você foi com quem você é. Inclui emoção, trauma, nostalgia, aprendizado implícito que nem você mesmo sabe que carrega.

---

### Por que isso importa?

Essas palavras criam uma **ilusão de familiaridade**. Quando dizemos que um modelo "aprendeu", "entende" ou "sabe", estamos usando atalhos linguísticos que podem nos enganar sobre o que o sistema realmente faz.

Ao longo deste workshop, vamos tentar usar esses termos com precisão — e sempre que um deles aparecer, vale lembrar: **estamos falando de matemática, não de experiência**.

> 💡 *A IA não aprendeu nada. Ela otimizou. Não treinou nada. Foi calculado parâmetros a partir de dados. Não sente nada. Ela calcula. E entender essa diferença é exatamente o que este workshop propõe.*

---
## EXEMPLO — Como crianças aprendem uma língua?

Uma criança não aprende uma língua apenas repetindo frases que ouviu.

Na verdade, ela frequentemente produz frases que **ninguém nunca lhe ensinou**.

Por exemplo, é comum ouvir crianças dizerem:

> "Eu fazi."

em vez de

> "Eu fiz."

Ou ainda:

> "Eu sabi."

em vez de

> "Eu soube."

Essas formas estão erradas para um adulto, mas revelam algo extremamente importante:

A criança **não está apenas imitando**.

Ela percebeu um padrão presente na língua.

Por exemplo:

```
comer  → comi

abrir  → abri

partir → parti

fazer  → fazi
```

Ela criou uma hipótese sobre a língua:

> "Para formar o passado na primeira pessoa, basta substituir a terminação do verbo."

Essa hipótese funciona para muitos verbos, mas não para todos. Como **fazer** é um verbo irregular, a criança produz uma forma inexistente na língua adulta.

Curiosamente, esse tipo de erro é considerado um sinal positivo do desenvolvimento linguístico, pois mostra que a criança está **generalizando regras**, e não apenas repetindo frases que ouviu. Ao longo do tempo, com novas experiências linguísticas, ela revisa suas hipóteses até chegar às formas utilizadas pelos adultos.[1]

---

## E uma IA?

Modelos de linguagem também identificam padrões em grandes quantidades de texto.

Mas existe uma diferença importante.

Uma criança pode produzir espontaneamente uma forma que nunca ouviu porque está construindo hipóteses sobre como a língua funciona.

Já um LLM não formula hipóteses explícitas sobre regras gramaticais.

Ele ajusta bilhões de parâmetros para reproduzir regularidades estatísticas observadas durante o treinamento.

Se uma determinada forma nunca apareceu nos dados, ou apareceu muito pouco, o modelo simplesmente terá pouca evidência para produzi-la.

Ele não "descobre" novas regras da mesma maneira que uma criança.

Em outras palavras:

> Uma criança cria hipóteses sobre a gramática e aprende gradualmente suas exceções.

> Um modelo estatístico aprende probabilidades e tenta reproduzir os padrões mais prováveis.

Essa diferença ajuda a entender por que devemos tomar cuidado ao usar palavras como **"aprender"** para descrever sistemas de IA.


[^1]: **KENEDY, Eduardo. _Curso básico de linguística gerativa_. São Paulo: Editora Contexto, 2024.**

---
## Antes de Começar — Sua Vez de Falar

Antes de mergulharmos na teoria, abrir espaço para ouvir os participantes. Sem resposta certa ou errada — o objetivo é calibrar expectativas e criar um ponto de partida honesto para as próximas quatro horas.

**Perguntas para discussão com o grupo:**

1. O que você espera aprender hoje? Qual pergunta você mais quer ver respondida ao final?
2. Você acha que já usa IA no seu dia a dia? Com que frequência e para quê?
3. Você tem algum receio em relação à IA? O que te preocupa?
4. Onde você se coloca no espectro entre cético total e entusiasta convicto?
5. Tem algo que você definitivamente *não* quer que este workshop seja?
6. Que tipo de informação do seu trabalho você já colou (ou colaria) num chatbot? Existe regra clara sobre isso no seu órgão?

---

## Quebra Gelo — Experimente Agora

Enquanto as apresentações acontecem, os participantes podem abrir um dos chatbots abaixo e começar a explorar. Todos têm acesso gratuito — basta ter uma conta ou criar uma na hora.

| Chatbot    | Empresa       | Link                                                   |
| ---------- | ------------- | ------------------------------------------------------ |
| ChatGPT    | OpenAI        | [chatgpt.com](https://chatgpt.com)                     |
| Gemini     | Google        | [gemini.google.com](https://gemini.google.com)         |
| Claude     | Anthropic     | [claude.ai](https://claude.ai)                         |
| Grok       | xAI           | [grok.com](https://grok.com)                           |
| Copilot    | Microsoft     | [copilot.microsoft.com](https://copilot.microsoft.com) |
| Le Chat    | Mistral       | [chat.mistral.ai](https://chat.mistral.ai)             |
| DeepSeek   | DeepSeek      | [chat.deepseek.com](https://chat.deepseek.com)         |
| Perplexity | Perplexity AI | [perplexity.ai](https://www.perplexity.ai)             |
| Qwen       | Alibaba Group | https://qwen.ai/home                                   |

> ⚠️ **Regra de ouro do workshop: use apenas dados públicos ou fictícios.** Estes são serviços de terceiros, em contas pessoais, sob termos que você não negociou. Nada de informação de contribuintes, processos, dados pessoais ou qualquer material sigiloso — nem "só para testar". Por que isso importa tanto será o tema de [[09.1 Segurança de Dados em Sistemas de IA]].

> 💡 **Sugestão de primeiro teste:** Faça a mesma pergunta em dois chatbots diferentes e compare as respostas. Isso por si só já revela muito sobre como esses sistemas funcionam — e sobre o que eles *não* são.

---

[[Índice]] | [[01.1 IA Hoje — Agentes e Engenharia|Próximo →]]

[[#01 Apresentação|↑ Topo]]
