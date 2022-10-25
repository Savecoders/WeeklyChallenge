

def isOrtogonales(vectorOne: dict, VectorTow: dict):
    return (vectorOne["i"] * VectorTow["i"]) + (vectorOne["j"] * VectorTow["j"]) == 0


def main():

    print(isOrtogonales(dict(i=1, j=2), dict(i=2, j=1)))
    print(isOrtogonales(dict(i=2, j=1), dict(i=-1, j=2)))


if __name__ == "__main__":
    main()
