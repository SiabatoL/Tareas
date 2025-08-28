import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters, feature, morphology, measure

def procesar_imagen(ruta_imagen):
    # Cargar la imagen
    image = io.imread(ruta_imagen)

    # Convertir a escala de grises si es necesario (RGB o RGBA → gris)
    if image.ndim == 3:
        if image.shape[2] == 4:  # RGBA
            image = color.rgba2rgb(image)
        gray_image = color.rgb2gray(image)
    else:
        gray_image = image

    # 1. Suavizar con filtro Gaussiano
    gray_smooth = filters.gaussian(gray_image, sigma=1)

    # 2. Detectar bordes con Canny
    edges = feature.canny(gray_smooth, sigma=2)

    # 3. Limpiar bordes (eliminar ruido pequeño)
    edges = morphology.remove_small_objects(edges, min_size=100)

    # 4. Encontrar contornos
    contours = measure.find_contours(edges, level=0.5)

    # Escalado y desplazamiento
    height, width = edges.shape
    escala_x = 11 / width
    escala_y = 11 / height
    posicion_x = -12
    posicion_y = 0

    # Vectores de puntos
    x, y = [], []

    for contour in contours:
        # Aquí puedes tomar todos los puntos para máxima resolución
        for point in contour:
            x.append(point[1] * escala_x + posicion_x)
            y.append((height - point[0]) * escala_y + posicion_y)

    # Dibujar los puntos
    plt.figure(figsize=(6,6))
    plt.plot(x, y, 'ro', markersize=1)  # puntos en rojo
    plt.axis("equal")
    plt.show()

    return np.array(x), np.array(y)


# Ejemplo de uso
ruta = "tu_imagen.png"  # Cambia por tu ruta
x, y = procesar_imagen(ruta)
