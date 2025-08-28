import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicitar al usuario las coordenadas
print("Ingrese tres coordenadas para realizar una gráfica en 3D")
x = float(input("Ingrese coordenada x: "))
y = float(input("Ingrese coordenada y: "))
z = float(input("Ingrese coordenada z: "))

# Crear figura y eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar el vector desde el origen
ax.quiver(0, 0, 0, x, y, z, color='b', arrow_length_ratio=0.1)

# Etiquetas y título
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Gráfica 3D')

# Ajustar límites para mejor visualización
max_val = max(abs(x), abs(y), abs(z)) * 1.2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

plt.show()
