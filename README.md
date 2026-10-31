# LLM na Prática: Entendendo Prompts e Modelos com Ollama

> Um curso hands-on de 4 horas para construir intuição real sobre como os Grandes Modelos de Linguagem (LLMs) funcionam — e por que os prompts importam tanto quanto o treinamento.

---

## Para Participantes do Workshop

### Material do curso

Todo o material de estudo está em [`material_aulas/workshop_apresen/`](material_aulas/workshop_apresen/).

Comece pelo **[Índice Geral](material_aulas/workshop_apresen/Índice.md)** para navegar pelas seções (12 principais + 01.1, 09.1 e 09.2) com links diretos para cada slide. Conceito e prática são intercalados: cada seção indica a demonstração associada.

> Os arquivos `.md` são otimizados para [Obsidian](https://obsidian.md/), mas podem ser lidos em qualquer editor de texto ou diretamente no GitHub.

### Demo interativo

Nas demonstrações ao longo do workshop, o instrutor serve uma aplicação web na rede local.
Acesse pelo endereço que o instrutor informar em sala — geralmente `http://192.168.x.x:8000`.

---

## Para Instrutores

### Estrutura do repositório

```
workshop_llm2p0/
├── material_aulas/      # Conteúdo do curso (slides, links, prompts de demo)
└── workshop_server/     # Servidor web usado nas demonstrações
```

### Setup rápido do servidor

Ver instruções detalhadas em [`workshop_server/README.md`](workshop_server/README.md).

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar o Ollama (em outro terminal)
ollama serve

# 3. Subir o servidor
cd workshop_server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Participantes conectam via: `http://<seu-ip-local>:8000`

### O que o workshop cobre

- Como LLMs processam e geram texto (próximo token, temperatura, amostragem)
- Diferença entre modelo base e modelo instruct (RLHF, instruction tuning)
- Como prompts afetam o comportamento do modelo
- Comparação entre modelos diferentes rodando lado a lado

---

## Sobre

Curso desenvolvido por Emilio Vital Brazil.
Construído com auxílio da API do Claude — uma demonstração prática do próprio conteúdo ensinado.

Licença: [Apache 2.0](LICENSE)
