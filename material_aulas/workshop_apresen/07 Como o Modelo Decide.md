[[Índice]] | [[06 Como os LLMs Aprendem|← Anterior]] | [[08 Chatbots|Próximo →]]

# 07 Como o Modelo "Decide"

[[#O modelo não escolhe — ele amostra]]
[[#Temperatura — do determinístico ao caótico]]
[[#Alucinações — por que o modelo inventa fatos]]
[[#O modelo não sabe o que não sabe]]
[[#Implicações práticas]]

---

## O modelo não escolhe — ele amostra

A cada passo de geração, o modelo produz uma lista com todos os tokens do seu vocabulário — tipicamente 50 mil a 100 mil itens — e atribui a cada um uma pontuação que reflete o quanto aquele token é provável dado o contexto atual. Essas pontuações são convertidas em probabilidades: números entre 0 e 1 que somam 1.

O modelo então **sorteia** um token a partir dessa distribuição.

A palavra "decide" no título desta seção é deliberadamente entre aspas. O modelo não delibera, não pondera, não considera opções. Ele executa um cálculo e faz uma amostragem. O resultado pode parecer uma escolha inteligente — e frequentemente é coerente e útil — mas o mecanismo é probabilístico, não intencional.

---

## Temperatura — do determinístico ao caótico

A **temperatura** é um parâmetro que controla o quão achatada ou pontuda é a distribuição de probabilidade antes da amostragem.

Com temperatura baixa (próxima de zero), a distribuição se concentra quase toda no token mais provável. O modelo fica previsível e repetitivo — dado o mesmo prompt, dará sempre a mesma resposta. É útil quando você precisa de consistência: código, cálculos, respostas factuais.

Com temperatura alta, a distribuição se achata: tokens menos prováveis ganham chance real de ser escolhidos. O modelo fica mais criativo, mais surpreendente — e mais propenso a errar. É útil para brainstorming, escrita criativa, geração de variações.

Pense assim: temperatura baixa é um músico tocando uma peça clássica ao pé da letra. Temperatura alta é o mesmo músico improvisando — pode ser genial, pode ser uma nota errada.

> 🛠️ **Demo ao vivo — veja a temperatura mexer na distribuição:** [`codigos_uteis/proximo_token.py`](../codigos_uteis/proximo_token.py) mostra as probabilidades reais do próximo token, ao lado da distribuição depois de aplicar a temperatura. Rode a **mesma frase** com temperaturas diferentes e compare:
>
> ```bash
> python proximo_token.py -t 0.3 "A capital do Brasil é"
> python proximo_token.py -t 2   "A capital do Brasil é"
> python proximo_token.py -t 2 --amostras 20 "A capital do Brasil é"
> ```
>
> Com `-t 0.3` o token mais provável domina (a barra cresce); com `-t 2` as barras se igualam e tokens improváveis passam a ser sorteados. O terceiro comando sorteia 20 vezes e conta o resultado: a cada rodada a contagem muda. `--gerar 12 -t 1` deixa o modelo escrever uma frase inteira com a temperatura escolhida — rode duas vezes e compare.

---

## Alucinações — por que o modelo inventa fatos

**Alucinação** é o termo técnico para quando um LLM gera informação factualmente incorreta com total fluência e aparente confiança. O modelo não mente — ele completa.

Para entender por que isso acontece, lembre do que o modelo aprendeu a fazer: prever o próximo token que é *estatisticamente plausível* dado o contexto. Ele não aprendeu a verificar se o que gerou é verdade. Não tem acesso a um banco de dados de fatos que possa consultar. Não tem memória de ter "lido" algo específico.

O que ele tem é uma enorme compressão estatística de padrões linguísticos. Quando você pergunta sobre a biografia de uma pessoa pouco conhecida, ele não recupera uma memória — ele *gera* uma sequência de tokens que se parece com uma biografia, baseado nos padrões de como biografias são escritas e nos fragmentos que viu sobre aquela pessoa ou sobre pessoas similares.

Se os fragmentos são escassos ou contraditórios, o modelo preenche os espaços com o que é estatisticamente plausível — e o resultado pode ser um nome, uma data, um título de artigo completamente inventado, mas escrito com a mesma fluência de um fato real.

Alguns padrões comuns de alucinação:

**Referências bibliográficas** — títulos de artigos que não existem, com autores reais e anos plausíveis. O modelo aprendeu como referências são formatadas e gera referências no mesmo formato, sem verificar se existem.

**Detalhes biográficos** — datas de nascimento, cargos, prêmios, citações atribuídas a pessoas reais mas inventadas. Quanto menos famosa a pessoa, maior o risco.

**Código com bugs sutis** — o código parece correto, compila, mas tem um erro lógico ou usa uma API que não existe da forma descrita. O modelo aprendeu padrões de código, não a semântica de execução.

**Fatos recentes** — o modelo não tem acesso a eventos após seu corte de treinamento. Quando perguntado sobre algo recente, pode "atualizar" fatos antigos com detalhes inventados.

> 🛠️ **Demo ao vivo:** Peça a qualquer chatbot uma referência bibliográfica sobre um tema técnico específico e pouco comum. Depois verifique se o artigo existe. A probabilidade de alucinação é alta — e a fluência da resposta falsa é indistinguível da verdadeira.

---

## O modelo não sabe o que não sabe

Aqui está a diferença crítica entre um LLM e um sistema que raciocina com incerteza:

Um humano que não sabe a resposta para uma pergunta geralmente *sabe que não sabe*. Pode dizer "não tenho certeza", "preciso verificar", "isso está fora da minha área". Essa metacognição — conhecimento sobre o próprio conhecimento — é fundamental para saber quando confiar numa resposta.

Um LLM padrão **não tem esse mecanismo nativo**. O processo de geração é o mesmo independentemente de o modelo ter sido treinado extensivamente sobre o assunto ou não ter visto quase nada sobre ele. A distribuição de probabilidade pode ser igualmente "confiante" nos dois casos — e a fluência do texto resultante é indistinguível.

Isso significa que a confiança aparente do modelo não é um sinal confiável de precisão. Um parágrafo bem escrito e assertivo sobre um tema que o modelo conhece mal parece exatamente igual a um parágrafo sobre algo que ele conhece bem.

Alguns modelos mais recentes foram ajustados para expressar incerteza em linguagem natural — "não tenho certeza", "você deveria verificar isso" — mas isso é comportamento aprendido por instrução, não uma propriedade estrutural do modelo. É o modelo *aprendendo a dizer* que não sabe, não o modelo *sabendo* que não sabe.

A distinção importa porque tem consequências práticas sérias: em contextos de alta confiabilidade — medicina, direito, engenharia, jornalismo — a ausência de incerteza calibrada é um risco real, não uma limitação menor.

---

## Implicações práticas

Três hábitos que seguem diretamente do que vimos:

**Verifique fatos específicos** — qualquer dado pontual que o modelo forneça (data, nome, número, referência) deve ser verificado em fonte primária antes de ser usado. A fluência não é garantia de precisão.

**Peça ao modelo para expressar incerteza** — prompts como *"se não tiver certeza, diga explicitamente"* ou *"aponte onde você pode estar errado"* ajudam, mas não eliminam o problema. São instruções que o modelo tenta seguir, não uma janela para seu estado interno real.

**Calibre o uso pela consequência do erro** — para brainstorming, rascunho inicial e tarefas criativas, alucinações são toleráveis ou até úteis. Para decisões com consequências reais, o LLM deve ser tratado como ponto de partida para investigação, não como fonte definitiva.

> 🛠️ **O que a engenharia faz a respeito:** em vez de pedir ao modelo que "lembre", dá-se a ele **ferramentas** (busca, consulta a bases, calculadora, execução de código) e **verificações** — de modo que o fato venha de uma fonte rastreável e a conta, de um programa. Veja [[01.1 IA Hoje — Agentes e Engenharia]].

> 💡 Voltaremos a esse tema na seção [[11 Antropomorfização]] — onde veremos como a fluência e a aparente confiança do modelo criam uma ilusão de compreensão que vai além das alucinações factuais.

---

[[Índice]] | [[06 Como os LLMs Aprendem|← Anterior]] | [[08 Chatbots|Próximo →]]

[[#07 Como o Modelo "Decide"|↑ Topo]]
