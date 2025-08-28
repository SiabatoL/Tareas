import control
import matplotlib.pyplot as plt
import numpy as np

# Definir los coeficientes del numerador y el denominador
# Ejemplo: G(s) = 1 / (s^2 + 2s + 1)
k=float(input("Ingrese el valor de la ganancia "))
wn=float(input("Ingrese el valor de la frecuencia natural "))
f=float(input("Ingrese el valor del factor de amortiguamiento "))

num = [k*wn**2]
den = [1, 2*f*wn, wn**2]

# Crear la función de transferencia
G = control.tf(num, den)
print("Función de Transferencia:")
print(G)

# Generar la respuesta al escalón
# Se puede usar step_response para obtener los datos y graficar manualmente, o step_plot para graficar directamente
# Para obtener los datos:
tiempo, respuesta = control.step_response(G)
if (f <1,f>0):
    print("sobreamortiguado")
elif (f==1):
    print("criticamente amortiguado")
elif (f>1):
    print("sobre amortiguado")
        
# Graficar usando matplotlib
plt.figure(figsize=(8, 6))
plt.plot(tiempo, respuesta)
plt.title('Sistema de Segundo Orden')
plt.xlabel('Tiempo')
plt.ylabel('Salida')
plt.grid(True)
plt.show()