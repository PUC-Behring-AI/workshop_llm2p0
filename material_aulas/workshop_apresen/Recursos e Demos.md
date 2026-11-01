
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
| 01.1 | agente_minimo.py | Agente com ferramentas, local (Ollama) |
| 01.1 | Building effective agents | Workflows vs. agentes |
| 01.1 | Model Context Protocol | Padrão aberto de conectores |
| 03 | Google Teachable Machine | Treinamento de modelos |
| 06 | Runcell Token Counter | Contagem de tokens |
| 06 | HF Tokenizer Playground | Comparar tokenização |
| 06 | Next Token Prediction | Próximo token |
| 06 | proximo_token.py | Próximo token, local e em português |
| 06 | Transformer Explainer | Transformer passo a passo (GPT-2 no navegador) |
| 06 | LLM Visualization (bbycroft) | Um LLM por dentro, em 3D |
| 06 | Tiktokenizer | Tokens por modelo, com IDs |
| 06 | Embedding Projector | Embeddings em 3D |
| 06 | Artificial Analysis | Benchmarks e custo de modelos |
| 09 | Leaked System Prompts | System prompts |
| 09.1 | guardrail_dlp.py | DLP determinístico (CPF, CNPJ, NF-e) |
| 09.1 | resumir_pdf.py | PDF → Apache Tika → resumo por LLM local; o PDF contaminado tem texto escondido que muda o resultado (prompt injection) |
| 09.1 | The lethal trifecta | Vazamento em agentes |
| 09.1 | OWASP Top 10 for LLM Apps | Catálogo de riscos |
| 09.2 | Ollama (demo local) | Soberania na prática |
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


## 01.1. IA Hoje — Agentes, Ferramentas e Engenharia

### Python: agente_minimo.py
Arquivo localizado em `codigos_uteis/agente_minimo.py`. Agente com *tool calling* em menos de 200 linhas, só biblioteca padrão, rodando 100% local no Ollama (`qwen3:8b`). Dados fictícios. Rode com e sem `--sem-ferramentas` para comparar; o terminal mostra cada pedido do modelo e cada resposta do programa. Requer modelo com suporte a *tools* (`ollama show <modelo>` deve listar `tools` em *Capabilities*).

### Anthropic — Building effective agents
[https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

Texto de referência sobre a distinção entre *workflows* (caminho definido por código) e *agentes* (caminho decidido pelo modelo), e sobre começar pelo mais simples.

### Model Context Protocol
[https://modelcontextprotocol.io](https://modelcontextprotocol.io)

Padrão aberto para conectar assistentes a ferramentas e fontes de dados. Bom para ilustrar como a integração é padronizada — e por que cada conector também é uma nova superfície de risco.

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
### Python: proximo_token.py
Arquivo localizado em `codigos_uteis/proximo_token.py`. **Plano B offline** do Next Token Prediction: mostra os candidatos a próximo token com probabilidades usando modelos do Ollama (modo *raw*, sem molde de chat), inclusive em português. Com `--gerar N --temperatura 1` gera token a token, amostrando — bom para mostrar por que a mesma pergunta dá respostas diferentes e como uma alucinação nasce.

### Sugestões adicionais (links testados em out/2026)

- **Transformer Explainer** — [https://poloclub.github.io/transformer-explainer/](https://poloclub.github.io/transformer-explainer/). O GPT-2 roda no seu navegador; você digita um texto e vê tokenização, embeddings, atenção e a distribuição do próximo token, com a temperatura ajustável. Complementa as seções 06 e 07 (e a "atenção" da 05).
- **LLM Visualization** — [https://bbycroft.net/llm](https://bbycroft.net/llm). Passeio em 3D por um LLM pequeno, camada a camada. Impacta pela escala; use como "olhem quanta coisa há aqui dentro" por 2 minutos.
- **Tiktokenizer** — [https://tiktokenizer.vercel.app](https://tiktokenizer.vercel.app). Mostra tokens **e IDs** para vários modelos; bom complemento ao Playground do Hugging Face.
- **Embedding Projector** — [https://projector.tensorflow.org](https://projector.tensorflow.org). Nuvem 3D de embeddings (Word2Vec etc.) para a parte final da seção 06; combina com o notebook `plot_embeddings.ipynb`.
- **3Blue1Brown — Redes Neurais** — [https://www.3blue1brown.com/topics/neural-networks](https://www.3blue1brown.com/topics/neural-networks). Referência para quem quiser aprofundar depois do workshop (indicação, não demo ao vivo).

### Referência — Tamanho e Crescimento dos Modelos
[https://artificialanalysis.ai](https://artificialanalysis.ai)

Painel com benchmarks, tamanho e custo de modelos atualizados continuamente. Útil para mostrar visualmente a explosão no número de parâmetros e a corrida entre laboratórios — GPT, Gemini, Claude, LLaMA e outros lado a lado.

---
## 09. System Prompt e Guard Rails

### Leaked System Prompts (GitHub)
[https://github.com/jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts)

Repositório com system prompts vazados ou publicados de produtos reais — ChatGPT, Claude, Copilot, Bing e outros. Muito concreto para mostrar que o system prompt não é magia nem mistério: é texto, escrito por humanos, que instrui o modelo antes da conversa começar.

---

## 09.1 / 09.2. Segurança de Dados e Soberania

### Python: guardrail_dlp.py
Arquivo localizado em `codigos_uteis/guardrail_dlp.py`. Detecta e mascara CPF, CNPJ, chave de acesso de NF-e, e-mail e telefone, validando dígitos verificadores. Já integrado a `guardrail_agents.py`. Rode direto (`python guardrail_dlp.py`) para a demonstração. Experimente "enganar" o filtro e discuta por que ele é uma camada, não a solução.

### The lethal trifecta (Simon Willison)
[https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

Explica por que agentes que combinam dados privados, conteúdo não confiável e canal de saída são vulneráveis a vazamento. Use junto ao exercício de classificação de cenários.

### OWASP Top 10 for LLM Applications
[https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/)

Catálogo de riscos de aplicações com LLM (injeção de prompt, divulgação de informação sensível, agência excessiva, cadeia de suprimentos etc.).

### Ollama — o demo como exemplo de soberania
[https://ollama.com](https://ollama.com)

Servidor de inferência local usado no demo. Atividade: desligar o Wi-Fi e continuar conversando com o modelo.

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
