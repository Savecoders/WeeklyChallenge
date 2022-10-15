

def isSymbolEditorial(s) -> bool:
    return s in "({["


def isSymbolEditorialClose(s) -> bool:
    return s in ")}]"


def removeNotEditorial(s) -> str:
    return "".join([c for c in s if isSymbolEditorial(c) or isSymbolEditorialClose(c)])


def isCompletedSymbol(stringSymbols) -> bool:

    if stringSymbols == '':
        return False

    stack = []
    keySymbols = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for symbol in stringSymbols:
        print(symbol)
        print(stack)
        if isSymbolEditorial(symbol):
            stack.append(symbol)
        else:
            if keySymbols[stack.pop()] != symbol:
                return False

    return len(stack) == 0


def main():
    s = '({12[3(aaaa2311)4]5 })'
    print(isCompletedSymbol(removeNotEditorial(s)))


if __name__ == "__main__":
    main()
