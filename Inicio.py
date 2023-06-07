import sys
from tkinter import font

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QFont, QColor
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QWidget, QToolBar, QAction, QVBoxLayout, \
    QDockWidget, QLabel, QSpacerItem, QSizePolicy, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

from Configuracion import Configuracion
from Fondo import Fondo
from Inventario import Inventario
from Productos import Productos
from Ventas import Ventas
from usuarios import Usuarios


# metodo constructor
class Inicio(QMainWindow):

    def __init__(self, parent=None):
        super(Inicio, self).__init__(parent)

        #definir una variable global para bloquear todos los botones
        self.registro = False


        Fondo.Creacion_ventana(self)
        Fondo.Creacion_barra(self)

        # AGREGAMOS LA BARRA DE HERRAMIENTAS
        self.addToolBar(Qt.LeftToolBarArea, self.barraHerramientas)


        #establecemos el fondo principal
        self.fondo = QWidget()

        #establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)



        #Establecemos la distribucion de los elementos en forma de formulario
        self.formulario = QFormLayout()


        # hacemos el letrero
        self.letrero1 = QLabel()

        # le escribimos el texto
        self.letrero1.setText("Iniciar sesión")

        # Establecer el tipo de letra
        self.fuenteTitulos = QFont("Comic Sans MS", 20)
        #negrilla
        self.fuenteTitulos.setBold(True)

        # Establecer el tipo de letra de subtitulos
        self.fuenteSubTitulos = QFont("Comic Sans MS", 14)
        #negrilla
        self.fuenteSubTitulos.setBold(True)


        # le asignamos el tipo de letra a los titulos
        self.letrero1.setFont(self.fuenteTitulos)


        # Centramos el texto
        self.letrero1.setAlignment(Qt.AlignCenter)

        #Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet('background-color: transparent; color: white; padding: 50px;')


        #agrego al layout
        self.formulario.addRow(self.letrero1)



        #Creamos un layout nuevo para alinear no se podia directamente por los qlineedit
        self.centroCaja = QVBoxLayout()


        # letrero de Usuario
        self.letreroUsuario = QLabel()

        # lo que vadecir el letrero
        self.letreroUsuario.setText("Usuario")

        # El tipo de fuente
        self.letreroUsuario.setFont(self.fuenteSubTitulos)


        #Le ponemos color de fondo, color de texto y margenes al letrero
        self.letreroUsuario.setStyleSheet('background-color: transparent; color: black; padding: 0px')


        #agrego al layout
        self.centroCaja.addWidget(self.letreroUsuario)



        # Campo para ingresar usuario
        self.idUsuario = QLineEdit()
        #lo ingresado sea minusculas
        # #definimos el ancho del campo en 80px
        self.idUsuario.setFixedWidth(150)
        # Establecemos que solo ingrese maximo 5 digitos
        self.idUsuario.setMaxLength(20)

        #formato de ingreso
        self.idUsuario.setStyleSheet("QLineEdit { background-color: white; color: black;}")

        self.centroCaja.addWidget(self.idUsuario)


        # letrero de Usuario
        self.letreroContraseña = QLabel()

        # lo que vadecir el letrero
        self.letreroContraseña.setText("Contraseña")

        # El tipo de fuente
        self.letreroContraseña.setFont(self.fuenteSubTitulos)

        # Alinear
        #self.letreroUsuario.setAlignment(Qt.AlignCenter)

        #Le ponemos color de fondo, color de texto y margenes al letrero
        self.letreroContraseña.setStyleSheet('background-color: transparent; color: black; padding: 0px')


        #agrego al layout
        self.centroCaja.addWidget(self.letreroContraseña)


        # Campo para ingresar usuario
        self.clave = QLineEdit()

        # #definimos el ancho del campo en 80px
        self.clave.setFixedWidth(150)
        # Establecemos que solo ingrese maximo 5 digitos
        self.clave.setMaxLength(20)

        #formato de ingreso
        self.clave.setStyleSheet("QLineEdit { background-color: white; color: black; }")

        self.clave.setEchoMode(QLineEdit.Password)

        #agrego al layout
        self.centroCaja.addWidget(self.clave)

        # Hacemos un boton para ingresar
        self.botonIngresar = QPushButton("Ingresar")
        # Establecemos el ancho del boton
        self.botonIngresar.setFixedWidth(100)

        #llamamos el metodo ingresar
        self.botonIngresar.clicked.connect(self.accionbotoningresar)

        self.botonIngresar.setFont(self.fuenteSubTitulos)

        self.centroCaja.addSpacing(30)

        self.centroCaja.addWidget(self.botonIngresar)

        self.centroCaja.setAlignment(Qt.AlignCenter)


        self.formulario.addRow(self.centroCaja)

        #linea final para agregar cosas
        self.fondo.setLayout(self.formulario)

    def accionesbarraproductos(self):

        if self.registro == False:
            return QMessageBox.warning(self, "Warning", "Ingrese Usuario y Contraseña")
        else:
            # Se oculta la ventana actual
            self.hide()
            print("control")
            # conectamos
            self.ventana_productos = Productos(self)
            print("control")
            # mostramos
            self.ventana_productos.show()
            print("control")

    def accionesbarraventa(self):
        if self.registro == False:
            return QMessageBox.warning(self, "Warning", "Ingrese Usuario y Contraseña")
        else:
            #Se oculta la ventana actual
            self.hide()
            print("control")
            #conectamos
            self.ventana_ventas = Ventas(self)
            print("control")
            #mostramos
            self.ventana_ventas.show()
            print("control")

    def accionbarrainventario(self):
        if self.registro == False:
            return QMessageBox.warning(self, "Warning", "Ingrese Usuario y Contraseña")
        else:
            #Se oculta la ventana actual
            self.hide()
            #print("control")
            #conectamos
            self.ventana_inventario = Inventario(self)
            #print("control")
            #mostramos
            self.ventana_inventario.show()
            #print("control")

    def accionbarraconfiguracion(self):
        if self.registro == False:
            return QMessageBox.warning(self, "Warning", "Ingrese Usuario y Contraseña")
        else:
            # Se oculta la ventana actual
            self.hide()
            # print("control")
            # conectamos
            self.ventana_configuracion = Configuracion(self)
            # print("control")
            # mostramos
            self.ventana_configuracion.show()
            # print("control")

    def accionbotoningresar(self):
        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = True

        if (
                self.clave.text() == '' or self.idUsuario.text() == ""
        ):
            self.datosCorrectos = False
            return QMessageBox.warning(self, "Warning", "Ingrese Usuario y Contraseña")
        if (
                not self.clave.text().isnumeric()
        ):
            self.datosCorrectos = False
            return QMessageBox.warning(self, "Warning", "La Contraseña debe ser numérica. "
                                                                    "\nNO ingrese letras "
                                                            "Ni caracteres especiales.")
        # Si los datos están correctos
        if (
                self.datosCorrectos
        ):
            # Abrimos el archivo en modo lectura:
            self.file = open('datos/usuarios.txt', 'rb')

            # Lista vacía para agregar todos los usuarios:
            usuarios1 = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por;
                lista = linea.split(";")
                # Se para si ya no hay más registros en el archivo
                if linea == '':
                    break
                # Creamos un objeto de tipo cliente llamado u:
                print(linea)
                u = Usuarios(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4]
                )

                # Metemos el objeto en la lista de usuarios:
                usuarios1.append(u)

            # Cerramos el archivo:
            self.file.close()

            # Variable para controlar si existe el documento:
            existeUsuario = False

            # Variable para controlar si existe el clave:
            existeclave = False

            # Buscamos en la lista usuario por usuario si existe la cédula:
            for u in usuarios1:

                # Comparamos el documento ingresado:
                # Si corresponde con el documento, es el usuario correcto:
                #prueba de comparacion no olvidar el .text()
                numero = len(usuarios1)
                print(u.usuario+" compara "+self.idUsuario.text()+" otra "+ u.password+" Compara "+self.clave.text() + "tamaño lista: " + str(numero))
                if u.usuario == self.idUsuario.text().lower() and u.password == self.clave.text():

                    # Indicamos que encontramos el usuario:
                    existeUsuario = True
                    existeclave = True
                    #print("enloqueciendo:"+str(u.admin))
                    if u.admin > str(0):
                        permiso = True
                    else:
                        permiso = False
                    #print("enloqueciendo2 "+str(permiso))


                    # Paramos el for:
                    break
                    # Si no existe un usuario con este usuario:
            if (
                    not existeUsuario or not existeclave
            ):
                return QMessageBox.warning(self, "Warning", "Usuario y Contraseña no coinciden")
            else:


                # Se oculta la ventana actual
                self.hide()
                # conectamos
                self.ventana_ventas = Ventas(self,permiso)
                # mostramos
                self.ventana_ventas.show()




if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    inicio = Inicio()

    inicio.show()

    sys.exit(app.exec_())
