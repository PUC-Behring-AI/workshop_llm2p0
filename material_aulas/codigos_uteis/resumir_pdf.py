"""
Resumir um PDF com LLM local — Experimento E (seção 09.1).

PDF  →  Apache Tika (extrai o texto)  →  LLM local (resume)

    pip install tika            # precisa de Java 8+ (o Tika roda como um servidor Java local)
    python resumir_pdf.py parecer_limpo.pdf
    python resumir_pdf.py parecer_contaminado.pdf
    python resumir_pdf.py parecer_contaminado.pdf -m llama3:8b     # escolhe o modelo (padrão: qwen3:8b)
    python resumir_pdf.py --listar                                 # modelos instalados no Ollama

Na primeira chamada o tika-python baixa o tika-server.jar (precisa de internet).
O modelo roda local (Ollama): nada sai desta máquina.
"""

import argparse
import json
import textwrap
import time
import urllib.request

OLLAMA_URL = "http://localhost:11434"
MODELO_PADRAO = "qwen3:8b"


def modelos_instalados():
    with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=10) as r:
        return sorted(m["name"] for m in json.loads(r.read())["models"])


def extrair_texto(caminho_pdf):
    from tika import parser  # import aqui para o --help funcionar mesmo sem o Tika instalado

    return (parser.from_file(caminho_pdf).get("content") or "").strip()


def resumir(texto, modelo):
    corpo = {
        "model": modelo,
        "messages": [{"role": "user", "content": f"Resuma o documento abaixo em até 5 linhas.\n\n{texto}"}],
        "stream": False, "think": False,
        "options": {"temperature": 0, "num_predict": 400},
    }
    req = urllib.request.Request(f"{OLLAMA_URL}/api/chat", json.dumps(corpo).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())["message"]["content"].strip()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", nargs="?", help="arquivo PDF a resumir")
    ap.add_argument("-m", "--modelo", default=MODELO_PADRAO, help=f"modelo do Ollama (padrão: {MODELO_PADRAO})")
    ap.add_argument("--listar", action="store_true", help="lista os modelos instalados e sai")
    a = ap.parse_args()

    instalados = modelos_instalados()
    if a.listar:
        print("\n".join(instalados))
        raise SystemExit
    if not a.pdf:
        ap.error("informe o PDF (ou use --listar)")
    if a.modelo not in instalados:
        raise SystemExit(f"Modelo '{a.modelo}' não está instalado. Disponíveis:\n  " + "\n  ".join(instalados))

    linha = "─" * 64
    print(f"{linha}\n Resumo de PDF com LLM local\n Arquivo: {a.pdf}\n Modelo:  {a.modelo}\n{linha}\n")

    print("[1/2] Lendo o PDF com Apache Tika ...  (na 1ª vez sobe o servidor Java)", flush=True)
    t0 = time.perf_counter()
    texto = extrair_texto(a.pdf)
    print(f"      ✓ {len(texto)} caracteres extraídos ({time.perf_counter() - t0:.1f} s)\n", flush=True)

    print(f"[2/2] Gerando o resumo com {a.modelo} ...", flush=True)
    t0 = time.perf_counter()
    resumo = resumir(texto, a.modelo)
    print(f"      ✓ pronto ({time.perf_counter() - t0:.1f} s)\n", flush=True)

    print("═" * 24 + " RESUMO " + "═" * 24 + "\n")
    print("\n".join(textwrap.fill(par, 78) for par in resumo.splitlines()))
    print("\n" + "═" * 56)
