# Archivo: modeling.py
import numpy as np
from scipy.interpolate import griddata

def generar_malla_municipal(x, y, z, municipio_poly):

    # 1. Extraer límites del municipio para la malla
    min_lon, min_lat, max_lon, max_lat = municipio_poly.bounds
    res = 300 # El GRID_RES que tenías

    grid_x, grid_y = np.meshgrid(
        np.linspace(min_lon, max_lon, res),
        np.linspace(min_lat, max_lat, res)
    )

    # 2. Interpolación Híbrida (La magia contra el derretimiento)
    gz_linear = griddata((x, y), z, (grid_x, grid_y), method='linear')
    gz_nearest = griddata((x, y), z, (grid_x, grid_y), method='nearest')

    # Combinación: Donde falla el lineal, entra el nearest
    grid_z = np.where(np.isnan(gz_linear), gz_nearest, gz_linear)

    return grid_x, grid_y, grid_z

def proyectar_contorno_a_relieve(municipio_poly, x, y, z):

    if hasattr(municipio_poly, 'exterior'):
        coords_borde = list(municipio_poly.exterior.coords)
    else:
        coords_borde = list(municipio_poly.geoms[0].exterior.coords)

    lon_b, lat_b = zip(*coords_borde)

    # Proyectamos + 5m para que no se entierre
    z_borde = griddata((x, y), z, (lon_b, lat_b), method='nearest') + 5

    return lon_b, lat_b, z_borde
