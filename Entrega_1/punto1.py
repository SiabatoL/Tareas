import numpy as np
        
# Declaración de vectores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Suma
suma = v1 + v2

# Resta
resta = v1 - v2

# Producto punto
producto_punto = np.dot(v1, v2)

# Producto cruz
producto_cruz = np.cross(v1, v2)

# División por un escalar
escalar = np.random.randint(1, 11)  # entero aleatorio entre 1 y 10
division_escalar1 = v1 / escalar
division_escalar2 = v2 / escalar

# Mostrar resultados
print(f"Vector 1 = {v1}")
print(f"Vector 2 = {v2}")
print()
print(f"Suma = {suma}")
print()
print(f"Resta = {resta}")
print()
print(f"Producto punto = {producto_punto}")
print()
print(f"Producto cruz = {producto_cruz}")
print()
print("División por un escalar:")
print(f"Escalar= {escalar}")
print(division_escalar1)
print()
print(division_escalar2)