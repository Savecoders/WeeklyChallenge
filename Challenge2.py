
""" Reto #2
  LA SUCESIÓN DE FIBONACCI
  Fecha publicación enunciado: 10/01/22
  Fecha publicación resolución: 17/01/22
  Dificultad: DIFÍCIL

  Enunciado: Escribe un programa que imprima los 50 primeros números
  de la sucesión de Fibonacci empezando en 0.
  La serie Fibonacci se compone por una sucesión de números 
  en la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci(num) -> None:
    aux = 0
    out = 1
    for i in range(num):
        counter = out + aux
        print(counter)
        out = aux
        aux = counter


fibonacci(50)
