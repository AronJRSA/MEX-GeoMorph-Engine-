import os
import sys
import numpy as np
import pandas as pd
import simplekml
import shapely.geometry as geom
from config.settings import PATHS, MUNICIPIO_CONFIG, MONTE_CARLO
from modules.ingestion import cargar_geometria_municipio, cargar_puntos_txt
from modules.modeling import generar_malla_municipal, proyectar_contorno_a_relieve
from modules.visualization import exportar_3d_interactivo, exportar_curvas_nivel

def generar_kml_simulacion(municipio_poly, ruta_salida):
    kml = simplekml.Kml()
    min_x, min_y, max_x, max_y = municipio_poly.bounds
    
    puntos_conteo = 0
    while puntos_conteo < MONTE_CARLO.get("n_puntos", 5000):
        rx = np.random.uniform(min_x, max_x)
        ry = np.random.uniform(min_y, max_y)
        punto = geom.Point(rx, ry)
        
        if municipio_poly.contains(punto):
            kml.newpoint(name=f"P_{puntos_conteo}", coords=[(rx, ry)])
            puntos_conteo += 1

    kml.save(ruta_salida)
def runner():


    # 1. Cargar Geometría del Municipio
    municipio_poly = cargar_geometria_municipio(
        PATHS["shp"], 
        indice_municipio=MUNICIPIO_CONFIG.get('id_inegi', 28)
    )

    if municipio_poly is None:

        sys.exit()



    # 2. Verificar si ya existe el TXT de la web
    ruta_txt = os.path.join(PATHS["input"], "SLP_SAS.txt")
    
    if not os.path.exists(ruta_txt):

        ruta_kml_output = os.path.join(PATHS["output"], "Puntos_Simulacion_Zaragoza.kml")
        
        # Generar el KML real
        generar_kml_simulacion(municipio_poly, ruta_kml_output)
        
        print("\n txt necesario")

        sys.exit()

    # 3. Iniciar Modelado solo si el TXT ya existe

    x, y, z = cargar_puntos_txt(ruta_txt)

    grid_data = generar_malla_municipal(x, y, z, municipio_poly)
    lon_b, lat_b, z_borde = proyectar_contorno_a_relieve(municipio_poly, x, y, z)

    # 4. Exportación de Resultados
    if not os.path.exists(PATHS["output"]): 
        os.makedirs(PATHS["output"])

    nombre_m = MUNICIPIO_CONFIG.get('nombre', 'San Luis Potosí')
    
    exportar_3d_interactivo(
        grid_data, lon_b, lat_b, z_borde, 
        os.path.join(PATHS["output"], f"{nombre_m}_3D_Profesional.html")
    )
    
    exportar_curvas_nivel(
        grid_data, municipio_poly, 
        os.path.join(PATHS["output"], f"{nombre_m}_Curvas_Nivel.png")
    )

    print(f"\n PROCESO FINALIZADO")

if __name__ == "__main__":
    runner()
