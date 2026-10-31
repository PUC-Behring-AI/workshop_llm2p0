"""
Próximo token — as probabilidades de verdade, 100% local (Ollama), só biblioteca padrão.

Plano B offline para o demo "Next Token Prediction" do Hugging Face, e com uma
vantagem: usa modelos que entendem português (o demo online usa o GPT-2 de 2019).

    python proximo_token.py "A capital do Brasil é"
    python proximo_token.py --modelo falcon:text "Era uma vez"
    python proximo_token.py --gerar 12 "O ICMS é um imposto"     # escolhe o mais provável, passo a passo
    python proximo_token.py --gerar 12 --temperatura 1 "O ICMS é um imposto"   # amostra pela distribuição

Usamos o modo "raw" do Ollama: o texto vai ao modelo SEM o molde de chat, ou seja,
o modelo apenas continua o texto — exatamente a tarefa da seção 06.
"""

import argparse
import json
import math
import random
import urllib.request

OLLAMA_URL = "http://localhost:11434"


def proximos_tokens(modelo: str, texto: str, k: int = 10):
    corpo = {
        "model": modelo, "prompt": texto, "raw": True, "stream": False,
        "think": False, "logprobs": True, "top_logprobs": k,
        "options": {"num_predict": 1, "temperature": 0},
    }
    req = urllib.request.Request(f"{OLLAMA_URL}/api/generate", json.dumps(corpo).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        dados = json.loads(r.read())
    return [(t["token"], math.exp(t["logprob"])) for t in dados["logprobs"][0]["top_logprobs"]]


def mostrar(texto, candidatos):
    print(f"\nTexto: {texto!r}\n")
    for tok, p in candidatos:
        print(f"  {p:7.2%}  {'█' * round(p * 40):<40}  {tok!r}")
    print(f"\n  (soma dos {len(candidatos)} candidatos: {sum(p for _, p in candidatos):.1%})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("texto")
    ap.add_argument("--modelo", default="qwen3:8b")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--gerar", type=int, default=0, help="quantos tokens gerar, um a um")
    ap.add_argument("--temperatura", type=float, default=0.0)
    a = ap.parse_args()

    texto = a.texto
    for _ in range(max(a.gerar, 1)):
        cands = proximos_tokens(a.modelo, texto, a.k)
        mostrar(texto, cands)
        if not a.gerar:
            break
        if a.temperatura <= 0:
            tok = cands[0][0]
        else:  # reamostra os k candidatos com a temperatura pedida
            pesos = [p ** (1 / a.temperatura) for _, p in cands]
            tok = random.choices([t for t, _ in cands], weights=pesos)[0]
        print(f"  → escolhido: {tok!r}")
        texto += tok
    print(f"\nTexto final: {texto}")
