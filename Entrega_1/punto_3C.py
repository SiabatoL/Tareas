import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Cálculo de carga y descarga RC
# -------------------------------
print("Ingrese los valores del circuito RC para calcular la ecuación de carga")

V = float(input("Ingrese valor de voltaje (V): "))
C = float(input("Ingrese capacitancia (F): "))
R = float(input("Ingrese resistencia (Ohmios): "))

s = R * C

ti = np.linspace(0, 5 * s, 400)

# Cálculo de la carga: V*(1 - exp(-t/RC))
e = 1 - np.exp(-ti / s)
carga = V * e

plt.figure()
plt.plot(ti, carga)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Ecuación de carga')
plt.grid(True)

# Cálculo de la descarga: V*exp(-t/RC)
des = np.exp(-ti / s)
descarga = V * des

plt.figure()
plt.plot(ti, descarga)
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Ecuación de descarga')
plt.grid(True)

plt.show()