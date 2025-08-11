import json
import os
from contacto import Contacto

class AgendaContactos:
    """ Clase que gestiona una colecciòn de contactos.

        Atributes:
            contactos (list): Lista de objetos Contacto
            ruta_archivo (str): Ruta al archivo de almacenamiento
    """

    def __init__(self, ruta_archivo = "contactos.json"):
        """
        Inicializar una nueva agenda de contactos.
        Args:
             ruta_archivo (str, optional): Ruta al archivo para guardar los contactos
        """
        self.contactos = []
        self.ruta_archivo = ruta_archivo

        # Intentar cargar contactos existentes si el archivo existe
        self.cargar()

    def agregar(self, contacto):
        """
        Añade un nuevo contacto a la agenda
        Args:
             contacto (Contacto): El contacto a añadir
        Returns:
            bool: True si se agregò correctamente
                  False si ya existe

        Verificar si ya existe un contacto con el mismo nombre
        """

        for c in self.contactos:
            if c.nombre.lower() == contacto.nombre.lower():

        # Si no existe, lo añadimos
        self.contactos.append(contacto)
        return True

    def buscar(self, termino):
        """
        Busca contactos que coincidan con el termino de busqueda
        Args:
            termino (str): Termino a buscar en nombre, telefono o email
        Returns:
            list: Lista de contactos que coinciden con la busqueda
        """

        resultados = []
        termino = termino.lower()

        for contacto in self.contactos:
            if (termino in contacto.nombre.lower() or
                termino in contacto.telefono.lower() or
                termino in contacto.email.lower()):
                reultados.append(contacto)

        return resultados
