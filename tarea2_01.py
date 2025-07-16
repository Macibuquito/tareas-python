# Ejercicio 1: El Reino Animal

# Objetivo: Demostrar Abstracción, Encapsulamiento y Herencia.

# Imagina que estás construyendo un sistema para gestionar diferentes tipos de animales en un zoológico virtual.

# Instrucciones:

#     Clase Base Animal:
#         Crea una clase base llamada Animal.
#         Esta clase debe tener atributos privados como nombre (String) y edad (int).
#         Implementa un constructor para inicializar estos atributos.
#         Aplica Encapsulamiento proporcionando métodos públicos getNombre(), getEdad(), setNombre(), setEdad().
#         Define un método abstracto hacerSonido() (o un método virtual que pueda ser sobreescrito) que no tome argumentos y no devuelva nada. Este método representará el sonido característico de cada animal.
#         Define un método concreto comer() que imprima un mensaje genérico como "El animal está comiendo.".

#     Clases Derivadas Perro y Gato:
#         Crea dos clases, Perro y Gato, que hereden de la clase Animal.
#         Cada clase debe tener un constructor que llame al constructor de la clase base.
#         Sobreescribe el método hacerSonido() en cada clase para que imprima el sonido específico del animal (e.g., "Guau guau!" para Perro, "Miau miau!" para Gato).

#     Clase de Prueba (Main o similar):
#         En tu método principal, crea instancias de Perro y Gato.
#         Llama a los métodos getNombre(), getEdad(), comer() y hacerSonido() para cada instancia.
#         Demuestra cómo puedes tratar a un Perro o un Gato como un Animal (por ejemplo, en una lista de Animales) y llamar a hacerSonido() para observar el comportamiento polimórfico (aunque el polimorfismo se verá más a fondo en el Ejercicio 2, aquí ya se empieza a vislumbrar).




# ------------------------------------------------------
# TAREA POO - Ejercicio 1: El Reino Animal
# Demuestra Abstracción, Encapsulamiento, Herencia y Polimorfismo
# ------------------------------------------------------


class Animal:                           # clase base llamada Animal 
    def __init__(self, nombre, edad):   # constructor para inicializar atributos nombre y edad
        self.__nombre = nombre          # atributo nombre (String)
        self.__edad = edad              # atributo edad (int)

    def getNombre(self):                # Método que devuelve el valor del atributo nombre
        print(f"{self.__nombre}")

    def getEdad(self):                  # Método que devuelve el valor del atributo edad
        print(f"{self.__edad}")

    def setNombre(self, nombre):        # Método que cambia el valor del atributo nombre 
        self.__nombre = nombre

    def setEdad(self, edad):            # Método que cambia el valor del atributo edad
        self.__edad = edad

    def hacerSonido(self):              # Método abstracto para el sonido que hace un animal
        pass

    def comer(self):                    # Método que imprime el mensaje genérico "El animal está comiendo".
        print("El animal esta comiendo")



class Perro(Animal):                    # clase que hereda de la clase base Animal
    def __init__(self, nombre, edad):   # constructor para inicializar atributos nombre y edad
        super().__init__(nombre, edad)  # constructor que llama al constructor de la clase base.

    def hacerSonido(self):              # Método que sobreescribe el método hacerSonido() para que imprima el sonido de un perro
        print("Guau guau!")


class Gato(Animal):                     # clase que hereda de la clase base Animal
    def __init__(self, nombre, edad):   # constructor para inicializar atributos nombre y edad
        super().__init__(nombre, edad)  # constructor que llama al constructor de la clase base.

    def hacerSonido(self):              # Método que sobreescribe el método hacerSonido() para que imprima el sonido de un gato
        print("Miau miau!")    


print()
perro = Perro("Doggy", 6)               # Instanciar la clase Perro con el objeto perro 
perro.getNombre()                       # Se utilizan los diferentes métodos de la clase Perro y de la clase base Animal 
perro.setNombre("Scooby")
perro.getNombre()
perro.getEdad()
perro.comer()
perro.hacerSonido()

print()
gato = Gato("Pichina", 2)               # Instanciar la clase Gato con el objeto gato
gato.getNombre()                        # Se utilizan los diferentes métodos de la clase Gato y de la clase base Animal 
perro.setNombre("Peluchito")
perro.getNombre()
gato.getEdad()
gato.comer()
gato.hacerSonido()

print()
print("Polimorfismo")                   # Se aplica polimorfismo para cada clase Perro y Gato
animales = [Perro("Doggy", 6), Gato("Pichina", 2)]
for animal in animales:
    animal.hacerSonido()



