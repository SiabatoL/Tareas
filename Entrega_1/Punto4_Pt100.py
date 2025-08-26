def resistencia_pt100(T):

    R0 = 100.0      # resistencia a 0 °C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  #  T < 0

    if T >= 0:
        R = R0 * (1 + A*T + B*(T**2))
    else:
        R = R0 * (1 + A*T + B*(T**2) + C*(T-100)*(T**3))
    
    return R

print("\n    Cálculo de resistencia RTD Pt100 \n")
T = float(input("Ingrese temperatura [°C]: "))
R = resistencia_pt100(T)
print(f"Resistencia a {T} °C = {R:.4f} ohmios")
