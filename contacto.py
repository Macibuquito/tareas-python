class Contacto:
        """
        Clase que representa un contacto en la agenda

        Attributes:
            nombre (str): Nombre completo del contacto
            telefono (str): Nùmero telefònico del contacto
            email (str): Direcciòn de correo electrònico
            direcciòn (str): Direcciòn fìsica del contacto
        """

        def __init__(self, nombre, telefono, email = "", direccion = ""):
            """ Inicializa un nuevo contacto."""
            self.nombre = nombre
            self.telefono = telefono
            self.email = email
            self.direccion = direccion

        def actualizar(self, nombre = None, telefono = None, email = None, direccion = None):

            """ Actualizar los datos del contacto con los valores proporcionados """
            if nombre is not None:
                self.nombre = nombre
            if telefono is not None:
                self.telefono = telefono
            if email is not None:
                self.email = email
            if direccion is not None:
                self.direccion = direccion

        def __str__(self):
            """
            Devuelve una representacion en texto del contacto
            """
            return f"Nombre: {self.nombre}\nTelefono: {self.telefono}\n Email: {self.email}\n Direccion: {self.direccion}"
