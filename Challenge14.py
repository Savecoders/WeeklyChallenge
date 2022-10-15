

def isArmstrong(n) -> bool:
    stringNumber = [*str(n)]
    count = 0
    for i in stringNumber:
        count += int(i)**len(stringNumber)

    return count == n


"""
Other solution 
def isArmstrong2(n) -> bool:
    stringNumber = [*str(n)]
    return sum([int(i)**len(stringNumber) for i in stringNumber]) == n
 """


def main():
    print(isArmstrong(153))


if __name__ == "__main__":
    main()
