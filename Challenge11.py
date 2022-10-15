

"""
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e 
 * imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 
 !   pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2
 !   pero NO estén presentes en str1.
"""


def printNonCommonChars(out1, out2) -> None:
    out1 = [*out1]
    out2 = [*out2]
    str1 = list(filter(lambda character: character not in out2, out1))
    str2 = list(filter(lambda character: character not in out1, out2))

    print(str1)
    print(str2)


def main():
    out1 = 'brais'
    out2 = 'moure'
    printNonCommonChars(out1, out2)


if __name__ == "__main__":
    main()
