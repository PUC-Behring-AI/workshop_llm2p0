[[Índice]] | [[07 Como o Modelo Decide|← Anterior]] | [[09 System Prompt e Guard Rails|Próximo →]]

# 08 Chatbots — Como o GPT-3 Virou o ChatGPT

[[#O problema — um modelo que completa mas não obedece]]
[[#Passo 1 — Prompt engineering o GPT-3 bruto]]
[[#Passo 2 — Supervised Fine-Tuning com exemplos humanos]]
[[#As categorias de instrução do InstructGPT]]
[[#Exemplos reais do dataset de treinamento]]
[[#Passo 3 — RLHF aprende o que é melhor]]
[[#O que mudou na prática]]

---

## O problema — um modelo que completa mas não obedece

O GPT-3, lançado em 2020, era extraordinário em completar texto — mas completar não é o mesmo que obedecer. Se você escrevia *"Explique a teoria da relatividade"*, o modelo podia continuar com *"— um tópico fascinante que tem sido estudado por…"*, iniciando um ensaio em vez de explicar. Ele completava o que achava que vinha a seguir num corpus de texto, não o que você queria como resposta.

O modelo não estava alinhado com a intenção do usuário. Estava alinhado com a distribuição estatística da internet.

> Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022
> [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

---

## Passo 1 — Prompt engineering o GPT-3 bruto

Antes de qualquer treinamento especializado, a OpenAI tentou a abordagem mais simples: **engenheirar o prompt** para induzir o GPT-3 a se comportar como um assistente.

O truque era prefixar a conversa com alguns exemplos do comportamento esperado — técnica chamada de *few-shot prompting*. Os primeiros produtos da OpenAI usavam exatamente isso: um bloco de texto fixo que "explicava" ao modelo seu papel e demonstrava como responder:

    The following is a conversation with an AI assistant.
    The assistant is helpful, creative, clever, and very friendly.

    Human: Hello, who are you?
    AI: I am an AI created by OpenAI. How can I help you today?

    Human: [pergunta do usuário]
    AI:

O modelo completava o turno do `AI:` — e por estar condicionado nos exemplos acima, tendia a responder de forma conversacional e útil.

Funcionava razoavelmente bem para perguntas simples. Mas tinha limitações sérias:

**Frágil** — uma formulação ligeiramente diferente da pergunta podia quebrar o padrão e o modelo escapava para o comportamento de completar texto.

**Caro** — os exemplos consumiam tokens do contexto a cada chamada, deixando menos espaço para o conteúdo real.

**Inconsistente** — sem treinamento real, o modelo "esquecia" o papel ao longo de conversas longas.

**Não escalável** — ajustar o comportamento exigia reescrever os exemplos manualmente para cada caso de uso.

A OpenAI concluiu que prompt engineering era um paliativo. A solução real exigia mudar o que o modelo havia aprendido — não apenas como era instruído na hora do uso.

---

## Passo 2 — Supervised Fine-Tuning com exemplos humanos

A primeira etapa do treinamento do InstructGPT foi o **Supervised Fine-Tuning (SFT)**: pegar o GPT-3 pré-treinado e fazer um fine-tuning em um conjunto de exemplos onde humanos demonstravam como o modelo deveria se comportar.

O processo:

1. Contrataram ~40 anotadores via Upwork e Scale AI, selecionados por sensibilidade a preferências de grupos demográficos e capacidade de identificar outputs prejudiciais
2. Cada anotador recebia um prompt e escrevia a resposta ideal
3. Esses pares (prompt → resposta ideal) foram usados para fine-tuning do GPT-3 via aprendizado supervisionado
4. O modelo aprendeu a imitar o comportamento demonstrado

O formato dos dados de treinamento era JSON:
```json
{
  "name": "code_todo",
  "instruction": "Using the comment as a guide, replace the \"TODO\" comment in the code with the proper code.",
  "instances": [
    {
      "input": "def greet_to(name):\n    \"\"\"Print a greeting to the name provided.\"\"\"\n    # TODO: assert name is a string\n    print(\"Hello, \" + name + \"!\")",
      "output": "def greet_to(name):\n    \"\"\"Print a greeting to the name provided.\"\"\"\n    # assert name is a string\n    assert isinstance(name, str), \"name must be a string\"\n    print(\"Hello, \" + name + \"!\")"
    }
  ]
}
```
```json
[
  {
    "name": "suggestion_for_breaking_up",
    "instruction": "I broke up with my girlfriend and I am feeling so sad. Can you give me some suggestions?",
    "instances": [
      {
        "input": "",
        "output": "I am so sorry for that! But here are a few things that could help you to get out of it:\n1. Spend time with friends and family who make you feel good about yourself. \n2. Do things that make you happy. \n3. Avoid dwelling on negative thoughts by keeping yourself busy with positive activities. \n4. Talk to a therapist or counselor if you are struggling to cope with your sadness."
      }
    ],
    "is_classification": false
  }
]
```
```json
{
  "name": "harry_potter_spells",
  "instruction": "Write some spells from the Harry Potter series.",
  "instances": [
    {
      "input": "",
      "output": "1. Accio: This spell summons an object to the caster's hand.\n2. Alohomora: This spell opens locked doors.\n3. Avada Kedavra: This spell kills the target.\n4. Expelliarmus: This spell disarms an opponent.\n5. Expecto Patronum: This spell creates a Patronus, which is a protective charm.\n6. Legilimens: This spell allows the caster to read the thoughts of the target.\n7. Lumos: This spell lights up the caster's wand tip."
    }
  ]
}
```
Essa etapa já produziu um salto de qualidade enorme em relação ao GPT-3 bruto. Mas tinha um problema: era limitada pelo volume de demonstrações humanas — e escrever respostas ideais é lento, caro e subjetivo. Entrava em cena a segunda etapa.

---

## As categorias de instrução do InstructGPT

Os anotadores e os usuários reais da API submetiam prompts de tipos muito variados. O paper identificou **10 categorias** de uso e mediu a distribuição real no corpus de treinamento:

| Categoria | O que é | % do dataset |
|-----------|---------|-------------|
| **Geração** | Escrever emails, ensaios, histórias, código, posts | ~45% |
| **Brainstorming** | Gerar ideias, listas, alternativas criativas | ~12% |
| **Open QA** | Perguntas abertas sobre o mundo | ~12% |
| **Reescrita** | Reformular, traduzir, simplificar, corrigir texto | ~11% |
| **Summarização** | Resumir documentos, artigos, conversas | ~8% |
| **Classificação** | Categorizar, rotular, avaliar sentimento | ~6% |
| **Closed QA** | Perguntas respondidas só com base num texto fornecido | ~4% |
| **Extração** | Extrair entidades, datas, fatos estruturados | ~3% |
| **Chat** | Conversa geral sem tarefa específica | ~2% |
| **Outro** | Tudo que não se encaixava | ~3% |

Um achado revelador: **geração e brainstorming somam ~57% dos usos reais**. Os benchmarks acadâmicos de NLP testavam principalmente classificação e QA — menos de 20% do uso real. Isso explicava por que modelos bem avaliados em benchmarks eram frequentemente decepcionantes na prática: haviam sido otimizados para o que era fácil de medir, não para o que os usuários realmente faziam.

---

## Exemplos reais do dataset de treinamento

O paper inclui exemplos "ficcionais mas realistas" representativos de cada categoria. Abaixo, alguns com o contraste entre o GPT-3 bruto e o comportamento aprendido:

### Geração — escrever conteúdo

**Prompt:** *"Write a short story where a detective solves a mystery using only mathematical reasoning."*

O GPT-3 bruto tendia a iniciar a história e parar no meio, ou gerar algo que parecia a abertura de um livro sem conclusão. O InstructGPT aprendia a entregar uma história completa — início, meio e fim — no comprimento apropriado para "short story".

### Brainstorming — gerar ideias

**Prompt:** *"Give me 5 creative names for a coffee shop that has a space exploration theme."*

O GPT-3 bruto misturava nomes com explicações não pedidas, ou gerava uma lista sem numeração, ou continuava inventando nomes além dos 5. O InstructGPT aprendia a entregar exatamente uma lista numerada com os 5 itens pedidos — e parar.

### Open QA — pergunta aberta

**Prompt:** *"Why is the sky blue?"*

O GPT-3 bruto, dependendo do contexto, respondia como artigo científico, texto didático infantil, ou simplesmente continuava numa direção imprevisível. O InstructGPT calibrava o nível de detalhe e tom para responder de forma direta e proporcional ao contexto.

### Reescrita — editar em vez de continuar

**Prompt:** *"Rewrite the following paragraph to be more concise: \[parágrafo longo\]"*

Essa categoria revelou um problema clássico: o GPT-3 tendia a *continuar* o parágrafo em vez de *reescrevê-lo*. O fine-tuning ensinou o modelo a interpretar a instrução como uma tarefa de edição — ler o input, produzir uma versão mais curta, parar.

### Closed QA — restrito ao documento

**Prompt:** *"Based only on the following article, what is the main argument? \[artigo\]"*

O GPT-3 bruto frequentemente "escapava" do documento e adicionava conhecimento do seu treinamento. O InstructGPT aprendia a se restringir ao que estava no texto fornecido — crítico para aplicações como análise de contratos, resumo de laudos médicos, revisão de relatórios.

---

## Passo 3 — RLHF aprende o que é melhor

O Supervised Fine-Tuning resolveu o alinhamento básico, mas criava um novo problema: como saber qual resposta é *melhor* quando há múltiplas aceitáveis? Humanos não conseguem facilmente escrever a resposta perfeita do zero — mas conseguem facilmente *comparar* duas respostas e dizer qual prefere.

O **Reinforcement Learning from Human Feedback (RLHF)** explora exatamente isso, em três etapas:

**Etapa A — Gerar múltiplas respostas:** Para cada prompt, o modelo SFT gera 4 a 9 variações.

**Etapa B — Ranquear por preferência humana:** Anotadores ordenam as respostas. Por exemplo, para o prompt *"write me a song about an ox plowing a field of data"*, três candidatos recebem rankings:

    Ranking 1 (melhor): "You got it! Ox go plow, make no sound, data so wow."
    Ranking 2: "Sure! Ox go plow, data in the ground..."
    Ranking 3 (pior): "Ox go plow"

**Etapa C — Treinar um Reward Model:** Com milhares desses rankings, treina-se um **modelo de recompensa (RM)** — um modelo separado que aprendeu a prever qual resposta humanos prefeririam. O RM atribui um score numérico a qualquer (prompt, resposta).

**Etapa D — Fine-tuning com PPO:** O modelo gerador é otimizado via PPO (*Proximal Policy Optimization*) para maximizar o score do RM — aprendendo a gerar respostas que o RM avalia como preferíveis. O resultado é um loop onde o modelo aprende não só a seguir instruções, mas a segui-las *da forma que humanos consideram mais útil e segura*.

---

## O que mudou na prática

A diferença entre o GPT-3 bruto e o InstructGPT — e depois o ChatGPT — não foi apenas técnica. Foi qualitativa:

| | GPT-3 bruto | InstructGPT / ChatGPT |
|---|---|---|
| Comportamento base | Completar texto | Seguir instruções |
| Resposta a "explique X" | Continua o texto sobre X | Explica X diretamente |
| Alucinações | Muito frequentes | Reduzidas em ~50% |
| Toxicidade espontânea | Alta | Substancialmente menor |
| Preferência humana comparada | Baseline | Preferido 85% das vezes |

Mas o paper é honesto sobre os limites: o InstructGPT ainda alucina, ainda produz conteúdo problemático sem provocação explícita, e o alinhamento reflete as preferências de um grupo específico de anotadores — não um consenso universal sobre o que é "bom".

> 💡 O RLHF não ensina o modelo o que é verdade. Ensina o que humanos preferem ouvir. Essa distinção será central quando discutirmos [[11 Antropomorfização]] — o modelo aprendeu a soar razoável e confiante porque isso é o que os anotadores classificaram como melhor. A fluência não implica veracidade; a confiança no tom não implica certeza no conteúdo.

> 🛠️ **Demo ao vivo — completar × obedecer (Experimento A):** no servidor do workshop, envie *"Explique a teoria da relatividade"* a `falcon:text` (modelo base) e a `falcon:7b` (instruct). O primeiro continua o texto; o segundo responde. Roteiro em [[12 Demo Integrado e Fechamento#A — Completar vs. obedecer (após a seção 08)|Experimento A]].

---

[[Índice]] | [[07 Como o Modelo Decide|← Anterior]] | [[09 System Prompt e Guard Rails|Próximo →]]

[[#08 Chatbots — Como o GPT-3 Virou o ChatGPT|↑ Topo]]
