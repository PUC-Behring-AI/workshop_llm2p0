# Material do Curso

Conteúdo completo do workshop **"LLM na Prática"** (4 horas).

## Navegando o material

Comece pelo **[Índice Geral](workshop_apresen/Índice.md)** — ele lista todas as seções (12 principais + 01.1, 09.1 e 09.2), a demonstração associada a cada uma e um cronograma de 4 horas.

> Os arquivos são formatados para [Obsidian](https://obsidian.md/). Para abrir o vault: `File → Open Vault → selecione a pasta workshop_apresen/`. Também funcionam em qualquer editor Markdown ou diretamente no GitHub.

## Estrutura

| Pasta / Arquivo | Conteúdo |
|---|---|
| `workshop_apresen/` | Slides do curso em Markdown (15 seções + índice + recursos) |
| `workshop_apresen/figs/` | Imagens e diagramas usados nos slides |
| `workshop_apresen/Recursos e Demos.md` | Links para demos externos usados durante a apresentação |
| `prompt_exemplos/` | 3 versões do prompt "Amigo Botafoguense" — usado no demo ao vivo |
| `codigos_uteis/` | Notebooks e scripts de apoio: guardrails com LLM, DLP determinístico (`guardrail_dlp.py`), agente mínimo com ferramentas (`agente_minimo.py`), resumo de PDF com Tika e demo de injeção de prompt (`resumir_pdf.py` e os PDFs `parecer_limpo`, `parecer_contaminado`, `parecer_contaminado_envio`) |

## Programa resumido

| # | Seção | Tema |
|---|---|---|
| 01 | Apresentação | Visão geral do curso |
| 01.1 | IA Hoje — Agentes e Engenharia | Modelo ≠ produto; ferramentas, laço agêntico, harness |
| 02 | O Que é IA | Definição e taxonomia |
| 03 | Machine Learning | Fundamentos de ML |
| 04 | Modelos Fundacionais | Scale e emergência |
| 05 | LLMs e Como Surgiram | Histórico e contexto |
| 06 | Como os LLMs Aprendem | Auto-supervisão, tokens, geração |
| 07 | Como o Modelo Decide | Temperatura, amostragem, alucinações |
| 08 | Chatbots | Fine-tuning, RLHF, instruction tuning |
| 09 | System Prompt e Guard Rails | Controle e segurança |
| 09.1 | Segurança de Dados em Sistemas de IA | Trajeto do dado, ameaças, defesa em profundidade |
| 09.2 | Soberania da Informação | Residência × soberania, quadro jurídico, espectro de opções |
| 10 | A Influência dos Prompts | Prompt engineering na prática |
| 11 | Antropomorfização | Por que modelos "parecem" conscientes |
| 12 | Demo Integrado e Fechamento | Roteiro dos experimentos (A–G) + reflexão final |
