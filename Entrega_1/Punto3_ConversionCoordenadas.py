import numpy as np

# Declaración Coordenadas rectangulares (x, y, z)
x = 3
y = 4
z = 5

# Conversión rectangulares a cilíndricas (r, theta, z)
r_cilindrica = np.sqrt(x**2 + y**2)
t_cilindrica = np.arctan2(y, x)
z_cilindrica = z

# Conversión rectangulares a esféricas (rho, phi, theta)
rho_esferica = np.sqrt(x**2 + y**2 + z**2)     # norma
phi_esferica = np.arccos(z / rho_esferica)     # ángulo con el eje z
theta_esferica = np.arctan2(y, x)              # ángulo en el plano xy

# Imprimir resultados
print("Coordenadas rectangulares:")
print(f"X = {x}")
print(f"Y = {y}")
print(f"Z = {z}")
print()

print("Coordenadas cilíndricas:")
print(f"r = {r_cilindrica}")
print(f"theta = {t_cilindrica}")
print(f"z = {z_cilindrica}")
print()

print("Coordenadas esféricas:")
print(f"rho = {rho_esferica}")
print(f"phi = {phi_esferica}")
print(f"theta = {theta_esferica}")
