Estudio de caso (Bogotá)

Proyecto listo para ejecutar localmente 
## Estructura
```
Proyecto_optimizacion_transporte_publico/
├── data/
│   └── sample_posts.csv
├── outputs/                # aquí se generan gráficos y tablas
├── src/
│   ├── scrape.py           # Selenium (con modo offline por CSV)
│   ├── nlp.py              # Análisis (spaCy o fallback basado en reglas)
│   ├── optimize.py         # Generación de propuestas
│   └── report.py           # Gráficos/tablas
├── tests/
│   └── test_pipeline.py    # PyTest + Hypothesis
├── main.py                 # Orquestación del pipeline
└── requirements.txt
```

## Uso rápido
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m spacy download es_core_news_sm  # opcional si desea spaCy

# Ejecutar pipeline (modo offline por CSV)
python main.py

# Ejecutar pruebas
pytest -v
```
