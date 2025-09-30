# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 693)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(27, 27, 27);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # --- Título ---
        self.label = QtWidgets.QLabel("CONTORNO DE IMAGEN", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 471, 141))
        self.label.setFont(QtGui.QFont("Arial", 21, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")

        # --- Créditos ---
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 460, 390, 133))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Nombres = QtWidgets.QLabel("Cristian Zamora - Laura Siabato", self.verticalLayoutWidget)
        self.Nombres.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.Nombres.setStyleSheet("color: white;")
        self.Nombres.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.Nombres)

        self.subtitulo = QtWidgets.QLabel("Ing. Mecatrónica Electiva Robótica", self.verticalLayoutWidget)
        self.subtitulo.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.subtitulo.setStyleSheet("color: white;")
        self.subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.subtitulo)

        self.year = QtWidgets.QLabel("2025 - 1", self.verticalLayoutWidget)
        self.year.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.year.setStyleSheet("color: white;")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.year)

        # --- Área para mostrar contorno ---
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(470, 180, 331, 271))

        # --- Botón para seleccionar imagen ---
        self.push_Seleccionarim = QtWidgets.QPushButton("Seleccionar imagen", self.centralwidget)
        self.push_Seleccionarim.setGeometry(QtCore.QRect(120, 250, 261, 111))
        self.push_Seleccionarim.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.push_Seleccionarim.setStyleSheet("background-color: black; color: white;")

        # --- Logo en la parte inferior derecha ---
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(470, 460, 331, 131))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # --- Menú superior y barra de estado ---
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # --- Eventos ---
        self.push_Seleccionarim.clicked.connect(self.seleccionar_imagen)

        # Mostrar logo automáticamente
        self.mostrar_logo("Logoecci.png")

    def mostrar_logo(self, nombre_archivo):
        """Muestra el logo en el QLabel inferior derecho"""
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

        if os.path.exists(ruta):
            pixmap = QtGui.QPixmap(ruta)
            pixmap = pixmap.scaled(self.logo.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.logo.setPixmap(pixmap)
        else:
            self.logo.setText("Logo no encontrado")

    def seleccionar_imagen(self):
        """Abre un cuadro de diálogo para seleccionar imagen y muestra SOLO su contorno"""
        opciones = QtWidgets.QFileDialog.Options()
        archivo, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Seleccionar imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp);;Todos los archivos (*)",
            options=opciones
        )
        if archivo:
            # Leer y procesar imagen con OpenCV
            img = cv2.imread(archivo, cv2.IMREAD_GRAYSCALE)
            if img is None:
                return

            # --- Preprocesamiento ---
            img_blur = cv2.GaussianBlur(img, (5, 5), 0)

            # --- Detección de bordes con Canny ---
            edges = cv2.Canny(img_blur, 50, 150)

            # --- Buscar contornos ---
            contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # --- Crear imagen negra y dibujar SOLO contornos ---
            img_contorno = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            img_contorno[:] = (0, 0, 0)  # Fondo negro
            cv2.drawContours(img_contorno, contornos, -1, (0, 0, 255), 2)

            # Convertir a formato Qt
            altura, ancho, canales = img_contorno.shape
            bytes_per_line = canales * ancho
            qimg = QtGui.QImage(img_contorno.data, ancho, altura, bytes_per_line, QtGui.QImage.Format_RGB888).rgbSwapped()

            # Mostrar en QGraphicsView
            pixmap = QtGui.QPixmap.fromImage(qimg)
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(pixmap)
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
