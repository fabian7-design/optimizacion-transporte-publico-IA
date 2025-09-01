from __future__ import annotations
import os
from src.scrape import collect_data_offline
from src.nlp import analyze_data
from src.optimize import propose_optimizations
from src.report import save_issues_table, plot_issues_bar, save_optimizations

BASE = os.path.dirname(__file__)
CSV = os.path.join(BASE, "data", "sample_posts.csv")
OUT_DIR = os.path.join(BASE, "outputs")

def main():
    texts = collect_data_offline(CSV)
    issues = analyze_data(texts)
    optimizations = propose_optimizations(issues, threshold=6)
    # Guardar resultados
    os.makedirs(OUT_DIR, exist_ok=True)
    table_csv = os.path.join(OUT_DIR, "tabla_incidencias.csv")
    bar_png = os.path.join(OUT_DIR, "grafico_incidencias.png")
    opt_txt = os.path.join(OUT_DIR, "propuestas.txt")
    df = save_issues_table(issues, table_csv)
    plot_issues_bar(issues, bar_png)
    save_optimizations(optimizations, opt_txt)
    # Resumen por consola
    print("Total de textos analizados:", len(texts))
    print("Ubicaciones detectadas:", len(issues))
    print("Top 5 ubicaciones:")
    print(df.head(5).to_string(index=False))
    print("\nPropuestas:")
    for p in optimizations:
        print("-", p)

if __name__ == "__main__":
    main()
