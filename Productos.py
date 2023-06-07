from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QAction, QToolBar, QLabel, QFormLayout, QWidget, QLineEdit, QComboBox, \
    QPushButton, QHBoxLayout, QMessageBox

from Fondo import Fondo
from Inventario import Inventario


class Productos(QMainWindow):
    def __init__(self,principal,permiso):
        super(Productos, self).__init__(principal)

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

        #accion inventario
        self.inventario.triggered.connect(self.accionbarrainventario)

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
        self.letrero1.setText("Nuevo producto")

        self.letreroexp = QLabel()
        self.letreroexp.setText("")

        # agregamos el letrero1
        self.formulario.addRow(self.letrero1)
        #agregamos la explicacion
        self.formulario.addRow(self.letreroexp)

        # Establecer el tipo de letra
        self.fuenteTitulos = QFont("Comic Sans MS", 20)
        # negrilla
        self.fuenteTitulos.setBold(True)

        # Establecer el tipo de letra de subtitulos
        self.fuenteSubTitulos = QFont("Comic Sans MS", 14)
        # negrilla
        self.fuenteSubTitulos.setBold(True)

        # le asignamos el tipo de letra a los titulos
        self.letrero1.setFont(self.fuenteTitulos)



        # botones de nuevo modificar y eliminar
        # nuevo
        self.botonnuevoP = QPushButton()
        self.botonnuevoP.setText("Agregar Producto")
        self.botonnuevoP.setFixedWidth(150)
        self.botonnuevoP.clicked.connect(self.casoCrear)

        # modificar
        self.botonmodificarP = QPushButton()
        self.botonmodificarP.setText("Modificar Producto")
        self.botonmodificarP.setFixedWidth(150)
        if permiso == True:
            self.botonmodificarP.clicked.connect(self.casoModificar)
        else:
            self.botonmodificarP.clicked.connect(self.sinPermisos)

        # eliminar
        self.botoneliminarP = QPushButton()
        self.botoneliminarP.setText("Eliminar Producto")
        self.botoneliminarP.setFixedWidth(150)
        if permiso == True:
            self.botonmodificarP.clicked.connect(self.casoEliminar)
        else:
            self.botonmodificarP.clicked.connect(self.sinPermisos)

        # sub layout
        self.ordenbotones = QHBoxLayout()
        self.ordenbotones.addWidget(self.botonnuevoP)
        self.ordenbotones.addWidget(self.botonmodificarP)
        self.ordenbotones.addWidget(self.botoneliminarP)
        # espacio en el formulario
        self.espacio = QWidget()
        self.espacio.setFixedHeight(50)

        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.ordenbotones)







        #Agregar al final

        self.fondo.setLayout(self.formulario)

    def accionbarrainventario(self):
        #Se oculta la ventana actual
        self.hide()
        print("control")
        #conectamos
        self.ventana_inventario = Inventario(self)
        print("control")
        #mostramos
        self.ventana_inventario.show()
        print("control")

    def casoCrear(self):
        self.letreroexp.setText("Ingrese los datos del nuevo producto")
        # caracteristicas del producto a crear
        # codigo
        self.letrerocodigo = QLabel()
        self.letrerocodigo.setText("Codigo del producto: ")
        self.codigoP = QLineEdit()
        self.codigoP.setFixedWidth(100)

        # Nombre
        self.letreronombre = QLabel()
        self.letreronombre.setText("Ingrese el nombre del producto: ")
        self.nombreP = QLineEdit()
        self.nombreP.setFixedWidth(300)

        # precio de compra o fabricacion
        self.letrerocosto = QLabel()
        self.letrerocosto.setText("Ingrese el precio de costo del producto: ")
        self.valorcostoP = QLineEdit()
        self.valorcostoP.setFixedWidth(100)

        # precio de venta
        self.letreroventa = QLabel()
        self.letreroventa.setText("Ingrese el precio de venta del producto:")
        self.valorventaP = QLineEdit()
        self.valorventaP.setFixedWidth(100)

        # Departamento
        self.letrerotipoP = QLabel()
        self.letrerotipoP.setText("Escoja el departamento del producto: ")
        self.departamento = QComboBox()
        self.departamento.addItem("Dama")
        self.departamento.addItem("Niñas")
        self.departamento.addItem("Hombres")
        self.departamento.addItem("Niños")
        self.departamento.addItem("Otros")
        self.departamento.setFixedWidth(100)

        # espacio en el formulario
        self.espacio = QWidget()
        self.espacio.setFixedHeight(50)

        # boton guardar
        self.botonguardar = QPushButton()
        self.botonguardar.setText("GUARDAR")
        self.botonguardar.setFixedWidth(200)
        self.botonguardar.setFixedHeight(50)

        # Agregar al formulario
        self.formulario.addRow(self.espacio)
        #self.formulario.addRow(self.ordenbotones)
        #self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.letrerocodigo, self.codigoP)
        self.formulario.addRow(self.letreronombre, self.nombreP)
        self.formulario.addRow(self.letrerocosto, self.valorcostoP)
        self.formulario.addRow(self.letreroventa, self.valorventaP)
        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.letrerotipoP, self.departamento)
        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.botonguardar)

    def casoModificar(self):
        self.nombreP.setReadOnly(True)
        self.valorcostoP.setReadOnly(True)
        self.valorventaP.setReadOnly(True)
        self.departamento.setDisabled(True)
        self.letrero1.setText("Modificar Producto")
        self.letreroexp.setText("Ingrese el codigo del producto a modificar \nEn caso de no recordarlo consultar en inventario")
        self.botonguardar.setText("Buscar")



    def casoEliminar(self):
        pass
    def sinPermisos(self):
        QMessageBox.warning(self, "Warning", "No cuenta con permisos")

    #def limpiarlayout(self):
     #   self.formulario = QFormLayout


