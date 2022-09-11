
"""Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra
 y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""


import re

message = "Hola, mi nombre es brais. Mi nombre completo es Brais Moure es decir (MoureDev)"


def countWords(message) -> dict:
    words = {}

    regexMessage = re.sub(r'[/\W+/g]', ' ', message).lower()

    strippedMessage = regexMessage.strip()

    for msg in strippedMessage.split():
        words[msg] = 1 if not msg in words else 1+words[msg]

    return words


def sortWords(words):

    listWords = list(words.items())

    listWords.sort(key=lambda x: x[1], reverse=True)

    return listWords[0]


print(countWords(message))
print(sortWords(countWords(message)))
