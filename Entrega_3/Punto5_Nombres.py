import numpy as np
import matplotlib.pyplot as plt

# Funciones de letra

def generar_letra_A():
    x_a1 = np.linspace(0, 1, 2)
    y_a1 = np.linspace(0, 2, 2)
    x_a2 = np.linspace(1, 2, 2)
    y_a2 = np.linspace(2, 0, 2) 
    x_a3 = np.linspace(2, 0.5, 2)
    y_a3 = np.linspace(0, 1, 2)
    x_a4 = np.linspace(0.5, 2, 2)
    y_a4 = np.linspace(1, 0, 2)

    x = np.concatenate([x_a1, x_a2, x_a3, x_a4])
    y = np.concatenate([y_a1, y_a2, y_a3, y_a4])
    return x, y

def generar_letra_B():
    x1 = np.linspace(0, 1, 2)
    y1 = np.linspace(0, 0, 2)

    t = np.linspace(-np.pi/2, np.pi/2, 6)
    x2 = 1 + np.cos(t)
    y2 = (1 + np.sin(t)) / 2
    x3 = 1 + np.cos(t)
    y3 = (3 + np.sin(t)) / 2

    x4 = np.linspace(1, 0, 2)
    y4 = np.linspace(2, 2, 2)
    x5 = np.linspace(0, 0, 2)
    y5 = np.linspace(2, 1, 2)
    x6 = np.linspace(1, 0, 2)
    y6 = np.linspace(1, 1, 2)
    x7 = np.linspace(0, 0, 2)
    y7 = np.linspace(1, 0, 2)

    x = np.concatenate([x1, x2, x3, x4, x5, x6, x7])
    y = np.concatenate([y1, y2, y3, y4, y5, y6, y7])
    return x, y

def generar_letra_C():
    t = np.linspace(np.pi/6, 3.6*np.pi/2, 7)
    x = 1 + np.cos(t)
    y = 1 + np.sin(t)
    return x, y

def generar_letra_D():
    t = np.linspace(-np.pi/2, np.pi/2, 6)
    x_d1 = 1 + np.cos(t)
    y_d1 = 1 + np.sin(t)

    x_d2 = np.linspace(1, 0, 2)
    y_d2 = np.linspace(2, 2, 2)

    x_d3 = np.linspace(0, 0, 3)
    y_d3 = np.linspace(2, 0, 3)

    x_d4 = np.linspace(0, 1, 2)
    y_d4 = np.linspace(0, 0, 2)

    x = np.concatenate([x_d1, x_d2, x_d3, x_d4])
    y = np.concatenate([y_d1, y_d2, y_d3, y_d4])
    return x, y

def generar_letra_E():
    x_e1 = np.linspace(1, 0, 2)
    y_e1 = np.linspace(2, 2, 2)

    x_e4 = np.linspace(1, 0, 2)
    y_e4 = np.linspace(1, 1, 2)

    x_e3 = np.linspace(0, 1, 2)
    y_e3 = np.linspace(1, 1, 2)

    x_e2 = np.linspace(0, 0, 2)
    y_e2 = np.linspace(2, 1, 2)

    x_e5 = np.linspace(0, 0, 2)
    y_e5 = np.linspace(1, 0, 2)

    x_e6 = np.linspace(0, 1, 2)
    y_e6 = np.linspace(0, 0, 2)

    x = np.concatenate([x_e1, x_e2, x_e3, x_e4, x_e5, x_e6])
    y = np.concatenate([y_e1, y_e2, y_e3, y_e4, y_e5, y_e6])
    return x, y

def generar_letra_F():
    # Horizontal arriba
    x_d1 = np.linspace(2.5, 0, 2)
    y_d1 = np.linspace(2, 2, 2)

    # Dibujar la de la mitad
    x_d3 = np.linspace(1, 0, 2)
    y_d3 = np.linspace(1, 1, 2)

    # Devuelta
    x_d4 = np.linspace(0, 1, 2)
    y_d4 = np.linspace(1, 1, 2)

    # Vertical arriba
    x_d2 = np.linspace(0, 0, 3)
    y_d2 = np.linspace(2, 1, 3)

    # Vertical abajo
    x_d5 = np.linspace(0, 0, 3)
    y_d5 = np.linspace(1, 0, 3)

    # Combinar
    x = np.concatenate([x_d1, x_d2, x_d3, x_d4, x_d5])
    y = np.concatenate([y_d1, y_d2, y_d3, y_d4, y_d5])

    return x, y
def generar_letra_G():
    # Barriga - semicirculo
    x_g2 = np.linspace(1.8, 1.8, 2)
    y_g2 = np.linspace(0.4, 0.8, 2)

    # Dibujar la de la mitad
    x_g3 = np.linspace(1.8, 1, 2)
    y_g3 = np.linspace(0.8, 0.8, 2)

    # Semicírculo
    t = np.linspace(np.pi/6, 3.6*np.pi/2, 8)
    x_g1 = 1 + np.cos(t)
    y_g1 = 1 + np.sin(t)

    # Combinar
    x = np.concatenate([x_g1, x_g2, x_g3])
    y = np.concatenate([y_g1, y_g2, y_g3])


    return x, y
def generar_letra_H():
    # Vertical izquierda
    x_h1 = np.linspace(0, 0, 3)
    y_h1 = np.linspace(0, 2, 3)

    # Vertical derecha
    x_h2 = np.linspace(2, 2, 3)
    y_h2 = np.linspace(0, 2, 3)

    # Horizontal en medio
    x_h3 = np.linspace(0, 2, 2)
    y_h3 = np.linspace(1, 1, 2)

    # Combinar
    x = np.concatenate([x_h1, x_h2, x_h3])
    y = np.concatenate([y_h1, y_h2, y_h3])

    return x, y
def generar_letra_I():
    # Horizontal arriba
    x = np.linspace(0, 0, 2)
    y = np.linspace(0, 2, 2)
 
    return x, y
def generar_letra_J():
    # Horizontal arriba
    x_j1 = np.linspace(0, 2, 3)
    y_j1 = np.linspace(2, 2, 3)

    # Vertical derecha
    x_j2 = np.linspace(2, 2, 3)
    y_j2 = np.linspace(0.5, 2, 3)

    # Curva abajo (como una U)
    t = np.linspace(np.pi, 2*np.pi, 10)
    x_j3 = 1 + np.cos(t)
    y_j3 = np.sin(t)

    # Ajustar curva abajo a la posición
    x_j3 = x_j3 * 1  # escala horizontal
    y_j3 = y_j3 * 0.5  # escala vertical
    x_j3 = x_j3 + 1  # mover al centro
    y_j3 = y_j3      # ya está en su lugar

    # Combinar
    x = np.concatenate([x_j1, x_j2, x_j3])
    y = np.concatenate([y_j1, y_j2, y_j3])

    return x, y
def generar_letra_K():
    # Vertical izquierda
    x_k1 = np.linspace(0, 0, 3)
    y_k1 = np.linspace(0, 2, 3)

    # Diagonal superior
    x_k2 = np.linspace(0, 2, 3)
    y_k2 = np.linspace(1, 2, 3)

    # Diagonal inferior
    x_k3 = np.linspace(0, 2, 3)
    y_k3 = np.linspace(1, 0, 3)

    # Combinar
    x = np.concatenate([x_k1, x_k2, x_k3])
    y = np.concatenate([y_k1, y_k2, y_k3])

    return x, y
def generar_letra_L():
    # Vertical izquierda
    x_l1 = np.linspace(0, 0, 3)
    y_l1 = np.linspace(0, 2, 3)

    # Horizontal abajo
    x_l2 = np.linspace(0, 2, 3)
    y_l2 = np.linspace(0, 0, 3)

    # Combinar
    x = np.concatenate([x_l1, x_l2])
    y = np.concatenate([y_l1, y_l2])

    return x, y
def generar_letra_M():
    # Vertical izquierda
    x_m1 = np.linspace(0, 0, 3)
    y_m1 = np.linspace(0, 2, 3)

    # Diagonal izquierda (subida)
    x_m2 = np.linspace(0, 1, 3)
    y_m2 = np.linspace(2, 0, 3)

    # Diagonal derecha (bajada)
    x_m3 = np.linspace(1, 2, 3)
    y_m3 = np.linspace(0, 2, 3)

    # Vertical derecha
    x_m4 = np.linspace(2, 2, 3)
    y_m4 = np.linspace(2, 0, 3)

    # Combinar
    x = np.concatenate([x_m1, x_m2, x_m3, x_m4])
    y = np.concatenate([y_m1, y_m2, y_m3, y_m4])

    return x, y
import numpy as np

def generar_letra_N():
    # Vertical izquierda
    x_n1 = np.linspace(0, 0, 3)
    y_n1 = np.linspace(0, 2, 3)

    # Diagonal
    x_n2 = np.linspace(0, 2, 3)
    y_n2 = np.linspace(2, 0, 3)

    # Vertical derecha
    x_n3 = np.linspace(2, 2, 3)
    y_n3 = np.linspace(0, 2, 3)

    # Combinar
    x = np.concatenate([x_n1, x_n2, x_n3])
    y = np.concatenate([y_n1, y_n2, y_n3])

    return x, y
def generar_letra_NY():
    # Base: letra N
    x_n, y_n = generar_letra_NY()

    # Virgulilla arriba (~)
    t = np.linspace(0, np.pi, 20)
    x_tilde = 0.5 + np.cos(t) * 0.5
    y_tilde = 2.2 + np.sin(t) * 0.2

    # Combinar
    x = np.concatenate([x_n, x_tilde])
    y = np.concatenate([y_n, y_tilde])

    return x, y
def generar_letra_O():
    # Círculo
    t = np.linspace(0, 2*np.pi, 50)
    x = np.cos(t) * 1 + 1   # centro en (1,1)
    y = np.sin(t) * 1 + 1

    return x, y
def generar_letra_P():
    # Vertical izquierda
    x_p1 = np.linspace(0, 0, 3)
    y_p1 = np.linspace(0, 2, 3)

    # Semicírculo arriba
    t = np.linspace(-np.pi/2, np.pi/2, 20)
    x_p2 = 1 + np.cos(t)
    y_p2 = 1.5 + np.sin(t) * 0.5

    # Combinar
    x = np.concatenate([x_p1, x_p2])
    y = np.concatenate([y_p1, y_p2])

    return x, y
def generar_letra_Q():
    # Círculo base (como O)
    t = np.linspace(0, 2*np.pi, 50)
    x_q = np.cos(t) * 1 + 1
    y_q = np.sin(t) * 1 + 1

    # Patita diagonal
    x_q2 = np.linspace(1.5, 2, 3)
    y_q2 = np.linspace(0.5, 0, 3)

    # Combinar
    x = np.concatenate([x_q, x_q2])
    y = np.concatenate([y_q, y_q2])

    return x, y
def generar_letra_R():
    # Vertical izquierda
    x_r1 = np.linspace(0, 0, 3)
    y_r1 = np.linspace(0, 2, 3)

    # Semicírculo arriba (como en P)
    t = np.linspace(-np.pi/2, np.pi/2, 20)
    x_r2 = np.cos(t)*2
    y_r2 = 1.5 + np.sin(t) * 0.5

    # Diagonal hacia abajo
    x_r3 = np.linspace(0, 2, 3)
    y_r3 = np.linspace(1, 0, 3)

    # Combinar
    x = np.concatenate([x_r1, x_r2, x_r3])
    y = np.concatenate([y_r1, y_r2, y_r3])

    return x, y
def generar_letra_S():
    # Curva superior
    t1 = np.linspace(3*np.pi/2, np.pi/4, 5)
    x2 = 1 + np.cos(t1)
    y2 = 1.5 + np.sin(t1) * 0.5

    # Curva inferior
    t2 = np.linspace(-4*np.pi/5, np.pi/2, 5)
    x1 = 1 + np.cos(t2)
    y1 = 0.5 + np.sin(t2) * 0.5

    # Combinar
    x = np.concatenate([x1, x2])
    y = np.concatenate([y1, y2])

    return x, y
def generar_letra_T():
    # Barra superior
    x_t1 = np.linspace(0, 2, 3)
    y_t1 = np.linspace(2, 2, 3)

    # Columna central
    x_t2 = np.linspace(1, 1, 3)
    y_t2 = np.linspace(2, 0, 3)

    # Combinar
    x = np.concatenate([x_t1, x_t2])
    y = np.concatenate([y_t1, y_t2])

    return x, y
def generar_letra_U():
    # Lado izquierdo
    x_u1 = np.linspace(0, 0, 3)
    y_u1 = np.linspace(1, 2, 3)

    # Parte curva inferior
    t = np.linspace(-np.pi, -np.pi/14, 8)
    x_u2 = 1 + np.cos(t)
    y_u2 = 1 + np.sin(t) * 1

    # Lado derecho
    x_u3 = np.linspace(2, 2, 3)
    y_u3 = np.linspace(1, 2, 3)

    # Combinar
    x = np.concatenate([x_u1, x_u2, x_u3])
    y = np.concatenate([y_u1, y_u2, y_u3])

    return x, y
def generar_letra_V():
    # Lado izquierdo
    x_v1 = np.linspace(0, 1, 3)
    y_v1 = np.linspace(2, 0, 3)

    # Lado derecho
    x_v2 = np.linspace(1, 2, 3)
    y_v2 = np.linspace(0, 2, 3)

    # Combinar
    x = np.concatenate([x_v1, x_v2])
    y = np.concatenate([y_v1, y_v2])

    return x, y
def generar_letra_W():
    # Lado izquierdo
    x_w1 = np.linspace(0, 0.5, 3)
    y_w1 = np.linspace(2, 0, 3)

    # Centro bajo
    x_w2 = np.linspace(0.5, 1, 3)
    y_w2 = np.linspace(0, 1, 3)

    # Centro bajo derecho
    x_w3 = np.linspace(1, 1.5, 3)
    y_w3 = np.linspace(1, 0, 3)

    # Lado derecho
    x_w4 = np.linspace(1.5, 2, 3)
    y_w4 = np.linspace(0, 2, 3)

    # Combinar
    x = np.concatenate([x_w1, x_w2, x_w3, x_w4])
    y = np.concatenate([y_w1, y_w2, y_w3, y_w4])

    return x, y
def generar_letra_X():
    # Diagonal 1
    x_x1 = np.linspace(0, 2, 3)
    y_x1 = np.linspace(0, 2, 3)

    # Diagonal 2
    x_x2 = np.linspace(0, 2, 3)
    y_x2 = np.linspace(2, 0, 3)

    # Combinar
    x = np.concatenate([x_x1, x_x2])
    y = np.concatenate([y_x1, y_x2])

    return x, y
def generar_letra_Y():
    # Brazo izquierdo
    x_y1 = np.linspace(0, 1, 3)
    y_y1 = np.linspace(2, 1, 3)

    # Brazo derecho
    x_y2 = np.linspace(2, 1, 3)
    y_y2 = np.linspace(2, 1, 3)

    # Columna central
    x_y3 = np.linspace(1, 1, 3)
    y_y3 = np.linspace(1, 0, 3)

    # Combinar
    x = np.concatenate([x_y1, x_y2, x_y3])
    y = np.concatenate([y_y1, y_y2, y_y3])

    return x, y
def generar_letra_Z():
    # Parte superior
    x_z1 = np.linspace(0, 2, 3)
    y_z1 = np.linspace(2, 2, 3)

    # Diagonal
    x_z2 = np.linspace(2, 0, 3)
    y_z2 = np.linspace(2, 0, 3)

    # Parte inferior
    x_z3 = np.linspace(0, 2, 3)
    y_z3 = np.linspace(0, 0, 3)

    # Combinar
    x = np.concatenate([x_z1, x_z2, x_z3])
    y = np.concatenate([y_z1, y_z2, y_z3])
    return x, y
# =========================
# Diccionario de letras
# =========================
letras = {
    "A": generar_letra_A,
    "B": generar_letra_B,
    "C": generar_letra_C,
    "D": generar_letra_D,
    "E": generar_letra_E,
    "F": generar_letra_F,
    "G": generar_letra_G,
    "H": generar_letra_H,
    "I": generar_letra_I,
    "J": generar_letra_J,
    "K": generar_letra_K,
    "L": generar_letra_L,
    "M": generar_letra_M,
    "N": generar_letra_N,
    "Ñ": generar_letra_NY,
    "O": generar_letra_O,
    "P": generar_letra_P,
    "Q": generar_letra_Q,
    "R": generar_letra_R,
    "S": generar_letra_S,
    "T": generar_letra_T,
    "U": generar_letra_U,
    "V": generar_letra_V,
    "W": generar_letra_W,
    "X": generar_letra_X,
    "Y": generar_letra_Y,
    "Z": generar_letra_Z,
}

def dibujar_texto(texto):
    plt.figure()
    desplazamiento = 0
    for letra in texto.upper():
        if letra in letras:
            x, y = letras[letra]()
            plt.plot(x + desplazamiento, y, linewidth=2)

            # Ajustar desplazamiento según la letra
            if letra == "I":
                desplazamiento += 1.25  # medio espacio para la I
            else:
                desplazamiento += 3    # espacio normal 

        elif letra == " ":
            desplazamiento += 4  # espacio grande 
    plt.axis("equal")
    plt.show()

# Ejemplo de uso
texto = input("Escribe una palabra: ")
dibujar_texto(texto)
