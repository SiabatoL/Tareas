import sys
import os
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.valor1 = None
        self.operacion = None
        self.setupUi()

    def setupUi(self):
        # --- Ventana principal ---
        self.setObjectName("main")
        self.resize(720, 734)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("background-color: rgb(27, 27, 27);")

        # --- Widget central ---
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # --- Título ---
        self.label = self.crear_label(
            texto="CALCULADORA",
            font_size=17,
            bold=True,
            color="white",
            geometry=(190, 30, 351, 61),
            align=QtCore.Qt.AlignCenter
        )

        # --- Campo de entrada ---
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 210, 241, 61))
        self.lineEdit.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.lineEdit.setStyleSheet("background-color: white; color: WHITE; padding: 5px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)

        # --- Display LCD ---
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(400, 130, 241, 141))
        self.lcdNumber.setStyleSheet("background-color: #d3e5da; border: 2px solid black;")
        self.lcdNumber.setDigitCount(10)

        # --- Layout botones ---
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 320, 651, 151))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Fila 1: operaciones básicas
        fila1 = QtWidgets.QHBoxLayout()
        self.boton_suma = self.crear_boton("+", fila1, lambda: self.guardar_operacion("+"))
        self.boton_resta = self.crear_boton("-", fila1, lambda: self.guardar_operacion("-"))
        self.boton_mult = self.crear_boton("*", fila1, lambda: self.guardar_operacion("*"))
        self.boton_div = self.crear_boton("/", fila1, lambda: self.guardar_operacion("/"))
        self.verticalLayout.addLayout(fila1)

        # Fila 2: funciones trigonométricas
        fila2 = QtWidgets.QHBoxLayout()
        self.boton_sen = self.crear_boton("Sen", fila2, lambda: self.calcular_funcion("sen"))
        self.boton_cos = self.crear_boton("Cos", fila2, lambda: self.calcular_funcion("cos"))
        self.boton_tan = self.crear_boton("Tan", fila2, lambda: self.calcular_funcion("tan"))
        self.boton_resultado = self.crear_boton("=", fila2, self.mostrar_resultado)
        self.verticalLayout.addLayout(fila2)

        # --- Imagen (Logo) ---
        self.Imagen1 = QtWidgets.QLabel(self.centralwidget)
        self.Imagen1.setGeometry(QtCore.QRect(440, 490, 241, 161))
        self.Imagen1.setScaledContents(True)
        self.cargar_imagen("Logoecci.png")

        # --- Créditos ---
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 500, 401, 148))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.agregar_credito("Laura Siabato - Cristian Zamora")
        self.agregar_credito("Ing. Mecatrónica - Electiva Robótica")
        self.agregar_credito("2025 - 1")

        # --- Menús ---
        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.setWindowTitle("Calculadora")

    # -------- Métodos auxiliares --------
    def crear_boton(self, texto, layout, funcion):
        boton = QtWidgets.QPushButton(texto)
        boton.setFont(QtGui.QFont("Arial", 13, QtGui.QFont.Bold))
        boton.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        boton.clicked.connect(funcion)
        layout.addWidget(boton)
        return boton

    def crear_label(self, texto, font_size=12, bold=False, color="white", geometry=None, align=None):
        label = QtWidgets.QLabel(self.centralwidget)
        if geometry:
            label.setGeometry(QtCore.QRect(*geometry))
        font = QtGui.QFont("Arial", font_size, QtGui.QFont.Bold if bold else QtGui.QFont.Normal)
        label.setFont(font)
        label.setText(texto)
        label.setStyleSheet(f"color: {color};")
        if align:
            label.setAlignment(align)
        return label

    def cargar_imagen(self, nombre_archivo):
        ruta_imagen = os.path.join(os.path.dirname(__file__), nombre_archivo)
        pixmap = QtGui.QPixmap(ruta_imagen)
        if not pixmap.isNull():
            self.Imagen1.setPixmap(pixmap)
        else:
            self.Imagen1.setText(f"No se encontró {nombre_archivo}")
            self.Imagen1.setStyleSheet("color: blue;")

    def agregar_credito(self, texto):
        lbl = QtWidgets.QLabel(texto, self.verticalLayoutWidget_2)
        lbl.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        lbl.setStyleSheet("color: white;")
        lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(lbl)

    def leer_texto(self):
        try:
            return float(self.lineEdit.text())
        except ValueError:
            return None

    def guardar_operacion(self, op):
        valor = self.leer_texto()
        if valor is not None:
            self.valor1 = valor
            self.operacion = op
            self.lcdNumber.display(valor)
            self.lineEdit.clear()
        else:
            self.lcdNumber.display("Err")

    def calcular_funcion(self, funcion):
        valor = self.leer_texto()
        if valor is None:
            self.lcdNumber.display("Err")
            return

        funciones = {
            "sen": math.sin,
            "cos": math.cos,
            "tan": math.tan
        }

        if funcion in funciones:
            try:
                resultado = funciones[funcion](math.radians(valor))
            except Exception:
                resultado = "Err"
        else:
            resultado = "Err"

        self.lcdNumber.display(resultado)

    def mostrar_resultado(self):
        if self.operacion is None or self.valor1 is None:
            self.lcdNumber.display("Err")
            return

        valor2 = self.leer_texto()
        if valor2 is None:
            self.lcdNumber.display("Err")
            return

        try:
            operaciones = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: "Err" if b == 0 else a / b
            }
            resultado = operaciones.get(self.operacion, lambda *_: "Err")(self.valor1, valor2)
            self.lcdNumber.display(resultado)
            self.lineEdit.clear()
            self.operacion = None
        except Exception:
            self.lcdNumber.display("Err")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = UiMain()
    ventana.show()
    sys.exit(app.exec_())
