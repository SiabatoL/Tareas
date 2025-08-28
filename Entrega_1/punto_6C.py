
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.measure import find_contours
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pyfirmata import Arduino, SERVO
import time
import math

# ---------------- Arduino Setup ----------------
#try:
    #board = Arduino('COM9')  # Cambia a tu puerto
 #   pin1 = board.get_pin('d:5:s')
  #  pin2 = board.get_pin('d:6:s')
   # time.sleep(1)
 #   pin1.write(0)
 #   pin2.write(144)  # 0.8*180 = 144 grados
#except Exception as e:
 #   print("No se pudo conectar al Arduino:", e)
  #  exit()

# ---------------- Utilidades ----------------
def adjust_angle(angle_rad):
    angle_deg = np.clip(np.degrees(angle_rad), 0, 180)
    return angle_deg

def inverse_kinematics_2r(l1, l2, x, y):
    d = np.hypot(x, y)
    if d > (l1 + l2):
        raise ValueError("Punto fuera del alcance")
    cos_theta2 = (x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2)
    cos_theta2 = np.clip(cos_theta2, -1, 1)
    theta2 = np.arccos(cos_theta2)
    k1 = l1 + l2 * np.cos(theta2)
    k2 = l2 * np.sin(theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)
    return theta1, theta2

def lspb(q0, qf, t):
    t_total = t[-1] - t[0]
    v = (qf - q0) / t_total
    return np.linspace(q0, qf, len(t)), None, None

# ---------------- Imagen y procesamiento ----------------
Tk().withdraw()
filename = askopenfilename(filetypes=[("Imagenes", "*.jpg *.png *.bmp")])
if not filename:
    print("Selección cancelada.")
    exit()

image = cv2.imread(filename)
gray = rgb2gray(image)
thresh = threshold_otsu(gray)
binary = gray > thresh
contours = find_contours(binary, 0.5)

height, width = binary.shape
escala_x = 11 / width
escala_y = 11 / height
pos_x = -12
pos_y = 0

x_coords = []
y_coords = []

for contour in contours:
    num_points = int(len(contour) / (0.035 * (height + height)))
    indices = np.round(np.linspace(0, len(contour) - 1, num_points)).astype(int)
    for idx in indices:
        pt = contour[idx]
        x_coords.append(pt[1] * escala_x + pos_x)
        y_coords.append((height - pt[0]) * escala_y + pos_y)

# ---------------- Trazo ----------------
l1, l2 = 10, 10
servo_angles = []
times = [0]

for i in range(len(x_coords) - 1):
    try:
        theta1_p1, theta2_p1 = inverse_kinematics_2r(l1, l2, x_coords[i], y_coords[i])
        theta1_p2, theta2_p2 = inverse_kinematics_2r(l1, l2, x_coords[i+1], y_coords[i+1])
    except ValueError:
        continue

    dist = np.hypot(x_coords[i+1] - x_coords[i], y_coords[i+1] - y_coords[i])
    t = np.linspace(0, 0.01 if dist < 0.5 else 0.2, 2)
    times.append(times[-1] + (t[-1] - t[0]))

    q1_traj, _, _ = lspb(theta1_p1, theta1_p2, t)
    q2_traj, _, _ = lspb(theta2_p1, theta2_p2, t)

    for q1, q2 in zip(q1_traj, q2_traj):
        s1 = adjust_angle(q1)
        s2 = adjust_angle(q2)
        servo_angles.append((s1, s2))

# ---------------- Movimiento y visualización ----------------
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-14, 1)
ax.set_ylim(-1, 12)
ax.set_title("Simulación del Brazo")

for i, (a1, a2) in enumerate(servo_angles):
    #pin1.write(a1)
    #pin2.write(a2)
    if i < len(times) - 1:
        time.sleep(times[i+1] - times[i])
    else:
        time.sleep(0.01)

    # Cinemática directa para visualizar
    theta1_rad = np.radians(a1)
    theta2_rad = np.radians(a2)
    x1 = l1 * np.cos(theta1_rad)
    y1 = l1 * np.sin(theta1_rad)
    x2 = x1 + l2 * np.cos(theta1_rad + theta2_rad)
    y2 = y1 + l2 * np.sin(theta1_rad + theta2_rad)

    ax.plot([0, x1, x2], [0, y1, y2], 'b-o')
    plt.pause(0.01)

plt.show()

# ---------------- Apagar servos al final ----------------
#pin1.write(0)
#pin2.write(144)
