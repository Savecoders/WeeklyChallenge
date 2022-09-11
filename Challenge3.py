"""Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""


def isPrimo(number) -> bool:

    if(number < 2):
        return True

    divisible = 0

    for i in range(1, number):
        if(number % i == 0):
            divisible += 1

    return divisible <= 2


for i in range(1, 100):

    if(isPrimo(i)):
        print(i)
