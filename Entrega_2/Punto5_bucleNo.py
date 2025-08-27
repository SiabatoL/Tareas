print("\n     Bucle\n")
continuar = "si"
while continuar.lower() == "si":
    continuar = input("\n¿Desea continuar? (si/no): ").lower()

    while continuar not in ("si", "no"):
        print("Entrada no válida")
        continuar = input("\nDesea continuar? (si/no): ").lower()

print("\nPrograma finalizado ✅")
