
""" Reto #4

  ÁREA DE UN POLÍGONO
  Fecha publicación enunciado: 24/01/22
  Fecha publicación resolución: 31/01/22
  Dificultad: FÁCIL
  
  !Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) 
  que sea capaz de calcular y retornar el área de un polígono.
  - La función recibirá por parámetro sólo UN polígono a la vez.
  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  - Imprime el cálculo del área de un polígono de cada tipo.
"""


from email.policy import Policy


class Polygon:

    def Area(self):
        return 0

    def getArea():
        print("Este es el area del polygon")


class Triangle():

    def __init__(self, base, height):

        self.__base = base
        self.__height = height

    def Area(self):
        return (self.__base * self.__height) / 2

    def getArea(self):
        print(f"El area del triangulo es: {self.Area()}")


triangulo = Triangle(12, 8)

triangulo.getArea()
