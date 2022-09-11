
"""Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número 
   decimal a binario sin utilizar funciones propias del lenguaje que 
   lo hagan directamente.
"""


def decimalToBinary(number) -> str:

    if round(number) == 0:
        return ""

    if number % 2 == 0:
        return decimalToBinary(number//2) + "0"
    else:
        return decimalToBinary(number//2) + "1"


print(decimalToBinary(10))
