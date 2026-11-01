"""
Chat com o pipeline de guardrails (DLP + modelo-juiz de entrada + modelo principal + modelo-juiz de saída).

    python guardrail_main.py        # abre o chat no terminal; digite "exit" para sair

Os modelos usados estão em config.py (Ollama local). Use apenas dados públicos ou fictícios.
"""

import argparse

if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()

    from guardrail_agents import GuardrailPipeline  # importado depois, para o --help ser rápido

    pipeline = GuardrailPipeline()

    while True:

        print()

        prompt = input("Você: ")

        if prompt.lower() == "exit":
            break

        resposta = pipeline.run(prompt)

        print()
        print("IA:")
        print(resposta)
