from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect('database.db')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(140, 80, 113, 23))
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 54, 15))
        self.label.setObjectName("label")
        
        self.siglas = QtWidgets.QLineEdit(self.centralwidget)
        self.siglas.setGeometry(QtCore.QRect(140, 110, 113, 23))
        self.siglas.setObjectName("siglas")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 110, 54, 15))
        self.label_1.setObjectName("label_1")
        
        self.Estadio = QtWidgets.QLineEdit(self.centralwidget)
        self.Estadio.setGeometry(QtCore.QRect(140, 140, 113, 23))
        self.Estadio.setObjectName("Estadio")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 54, 15))
        self.label_2.setObjectName("label_2")
        
        self.seguidores = QtWidgets.QLineEdit(self.centralwidget)
        self.seguidores.setGeometry(QtCore.QRect(140, 170, 113, 23))
        self.seguidores.setText("")
        self.seguidores.setObjectName("seguidores")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 54, 15))
        self.label_3.setObjectName("label_3")
        
        self.campeonatos = QtWidgets.QLineEdit(self.centralwidget)
        self.campeonatos.setGeometry(QtCore.QRect(140, 200, 113, 23))
        self.campeonatos.setText("")
        self.campeonatos.setObjectName("campeonatos")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 200, 54, 15))
        self.label_4.setObjectName("label_4")
        
        # Botón guardar
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(70, 240, 211, 21))
        self.guardar.setObjectName("guardar")
        
        # Botón actualizar
        self.actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.actualizar.setGeometry(QtCore.QRect(70, 270, 211, 21))
        self.actualizar.setObjectName("actualizar")
        
        self.listaEquipos = QtWidgets.QTableWidget(self.centralwidget)
        self.listaEquipos.setGeometry(QtCore.QRect(300, 50, 450, 400))
        self.listaEquipos.setObjectName("listaEquipos")
        self.listaEquipos.setColumnCount(5)
        self.listaEquipos.setRowCount(0)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Configurar botones
        self.crear_base()
        self.obtener_informacion()
        self.guardar.clicked.connect(self.guardar_informacion)
        self.actualizar.clicked.connect(self.obtener_informacion)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestión de Equipos"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_1.setText(_translate("MainWindow", "Siglas"))
        self.label_2.setText(_translate("MainWindow", "Estadio"))
        self.label_3.setText(_translate("MainWindow", "Seguidores"))
        self.label_4.setText(_translate("MainWindow", "Campeonatos"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.actualizar.setText(_translate("MainWindow", "Actualizar"))

    def crear_base(self):
        cursor = conn.cursor()
        cadena_sql = 'CREATE TABLE IF NOT EXISTS Equipos (nombre TEXT, siglas TEXT, estadio TEXT, seguidores INTEGER, campeonatos INTEGER)'
        cursor.execute(cadena_sql)
        conn.commit()
        cursor.close()

    def guardar_informacion(self):
        cursor = conn.cursor()
        nombre = self.nombre.text()
        siglas = self.siglas.text()
        estadio = self.Estadio.text()
        seguidores = int(self.seguidores.text())
        campeonatos = int(self.campeonatos.text())
        
        cadena_sql = "INSERT INTO Equipos (nombre, siglas, estadio, seguidores, campeonatos) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(cadena_sql, (nombre, siglas, estadio, seguidores, campeonatos))
        conn.commit()
        cursor.close()
        self.obtener_informacion()

    def obtener_informacion(self):
        cursor = conn.cursor()
        cadena_consulta_sql = "SELECT * FROM Equipos"
        cursor.execute(cadena_consulta_sql)
        informacion = cursor.fetchall()
        self.listaEquipos.setRowCount(len(informacion))
        for row_index, row_data in enumerate(informacion):
            for col_index, col_data in enumerate(row_data):
                self.listaEquipos.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col_data)))
        self.listaEquipos.setHorizontalHeaderLabels(["Nombre", "Siglas", "Estadio", "Seguidores", "Campeonatos"])
        cursor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
