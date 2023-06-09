import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QFormLayout, QAction, QToolBar, QLabel, QTableWidget, QLineEdit, \
    QPushButton, QHBoxLayout, QApplication

from Fondo import Fondo


class Inventario(QMainWindow):
    def __init__(self,principal):
        super(Inventario, self).__init__(principal)

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
        self.letrero1.setText("Inventario")

        # agregamos el letrero1
        self.formulario.addRow(self.letrero1)

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

        # se crea la tabla
        self.tabla_productos = QTableWidget()

        self.tabla_productos.setHorizontalHeaderLabels(['Nombre', 'Precio', 'Stock'])  # Encabezados de columna
        self.tabla_productos.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar edición de celdas

        # Agregamos los botones

        # agregamos texto para ingresar codigo del producto
        self.labelcodigo = QLabel()
        self.labelcodigo.setText("Ingrese codigo del producto: ")

        # agregar un qline edit para el codigo
        self.codigoproducto = QLineEdit()
        self.codigoproducto.setFixedWidth(150)
        self.codigoproducto.setFixedHeight(20)

        # creamos el boton de agregar producto
        self.botonagregar = QPushButton()

        # agrego el texto al boton
        self.botonagregar.setText("Agregar a Inventario")

        # controlo tamaño
        self.botonagregar.setFixedWidth(150)

        # boton eliminar
        self.botoneliminarp = QPushButton()
        self.botoneliminarp.setText("Eliminar producto")
        self.botoneliminarp.setFixedWidth(150)

        # boton buscar
        self.botonbuscar = QPushButton()
        self.botonbuscar.setText("Modificar Producto")
        self.botonbuscar.setFixedWidth(150)

        # boton agregar inventario
        self.botonagregarInventario = QPushButton()
        self.botonagregarInventario.setText("Agregar Inventario")
        self.botonagregarInventario.setFixedWidth(150)

        # Establecer el tipo de letra de subtitulos
        self.fuenteSubTitulos1 = QFont("Arial Black", 30)
        # negrilla
        self.fuenteSubTitulos1.setBold(True)

        # agrego label abajo que diga subtotal
        self.subtotal = QLabel()
        self.subtotal.setText(" ")
        self.subtotal.setFont(self.fuenteSubTitulos1)

        # Boton de pagar
        self.botonpagar = QPushButton()
        self.botonpagar.setText("PAGAR")
        self.botonpagar.setFixedWidth(200)
        self.botonpagar.setFixedHeight(50)

        # creemos un layout para mover el boton de pagar a la derecha
        self.layoutpagar = QHBoxLayout()
        self.layoutpagar.addWidget(self.subtotal)
        self.layoutpagar.addStretch()
        #self.layoutpagar.addWidget(self.botonpagar)

        # agrego el label
        self.formulario.addRow(self.labelcodigo)

        # sub layout de solo botones en la parte de arriba
        self.botonesarriba = QHBoxLayout()
        self.botonesarriba.addWidget(self.botonagregar)
        self.botonesarriba.addWidget(self.botoneliminarp)
        self.botonesarriba.addWidget(self.botonbuscar)


        # agregamos botones
        self.formulario.addRow(self.codigoproducto, self.botonesarriba)

        # agrego la qtable
        self.formulario.addRow(self.tabla_productos)

        # agrego subtotal y pagar
        self.formulario.addRow(self.layoutpagar)

        # linea final para agregar cosas
        self.fondo.setLayout(self.formulario)


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    inventario = Inventario(principal=None)

    inventario.show()

    sys.exit(app.exec_())