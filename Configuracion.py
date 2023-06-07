from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QFormLayout, QAction, QToolBar, QLabel, QTableWidget, QLineEdit, \
    QPushButton, QHBoxLayout

from Fondo import Fondo

class Configuracion(QMainWindow):
    def __init__(self,principal):
        super(Configuracion, self).__init__(principal)

        self.ventanalogin = principal

        Fondo.Creacion_ventana(self)
        #Fondo.Creacion_barra(self)

        # TAMAÑO DE LOS ICONOS DE LA BARRA DE HERRAMIENTAS
        self.iconotamaño = 90
        # CREAMOS LA BARRA DE HERRAMIENTAS
        self.barraHerramientas = QToolBar("Barra de herramientas")
        # ESTABLECEMOS EL TAMAÑO DE LOS ICONOS DE LAS OPCIONES
        self.barraHerramientas.setIconSize(QSize(self.iconotamaño, self.iconotamaño))
        # definimos orientacion
        self.barraHerramientas.setOrientation(Qt.Vertical)

        # se establece el estilo
        self.barraHerramientas.setStyleSheet('background-color: #F49AE7;'
                                             'border: 1px solid white')
        # para que no se mueva el qtoolbar
        self.barraHerramientas.setMovable(False)

        # se va cargar la imagen como QPixmap para que sea transparente
        self.imageningreso = QPixmap("")

        self.imagenproductos = QPixmap("")

        self.imagenventa = QPixmap("")

        self.imagencotizador = QPixmap()

        self.imageninventario = QPixmap()

        self.imagenconfiguracion = QPixmap()

        self.imagenlogo = QPixmap("imagenes/Icono.jpeg")

        # crear logo
        self.logo = QAction(QIcon(self.imagenlogo.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Logo", self)

        # CREAMOS LA OPCION PARA LA ventana de ingreso tool tip es la parte que dice "iniciar sesion"
        self.usuario = QAction(QIcon(self.imageningreso.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Usuario",
                               self)

        # crear boton ventas
        self.ventas = QAction(QIcon(self.imagenventa.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Ventas", self)

        # acciones ventas
        # self.ventas.triggered.connect(self.accionesbarraventa)

        # Crear boton cotizacion
        self.cotizador = QAction(QIcon(self.imagencotizador.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                 "Cotizador", self)

        # Crear boton productos
        self.productos = QAction(QIcon(self.imagencotizador.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                 "Productos", self)
        # accion productos
        # self.productos.triggered.connect(self.accionesbarraproductos)

        # Crear boton configuracion
        self.configuracion = QAction(QIcon(self.imagenconfiguracion.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                     "Configuración", self)

        # Crear boton inventario
        self.inventario = QAction(QIcon(self.imagenconfiguracion.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                  "Inventario", self)

        # agregar el boton
        self.barraHerramientas.addAction(self.logo)
        self.barraHerramientas.addAction(self.usuario)
        self.barraHerramientas.addAction(self.ventas)
        # self.barraHerramientas.addAction(self.cotizador)
        self.barraHerramientas.addAction(self.productos)
        self.barraHerramientas.addAction(self.inventario)
        self.barraHerramientas.addAction(self.configuracion)

        # AGREGAR LA BARRA
        self.addToolBar(Qt.LeftToolBarArea, self.barraHerramientas)

        # establecemos el fondo principal
        self.fondo = QWidget()

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribucion de los elementos en forma de formulario
        self.formulario = QFormLayout()

        # hacemos el letrero
        self.letrero1 = QLabel()

        # ponemos el titulo ventas
        self.letrero1.setText("Configuracion")

        # linea final para agregar cosas
        self.fondo.setLayout(self.formulario)