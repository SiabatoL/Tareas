import numpy as np
import matplotlib.pyplot as plt

# Crear matriz MTR de ceros con dimensiones (201, 2)
MTR = np.zeros((201, 2))

# Crear vector de temperaturas de -200 a 200 con paso de 2
MT = np.arange(-200, 202, 2)  # Incluye 200
MT = MT.reshape(-1, 1)  # Convertir a columna

MTR[:, 0] = MT[:, 0]

# Constantes para PT100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

# Calcular resistencia según la temperatura
for i in range(201):
    T = MT[i][0]
    if T >= 0:
        R = 100 * (1 + A*T + B*T**2)
    else:
        R = 100 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)
    
    MTR[i, 1] = R

# Graficar
plt.plot(MTR[:, 0], MTR[:, 1], 'b')
plt.title('Resistencias vs Temperatura - PT100')
plt.xlabel('Temperatura [°C]')
plt.ylabel('Resistencia [Ohmios]')
plt.grid(True)
plt.show()