# Workshop LLM — Índice Geral

> **Duração total:** 4 horas — conceito e prática **misturados**: cada ideia é seguida, quando possível, de uma demonstração ao vivo.

---

## Seções

| #    | Seção                                                     | Demonstração associada                                 |
| ---- | --------------------------------------------------------- | ------------------------------------------------------ |
| 01   | [[01 Apresentação]]                                       | Quebra-gelo: mesma pergunta em dois chatbots (dados públicos) |
| 01.1 | [[01.1 IA Hoje — Agentes e Engenharia]]                   | Atividade “pergunte ao chatbot” + `agente_minimo.py` com e sem ferramentas (Exp. D) |
| 02.1 | [[02.1 O Que é IA]]                                       | displaCy (opcional)                                    |
| 02.2 | [[02.2 Appendix O que é Linguagem Natural]]               | Apêndice — leitura                                     |
| 03   | [[03 Machine Learning]]                                   | Teachable Machine (opcional)                           |
| 04   | [[04 Modelos Fundacionais]]                               | —                                                      |
| 05   | [[05 LLMs e Como Surgiram]]                               | —                                                      |
| 06   | [[06 Como os LLMs Aprendem]]                              | Tokenizadores; `proximo_token.py`                      |
| 07   | [[07 Como o Modelo Decide]]                               | Temperatura 1 e alucinação (`proximo_token.py --gerar`)|
| 08   | [[08 Chatbots]]                                           | Completar × obedecer: `falcon:text` × `falcon:7b` (Exp. A) |
| 09   | [[09 System Prompt e Guard Rails]]                        | Amigo Botafoguense V0→V2 e testes (Exp. B e C)         |
| 09.1 | [[09.1 Segurança de Dados em Sistemas de IA]]             | DLP e injeção; exercício dos cenários (Exp. E)         |
| 09.2 | [[09.2 Soberania da Informação]]                          | Teste do Wi-Fi (Exp. F)                                |
| 10   | [[10 Influência dos Prompts]]                             | Um jailbreak histórico; persona própria (Exp. G, opcional) |
| 11   | [[11 Antropomorfização]]                                  | Pergunta de "sentimento" a um chatbot                  |
| 12   | [[12 Demo Integrado e Fechamento]]                        | Roteiro dos experimentos + reflexão final              |

> 🛠️ O servidor do workshop (sandbox e arena, rede local): [abrir](http://0.0.0.0:8000).

---

## Sugestão de cronograma (4 h)

Proposta para este público (gestores e cientistas de dados); ajuste conforme a turma. As seções de base (02–05) são **comprimidas** para dar espaço ao que mais importa aqui: 01.1, 06, 09, 09.1 e 09.2. Cada linha já inclui a demonstração.

| Bloco | Conceito + demonstração | Tempo | Acumulado |
|---|---|---|---|
| 1 | **Abertura** (01) — quebra-gelo só com dados públicos/fictícios | 10 min | 10 |
| 2 | **IA hoje** (01.1) — atividade “pergunte ao chatbot” (≈ 10 min) + agente mínimo com e sem ferramentas | 30 min | 40 |
| 3 | **Fundamentos** (02.1, 03, 04, 05) — só o fio condutor; 02.2 é leitura | 15 min | 55 |
| 4 | **Tokens e próximo token** (06) + tokenizadores e `proximo_token.py` | 25 min | 80 |
| 5 | **Como o modelo "decide"** (07) + temperatura 1 e alucinação ao vivo | 15 min | 95 |
| — | *Intervalo* | 10 min | 105 |
| 6 | **Chatbots** (08) + completar × obedecer (Exp. A) | 15 min | 120 |
| 7 | **System prompt e guard rails** (09) + Botafoguense V0→V2 e testes (Exp. B, C) | 30 min | 150 |
| 8 | **Segurança de dados** (09.1) + DLP, injeção, cenários (Exp. E) | 30 min | 180 |
| 9 | **Soberania** (09.2) + teste do Wi-Fi (Exp. F) | 25 min | 205 |
| 10 | **Prompts e antropomorfização** (10, 11) — um jailbreak e um caso; resto é leitura | 15 min | 220 |
| 11 | **Fechamento** (12) — reflexão final | 15 min | 235 |
| — | *Folga* | 5 min | 240 |

> ⚠️ Cronograma apertado. Se atrasar, os candidatos a corte são: casos de dano da seção 11 (deixar como leitura), o Exp. C e o Exp. G (tarefa para casa). **Preserve** A, E e F — são os que conectam com o público.
>
> 💡 Intervalo no meio do dia (após o bloco 5), quando a parte de "como funciona por dentro" termina e começa a de "controle e segurança".

---

## Recursos e Referências

| Tipo | Arquivo |
|------|---------|
| Links e demos para uso em sala | [[Recursos e Demos]] |
| Prompts do demo — Amigo Botafoguense (3 versões) | [[Demo Prompts — Amigo Botafoguense]] |
| Agente mínimo com ferramentas (local) | `codigos_uteis/agente_minimo.py` |
| Próximo token, local e em português | `codigos_uteis/proximo_token.py` |
| DLP determinístico (CPF, CNPJ, NF-e…) | `codigos_uteis/guardrail_dlp.py` |

---

*Navegue pelos links acima para acessar cada seção. Todos os arquivos estão na mesma pasta. Imagens em `figs/`.*
