# MEX-GeoMorph-Engine
#  
### **Automated Topographic Modeling & 3D Visualization Pipeline**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Engine: GeoPandas](https://img.shields.io/badge/Engine-GeoPandas-green.svg)](https://geopandas.org/)

---

## English Description

**MEX-GeoMorph-Engine** is a high-performance data engineering pipeline designed to transform **INEGI Geostatistical Framework** vectors and topographic datasets into high-precision 3D models and interactive technical cartography.

### National Scalability & Architecture
* **Federal Scope:** Compatible with the official data structure of the Mexican Republic. Simply link the dataset of any state or municipality to process its topography automatically.
* **Modular Pipeline:** Standardized ingestion, spatial join, and normalization of **SHP, KML, and TXT** files.
* **Case Study (Zaragoza, SLP):** Selected as a technical benchmark due to its complex mountainous terrain, ideal for stress-testing interpolation algorithms and 3D relief accuracy.

### Key Outputs
1. **Interactive 3D Model:** Plotly-based HTML visualization for terrain analysis.
2. **Monte Carlo Simulation:** Spatial distribution of thousands of points to validate model density.
3. **Topographic Contour Maps:** PNG/PDF technical maps with elevation labels, ready for GIS integration.

---

## Descripción en Español

**MEX-GeoMorph-Engine** es un pipeline de ingeniería de datos diseñado para transformar vectores del **Marco Geoestadístico del INEGI** y conjuntos de datos topográficos en modelos 3D de alta precisión y cartografía técnica interactiva, permite conocer la topografía de cualquier municipio de México, a través de curvas de nivel y modelado 3E.

### Escalabilidad Nacional y Arquitectura
* **Alcance Federal:** Compatible con la estructura de datos oficial de la República Mexicana. Basta con vincular el dataset de cualquier estado o municipio para procesar su topografía de forma automática.
* **Pipeline Modular:** Ingesta, unión espacial y normalización estandarizada de archivos **SHP, KML y TXT**.
* **Caso de Estudio (Zaragoza, SLP):** Seleccionado como benchmark técnico debido a su compleja orografía montañosa, ideal para validar algoritmos de interpolación y precisión de relieve 3D.

---

## Visual Results / Resultados Visuales

### 1. Interactive 3D Terrain / Modelo 3D Interactivo
> ![3D Model](Imagenes_MEX-GeoMorph-Engine/3d.png)

### 2. Monte Carlo Spatial Validation / Validación Espacial Monte Carlo
> ![Monte Carlo](Imagenes_MEX-GeoMorph-Engine/Simulacion_Montecarlo_vist_kml.png)

### 3. Contour Map / Mapa de Curvas de Nivel
> ![Contour Map](Imagenes_MEX-GeoMorph-Engine/Zaragoza_Curvas_Nivel.png)

## Stack & Structure

* **Language:** `Python 3.x`
* **GIS:** `GeoPandas`, `Shapely`, `PyProj`.
* **Data Science:** `Pandas`, `NumPy`, `SciPy` (RBF Interpolation).
* **Visualization:** `Matplotlib`, `Plotly`, `Folium`.
### Project Structure
```text
├── config/
│   └── settings.py      # Parámetros globales e ID selection
├── data/
│   ├── raw/             # Insumos originales (SHP, KML, TXT)
│   └── output/          # Resultados generados
├── modules/
│   ├── ingestion.py     # Limpieza de datos y SHP processing
│   ├── modeling.py      # Lógica de Monte Carlo e Interpolación
│   └── visualization.py # Generación de visuales 3D y Contornos
├── main.py              # Script principal de ejecución
└── README.md            # Documentación
