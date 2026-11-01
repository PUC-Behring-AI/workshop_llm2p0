OLLAMA_URL = "http://localhost:11434"

MAIN_MODEL = "deepseek-r1:14b"
INPUT_GUARD_MODEL = "deepseek-r1:14b"
OUTPUT_GUARD_MODEL = "deepseek-r1:14b"

if __name__ == "__main__":
    import argparse

    argparse.ArgumentParser(
        description="Módulo de apoio: endereço do Ollama e modelos dos guardrails. "
                    "Edite as constantes deste arquivo; para executar o pipeline use  python guardrail_main.py"
    ).parse_args()
