from __future__ import annotations
from typing import Dict, List, Tuple

def propose_optimizations(issues: Dict[str, int], threshold: int = 5) -> List[str]:
    suggestions = []
    for location, count in sorted(issues.items(), key=lambda kv: kv[1], reverse=True):
        if count >= threshold:
            suggestions.append(f"Aumentar la frecuencia de buses en {location} (incidencias: {count})")
    # Algunas reglas adicionales ilustrativas
    if not suggestions and issues:
        top_loc, top_cnt = max(issues.items(), key=lambda kv: kv[1])
        suggestions.append(f"Piloto de refuerzo en hora pico en {top_loc} (incidencias: {top_cnt})")
    return suggestions
