# Archivo: visualization.py
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import MODEL_CONFIG, MUNICIPIO_CONFIG

def exportar_3d_interactivo(grid_data, lon_b, lat_b, z_borde, ruta_salida):
    grid_x, grid_y, grid_z = grid_data
    fig = go.Figure()

    # 1. El Terreno
    fig.add_trace(go.Surface(
        x=grid_x, y=grid_y, z=grid_z,
        colorscale=MODEL_CONFIG["colorscale"],
        name='Relieve Terrestre',
        colorbar=dict(title="msnm")
    ))

    # 2. El Contorno
    fig.add_trace(go.Scatter3d(
        x=lon_b, y=lat_b, z=z_borde,
        mode='lines',
        line=dict(
            color=MODEL_CONFIG["contour_color"], 
            width=MODEL_CONFIG["contour_width"]
        ),
        name='Límite Municipal'
    ))

    # 3. Configuración de la Escena
    nombre_mun = MUNICIPIO_CONFIG.get('nombre', 'San Luis Potosí')
    
    fig.update_layout(
        title=f"Modelado 3D - {nombre_mun}",
        template="plotly_dark",
        scene=dict(
            aspectratio=dict(x=1, y=1, z=MODEL_CONFIG["z_scale"]),
            xaxis=dict(title="Longitud"),
            yaxis=dict(title="Latitud"),
            zaxis=dict(title="Altitud (m)")
        ),
        margin=dict(l=0, r=0, b=0, t=50)
    )

    fig.write_html(ruta_salida)


def exportar_curvas_nivel(grid_data, municipio_poly, ruta_salida):
    grid_x, grid_y, grid_z = grid_data
    fig, ax = plt.subplots(figsize=(12, 10), facecolor='white')

    # 1. Dibujar el límite del municipio
    if hasattr(municipio_poly, 'exterior'):
        bx, by = municipio_poly.exterior.xy
        ax.plot(bx, by, color='black', linewidth=2, zorder=5)
    else:
        for part in municipio_poly.geoms:
            bx, by = part.exterior.xy
            ax.plot(bx, by, color='black', linewidth=2, zorder=5)

    # 2. Dibujar curvas de nivel
    contorno = ax.contour(
        grid_x, grid_y, grid_z, 
        levels=15, 
        cmap='viridis', 
        linewidths=0.8, 
        zorder=2
    )

    # 3. Etiquetas de altitud
    ax.clabel(contorno, inline=True, fontsize=8, fmt='%1.0f', colors='black')
    nombre_mun = MUNICIPIO_CONFIG.get('nombre', 'Zaragoza')
    ax.set_title(f"Mapa Topográfico: {nombre_mun}", fontsize=15)
    
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
