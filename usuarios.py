class Usuarios:
    def __init__(self, nombrecompleto,
                 usuario,
                 password,
                 documento,
                 admin):

        self.nombrecompleto = nombrecompleto
        self.usuario = usuario
        self.password = password
        self.documento = documento
        #Usuario administrador = 1, usuario clasico = 0
        self.admin = admin


    def __str__(self):
        return f"Nombre: {self.nombrecompleto} Documento: {self.documento}"