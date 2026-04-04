# Archivo: ingestion.py
import pandas as pd
import geopandas as gpd
import xml.etree.ElementTree as ET
import os

# Parche crítico para evitar errores si falta el archivo .shx
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

def cargar_puntos_txt(ruta_archivo):
    """
    Lee los puntos de elevación desde un archivo TXT.
    Limpia los nombres de las columnas para evitar errores de espacios.
    """
    try:
        df = pd.read_csv(ruta_archivo, sep=None, engine='python')
        # Limpieza de espacios en blanco en los encabezados
        df.columns = [c.strip() for c in df.columns]
        
        x = df['longitude'].values
        y = df['latitude'].values
        z = df['altitude (m)'].values

        return x, y, z
    except Exception as e:
        return None, None, None

def cargar_geometria_municipio(ruta_shp, indice_municipio=28):
    """
    Carga el Shapefile del INEGI y lo proyecta a coordenadas globales (WGS84).
   
    """
    try:
        gdf = gpd.read_file(ruta_shp)
        
        # Si el archivo no tiene sistema de coordenadas, asignamos el de INEGI (EPSG:6362)
        if gdf.crs is None:
            gdf.set_crs(epsg=6362, inplace=True)
            
        # Convertir a Latitud/Longitud para que coincida con el GPS
        gdf = gdf.to_crs(epsg=4326)
        
        municipio_poly = gdf.geometry.values[indice_municipio]
        
        return municipio_poly
    except Exception as e:

        return None

def extraer_vertices_kml(ruta_kml):
    """
    Extrae las coordenadas de un archivo KML para definir áreas de interés.
   
    """
    try:
        tree = ET.parse(ruta_kml)
        root = tree.getroot()
        ns = {"kml": "http://www.opengis.net/kml/2.2"}
        
        puntos = []
        for pm in root.findall(".//kml:Placemark", ns):
            coords = pm.find(".//kml:coordinates", ns)
            if coords is not None:
                c_text = coords.text.strip().replace('\n', '').replace('\t', '')
                c_list = c_text.split(",")
                puntos.append((float(c_list[0]), float(c_list[1])))
        return puntos
    except Exception as e:

        return []