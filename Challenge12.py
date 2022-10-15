
import re


def isPalindrome(wordOne) -> bool:

    wordOne = re.sub(r'[/\W+/g]', ' ', wordOne).lower()

    wordOne = wordOne.lower().replace(" ", '')
    wordTwo = wordOne.lower()[::-1].replace(" ", '')

    return wordOne == wordTwo


def main():
    print(isPalindrome("Ana lleva al oso la avellana."))


if __name__ == "__main__":
    main()
