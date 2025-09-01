from __future__ import annotations
import os
from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt

def save_issues_table(issues: Dict[str, int], out_csv: str):
    df = pd.DataFrame(sorted(issues.items(), key=lambda kv: kv[1], reverse=True), columns=["ubicacion", "incidencias"])
    df.to_csv(out_csv, index=False)
    return df

def plot_issues_bar(issues: Dict[str, int], out_png: str):
    items = sorted(issues.items(), key=lambda kv: kv[1], reverse=True)[:10]
    if not items:
        return
    labels, values = zip(*items)
    plt.figure(figsize=(8, 4.5))
    plt.bar(labels, values)
    plt.xticks(rotation=30, ha="right")
    plt.title("Top de ubicaciones con más menciones")
    plt.tight_layout()
    plt.savefig(out_png, dpi=160)
    plt.close()

def save_optimizations(optimizations, out_txt: str):
    with open(out_txt, "w", encoding="utf-8") as f:
        for line in optimizations:
            f.write(line + "\n")
