import numpy as np

# Declaración de matrices
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Suma
suma = matriz1 + matriz2

# Resta
resta = matriz1 - matriz2

# Producto punto (producto escalar entre todos los elementos)
producto_punto = np.dot(matriz1.flatten(), matriz2.flatten())

# Producto cruz (producto vectorial fila a fila)
# En MATLAB cross(matriz1, matriz2) calcula fila a fila
producto_cruz = np.cross(matriz1, matriz2)

# División elemento a elemento
division = matriz1 / matriz2

# Mostrar resultados
print("Matriz 1:")
print(matriz1)
print("Matriz 2:")
print(matriz2)
print("Suma de matrices:")
print(suma)
print("Resta de matrices:")
print(resta)
print(f"Producto punto (producto escalar) = {producto_punto}")
print("Producto cruz (producto vectorial):")
print(producto_cruz)
print("División de matrices (elemento a elemento):")
print(division)
