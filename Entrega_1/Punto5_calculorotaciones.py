import numpy as np

def rotacion(angulo, eje):

    if eje.lower() == 'x':
        rot = np.array([[1, 0, 0],
                        [0, np.cos(angulo), -np.sin(angulo)],
                        [0, np.sin(angulo),  np.cos(angulo)]])
    elif eje.lower() == 'y':
        rot = np.array([[ np.cos(angulo), 0, np.sin(angulo)],
                        [0, 1, 0],
                        [-np.sin(angulo), 0, np.cos(angulo)]])
    elif eje.lower() == 'z':
        rot = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                        [np.sin(angulo),  np.cos(angulo), 0],
                        [0, 0, 1]])
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'")
    
    return rot

angulo = np.deg2rad(45) # 45 grados

print()
print(angulo)
print()
print("Rotación en X:")
print(rotacion(angulo, 'x'))

print("\nRotación en Y:")
print(rotacion(angulo, 'y'))

print("\nRotación en Z:")
print(rotacion(angulo, 'z'))
