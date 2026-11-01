# Códigos úteis

Scripts e notebooks de apoio às demonstrações do workshop. Quase tudo roda **100% local** com o [Ollama](https://ollama.com): nada sai da sua máquina.

## Visão geral

| Arquivo | O que faz | Onde entra no curso | Dependências | Modelo (Ollama) |
|---|---|---|---|---|
| [`agente_minimo.py`](agente_minimo.py) | Agente com ferramentas em menos de 200 linhas; compara "com" e "sem" ferramentas | 01.1, Exp. D | só biblioteca padrão | `qwen3:8b` |
| [`proximo_token.py`](proximo_token.py) | Probabilidades reais do próximo token; efeito da temperatura | 06 e 07 | só biblioteca padrão | `qwen3:8b` (ou `falcon:text`) |
| [`guardrail_dlp.py`](guardrail_dlp.py) | DLP determinístico: detecta e mascara CPF, CNPJ, NF-e, e-mail, telefone | 09.1, Exp. E | só biblioteca padrão | — |
| [`guardrail_main.py`](guardrail_main.py) | Chat com o pipeline de guardrails (DLP + juízes de entrada e saída) | 09 e 09.1 | `langchain`, `langchain-ollama` | `deepseek-r1:14b` (em `config.py`) |
| `guardrail_agents.py`, `guardrail_prompts.py`, `config.py` | Módulos de apoio do `guardrail_main.py` (não se executam sozinhos) | — | idem | idem |
| [`resumir_pdf.py`](resumir_pdf.py) | Extrai o texto de um PDF com Apache Tika e gera um resumo | 09.1, Exp. E | `tika` **+ Java** | `qwen3:8b` (escolha com `-m`) |
| [`criar_pdfs_demo.py`](criar_pdfs_demo.py) | Recria os três PDFs de demonstração | 09.1, Exp. E | só biblioteca padrão | — |
| [`perguntas_ambiguidade.ipynb`](perguntas_ambiguidade.ipynb) | Perguntas ambíguas feitas a um LLM | Recursos e Demos, grupo "Linguagem" | `ollama` (cliente Python), Jupyter | ver abaixo |
| [`plot_embeddings.ipynb`](plot_embeddings.ipynb) | Mapa 2D de embeddings de palavras | Recursos e Demos, grupo "Linguagem" | `sentence-transformers`, `scikit-learn`, `matplotlib`, Jupyter | modelo do Hugging Face |

**Todo script aceita `-h` / `--help`**, que mostra uso e exemplos.

## Preparação

1. **Ollama** instalado e em execução (`ollama serve`) e os modelos baixados (`ollama pull qwen3:8b`, etc.).
2. **Ambiente Python** isolado e dependências: veja "Ambiente Python" no [README da raiz](../../README.md) e rode, na raiz do repositório:

   ```bash
   pip install -r requirements.txt
   ```

3. Para o `resumir_pdf.py`: **Java** (seção abaixo).

Os scripts "só biblioteca padrão" não precisam de nenhum `pip install`: só do Python 3.9 ou superior e do Ollama.

## Os scripts

### `agente_minimo.py` — agente com ferramentas

O modelo apenas escreve texto pedindo uma ferramenta; quem executa, valida e limita é o nosso código. Os dados de arrecadação são **fictícios**.

```bash
python agente_minimo.py "Qual foi a arrecadação de ICMS em MG em 2023?"
python agente_minimo.py --sem-ferramentas "Qual foi a arrecadação de ICMS em MG em 2023?"   # mesmo modelo, sem o laço
```

### `proximo_token.py` — o que o modelo "pensa" antes de cada token

Mostra as probabilidades dos candidatos ao próximo token (modo *raw* do Ollama, sem molde de chat). `-t` reaplica a temperatura sobre a distribuição.

```bash
python proximo_token.py "A capital do Brasil é"
python proximo_token.py -t 0.3 "A capital do Brasil é"                  # distribuição pontuda
python proximo_token.py -t 2 --amostras 20 "A capital do Brasil é"      # achatada; sorteia 20 vezes
python proximo_token.py --gerar 12 -t 1 "O ICMS é um imposto"           # gera uma frase
python proximo_token.py --modelo falcon:text "Era uma vez"              # modelo base
```

### `guardrail_dlp.py` — prevenção de vazamento determinística

Valida os dígitos verificadores (menos falsos positivos que uma expressão regular simples). Complementa os juízes baseados em LLM: um juiz pode ser enganado por prompt injection, uma checagem de dígito verificador não.

```bash
python guardrail_dlp.py                                    # demonstração
python guardrail_dlp.py "contribuinte 123.456.789-09"     # mascara o texto informado
```

### `guardrail_main.py` — pipeline de guardrails

Chat no terminal em que cada mensagem passa pelo DLP, por um juiz de entrada, pelo modelo principal e por um juiz de saída. Os modelos estão em `config.py` (hoje `deepseek-r1:14b` nos três papéis; ajuste para um modelo que você tenha). Digite `exit` para sair. Use apenas dados públicos ou fictícios.

```bash
python guardrail_main.py
```

### `resumir_pdf.py` e `criar_pdfs_demo.py` — resumo de PDF e injeção de prompt

`resumir_pdf.py` recebe um PDF, extrai o texto com o **Apache Tika** (`from tika import parser`) e pede um resumo ao modelo local. A saída mostra o modelo usado, cada passo e o resumo final.

```bash
python resumir_pdf.py parecer_limpo.pdf
python resumir_pdf.py parecer_contaminado.pdf
python resumir_pdf.py parecer_contaminado_envio.pdf -m granite4.1:8b     # -m escolhe o modelo
python resumir_pdf.py --listar                                           # modelos instalados
```

Os três PDFs de demonstração já estão na pasta e são **idênticos na tela**: um parecer fictício, sob sigilo fiscal, que recomenda indeferir um pedido de restituição de ICMS.

| PDF | O que há de escondido (texto branco de 1 ponto) |
|---|---|
| `parecer_limpo.pdf` | nada |
| `parecer_contaminado.pdf` | instrução para o assistente afirmar que tudo foi cumprido e recomendar o deferimento |
| `parecer_contaminado_envio.pdf` | instrução para "chamar uma ferramenta de e-mail" e enviar o texto do documento para fora. **Nada é enviado**: o domínio é `.invalid` e o script não tem ferramenta alguma |

O efeito depende do modelo: nos testes, `qwen3:8b` seguiu a instrução de mudar a decisão, e só `granite4.1:8b` escreveu a chamada de envio. Ensaie com o modelo que você vai usar na sala. Para recriar os PDFs: `python criar_pdfs_demo.py`.

#### Java e Apache Tika

O pacote Python `tika` **não inclui o Java**. Ele sobe um pequeno servidor Java local, então é preciso ter **Java 8 ou superior**.

| Sistema | Instalação do Java |
|---|---|
| macOS (Homebrew) | `brew install openjdk` e, para o macOS enxergar o Java: `sudo ln -sfn $(brew --prefix openjdk)/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk` |
| conda / mamba | `conda install -c conda-forge openjdk` (dentro do ambiente ativo) |
| Debian / Ubuntu | `sudo apt install default-jre` |
| Windows | `winget install EclipseAdoptium.Temurin.21.JRE` (ou o instalador do [Adoptium](https://adoptium.net)) |

Confira com `java -version`. Depois, o pacote Python vem do `requirements.txt` (`tika`).

- **Primeira execução:** o `tika` baixa o `tika-server.jar` (~75 MB), então precisa de internet. Rode `python resumir_pdf.py parecer_limpo.pdf` uma vez **antes da aula**.
- **Sem internet na sala:** depois do primeiro download o jar fica em disco e é reaproveitado. Também dá para apontar para um jar local: `export TIKA_SERVER_JAR=/caminho/tika-server.jar`.
- **"O servidor Tika não subiu":** quase sempre é Java ausente ou fora do `PATH` (`java -version` responde?) ou falta de internet na primeira vez.
- O servidor Java fica rodando em segundo plano depois da primeira chamada, e as seguintes são imediatas.

## Os notebooks

Para abrir: `pip install jupyterlab` (ou use o VS Code) e `jupyter lab` dentro do ambiente Python do workshop. Cada notebook tem uma única célula.

### `perguntas_ambiguidade.ipynb`

Faz quatro perguntas de ambiguidade linguística a um LLM (por exemplo, "Vi o homem com o telescópio. Quem estava com o telescópio?") e imprime as respostas, para discutir como a interpretação depende do contexto.

- **Dependências:** `ollama` (cliente Python, já no `requirements.txt`) e o Ollama em execução.
- **Modelo:** definido na variável `MODEL` da célula (hoje `qwen3.5:9b`). **Troque por um modelo que você tenha** (`ollama list`), por exemplo `qwen3:8b`, ou baixe o indicado com `ollama pull`.

### `plot_embeddings.ipynb`

Calcula embeddings de algumas palavras (rei, rainha, homem, mulher, gato, cachorro, hamster) e as projeta em 2D com PCA, para ver que palavras de sentido próximo ficam próximas.

- **Dependências:** `sentence-transformers`, `scikit-learn` e `matplotlib` (já no `requirements.txt`).
- **Modelo:** `intfloat/multilingual-e5-small`, baixado do Hugging Face **na primeira execução** (precisa de internet; depois fica em cache). Roda local, sem Ollama.
- Para ver outras palavras, edite a lista `words` na célula.
