

def calculateSet(listOne: list, ListTwo, boolean: bool) -> list:

    Values = []

    if boolean:
        for i in range(len(listOne)):
            if listOne[i] in ListTwo and listOne[i] not in Values:
                Values.append(listOne[i])
    else:
        for i in range(len(listOne)):
            if listOne[i] not in ListTwo and listOne[i] not in Values:
                Values.append(listOne[i])

        for i in range(len(ListTwo)):
            if ListTwo[i] not in listOne and ListTwo[i] not in Values:
                Values.append(ListTwo[i])

    return Values


def main():
    listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listTwo = [1, 3, 5, 7, 9, 10]
    print(calculateSet(listOne, listTwo, True))
    print(calculateSet(listOne, listTwo, False))


if __name__ == "__main__":
    main()
