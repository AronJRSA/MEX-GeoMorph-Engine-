import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATHS = {
    "input": os.path.join(BASE_DIR, "data", "input"),
    "output": os.path.join(BASE_DIR, "data", "output"),
    "shp": os.path.join(BASE_DIR, "data", "input", "24mun.shp")
}


MUNICIPIO_CONFIG = {
    "nombre": "Zaragoza",
    "id_inegi": 28,  
    "epsg_original": 6362,  
    "epsg_destino": 4326    
}

MODEL_CONFIG = {
    "grid_resolution": 400,  #
    "z_scale": 0.13,          
    "colorscale": "earth",   
    "contour_color": "blue", 
    "contour_width": 1
}

MONTE_CARLO = {
    "n_puntos": 5000,       
    "offset_borde": 20       
}
