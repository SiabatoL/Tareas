import random
x=int(input("Ingrese cantidad de numeros aleatorios"))
min=int(input("Ingrese rango minimo de los numeros"))
max=int(input("Ingrese rango maximo de los numeros"))
for i in range(x):
     print(random.uniform(min, max))