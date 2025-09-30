# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

# --- Intento de importar GPIO ---
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    RPI_AVAILABLE = True
except (ImportError, RuntimeError):
    # Simulación para pruebas en PC
    import random
    RPI_AVAILABLE = False

    class MockGPIO:
        BCM = "BCM"
        IN = "IN"
        HIGH = 1
        LOW = 0

        def setmode(self, mode):
            print(f"[MockGPIO] setmode({mode})")

        def setup(self, pin, mode):
            print(f"[MockGPIO] setup(pin={pin}, mode={mode})")

        def input(self, pin):
            # Devuelve aleatorio para simular cambios
            return random.choice([self.HIGH, self.LOW])

        def cleanup(self):
            print("[MockGPIO] cleanup()")

    GPIO = MockGPIO()  # Usar la simulación


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
        self.TITULO = QtWidgets.QLabel(self.centralwidget)
        self.TITULO.setGeometry(QtCore.QRect(180, 10, 551, 141))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.TITULO.setFont(font)
        self.TITULO.setAlignment(QtCore.Qt.AlignCenter)

        # --- Info ---
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 460, 390, 133))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.Nombres = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Nombres.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.Nombres.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.Nombres)

        self.subtitulo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.subtitulo.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.subtitulo)

        self.year = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.year.setFont(QtGui.QFont("Arial", 11, QtGui.QFont.Bold))
        self.year.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.year)

        # --- Logo (placeholder) ---
        self.logo = QtWidgets.QGraphicsView(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(470, 460, 331, 131))

        # --- Label de Estado ---
        self.testigoLectura = QtWidgets.QLabel(self.centralwidget)
        self.testigoLectura.setGeometry(QtCore.QRect(310, 250, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.testigoLectura.setFont(font)
        self.testigoLectura.setAlignment(QtCore.Qt.AlignCenter)
        self.testigoLectura.setStyleSheet("background-color: black; color: white;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # --- Configuración de GPIO ---
        self.GPIO_PIN = 17
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.GPIO_PIN, GPIO.IN)
        except Exception as e:
            print(f"[ERROR GPIO] {e}")

        # --- Timer para actualizar estado ---
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_estado)
        self.timer.start(500)  # 500 ms

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lectura de Puertos"))
        self.TITULO.setText(_translate("MainWindow", "<html><body><p><span style='font-size:28pt; color:white;'>LECTURA DE PUERTOS</span></p></body></html>"))
        self.Nombres.setText(_translate("MainWindow", "<html><body><p><span style='color:white;'>Cristian Zamora - Laura Siabato</span></p></body></html>"))
        self.subtitulo.setText(_translate("MainWindow", "<html><body><p><span style='color:white;'>Ing. Mecatrónica Electiva Robótica</span></p></body></html>"))
        self.year.setText(_translate("MainWindow", "<html><body><p><span style='color:white;'>2025 - 1</span></p></body></html>"))
        self.testigoLectura.setText(_translate("MainWindow", "TESTIGO"))

    def actualizar_estado(self):
        """Lee el pin GPIO (o simula en PC)"""
        try:
            estado = GPIO.input(self.GPIO_PIN)
            if estado == GPIO.HIGH:
                self.testigoLectura.setText("ALTO")
                self.testigoLectura.setStyleSheet("background-color: red; color: white;")
            else:
                self.testigoLectura.setText("BAJO")
                self.testigoLectura.setStyleSheet("background-color: blue; color: white;")
        except Exception as e:
            print(f"[ERROR lectura GPIO] {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    finally:
        try:
            GPIO.cleanup()
        except Exception:
            pass
