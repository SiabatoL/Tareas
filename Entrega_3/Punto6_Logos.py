import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters, measure
from tkinter import Tk, filedialog

def seleccionar_imagen():
    # Ocultar la ventana principal de Tk
    root = Tk()
    root.withdraw()

    # Abrir un cuadro de diálogo para seleccionar archivo
    file_path = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes", "*.jpg;*.png;*.bmp"), ("Todos los archivos", "*.*")]
    )

    return file_path


def procesar_imagen(ruta_imagen):
    # Cargar la imagen
    image = io.imread(ruta_imagen)

    # Convertir a escala de grises si es necesario
    if image.ndim == 3:
        if image.shape[2] == 4:  # RGBA
            image = image[:, :, :3]  # ignorar el canal alfa
        gray_image = color.rgb2gray(image)
    else:
        gray_image = image

    # Binarización usando Otsu
    threshold = filters.threshold_otsu(gray_image)
    binary_image = gray_image > threshold

    # Encontrar contornos
    contours = measure.find_contours(binary_image, level=0.5)

    # Escalado y desplazamiento
    height, width = binary_image.shape
    escala_x = 11 / width
    escala_y = 11 / height
    posicion_x = -12
    posicion_y = 0

    # Vectores de puntos
    x, y = [], []

    for contour in contours:
        num_points = int(np.ceil(len(contour) / (0.005 * (height + height))))
        sample_indices = np.round(np.linspace(0, len(contour) - 1, num_points)).astype(int)

        for idx in sample_indices:
            point = contour[idx]
            x.append(point[1] * escala_x + posicion_x)
            y.append((height - point[0]) * escala_y + posicion_y)

    # Dibujar los puntos
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'ro', markersize=2)  # puntos en rojo
    plt.axis("equal")
    plt.show()

    return np.array(x), np.array(y)


# Ejemplo de uso
ruta = seleccionar_imagen()
if ruta:  # Solo procesar si se seleccionó una imagen
    x, y = procesar_imagen(ruta)
else:
    print("No se seleccionó ninguna imagen.")

