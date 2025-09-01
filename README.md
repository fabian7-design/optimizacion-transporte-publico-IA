# Optimización del Transporte Público con IA

Este proyecto implementa un prototipo de **optimización del transporte público en Bogotá** utilizando técnicas de Inteligencia Artificial (IA), con el objetivo de demostrar cómo la tecnología puede contribuir significativamente sin necesidad de grandes inversiones en infraestructura física.

## 🚀 Objetivo
Analizar publicaciones textuales relacionadas con transporte público para identificar patrones de incidencias por ubicación y generar propuestas de mejora.

## 📂 Estructura del proyecto
```
Proyecto_optimizacion_transporte_publico/
│── data/
│   └── sample_posts.csv
│── outputs/
│   ├── grafico_incidencias.png
│   ├── propuestas.txt
│   └── tabla_incidencias.csv
│── src/
│   ├── scrape.py
│   ├── nlp.py
│   ├── optimize.py
│   └── report.py
│── tests/
│   └── test_pipeline.py
│── main.py
│── requirements.txt
│── README.md
```

## ⚙️ Instalación y configuración
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/optimizacion-transporte-publico-IA.git
   cd optimizacion-transporte-publico-IA
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows
   source .venv/bin/activate  # En Linux/Mac
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución
Ejecutar el pipeline principal con:
```bash
python main.py
```

Esto generará en la carpeta `outputs/`:
- `tabla_incidencias.csv` → tabla con las incidencias por ubicación.
- `grafico_incidencias.png` → gráfico de barras con las principales incidencias.
- `propuestas.txt` → archivo con propuestas de optimización.

## 🧪 Pruebas automatizadas
El proyecto incluye **tests con PyTest e Hypothesis**. Para ejecutarlos:
```bash
pytest
```

## 📊 Resultados esperados
- Total de textos analizados.
- Número de ubicaciones detectadas.
- Top 5 de ubicaciones con mayor número de incidencias.
- Propuestas automáticas de optimización basadas en los patrones encontrados.

## 👨‍💻 Tecnologías utilizadas
- Python 3.12
- Pandas
- Matplotlib
- PyTest
- Hypothesis

## 📌 Autor
Proyecto académico desarrollado por Luis Fabian Diaz como parte de las actividades de **Inteligencia Artificial aplicada al análisis de datos y sistemas distribuidos**.
