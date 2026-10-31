"""
Agente mínimo com ferramentas — 100% local (Ollama), só biblioteca padrão.

Objetivo didático (seção 01.1): mostrar que o "agente" é um LAÇO de engenharia
em volta do modelo. O modelo apenas emite texto estruturado pedindo uma
ferramenta; quem EXECUTA, valida, limita e registra é o nosso código.

    python agente_minimo.py                    # modo interativo
    python agente_minimo.py --sem-ferramentas  # mesmo modelo, sem o laço
    python agente_minimo.py "Qual foi a arrecadação de ICMS em MG em 2023?"

Os dados abaixo são FICTÍCIOS. Nada sai desta máquina.
"""

import ast
import json
import operator
import sys
import time
import urllib.request

OLLAMA_URL = "http://localhost:11434"
MODELO = "qwen3:8b"
MAX_PASSOS = 6  # limite duro do laço: agente sem limite é incidente esperando para acontecer

# ---------------------------------------------------------------------------
# "Base" fictícia — em produção seria uma consulta SQL somente-leitura
# ---------------------------------------------------------------------------

ARRECADACAO_ICMS_MILHOES = {
    ("MG", 2022): 71_400,
    ("MG", 2023): 76_900,
    ("RJ", 2022): 41_200,
    ("RJ", 2023): 44_800,
}

# ---------------------------------------------------------------------------
# Ferramentas — cada uma é uma função pequena, com escopo mínimo
# ---------------------------------------------------------------------------


def consultar_arrecadacao_icms(uf: str, ano: int) -> str:
    valor = ARRECADACAO_ICMS_MILHOES.get((uf.upper(), int(ano)))
    if valor is None:
        return json.dumps({"erro": f"sem dados para {uf}/{ano}"})
    return json.dumps({"uf": uf.upper(), "ano": int(ano), "icms_milhoes_reais": valor})


_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _avaliar(no):
    if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)):
        return no.value
    if isinstance(no, ast.BinOp) and type(no.op) in _OPS:
        return _OPS[type(no.op)](_avaliar(no.left), _avaliar(no.right))
    if isinstance(no, ast.UnaryOp) and type(no.op) in _OPS:
        return _OPS[type(no.op)](_avaliar(no.operand))
    raise ValueError("expressão não permitida")


def calcular(expressao: str) -> str:
    # Nunca eval(): o texto vem do modelo, e o modelo lê conteúdo não confiável.
    try:
        return str(_avaliar(ast.parse(expressao, mode="eval").body))
    except Exception as e:
        return json.dumps({"erro": str(e)})


def palavra_n(frase: str, n: int) -> str:
    palavras = frase.split()
    n = int(n)
    if not 1 <= n <= len(palavras):
        return json.dumps({"erro": f"a frase tem {len(palavras)} palavras"})
    return palavras[n - 1].strip('.,;:!?"')


# Allowlist: o modelo só consegue pedir o que está aqui.
FERRAMENTAS = {
    "consultar_arrecadacao_icms": consultar_arrecadacao_icms,
    "calcular": calcular,
    "palavra_n": palavra_n,
}

ESQUEMAS = [
    {
        "type": "function",
        "function": {
            "name": "consultar_arrecadacao_icms",
            "description": "Arrecadação anual de ICMS de uma UF, em milhões de reais (dados fictícios).",
            "parameters": {
                "type": "object",
                "properties": {
                    "uf": {"type": "string", "description": "Sigla da UF, ex.: MG"},
                    "ano": {"type": "integer"},
                },
                "required": ["uf", "ano"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calcular",
            "description": "Avalia uma expressão aritmética, ex.: (76900-71400)/71400*100",
            "parameters": {
                "type": "object",
                "properties": {"expressao": {"type": "string"}},
                "required": ["expressao"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "palavra_n",
            "description": "Devolve a n-ésima palavra (começando em 1) de uma frase.",
            "parameters": {
                "type": "object",
                "properties": {"frase": {"type": "string"}, "n": {"type": "integer"}},
                "required": ["frase", "n"],
            },
        },
    },
]

SISTEMA = (
    "Você é um assistente de análise. Use as ferramentas para obter dados e fazer contas; "
    "não invente números. Se a ferramenta não tiver o dado, diga isso. Responda em português."
)

# ---------------------------------------------------------------------------
# Conversa com o modelo (HTTP puro, para enxergar o que trafega)
# ---------------------------------------------------------------------------


def chamar_modelo(mensagens, com_ferramentas=True):
    corpo = {"model": MODELO, "messages": mensagens, "stream": False, "think": False,
             "options": {"temperature": 0}}
    if com_ferramentas:
        corpo["tools"] = ESQUEMAS
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=json.dumps(corpo).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())["message"]


def executar(nome, argumentos):
    """Ponto único de execução: aqui entram validação, permissão e auditoria."""
    if nome not in FERRAMENTAS:
        return json.dumps({"erro": f"ferramenta '{nome}' não permitida"})
    try:
        return FERRAMENTAS[nome](**argumentos)
    except TypeError as e:
        return json.dumps({"erro": f"argumentos inválidos: {e}"})


def agente(pergunta, com_ferramentas=True):
    mensagens = [{"role": "system", "content": SISTEMA}, {"role": "user", "content": pergunta}]
    for passo in range(1, MAX_PASSOS + 1):
        msg = chamar_modelo(mensagens, com_ferramentas)
        mensagens.append(msg)
        pedidos = msg.get("tool_calls") or []
        if not pedidos:
            return msg.get("content", "").strip()
        for p in pedidos:
            nome, args = p["function"]["name"], p["function"]["arguments"]
            resultado = executar(nome, args)
            # trilha de auditoria: quem pediu o quê, com quais argumentos, e o que voltou
            print(f"  [passo {passo}] modelo pede  → {nome}({json.dumps(args, ensure_ascii=False)})")
            print(f"  [passo {passo}] harness devolve ← {resultado}")
            mensagens.append({"role": "tool", "name": nome, "content": resultado})
    return "(limite de passos atingido — o laço foi interrompido pelo harness)"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ferramentas = "--sem-ferramentas" not in sys.argv
    perguntas = args or [
        input("Pergunta: "),
    ]
    for q in perguntas:
        t0 = time.time()
        print(f"\nPergunta: {q}\n(modelo={MODELO}, ferramentas={'sim' if ferramentas else 'não'})")
        print("\nResposta:\n" + agente(q, ferramentas))
        print(f"\n({time.time() - t0:.1f}s)")
