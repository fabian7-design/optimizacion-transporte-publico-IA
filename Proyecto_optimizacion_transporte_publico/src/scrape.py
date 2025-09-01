from __future__ import annotations
from dataclasses import dataclass
from typing import List
import time
import os
import pandas as pd

# Intentamos importar Selenium; si no está disponible, el modo offline sigue funcionando
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
except Exception:
    webdriver = None
    By = None
    Service = None
    Options = None

@dataclass
class Post:
    texto: str
    fecha: str
    fuente: str = "X/Twitter"

def setup_selenium(chromedriver_path: str | None = None, headless: bool = True):
    if webdriver is None:
        raise RuntimeError("Selenium no está disponible en este entorno.")
    options = Options()
    options.headless = headless
    service = Service(chromedriver_path) if chromedriver_path else Service()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def collect_data(driver, url: str) -> List[str]:
    driver.get(url)
    time.sleep(5)  # Espera a que cargue
    tweets = driver.find_elements(By.CSS_SELECTOR, 'article')
    return [t.text for t in tweets]

def collect_data_offline(csv_path: str) -> List[str]:
    df = pd.read_csv(csv_path)
    return df['texto'].astype(str).tolist()

if __name__ == "__main__":
    # Ejemplo de uso offline (por defecto)
    here = os.path.dirname(__file__)
    csv_path = os.path.join(os.path.dirname(here), "data", "sample_posts.csv")
    textos = collect_data_offline(csv_path)
    print(f"Ejemplos cargados: {len(textos)}")
    print(textos[:3])
