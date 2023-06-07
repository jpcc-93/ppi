from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QAction, QToolBar, QLabel, QFormLayout, QWidget, QLineEdit, QComboBox, \
    QPushButton, QHBoxLayout, QMessageBox

from Fondo import Fondo
from Inventario import Inventario
from claseproductos import Claseproductos


class Productos(QMainWindow):
    def __init__(self,principal,permiso):
        super(Productos, self).__init__(principal)

        self.ventanalogin = principal
        self.permiso1 = permiso


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



        self.crear_botones()
    def crear_botones(self):

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
        if self.permiso1 == True:
            self.botonmodificarP.clicked.connect(self.casoModificar)
        else:
            self.botonmodificarP.clicked.connect(self.sinPermisos)

        # eliminar
        self.botoneliminarP = QPushButton()
        self.botoneliminarP.setText("Eliminar Producto")
        self.botoneliminarP.setFixedWidth(150)
        if self.permiso1 == True:
            self.botoneliminarP.clicked.connect(self.casoEliminar)
        else:
            self.botoneliminarP.clicked.connect(self.sinPermisos)

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

    def crearformularios(self):
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
        self.multibotonguardar = QPushButton()
        self.multibotonguardar.setText("Guardar")
        self.multibotonguardar.setFixedWidth(200)
        self.multibotonguardar.setFixedHeight(50)

        # Agregar al formulario
        self.formulario.addRow(self.espacio)
        # self.formulario.addRow(self.ordenbotones)
        # self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.letrerocodigo, self.codigoP)
        self.formulario.addRow(self.letreronombre, self.nombreP)
        self.formulario.addRow(self.letrerocosto, self.valorcostoP)
        self.formulario.addRow(self.letreroventa, self.valorventaP)
        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.letrerotipoP, self.departamento)
        self.formulario.addRow(self.espacio)
        self.formulario.addRow(self.multibotonguardar)

    def casoCrear(self):
        self.limpiarlayout()
        self.crear_botones()
        self.crearformularios()
        self.botonnuevoP.setDisabled(True)
        self.botonmodificarP.setDisabled(False)
        self.botoneliminarP.setDisabled(False)
        self.multibotonguardar.clicked.connect(self.accionmultiBotonguardar)

    def casoModificar(self):
        self.limpiarlayout()
        self.crear_botones()
        self.crearformularios()
        self.botonmodificarP.setDisabled(True)
        self.botonnuevoP.setDisabled(False)
        self.botoneliminarP.setDisabled(False)
        self.nombreP.setReadOnly(True)
        self.valorcostoP.setReadOnly(True)
        self.valorventaP.setReadOnly(True)
        self.departamento.setDisabled(True)
        self.letrero1.setText("Modificar Producto")
        self.letreroexp.setText("Ingrese el codigo del producto a modificar \nEn caso de no recordarlo consultar en inventario")
        self.multibotonguardar.setText("Buscar")
        self.multibotonguardar.clicked.connect(self.accionmultiBotonbuscar)

    def casoEliminar(self):
        self.limpiarlayout()
        self.crear_botones()
        self.crearformularios()
        self.botonmodificarP.setDisabled(False)
        self.botonnuevoP.setDisabled(False)
        self.botoneliminarP.setDisabled(True)
        self.nombreP.setReadOnly(True)
        self.valorcostoP.setReadOnly(True)
        self.valorventaP.setReadOnly(True)
        self.departamento.setDisabled(True)
        self.letrero1.setText("Eliminar Producto")
        self.letreroexp.setText(
            "Ingrese el codigo del producto a eliminar \nEn caso de no recordarlo consultar en inventario")
        self.multibotonguardar.setText("Buscar")
    def accionmultiBotonguardar(self):
        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = True

        #se valida para ingresar todos los campos
        if(
            self.codigoP.text() == ""
            or self.nombreP.text() == ""
            or self.valorventaP.text() == ""
            or self.departamento == ""
        ):
            self.datosCorrectos = False
            self.datosIncompletos()
        # se revisa que los campos sean numericos
        else:
            if(
                not self.codigoP.text().isnumeric()

            ):
                QMessageBox.warning(self, "Warning", "El campo codigo debe ser numerico")
                self.datosCorrectos = False
            if (
                    not self.valorcostoP.text().isnumeric()
            ):
                QMessageBox.warning(self, "Warning", "El campo precio costo debe ser numerico")
                self.datosCorrectos = False
            if(
                not self.valorventaP.text().isnumeric()
            ):
                QMessageBox.warning(self, "Warning", "El campo precio venta debe ser numerico")
                self.datosCorrectos = False
            if(
                self.nombreP.text().isspace()
            ):
                QMessageBox.warning(self, "Warning", "El campo nombre no puede contener espacios")
                self.datosCorrectos = False


        # se recorre el archivo para que el codigo no se repita
        # Abrimos el archivo en modo lectura:
        self.file = open('datos/productos.txt', 'rb')

        # Lista vacía para agregar todos los usuarios:
        productos1 = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Se para si ya no hay más registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamado u:
            print(linea)
            u = Claseproductos(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
            )

            # Metemos el objeto en la lista de usuarios:
            productos1.append(u)

        # Cerramos el archivo:
        self.file.close()

        #recorremos los productos para comparar que no exista el codigo
        for u in productos1:
            #comparamos el codigo ingresado
            if u.codigo == self.codigoP.text():
                QMessageBox.warning(self, "Warning", "El codigo ya existe")
                self.datosCorrectos = False

        # se gurda el producto
        if(self.datosCorrectos):
            # abrimos el archivo en modo agregar escribiendo datos en binario

            self.file = open('datos/productos.txt', 'ab')

            # traer el texto de los QLineEdit y los agrega concatenandolos
            # para escribirlos en formato binario utf-8
            self.file.write(bytes(
                self.codigoP.text() + ";"
                + self.nombreP.text() + ";"
                + self.valorcostoP.text() + ";"
                + self.valorventaP.text() + ";"
                + self.departamento.currentText() + ";"
                + self.inventario.text() + "\n"
                , encoding='UTF-8'))
            # cerramos el archivo
            self.file.close()

            self.limpiarcampos()
            QMessageBox.information(self,"Confirmado","Se creo el producto correctamente")

    def accionmultiBotonbuscar(self):
        # variable para controral si el ingreso de los datos estan correctos
        self.datosCorrectos = False

        if (
                self.codigoP.text() == ""
        ):
            QMessageBox.warning(self,"Warning","Debe de ingresar el codigo del producto")
            self.datosCorrectos = False
        else:
            if(
                not self.codigoP.text().isnumeric()

            ):
                QMessageBox.warning(self, "Warning", "El campo codigo debe ser numerico")
                self.datosCorrectos = False

        # Abrimos el archivo en modo lectura:
        self.file = open('datos/productos.txt', 'rb')

        # Lista vacía para agregar todos los usuarios:
        productos1 = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Se para si ya no hay más registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamado u:
            print(linea)
            u = Claseproductos(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
            )

            # Metemos el objeto en la lista de usuarios:
            productos1.append(u)

        # Cerramos el archivo:
        self.file.close()

        for u in productos1:
            # comparamos el codigo ingresado
            if u.codigo == self.codigoP.text():
                self.datosCorrectos = True
                break

        if(not self.datosCorrectos):
            QMessageBox.warning(self, "Warning", "El codigo no existe")
        else:
            self.nombreP.setText(u.nombre)
            self.valorcostoP.setText(u.valorcompra)
            self.valorventaP.setText(u.valorventa)
            self.departamento.setCurrentText(u.departamento)


    def sinPermisos(self):
        QMessageBox.warning(self, "Warning", "No cuenta con permisos")
    def datosIncompletos(self):
        QMessageBox.warning(self, "Warning", "Datos incompletos para crear producto")

    def limpiarlayout(self):
        borrador = self.formulario.count()

        while self.formulario.count() > 0:
            item = self.formulario.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            del item

    def limpiarcampos(self):
        self.codigoP.setText("")
        self.nombreP.setText("")
        self.valorcostoP.setText("")
        self.valorventaP.setText("")
        self.inventario.setText("")


