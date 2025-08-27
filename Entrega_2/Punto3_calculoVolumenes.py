import math

def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (base * altura) / 3

def volumen_cono_truncado(r1, r2, h):
    return (math.pi * h / 3) * (r1**2 + r1*r2 + r2**2)

def volumen_cilindro(r, h):
    return math.pi * (r**2) * h


# Mainmeremeinmein
print("\n    Cálculo de Volúmenes\n")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro\n")

opcion = int(input("Seleccione el sólido (1-4): "))

match opcion:
    case 1:
        base = float(input("Ingrese el área de la base: "))
        altura = float(input("Ingrese la altura: "))
        V = volumen_prisma(base, altura)
        print(f"Volumen del prisma = {V:.2f}")
    
    case 2:
        base = float(input("Ingrese el área de la base: "))
        altura = float(input("Ingrese la altura: "))
        V = volumen_piramide(base, altura)
        print(f"Volumen de la pirámide = {V:.2f}")
    
    case 3:
        r1 = float(input("Ingrese el radio mayor: "))
        r2 = float(input("Ingrese el radio menor: "))
        h = float(input("Ingrese la altura: "))
        V = volumen_cono_truncado(r1, r2, h)
        print(f"Volumen del cono truncado = {V:.2f}")
    
    case 4:
        r = float(input("Ingrese el radio de la base: "))
        h = float(input("Ingrese la altura: "))
        V = volumen_cilindro(r, h)
        print(f"Volumen del cilindro = {V:.2f}")
    
    case _:
        print("Opción no válida.")
