# Ejercicio 2: Calculadora de Formas Geométricas

# Objetivo: Demostrar Abstracción y Polimorfismo.

# Vas a construir una aplicación que calcule el área y el perímetro de diferentes formas geométricas.

# Instrucciones:

#     Clase Abstracta Forma:
#         Crea una clase abstracta llamada Forma.
#         Esta clase debe tener un método abstracto calcularArea() que devuelva un double.
#         Esta clase debe tener un método abstracto calcularPerimetro() que devuelva un double.
#         (Opcional) Puedes añadir un atributo nombre para la forma y su encapsulamiento.

#     Clases Concretas Circulo y Rectangulo:
#         Crea dos clases, Circulo y Rectangulo, que hereden de la clase Forma.
#         Circulo debe tener un atributo para el radio.
#         Rectangulo debe tener atributos para ancho y alto.
#         Implementa los constructores para inicializar sus atributos.
#         Sobreescribe los métodos calcularArea() y calcularPerimetro() en cada clase con la lógica específica para esa forma.
#             Para Circulo: Área = π * radio², Perímetro = 2 * π * radio.
#             Para Rectangulo: Área = ancho * alto, Perímetro = 2 * (ancho + alto).

#     Clase de Prueba (Main o similar):
#         Crea una lista (o array) de objetos de tipo Forma.
#         Añade instancias de Circulo y Rectangulo a esta lista.
#         Itera sobre la lista y, para cada Forma, llama a calcularArea() y calcularPerimetro().
#         Observa cómo, a pesar de que todas las llamadas se hacen a través de una referencia de tipo Forma, el método correcto (específico de Circulo o Rectangulo) es invocado. Esto es el Polimorfismo en acción.
#         Imprime los resultados de área y perímetro para cada forma.


# ------------------------------------------------------
# Alumno: Carlos Eduardo Vargas Fernandez
# Correo: carlosevargasfernadez@gmail.com
# Curso: Python POO
# Nacionalidad: Peruano


# TAREA POO - Ejercicio 2: Áreas y perimetros
# Demuestra Abstracción, Encapsulamiento, Herencia y Polimorfismo
# ------------------------------------------------------


import math

class Forma:                              # Clase abstracta llamada Forma
    def __init__(self, nombre):
        self.__nombre = nombre            # Atributo nombre para la forma y su encapsulamiento
    def calcularArea(self):               # Método abstracto calcularArea()
        pass
    def calcularPerimetro(self):          # Método abstracto calcularPerimetro()
        pass

class Circulo(Forma):                     # Clase Circulo que hereda de la clase Forma.
    def __init__(self, nombre, radio):    # Constructor para inicializar los atributos de la clase Circulo
        super().__init__(nombre)          # Constructor que llama al constructor de la clase base.
        self.radio = radio                # Atributo radio de la clase Circulo
    def calcularArea(self):               # Método para calcular el área de Circulo
        return math.pi * self.radio ** 2
    def calcularPerimetro(self):          # Método para calcular el perímetro de Circulo
        return 2 * math.pi * self.radio

class Rectangulo(Forma):                        # Clase Rectangulo que hereda de la clase Forma.
    def __init__(self, nombre, ancho, alto):    # Constructor para inicializar los atributos de la clase Rectangulo
        super().__init__(nombre)                # Constructor que llama al constructor de la clase base.
        self.ancho = ancho                      # Atributo ancho de la clase Rectangulo
        self.alto = alto                        # Atributo alto de la clase Rectangulo

    def calcularArea(self):               # Método para calcular el área de Rectangulo
        return self.ancho * self.alto
    def calcularPerimetro(self):          # Método para calcular el perímetro de Rectangulo
        return 2 * (self.ancho + self.alto)

formas = [Circulo("C1", 5), Rectangulo("R1",5, 5)]    # lista con las clases Circulo y Rectangulo con sus respectivos atributos

for forma in formas:                      # Bucle para calcular las areas y perimetros de Circulo y Rectangulo
    print(forma.calcularArea())
    print(forma.calcularPerimetro())












