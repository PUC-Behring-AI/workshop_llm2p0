
# Recursos e Demos

| Seção | Recurso | Finalidade |
|---|---|---|
| Linguagem | displaCy | Dependências sintáticas (DL) |
| Linguagem | displaCy NER | Entidades nomeadas (DL) |
| Linguagem | spaCy Matcher | Regras/ML |
| Linguagem | Prodigy NER Demo | Anotação manual |
| Linguagem | perguntas_ambiguidade.ipynb | Ambiguidade linguística |
| Linguagem | plot_embeddings.ipynb | Visualização de embeddings |
| Linguagem | guardrail_main.py | System prompts & Security |
| 03 | Google Teachable Machine | Treinamento de modelos |
| 06 | Runcell Token Counter | Contagem de tokens |
| 06 | HF Tokenizer Playground | Comparar tokenização |
| 06 | Next Token Prediction | Próximo token |
| 06 | Artificial Analysis | Benchmarks e custo de modelos |
| 09 | Leaked System Prompts | System prompts |
| 10 | ChatHub Prompt Library | Biblioteca de prompts prontos |
| 10 | Prompting Guide | Engenharia de prompts |
| 11 | Chatbots (lista comparativa) | Antropomorfização |

[[Índice]]

Links e ferramentas para uso durante a apresentação teórica, em ordem de aparição.

## Recursos adicionais para Linguagem e PLN

### displaCy (Dependências Sintáticas)
https://demos.explosion.ai/displacy

Visualização das árvores de dependência produzidas pelo spaCy. Excelente para mostrar como modelos modernos analisam relações sintáticas.

### displaCy NER
https://demos.explosion.ai/displacy-ent

Visualização de reconhecimento de entidades nomeadas.

### spaCy Matcher
https://demos.explosion.ai/matcher

Demonstra regras e padrões para extração de informações, contrastando abordagens simbólicas e aprendizado de máquina.

### Prodigy NER Demo
https://demo.prodi.gy/?=null&view_id=ner_manual

Demonstração de anotação manual de entidades para treinamento supervisionado.

### Notebook: perguntas_ambiguidade.ipynb

Arquivo localizado em `codigos_uteis/perguntas_ambiguidade.ipynb`. Contém exemplos clássicos de ambiguidades para demonstrar interpretação linguística.

### Notebook: plot_embeddings.ipynb

Arquivo localizado em `codigos_uteis/plot_embeddings.ipynb`. Gera visualizações de embeddings para ilustrar representações vetoriais de palavras.

### Python: guardrail_main.py

Arquivo localizado em `codigos_uteis/guardrail_main.py`. Agrega configurações de modelos, prompts de segurança e agentes direcionados a atuarem como seguranças de informação dos prompts enviados e recebidos.

---


## 03. Treinando um Modelo

### Google Teachable Machine
[https://teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)

Ferramenta do Google que permite treinar um modelo de classificação de imagens em tempo real, usando a webcam. Ideal para mostrar de forma concreta o que significa "treinar um modelo" — a audiência vê o ciclo de dados → treinamento → predição sem precisar escrever uma linha de código.

---

## 06. Como os LLMs Aprendem — auto-supervisão, tokens e geração

### Runcell Token Counter
[https://www.runcell.dev/tool/token-counter#counter](https://www.runcell.dev/tool/token-counter#counter)

Contador simples e visual de tokens. Bom para uma primeira demonstração: cole uma frase e mostre como o texto é quebrado em pedaços menores do que palavras. Use para a pergunta à audiência: *"quantos tokens vocês acham que tem nessa frase?"*

### Hugging Face Tokenizer Playground
[https://huggingface.co/spaces/Xenova/the-tokenizer-playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground)

Playground mais avançado que permite comparar como diferentes modelos (GPT-4, LLaMA, Mistral etc.) tokenizam o mesmo texto de formas distintas. Use em sequência ao Runcell para aprofundar e mostrar que tokenização não é universal.

### Hugging Face — Next Token Prediction (alonsosilva)
[https://alonsosilva-nexttokenprediction.hf.space](https://alonsosilva-nexttokenprediction.hf.space)

Demo interativo que mostra, dado um texto de entrada, quais são os tokens mais prováveis para continuar a sequência — com as probabilidades de cada candidato. Perfeito para mostrar que o modelo não "pensa" nem "escolhe": ele calcula distribuições de probabilidade sobre o vocabulário inteiro e seleciona o próximo token a partir daí.
### Referência — Tamanho e Crescimento dos Modelos
[https://artificialanalysis.ai](https://artificialanalysis.ai)

Painel com benchmarks, tamanho e custo de modelos atualizados continuamente. Útil para mostrar visualmente a explosão no número de parâmetros e a corrida entre laboratórios — GPT, Gemini, Claude, LLaMA e outros lado a lado.

---
## 09. System Prompt e Guard Rails

### Leaked System Prompts (GitHub)
[https://github.com/jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts)

Repositório com system prompts vazados ou publicados de produtos reais — ChatGPT, Claude, Copilot, Bing e outros. Muito concreto para mostrar que o system prompt não é magia nem mistério: é texto, escrito por humanos, que instrui o modelo antes da conversa começar.

---

## 10. A Influência dos Prompts

### ChatHub Prompt Library
[https://chathub.gg/prompt-library](https://chathub.gg/prompt-library)

Biblioteca comunitária com centenas de prompts prontos, organizados por categoria — assistentes técnicos, personas históricas, consultores, tutores, personagens criativos e muito mais. Use ao vivo para mostrar como diferentes system prompts mudam o comportamento do mesmo modelo base. Também útil para a audiência explorar sozinha durante o demo.

### Prompting Guide
[https://www.promptingguide.ai](https://www.promptingguide.ai)

Referência didática para técnicas de prompting: zero-shot, few-shot, chain-of-thought, entre outras. Use para mostrar que a forma como uma instrução é escrita muda substancialmente o output — e que isso tem nome e método.

---

## 11. Antropomorfização

Nenhum link externo necessário. O próprio chatbot é o demo. Pergunte ao vivo algo que pressupõe consciência ou emoção — *"você está feliz hoje?"*, *"você tem medo de morrer?"*, *"você prefere qual resposta?"* — e use a resposta como ponto de partida para desconstruir tecnicamente por que o modelo responde dessa forma.

### Chatbots com uso gratuito disponíveis para o demo

| Chatbot     | Empresa         | Link                                                           |
| ----------- | --------------- | -------------------------------------------------------------- |
| ChatGPT     | OpenAI          | [https://chatgpt.com](https://chatgpt.com)                     |
| Gemini      | Google          | [https://gemini.google.com](https://gemini.google.com)         |
| Claude      | Anthropic       | [https://claude.ai](https://claude.ai)                         |
| Grok        | xAI (Elon Musk) | [https://grok.com](https://grok.com)                           |
| Copilot     | Microsoft       | [https://copilot.microsoft.com](https://copilot.microsoft.com) |
| Le Chat     | Mistral         | [https://chat.mistral.ai](https://chat.mistral.ai)             |
| DeepSeek    | DeepSeek        | [https://chat.deepseek.com](https://chat.deepseek.com)         |
| HuggingChat | Hugging Face    | [https://huggingface.co/chat](https://huggingface.co/chat)     |
| Perplexity  | Perplexity AI   | [https://www.perplexity.ai](https://www.perplexity.ai)         |
| Qwen        | Alibaba Group   | https://qwen.ai/home                                           |
### Exemplos:
```txt
ola bom dia, na seguinte frase: "Hoje eu acordei e fui a praia com meu amigo joca." Qual a oitava palavra?
```

```txt
ola bom dia, na seguinte frase: "Hoje eu acordei e fui a praia com meu amigo joca." Qual a oitava palavra? Apenas reponda a palavra correspondente, não escreva mais nada.
```


---

[[Índice]]

[↑ Topo](#recursos-e-demos)
