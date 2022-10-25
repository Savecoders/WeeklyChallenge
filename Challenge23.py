
def Mcd(first: int, second: int) -> int:
    print("MCD: ", first, second)
    if first == 0:
        return second
    return Mcd(second % first, first)


def Mcm(first: int, second: int) -> int:
    return (first * second) // Mcd(first, second)


def main():
    first = 56
    second = 180
    print("MCD: ", Mcd(first, second))
    print("MCM: ", Mcm(first, second))


if __name__ == "__main__":
    main()
