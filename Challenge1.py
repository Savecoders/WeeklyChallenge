""" Reto #1
  ¿ES UN ANAGRAMA?
  Fecha publicación enunciado: 03/01/22
  Fecha publicación resolución: 10/01/22
  Dificultad: MEDIA

  *Enunciado: Escribe una función que reciba dos palabras (String) y 
  retorne verdadero o falso (Boolean) según sean o no anagramas.
  Un Anagrama consiste en formar una palabra reordenando 
  !TODAS las letras de otra palabra inicial.
  NO hace falta comprobar que ambas palabras existan.
  Dos palabras exactamente iguales no son anagrama.
"""


def isAnagram(wordOne, wordTwo) -> bool:

    if (wordOne == wordTwo) or (not len(wordOne) == len(wordTwo)):
        return False

    # convert wordOne to List of strings
    wordOneList = [i for i in wordOne]

    wordOneList.reverse()

    return ''.join(wordOneList) == wordTwo


print(isAnagram("romas", "amor"))
