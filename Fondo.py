from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDesktopWidget, QToolBar, QAction



class Fondo():
    def Creacion_ventana(self):
        # poner titulo
        self.setWindowTitle("Sueños De Angel")

        # Establecer propiedades de ancho y alto
        self.ancho = 800
        self.alto = 600

        # establecer el tamaño
        self.resize(self.ancho, self.alto)

        # lineas para ventana en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que no se pueda cambiar el tamaño
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos una imagen de fondo para toda la ventana
        self.setStyleSheet('QMainWindow {background-image: url(imagenes/imagen fondo2p.jpg);'
                           'background-repeat: no-repeat;'
                           'background-position: center;}')

    def Creacion_barra(self):
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

        # CREAMOS LA OPCION PARA LA ventana de ingreso tool tip es la parte que dice "iniciar sesion"
        self.usuario = QAction(QIcon(self.imageningreso.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Usuario",
                               self)
        #crear logo
        self.logo = QAction(QIcon(self.imagenlogo.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Logo", self)

        # crear boton ventas
        self.ventas = QAction(QIcon(self.imagenventa.scaled(QSize(self.iconotamaño, self.iconotamaño))), "Ventas", self)

        # acciones ventas
        self.ventas.triggered.connect(self.accionesbarraventa)

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
        #accion configuracion
        self.configuracion.triggered.connect(self.accionbarraconfiguracion)

        # Crear boton inventario
        self.inventario = QAction(QIcon(self.imagenconfiguracion.scaled(QSize(self.iconotamaño, self.iconotamaño))),
                                  "Inventario", self)
        #accion inventario
        self.inventario.triggered.connect(self.accionbarrainventario)

        # agregar el boton
        self.barraHerramientas.addAction(self.logo)
        #self.barraHerramientas.addAction(self.usuario)
        self.barraHerramientas.addAction(self.ventas)
        #self.barraHerramientas.addAction(self.cotizador)
        self.barraHerramientas.addAction(self.productos)
        self.barraHerramientas.addAction(self.inventario)
        self.barraHerramientas.addAction(self.configuracion)


    #def accionesbarraventa(self):
     #   pass
        #Se oculta la ventana actual
        #self.hide()
        #conectamos con ventana ventas
        #self.ventana_ventas =Ventas(self)

        #mostramos la ventana
        #self.ventana_ventas.show()
#    def accionesbarraproductos(self):
    #    pass