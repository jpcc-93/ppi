class Claseproductos:
    def __init__(self, codigo,
                 nombre,
                 valorcompra,
                 valorventa,
                 departamento,
                 cantidad):

        self.codigo = codigo
        self.nombre = nombre
        self.valorcompra = valorcompra
        self.valorventa = valorventa
        self.departamento = departamento
        self.cantidad = cantidad


    def __str__(self):
        return f"Nombre: {self.nombre} codigo: {self.codigo}"

    def __del__(self):
        self.codigo = None
        self.nombre = None
        self.valorcompra = None
        self.valorventa = None
        self.departamento = None
        self.cantidad = None