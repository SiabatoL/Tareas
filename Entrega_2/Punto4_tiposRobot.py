def descripcion_robot(opcion):
    match opcion:
        case 1:
            return "Esférico → Dos articulaciones rotacionales y una prismática"
        case 2:
            return "Cilíndrico → Dos prismáticas y una rotacional"
        case 3:
            return "Cartesiano → Tres prismáticas"
        case 4:
            return "SCARA → Dos articulaciones rotacionales y una prismática"
        case 5:
            return "Angular → Todas sus articulaciones rotacionales"
        case _:
            return "Opción no válida."


#mainme
print("\n     Tipos de Robots\n")
print("1. Esférico")
print("2. Cilíndrico")
print("3. Cartesiano")
print("4. SCARA")
print("5. Angular")

try:
    opcion = int(input("Seleccione el robot (1-5): "))
    descripcion = descripcion_robot(opcion)
    print(f"\n{descripcion}")
except ValueError:
    print("\nEntrada no válida, por favor ingrese un número entre 1 y 5.")
