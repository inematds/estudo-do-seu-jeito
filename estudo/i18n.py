"""Textos do app do aluno, do placar e dos métodos em PT, EN e ES.

O idioma vem do materia.json (campo "idioma": "pt", "en" ou "es"; sem o campo = "pt"). Chave que faltar num idioma
cai no texto em português, para o app nunca ficar com buraco.
"""
import json
from functools import lru_cache
from importlib import resources

IDIOMAS = ("pt", "en", "es")
LANG_HTML = {"pt": "pt-BR", "en": "en", "es": "es"}


@lru_cache(maxsize=None)
def _carregar(idioma: str) -> dict:
    return json.loads((resources.files("estudo") / f"i18n_{idioma}.json").read_text(encoding="utf-8"))


def idioma_de(materia: dict) -> str:
    i = (materia or {}).get("idioma", "pt")
    return i if i in IDIOMAS else "pt"


def textos(idioma: str) -> dict:
    """Devolve {"app": {...}, "placar": {...}, "metodos": {...}} já completado com o PT onde faltar."""
    base = _carregar("pt")
    if idioma not in IDIOMAS or idioma == "pt":
        return base
    outro = _carregar(idioma)
    saida = {}
    for parte, valores in base.items():
        if parte == "metodos":
            saida[parte] = {m: {**d, **outro.get(parte, {}).get(m, {})} for m, d in valores.items()}
        else:
            saida[parte] = {**valores, **outro.get(parte, {})}
    return saida
