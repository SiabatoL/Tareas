# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.label = QtWidgets.QLabel("TIPOS DE ROBOT", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 361, 141))
        self.label.setFont(QtGui.QFont("Arial", 21, QtGui.QFont.Bold))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white;")

        # --- Créditos ---
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 460, 390, 133))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Nombres = QtWidgets.QLabel("Cristian Zamora - Laura Siabato")
        self.Nombres.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.Nombres.setStyleSheet("color: white;")
        self.Nombres.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.Nombres)

        self.subtitulo = QtWidgets.QLabel("Ing. Mecatrónica - Electiva Robótica")
        self.subtitulo.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.subtitulo.setStyleSheet("color: white;")
        self.subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.subtitulo)

        self.year = QtWidgets.QLabel("2025 - 1")
        self.year.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.year.setStyleSheet("color: white;")
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.year)

        # --- Logo ---
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(470, 460, 331, 131))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)

        # --- Botón con menú emergente ---
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(80, 220, 371, 71))
        self.toolButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.toolButton.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.toolButton.setStyleSheet("color: blue; background-color:rgb(27, 27, 27); border-radius: 5px;")
        self.toolButton.setText("Seleccionar tipo de robot")

        # --- Área de imágenes ---
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(520, 210, 281, 211))
        self.graphicsView.setStyleSheet("background-color: white; border: 2px solid black;")

        # --- Subtítulo ---
        self.Nombres_2 = QtWidgets.QLabel("_ _ _ _ _ _ _", self.centralwidget)
        self.Nombres_2.setGeometry(QtCore.QRect(70, 360, 388, 39))
        self.Nombres_2.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.Nombres_2.setStyleSheet("color: white;")
        self.Nombres_2.setAlignment(QtCore.Qt.AlignCenter)

        # --- Descripción dinámica ---
        self.descripcion = QtWidgets.QLabel("Seleccione un tipo de robot", self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(80, 320, 371, 41))
        self.descripcion.setStyleSheet("color: white; font-size: 14px;")
        self.descripcion.setAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # --- Barra de menú y estado ---
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 29))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # --- Diccionario de robots (imagen + descripción) ---
        self.robots = {
            "Robot cartesiano": ("im1.png", "Tres Prismáticas."),
            "Robot esférico": ("im2.png", "Dos articulaciones rotacionales y una prismática."),
            "Robot cilíndrico": ("im3.png", "Dos prismáticas una rotacional."),
        }

        # --- Crear menú ---
        self.crear_menu()

        # --- Mostrar logo al inicio ---
        self.mostrar_logo("Logoecci.png")

    def crear_menu(self):
        """Crea un menú emergente con opciones dinámicas según el diccionario"""
        menu = QtWidgets.QMenu()
        for nombre, (imagen, descripcion) in self.robots.items():
            action = menu.addAction(nombre)
            action.triggered.connect(lambda checked, img=imagen, desc=descripcion: self.mostrar_imagen(img, desc))
        self.toolButton.setMenu(menu)

    def mostrar_imagen(self, nombre_archivo, descripcion_texto):
        """Muestra la imagen seleccionada en el GraphicsView"""
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        scene = QtWidgets.QGraphicsScene()

        if os.path.exists(ruta):
            pixmap = QtGui.QPixmap(ruta)
            item = scene.addPixmap(pixmap)
            # Ajuste proporcional
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(item, QtCore.Qt.KeepAspectRatio)
        else:
            text_item = scene.addText("No se encontró " + nombre_archivo)
            text_item.setDefaultTextColor(QtCore.Qt.red)
            self.graphicsView.setScene(scene)

        # Actualizar descripción
        self.descripcion.setText(descripcion_texto)

    def mostrar_logo(self, nombre_archivo):
        """Muestra el logo institucional en el QLabel inferior derecho"""
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        if os.path.exists(ruta):
            pixmap = QtGui.QPixmap(ruta)
            pixmap = pixmap.scaled(self.logo.size(),
                                   QtCore.Qt.KeepAspectRatio,
                                   QtCore.Qt.SmoothTransformation)
            self.logo.setPixmap(pixmap)
        else:
            self.logo.setText("Logo no encontrado")
            self.logo.setStyleSheet("color: red; border: 2px solid black;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
