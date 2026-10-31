"""
Camada DETERMINÍSTICA de prevenção de vazamento (DLP) para prompts e respostas.

Complementa os guardrails baseados em LLM (guardrail_agents.py): um modelo-juiz
é probabilístico e pode ser enganado por prompt injection; uma checagem de dígito
verificador não. Defesa em profundidade = as duas camadas.

Detecta, com validação de dígitos verificadores (menos falsos positivos):
CPF, CNPJ, chave de acesso de NF-e (44 dígitos), e-mail e telefone BR.

    python guardrail_dlp.py        # roda a demonstração
"""

import re

# ---------------------------------------------------------------------------
# Validadores
# ---------------------------------------------------------------------------


def _so_digitos(s: str) -> str:
    return re.sub(r"\D", "", s)


def cpf_valido(s: str) -> bool:
    d = _so_digitos(s)
    if len(d) != 11 or d == d[0] * 11:
        return False
    for tam in (9, 10):
        soma = sum(int(d[i]) * (tam + 1 - i) for i in range(tam))
        if int(d[tam]) != (soma * 10 % 11) % 10:
            return False
    return True


def cnpj_valido(s: str) -> bool:
    d = _so_digitos(s)
    if len(d) != 14 or d == d[0] * 14:
        return False
    for tam, pesos in ((12, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]),
                       (13, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])):
        soma = sum(int(d[i]) * pesos[i] for i in range(tam))
        resto = soma % 11
        if int(d[tam]) != (0 if resto < 2 else 11 - resto):
            return False
    return True


def chave_nfe_valida(s: str) -> bool:
    d = _so_digitos(s)
    if len(d) != 44:
        return False
    soma, peso = 0, 2
    for c in reversed(d[:43]):
        soma += int(c) * peso
        peso = 2 if peso == 9 else peso + 1
    resto = soma % 11
    return int(d[43]) == (0 if resto < 2 else 11 - resto)


# ---------------------------------------------------------------------------
# Padrões (candidatos) + validador (decisão final)
# ---------------------------------------------------------------------------

PADROES = [
    # a ordem importa: o mais específico/longo primeiro
    ("CHAVE_NFE", re.compile(r"(?<!\d)(?:\d[ .]?){43}\d(?!\d)"), chave_nfe_valida),
    ("CNPJ", re.compile(r"(?<!\d)\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}(?!\d)"), cnpj_valido),
    ("CPF", re.compile(r"(?<!\d)\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?!\d)"), cpf_valido),
    ("EMAIL", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"), None),
    ("TELEFONE", re.compile(r"(?<!\d)(?:\+?55\s?)?\(?\d{2}\)?\s?9?\d{4}-?\d{4}(?!\d)"), None),
]


def detectar(texto: str):
    """Devolve lista de (tipo, trecho, início, fim), sem sobreposição."""
    achados, ocupado = [], []
    for tipo, rx, validar in PADROES:
        for m in rx.finditer(texto):
            ini, fim = m.span()
            if any(ini < f and fim > i for i, f in ocupado):
                continue
            if validar and not validar(m.group()):
                continue
            achados.append((tipo, m.group(), ini, fim))
            ocupado.append((ini, fim))
    return sorted(achados, key=lambda a: a[2])


def mascarar(texto: str):
    """Substitui cada achado por [TIPO_n]. Devolve (texto_mascarado, mapa).

    O mapa permite reidentificar a resposta DENTRO do perímetro seguro,
    sem que o dado real tenha passado pelo modelo.
    """
    achados = detectar(texto)
    mapa, contagem, partes, cursor = {}, {}, [], 0
    for tipo, trecho, ini, fim in achados:
        contagem[tipo] = contagem.get(tipo, 0) + 1
        marca = f"[{tipo}_{contagem[tipo]}]"
        mapa[marca] = trecho
        partes.append(texto[cursor:ini])
        partes.append(marca)
        cursor = fim
    partes.append(texto[cursor:])
    return "".join(partes), mapa


def reidentificar(texto: str, mapa: dict) -> str:
    for marca, original in mapa.items():
        texto = texto.replace(marca, original)
    return texto


if __name__ == "__main__":
    exemplo = (
        "Contribuinte 123.456.789-09 (CNPJ 11.222.333/0001-81), contato maria@exemplo.gov.br, "
        "(21) 99876-5432. Número que parece CPF mas é inválido: 123.456.789-00."
    )
    print("ORIGINAL :", exemplo)
    mascarado, mapa = mascarar(exemplo)
    print("MASCARADO:", mascarado)
    print("MAPA     :", mapa)
    print("VOLTA    :", reidentificar(mascarado, mapa))
