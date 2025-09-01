from __future__ import annotations
from collections import Counter
from typing import Dict, Iterable

# Intentamos usar spaCy; si falla, empleamos un analizador por reglas
def _spacy_analyze(texts: Iterable[str]) -> Dict[str, int]:
    import spacy
    try:
        nlp = spacy.load("es_core_news_sm")
    except Exception as e:
        raise RuntimeError("spaCy está instalado pero el modelo 'es_core_news_sm' no. "
                           "Ejecute: python -m spacy download es_core_news_sm") from e
    issues = Counter()
    for txt in texts:
        doc = nlp(txt)
        for ent in doc.ents:
            if ent.label_ in ("LOC", "GPE"):
                issues[ent.text] += 1
    return dict(issues)

def _rule_based_analyze(texts: Iterable[str]) -> Dict[str, int]:
    barrios = [
        "Suba", "Kennedy", "Usaquén", "Chapinero", "Engativá", "Fontibón",
        "Bosa", "Teusaquillo", "San Cristóbal", "Ciudad Bolívar", "Usme",
        "Mártires", "Antonio Nariño", "Puente Aranda", "Rafael Uribe", "Barrios Unidos",
        "Tunjuelito", "La Candelaria", "Santa Fe"
    ]
    # normalización simple
    import re
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, barrios)) + r")\b", flags=re.IGNORECASE)
    counter = Counter()
    for txt in texts:
        for m in pattern.finditer(txt):
            counter[m.group(1).title()] += 1
    return dict(counter)

def analyze_data(texts: Iterable[str]) -> Dict[str, int]:
    try:
        # Si spaCy está disponible y el modelo está cargado, úselo
        import spacy  # noqa: F401
        return _spacy_analyze(texts)
    except Exception:
        # Fallback por reglas
        return _rule_based_analyze(texts)
