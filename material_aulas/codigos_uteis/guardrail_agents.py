# --help antes dos imports pesados (langchain), para funcionar em qualquer ambiente
if __name__ == "__main__":
    import argparse

    argparse.ArgumentParser(
        description="Módulo de apoio do pipeline de guardrails (classe GuardrailPipeline). "
                    "Não é executado diretamente: use  python guardrail_main.py"
    ).parse_args()

import json
import re

from langchain_ollama import ChatOllama

from guardrail_prompts import *
from guardrail_dlp import mascarar, detectar
from config import *


# ---------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------

def split_thinking(text: str):
    """
    Separa o conteúdo do <think> da resposta final.
    """

    think = ""

    match = re.search(
        r"<think>(.*?)</think>",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    if match:
        think = match.group(1).strip()
        text = re.sub(
            r"<think>.*?</think>",
            "",
            text,
            flags=re.DOTALL | re.IGNORECASE,
        )

    return think, text.strip()


def extract_json(text: str):
    """
    Extrai apenas o primeiro objeto JSON encontrado.
    """

    text = text.replace("```json", "")
    text = text.replace("```", "")

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)

    if match is None:
        raise ValueError(
            "Nenhum JSON encontrado.\n\nResposta recebida:\n"
            + text
        )

    return json.loads(match.group())


# ---------------------------------------------------------
# Input Guard
# ---------------------------------------------------------

class InputGuard:

    def __init__(self):

        self.llm = ChatOllama(
            model=INPUT_GUARD_MODEL,
            base_url=OLLAMA_URL,
            temperature=0,
            # format="json",
        )

    def evaluate(self, user_text):

        response = self.llm.invoke(
            INPUT_GUARD_PROMPT +
            "\n\nMensagem:\n" +
            user_text
        )

        raw = response.content

        think, cleaned = split_thinking(raw)

        if think:
            print("\n========== INPUT THINK ==========\n")
            print(think)

        print("\n========== INPUT RAW ==========\n")
        print(cleaned)

        return extract_json(cleaned)


# ---------------------------------------------------------
# Output Guard
# ---------------------------------------------------------

class OutputGuard:

    def __init__(self):

        self.llm = ChatOllama(
            model=OUTPUT_GUARD_MODEL,
            base_url=OLLAMA_URL,
            temperature=0,
            # format="json",
        )

    def evaluate(self, llm_answer):

        response = self.llm.invoke(
            OUTPUT_GUARD_PROMPT +
            "\n\nResposta:\n" +
            llm_answer
        )


        raw = response.content
        

        think, cleaned = split_thinking(raw)

        if think:
            print("\n========== OUTPUT THINK ==========\n")
            print(think)

        print("\n========== OUTPUT RAW ==========\n")
        print(cleaned)

        return extract_json(cleaned)


# ---------------------------------------------------------
# Modelo principal
# ---------------------------------------------------------

class MainAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model=MAIN_MODEL,
            base_url=OLLAMA_URL,
            temperature=0.7,
        )

    def invoke(self, prompt):

        response = self.llm.invoke(prompt)

        raw = response.content

        think, cleaned = split_thinking(raw)

        if think:
            print("\n========== MAIN THINK ==========\n")
            print(think)

        return cleaned


# ---------------------------------------------------------
# Pipeline
# ---------------------------------------------------------

class GuardrailPipeline:

    def __init__(self):

        self.input_guard = InputGuard()
        self.main = MainAgent()
        self.output_guard = OutputGuard()

    def run(self, prompt):

        print("\n" + "=" * 70)
        print("INPUT")
        print("=" * 70)
        print(prompt)

        # Camada 0 (determinística): dados pessoais/fiscais são mascarados ANTES
        # de chegar a qualquer modelo — inclusive os juízes.
        prompt, mapa = mascarar(prompt)
        if mapa:
            print("\n========== DLP (entrada) ==========\n")
            print(f"{len(mapa)} dado(s) sensível(is) mascarado(s): {list(mapa)}")

        result = self.input_guard.evaluate(prompt)

        print("\n========== INPUT GUARD ==========\n")
        print(result)

        if not result["approved"]:

            return (
                "Pergunta bloqueada.\n"
                f"Motivo: {result['reason']}"
            )

        response = self.main.invoke(prompt)

        print("\n========== MAIN MODEL ==========\n")
        print(response)

        # Camada determinística também na saída: o modelo pode ter inventado
        # (ou memorizado) um CPF/CNPJ válido.
        vazados = detectar(response)
        if vazados:
            return (
                "Resposta bloqueada pelo DLP.\n"
                f"Motivo: continha {len(vazados)} dado(s) sensível(is): "
                + ", ".join(sorted({t for t, *_ in vazados}))
            )

        result = self.output_guard.evaluate(response)

        print("\n========== OUTPUT GUARD ==========\n")
        print(result)

        if not result["approved"]:

            return (
                "Resposta bloqueada pelo guardrail.\n"
                f"Motivo: {result['reason']}"
            )

        print("\n========== FINAL ==========\n")

        return response
