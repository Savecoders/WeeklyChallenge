
import string


def drawPolygon(size: int, figure: str) -> int:

    if figure == "triangule":
        triangule = "*"
        for i in range(3, size):
            print(triangule)
            triangule = triangule + "**"

        triangule = "*"

        for i in range(1, size):
            print(" "*(size-i-1), triangule, " "*(size-i-1))
            triangule = triangule + "**"

    if figure == "square":

        square = "*"
        print()
        print(square*size)
        for i in range(1, size-2):
            print(square, " "*(size-4), square)

        print(square*size)


def main():

    drawPolygon(10, "triangule")
    drawPolygon(11, "square")


if __name__ == "__main__":
    main()
