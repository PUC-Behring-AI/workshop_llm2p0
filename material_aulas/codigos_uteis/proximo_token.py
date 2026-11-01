"""
Próximo token — as probabilidades de verdade, 100% local (Ollama), só biblioteca padrão.

Plano B offline para o demo "Next Token Prediction" do Hugging Face, e com uma
vantagem: usa modelos que entendem português (o demo online usa o GPT-2 de 2019).

    python proximo_token.py "A capital do Brasil é"
    python proximo_token.py --modelo falcon:text "Era uma vez"
    python proximo_token.py --gerar 12 "O ICMS é um imposto"     # escolhe o mais provável, passo a passo
    python proximo_token.py --gerar 12 --temperatura 1 "O ICMS é um imposto"   # amostra pela distribuição

Temperatura (seção 07): com --temperatura T o script mostra, ao lado da distribuição original do
modelo, como ela fica depois de aplicar a temperatura T — baixa afunila, alta achata:

    python proximo_token.py -t 0.3 "A capital do Brasil é"        # distribuição pontuda
    python proximo_token.py -t 2   "A capital do Brasil é"        # distribuição achatada
    python proximo_token.py -t 1.5 --amostras 20 "A capital do Brasil é"   # sorteia 20 vezes e conta

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


def aplicar_temperatura(candidatos, temperatura: float):
    """Reaplica a temperatura T às probabilidades: p_i ∝ p_i^(1/T), renormalizado.

    É o mesmo que softmax(logits / T). T < 1 afunila a distribuição; T > 1 achata;
    T = 0 vira "sempre o mais provável". Só vale para os k candidatos mostrados.
    """
    if temperatura <= 0:
        melhor = max(range(len(candidatos)), key=lambda i: candidatos[i][1])
        return [(t, 1.0 if i == melhor else 0.0) for i, (t, _) in enumerate(candidatos)]
    pesos = [p ** (1 / temperatura) for _, p in candidatos]
    total = sum(pesos)
    return [(t, w / total) for (t, _), w in zip(candidatos, pesos)]


def mostrar(texto, candidatos, temperatura=None):
    print(f"\nTexto: {texto!r}\n")
    if temperatura is None:
        for tok, p in candidatos:
            print(f"  {p:7.2%}  {'█' * round(p * 40):<40}  {tok!r}")
        print(f"\n  (soma dos {len(candidatos)} candidatos: {sum(p for _, p in candidatos):.1%})")
        return
    ajustadas = aplicar_temperatura(candidatos, temperatura)
    print(f"  {'original':>8}  {'T=' + format(temperatura, 'g'):>8}")
    for (tok, p), (_, q) in zip(candidatos, ajustadas):
        print(f"  {p:8.2%}  {q:8.2%}  {'█' * round(q * 40):<40}  {tok!r}")
    print(f"\n  (distribuição renormalizada entre os {len(candidatos)} candidatos mostrados)")


def sortear(candidatos, temperatura: float):
    """Escolhe um token pela distribuição já ajustada pela temperatura."""
    ajustadas = aplicar_temperatura(candidatos, temperatura)
    return random.choices([t for t, _ in ajustadas], weights=[q for _, q in ajustadas])[0]


def mostrar_amostras(candidatos, temperatura: float, n: int):
    contagem = {}
    for _ in range(n):
        tok = sortear(candidatos, temperatura)
        contagem[tok] = contagem.get(tok, 0) + 1
    print(f"\n  {n} sorteios com T={temperatura:g}:")
    for tok, c in sorted(contagem.items(), key=lambda x: -x[1]):
        print(f"  {c:4d}  {'█' * round(40 * c / n):<40}  {tok!r}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("texto")
    ap.add_argument("--modelo", default="qwen3:8b")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--gerar", type=int, default=0, help="quantos tokens gerar, um a um")
    ap.add_argument("-t", "--temperatura", type=float, default=None,
                    help="temperatura (0 = sempre o mais provável; 1 = distribuição original do modelo). "
                         "Sem ela, mostra só a distribuição original e --gerar escolhe o mais provável")
    ap.add_argument("--amostras", type=int, default=0,
                    help="sorteia N vezes o próximo token (usa a temperatura; 1 se não for dada)")
    a = ap.parse_args()

    texto = a.texto
    for _ in range(max(a.gerar, 1)):
        cands = proximos_tokens(a.modelo, texto, a.k)
        mostrar(texto, cands, a.temperatura)
        if a.amostras:
            mostrar_amostras(cands, 1.0 if a.temperatura is None else a.temperatura, a.amostras)
        if not a.gerar:
            break
        tok = cands[0][0] if not a.temperatura else sortear(cands, a.temperatura)
        print(f"  → escolhido: {tok!r}")
        texto += tok
    print(f"\nTexto final: {texto}")
