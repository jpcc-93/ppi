from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QFormLayout, QAction, QToolBar, QTableWidget, QPushButton, \
    QVBoxLayout, QTableWidgetItem, QLabel, QLineEdit, QHBoxLayout, QMessageBox

from Configuracion import Configuracion
from Fondo import Fondo
from Inventario import Inventario
from Productos import Productos


class Ventas(QMainWindow):
    def __init__(self,principal,permiso):
        super(Ventas, self).__init__(principal)

        self.ventanalogin = principal
        #print("original: " + str(permiso))
        self.permiso = permiso
        #print("nuevo valor: " + str(self.permiso1))


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
        #self.ventas.triggered.connect(self.accionesbarraventa)

        # Crear boton cotizacion
        self.cotizador = QAction(QIcon(self.imagencotizador.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                 "Cotizador", self)

        # Crear boton productos
        self.productos = QAction(QIcon(self.imagencotizador.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                 "Productos", self)
        #accion productos
        self.productos.triggered.connect(self.accionesbarraproductos)

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
        #self.barraHerramientas.addAction(self.usuario)
        #self.barraHerramientas.addAction(self.ventas)
        #self.barraHerramientas.addAction(self.cotizador)
        self.barraHerramientas.addAction(self.productos)
        self.barraHerramientas.addAction(self.inventario)
        self.barraHerramientas.addAction(self.configuracion)
        self.configuracion.triggered.connect(self.accionbarraconfiguracion)



        #AGREGAR LA BARRA
        self.addToolBar(Qt.LeftToolBarArea,self.barraHerramientas)



        # establecemos el fondo principal
        self.fondo = QWidget()

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribucion de los elementos en forma de formulario
        self.formulario = QFormLayout()

        # hacemos el letrero
        self.letrero1 = QLabel()

        #ponemos el titulo ventas
        self.letrero1.setText("Ventas")

        #agregamos el letrero1
        self.formulario.addRow(self.letrero1)



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


        # se crea la tabla
        self.tabla_productos = QTableWidget()

        self.tabla_productos.setHorizontalHeaderLabels(['Nombre', 'Precio', 'Stock'])  # Encabezados de columna
        self.tabla_productos.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar edición de celdas

        #Agregamos los botones

        #agregamos texto para ingresar codigo del producto
        self.labelcodigo = QLabel()
        self.labelcodigo.setText("Ingrese codigo del producto: ")

        #agregar un qline edit para el codigo
        self.codigoproducto = QLineEdit()
        self.codigoproducto.setFixedWidth(150)
        self.codigoproducto.setFixedHeight(20)

        #creamos el boton de agregar producto
        self.botonagregar = QPushButton()

        #agrego el texto al boton
        self.botonagregar.setText("Agregar producto")

        #controlo tamaño
        self.botonagregar.setFixedWidth(150)

        #boton eliminar
        self.botoneliminarp = QPushButton()
        self.botoneliminarp.setText("Eliminar producto")
        self.botoneliminarp.setFixedWidth(150)

        #boton buscar
        self.botonbuscar = QPushButton()
        self.botonbuscar.setText("Buscar Producto")
        self.botonbuscar.setFixedWidth(150)

        # Establecer el tipo de letra de subtitulos
        self.fuenteSubTitulos1 = QFont("Arial Black", 30)
        #negrilla
        self.fuenteSubTitulos1.setBold(True)

        #agrego label abajo que diga subtotal
        self.subtotal = QLabel()
        self.subtotal.setText("SUB TOTAL: $ 0 ")
        self.subtotal.setFont(self.fuenteSubTitulos1)

        #Boton de pagar
        self.botonpagar = QPushButton()
        self.botonpagar.setText("PAGAR")
        self.botonpagar.setFixedWidth(200)
        self.botonpagar.setFixedHeight(50)

        #creemos un layout para mover el boton de pagar a la derecha
        self.layoutpagar = QHBoxLayout()
        self.layoutpagar.addWidget(self.subtotal)
        self.layoutpagar.addStretch()
        self.layoutpagar.addWidget(self.botonpagar)




        #agrego el label
        self.formulario.addRow(self.labelcodigo)



        # sub layout de solo botones en la parte de arriba
        self.botonesarriba = QHBoxLayout()
        self.botonesarriba.addWidget(self.botonagregar)
        self.botonesarriba.addWidget(self.botoneliminarp)
        self.botonesarriba.addWidget(self.botonbuscar)

        #agregamos botones
        self.formulario.addRow(self.codigoproducto,self.botonesarriba)


        #agrego la qtable
        self.formulario.addRow(self.tabla_productos)

        #agrego subtotal y pagar
        self.formulario.addRow(self.layoutpagar)









        #linea final para agregar cosas
        self.fondo.setLayout(self.formulario)

    def accionesbarraproductos(self):
        # Se oculta la ventana actual
        self.hide()
        #print("control")
        # conectamos
        self.ventana_productos = Productos(self,self.permiso)
        #print("control")
        # mostramos
        self.ventana_productos.show()
        #print("control")

    def accionbarrainventario(self):
        if self.permiso1 == 0:

            print("control")
            # conectamos
            QMessageBox.warning(self, "Warning", "No tiene permisos")
        else:
            #Se oculta la ventana actual
            self.hide()
            print("control")
            #conectamos
            self.ventana_inventario = Inventario(self)
            print("control")
            #mostramos
            self.ventana_inventario.show()
            print("control")

    def accionbarraconfiguracion(self):

        if self.permiso == 0:

            #print("control")
            # conectamos
            QMessageBox.warning(self, "Warning", "No tiene permisos")
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






