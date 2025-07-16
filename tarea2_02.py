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


import math

class Forma:
    def __init__(self, nombre):
        self.__nombre = nombre
    def calcularArea(self):
        pass
    def calcularPerimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    def calcularArea(self):
        return math.pi * self.radio ** 2
    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Forma):
    def __init__(self, nombre, ancho, alto):
        super().__init__(nombre)
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        return self.ancho * self.alto
    def calcularPerimetro(self):
        return 2 * (self.ancho + self.alto)

formas = [Circulo("C1", 5), Rectangulo("R1",5, 5)]

for forma in formas:
    print(forma.calcularArea())
    print(forma.calcularPerimetro())












