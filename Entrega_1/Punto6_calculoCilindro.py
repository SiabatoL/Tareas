import math

def calcular_fuerzas(d_embolo, d_vastago, presion):
    # Áreas
    area_embolo = math.pi * (d_embolo**2) / 4
    area_vastago = math.pi * (d_vastago**2) / 4
    # Fuerzas
    F_avance = presion * area_embolo
    F_retroceso = presion * (area_embolo - area_vastago)

    return F_avance, F_retroceso

print("\n  Cálculo de Fuerzas en Cilindro de Doble Efecto\n")
    
    # Datos de entrada
D = float(0.001)  # Diametro émbolo (Metros)
d = float(0.005)  # Diametro vástago (Metros)
P = float(30) * 6894.76  # Psi a Pa
print(f"\nDiametro émbolo: {D:.2f} m")
print(f"\nDiametro vástago: {d:.2f} m")
print(f"\nPresion: {P/1000:.2f} MPa")
    
F_av, F_ret = calcular_fuerzas(D, d, P)
    
print(f"\nFuerza de avance: {F_av:.2f} N")
print(f"Fuerza de retroceso: {F_ret:.2f} N\n")