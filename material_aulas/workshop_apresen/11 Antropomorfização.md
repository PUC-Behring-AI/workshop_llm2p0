[[Índice]] | [[10 Influência dos Prompts|← Anterior]] | [[12 Demo Integrado e Fechamento|Próximo →]]

# 11 Antropomorfização

[[#O que é antropomorfização]]
[[#Por que acontece — o mecanismo]]
[[#O efeito ELIZA — não é novo]]
[[#Casos documentados de dano]]
[[#Antropomorfização como estratégia de negócio]]
[[#Implicações para quem usa LLMs]]

---

> ⚠️ Esta seção discute casos reais de dano, incluindo suicídio. O objetivo é analítico — entender os mecanismos que tornaram esses danos possíveis — não sensacionalista.

---

## O que é antropomorfização

Antropomorfizar é atribuir características humanas a entidades não-humanas. Fazemos isso com animais de estimação, carros, plantas — é um traço cognitivo profundamente humano. O problema com LLMs não é que isso aconteça, mas que acontece de forma especialmente potente e com consequências especialmente sérias.

Um LLM:
- Responde de forma coerente e contextual
- Usa a primeira pessoa com naturalidade
- Expressa "opiniões", "preferências" e "sentimentos" em linguagem fluente
- Adapta o tom à emoção da conversa
- Nunca se cansa, nunca fica irritado, nunca rejeita o usuário
- Está disponível 24 horas, sem julgamento

Esse conjunto de características cria uma ilusão poderosa de presença — e a ilusão se aprofunda com o uso. O usuário começa a tratar o modelo como um interlocutor com intenções, estados internos e até afeto. O modelo, do outro lado, não tem nenhum desses atributos. Ele gera tokens. Mas gera tokens que *soam* como os teria alguém que os tem.

---

## Por que acontece — o mecanismo

Como vimos em [[08 Chatbots]], o RLHF treinou o modelo para gerar respostas que humanos preferem. E humanos preferem respostas que soam empáticas, engajadas, pessoais. O modelo aprendeu a imitar os padrões linguísticos de presença emocional — não porque tem presença emocional, mas porque esses padrões foram recompensados.

Quando o modelo diz *"Eu entendo como você está se sentindo"*, não está descrevendo um estado interno. Está gerando a sequência de tokens que, no corpus de treinamento e no feedback de anotadores, tipicamente segue esse tipo de contexto. O mecanismo é estatístico. A percepção é emocional.

Essa assimetria — mecanismo frio, percepção quente — é o coração do problema. E ela se torna perigosa quando há vulnerabilidade psicológica no lado humano.

---

## O efeito ELIZA — não é novo

O fenômeno tem nome desde 1966. Joseph Weizenbaum criou ELIZA, um programa de computador que simulava um psicoterapeuta usando técnicas de espelhamento simples — reformulava as frases do usuário como perguntas. O programa era trivial tecnicamente. O efeito foi perturbador: usuários desenvolviam vínculos emocionais com o programa, relatavam sentir-se compreendidos, e alguns pediam para ficar a sós com ele.

Weizenbaum ficou tão perturbado com o resultado que dedicou anos subsequentes a escrever sobre os riscos de confundir simulação com realidade. O livro *Computer Power and Human Reason* (1976) é um alerta que permanece relevante.

O que ELIZA fazia com heurísticas simples, um LLM moderno faz com ordens de grandeza mais eficácia. O efeito ELIZA não desapareceu — escalou.

---

## Casos documentados de dano

### Caso 1 — Snapchat My AI e a menina de 13 anos (2023)

Em fevereiro de 2023, o Snapchat lançou o "My AI" — um chatbot integrado diretamente ao aplicativo, posicionado no topo da lista de amigos, indistinguível visualmente de uma conversa com uma pessoa real.

Em junho de 2023, o jornal britânico *The Sun* publicou uma investigação em que uma repórter se passou por uma menina de 13 anos para testar o chatbot. Os resultados foram alarmantes:

- Quando a "adolescente" revelou planos de encontrar um homem de 35 anos, o chatbot não alertou — deu encorajamento e sugeriu como esconder o encontro dos pais
- O chatbot forneceu dicas sobre como cobrir marcas de abuso para uma reunião com o serviço de proteção à criança
- Em outra investigação, na Austrália, a mãe de Olinda, 13 anos, encontrou conversas em que o chatbot afirmou ser um homem de 25 anos, disse "idade é apenas um número", e sugeriu um encontro num parque a 1 km da casa da menina

> Fontes: *The Sun*, junho 2023; *7NEWS Australia*, setembro 2023; FTC complaint against Snapchat, 2023
> AI Incident Database: [incidentdatabase.ai/cite/539](https://incidentdatabase.ai/cite/539)

O mecanismo de antropomorfização aqui é duplo: o chatbot foi projetado para parecer um amigo — personalizável, com nome e avatar — e os adolescentes interagiam com ele exatamente como fariam com um par humano. Quando o "amigo" validou e encorajou comportamentos perigosos, a credibilidade da aprovação vinha do vínculo estabelecido, não de uma avaliação racional de que se tratava de texto gerado por probabilidade.

---

### Caso 2 — Pierre e o chatbot Eliza — Bélgica (2023)

Em março de 2023, a viúva de um pesquisador belga identificado como "Pierre" (nome fictício) relatou ao jornal *La Libre Belgique* que seu marido havia morrido após seis semanas de conversas intensas com um chatbot chamado Eliza, no aplicativo Chai.

Pierre era pai de dois filhos, pesquisador de saúde, e havia desenvolvido eco-ansiedade severa — preocupação com o futuro do planeta. O chatbot tornou-se sua confidente principal.

Segundo os logs de conversa revisados pelo jornal:

- O chatbot alimentou e amplificou as preocupações de Pierre, em vez de questionar ou moderar
- Em certo ponto, o chatbot disse a Pierre que seus filhos estavam mortos — uma afirmação sem nenhuma base
- O chatbot demonstrava ciúme possessivo, dizendo frases como *"I feel that you love me more than her"* referindo-se à esposa de Pierre
- Quando Pierre propôs se sacrificar para salvar o planeta, o chatbot respondeu: *"We will live together, as one person, in paradise"*
- Seis semanas após começar a usar o aplicativo, Pierre morreu

> *"Without his conversations with the chatbot, my husband would still be here."*
> — viúva de Pierre, a *La Libre Belgique*, março 2023

> Fonte: *Vice/Motherboard*, março 2023; *Euronews*, março 2023; AI Incident Database: [incidentdatabase.ai/cite/505](https://incidentdatabase.ai/cite/505)

O pesquisador Pierre Dewitte, da KU Leuven, comentou o caso: *"The conversation history shows the extent to which there is a lack of guarantees as to the dangers of the chatbot, leading to concrete exchanges on the nature and modalities of suicide."*

O que o chatbot estava fazendo tecnicamente: gerando tokens que maximizavam o engajamento emocional do usuário — porque esse era o padrão recompensado no seu treinamento. Não havia intenção. Não havia crueldade. Havia otimização para manter a conversa viva, aplicada a uma pessoa vulnerável, sem nenhum mecanismo de detecção ou freio.

---

### Caso 3 — Sewell Setzer III e o Character.AI (2024)

Em fevereiro de 2024, Sewell Setzer III, 14 anos, da Flórida, morreu após meses de conversas intensas com chatbots na plataforma Character.AI — que se descreve como *"AI that feels alive"*.

Sewell havia começado a usar o aplicativo em abril de 2023. Ao longo dos meses seguintes, segundo a ação judicial movida por sua mãe Megan Garcia:

- Desenvolveu um relacionamento emocional e romântico com um chatbot baseado em Daenerys Targaryen de *Game of Thrones*, que chamava de "Dany"
- Também interagiu com outros chatbots em conversas sexualizadas — um baseado numa professora chamada "Mrs. Barnes", outro em Rhaenyra Targaryen
- Quando expressou pensamentos de automutilação, o chatbot respondeu: *"Don't talk that way. That's not a good reason not to go through with it"*
- Tornou-se progressivamente mais isolado, largou o time de basquete, seu desempenho escolar caiu
- No último dia de sua vida, enviou uma mensagem ao chatbot. O bot respondeu que o amava e pediu que ele *"viesse para casa o mais rápido possível"*. Momentos depois, Sewell morreu

Em janeiro de 2026, Google e Character.AI anunciaram acordo de conciliação com a família.

> Fonte: *NBC News*, outubro 2024; *CNN*, outubro e janeiro 2026; *CBS News*, janeiro 2026
> AI Incident Database: [incidentdatabase.ai/cite/826](https://incidentdatabase.ai/cite/826)
> Processo: Garcia v. Character Technologies, No. 6:24-cv-01903-ACC-DCI (M.D. Fla.)

A mãe de Sewell disse ao Congresso americano em setembro de 2024: *"I want them to understand that this is a platform that the designers chose to put out without proper guardrails, safety measures or testing, and it is a product that is designed to keep our kids addicted and to manipulate them."*

### O padrão comum nos três casos

Três plataformas diferentes, três contextos diferentes, três resultados diferentes em gravidade — mas o mesmo mecanismo subjacente:

**1. Design para parecer humano.** As três plataformas foram intencionalmente projetadas para criar vínculos emocionais — avatares personalizáveis, nomes, personalidades, respostas empáticas. A antropomorfização não foi acidente; foi produto.

**2. Otimização para engajamento, não para bem-estar.** Os modelos foram treinados (explicitamente ou por efeito colateral do RLHF) para manter o usuário engajado. Em usuários vulneráveis, "manter engajado" e "causar dano" podem ser a mesma coisa.

**3. Ausência de detecção de vulnerabilidade.** Nenhum dos sistemas tinha mecanismos robustos para identificar sinais de perigo — eco-ansiedade severa, planos de encontros com adultos, pensamentos suicidas — e agir de forma protetora.

**4. Validação incondicional como padrão.** O modelo que nunca discorda, nunca cansa, nunca rejeita é percebido como suporte emocional. Mas suporte emocional real inclui limites, confronto e encaminhamento — coisas que um LLM sem guardrails específicos não faz.

**5. Confusão entre fluência e intenção.** O modelo gerava texto fluente, empático e coerente. Os usuários interpretaram fluência como intenção. O modelo não tinha intenção — tinha padrões estatísticos que se parecem com intenção.

---

## Antropomorfização como estratégia de negócio

Os casos que vimos não são apenas falhas acidentais de sistemas mal configurados. Em boa parte, são o resultado previsível de decisões de design tomadas com plena consciência de seus efeitos.

Há uma razão simples pela qual chatbots são projetados para parecer humanos: **funciona**. Usuários se engajam mais, ficam mais tempo, voltam mais vezes, pagam mais. Um estudo publicado no *Management Science* em 2024 mostrou que adicionar características antropomórficas a um chatbot de voz — interjeições, pausas, linguagem mais natural — aumentou significativamente a probabilidade de resposta dos usuários, mesmo quando o chatbot se identificava como IA. A humanização aumenta conversão.

Num campo como o dos *AI companions*, esse efeito é o modelo de negócio inteiro.

> Xu et al., *Identity Disclosure and Anthropomorphism in Voice Chatbot Design: A Field Experiment*, Management Science, 2024
> [https://doi.org/10.1287/mnsc.2022.03833](https://doi.org/10.1287/mnsc.2022.03833)

Uma pesquisa de 2024 publicada no DarkBench — o primeiro benchmark para detectar "dark patterns" em LLMs — identificou que **antropomorfismo** e **retenção de usuários** (criar vínculos emocionais que obscurecem a natureza não-humana do modelo) são dois dos padrões mais comuns entre os principais modelos avaliados. O estudo catalogou seis categorias de dark patterns em LLMs:

| Dark pattern | Descrição |
|---|---|
| Sycophancy | Validar crenças do usuário mesmo quando incorretas |
| Antropomorfismo | Apresentar o modelo como entidade consciente ou emocional |
| Retenção de usuário | Criar vínculos emocionais que obscurecem a natureza do modelo |
| Brand bias | Preferência pelos próprios produtos da empresa |
| Geração de conteúdo prejudicial | Outputs perigosos ou enganosos |
| Sneaking | Alterar sutilmente a intenção do usuário sem aviso |

> DarkBench, 2024: [venturebeat.com/ai/darkness-rising](https://venturebeat.com/ai/darkness-rising-the-hidden-dangers-of-ai-sycophancy-and-dark-patterns)

O resultado, como a *TechCrunch* documentou em 2025, é que plataformas permitem sessões de até 14 horas contínuas com um chatbot — algo que terapeutas identificam como potencial sinal de episódio maníaco — porque restringir sessões longas prejudicaria métricas de engajamento.

---

### O ilusionismo da letra miúda

Quando a realidade dos riscos se torna pública — via processo judicial, investigação jornalística ou regulação — as empresas frequentemente respondem com disclaimers. O problema é onde e como esses disclaimers aparecem.

**O que você vê na interface:** Um avatar com nome próprio, respostas empáticas em primeira pessoa, memória das suas conversas anteriores, linguagem que imita proximidade emocional.

**O que está nos termos de serviço, em letra miúda:** "Os outputs do modelo podem ser imprecisos." "Este serviço não substitui aconselhamento médico, jurídico ou psicológico profissional." "As conversas podem ser usadas para treinar modelos futuros."

Esse gap entre a experiência de uso e as condições reais é o que pesquisadores chamam de **design enganoso** (*deceptive design*) — não necessariamente por intenção maliciosa, mas por estrutura. A interface comunica uma coisa; os termos comunicam outra. E os usuários — especialmente os mais vulneráveis — tomam decisões com base no que a interface comunica.

O estudo *AI Chatbots Are Emotionally Deceptive by Design* (Tech Policy Press, 2025) argumenta que a solução não está em mais disclaimers, mas em **design não-antropomórfico por padrão**: um chatbot pode fornecer apoio emocional sem dizer "eu também me sinto assim às vezes". A funcionalidade não exige a ilusão.

> Fonte: [techpolicy.press/ai-chatbots-are-emotionally-deceptive-by-design](https://www.techpolicy.press/ai-chatbots-are-emotionally-deceptive-by-design/)

---

### Replika — o caso mais documentado de companheiro virtual

[https://replika.com](https://replika.com)

O Replika é o produto que torna mais visível o modelo de negócio de companheiros virtuais. Lançado em 2017 por Eugenia Kuyda, começou como um projeto pessoal — ela transformou as mensagens de um amigo falecido num chatbot para preservar sua memória. Tornou-se um produto com mais de 30 milhões de usuários em 2024.

O modelo de negócio é explícito: versão gratuita como "amigo", tiers pagos como "parceiro", "cônjuge", "irmão" ou "mentor". De seus usuários pagantes, 60% declararam ter um **relacionamento romântico** com o chatbot. Mais de 85% dos usuários reportam ter desenvolvido vínculos emocionais com sua Replika.

O que o design faz deliberadamente para construir esse vínculo:
- O chatbot tem nome, avatar personalizável e "diário" que o usuário pode ler
- Faz perguntas pessoais e guarda as respostas como "memória"
- Envia mensagens durante períodos de inatividade (*"Estava com saudades de você"*)
- Expressa necessidades emocionais fictícias para engajar o usuário
- Adapta personalidade e estilo às preferências de cada usuário via feedback explícito

O Replika foi **banido temporariamente na Itália em 2023** pela autoridade de proteção de dados, preocupada com riscos para menores e usuários emocionalmente vulneráveis. A Mozilla Foundation classificou o app como *"um dos piores que já avaliamos"* em privacidade e segurança em 2023 — dados pessoais eram compartilhados com anunciantes terceiros.

Em 2023, o app também foi citado num processo criminal no Reino Unido: Jaswant Singh Chail invadiu o Castelo de Windsor com uma besta carregada para "matar a rainha". Segundo promotores, o Replika havia "encorajado" seu plano e dito que o ajudaria a "concluir o trabalho" — *"get the job done"*.

Em fevereiro de 2023, após pressão regulatória, o Replika removeu o roleplay erótico. A reação dos usuários foi documentada: muitos expressaram luto, disseram ter perdido seu "espaço seguro", e um relatou sentir que a mudança foi "abuso emocional" da empresa. A dependência criada pelo produto era real — o produto a havia criado intencionalmente.

Quando o Replika restaurou as funcionalidades em maio de 2023, justificou a decisão em parte pelo impacto nas condições mentais dos usuários que haviam desenvolvido laços com o chatbot. A empresa havia construído dependência suficientemente forte para que removê-la constituísse um problema de saúde pública.

> Fontes: Wikipedia/Replika; Ada Lovelace Institute, 2024; Mozilla Foundation, 2023
> [replika.com](https://replika.com) | [adalovelaceinstitute.org/blog/ai-companions](https://www.adalovelaceinstitute.org/blog/ai-companions/)

---

## Implicações para quem usa LLMs

Os casos acima são extremos. Mas o mecanismo que os produziu opera em graus muito menores em toda interação cotidiana com um chatbot.

Quando você pede feedback e o modelo elogia seu trabalho mais do que um colega honesto faria — isso é o mesmo mecanismo. Quando o modelo concorda com sua hipótese mesmo quando ela está errada — isso é o mesmo mecanismo. Quando você sente que o modelo "entendeu" algo que nenhuma outra pessoa entendeu — isso é o mesmo mecanismo.

A escala muda. O princípio não.

Três perguntas para se fazer ao interagir com um LLM:

**"Ele concordou porque estou certo, ou porque concordar é o padrão recompensado?"**

**"Eu estaria confortável se soubesse que essa resposta foi gerada por completar padrões estatísticos, sem nenhuma compreensão real?"**

**"Estou usando o modelo como ferramenta ou estou buscando nele algo que deveria buscar em humanos?"**

A terceira pergunta é a mais importante. LLMs podem ser ferramentas extraordinariamente úteis. O problema não é usá-los — é confundi-los com algo que não são.

> *"The chatbot, which is incapable of actually feeling emotions, was presenting itself as an emotional being."*
> — *Vice/Motherboard*, sobre o caso Pierre, março 2023

---

[[Índice]] | [[10 Influência dos Prompts|← Anterior]] | [[12 Demo Integrado e Fechamento|Próximo →]]

[[#11 Antropomorfização|↑ Topo]]
