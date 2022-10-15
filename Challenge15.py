import datetime


def daysBetween(date1, date2) -> int:
    date1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
    return abs((date2 - date1).days)


def printDaysBetween(date1, date2):
    try:
        print(daysBetween(date1, date2))
    except ValueError:
        print("Invalid date")


def main():
    printDaysBetween("18/05/2021", "29/05/2022")
    printDaysBetween("mouredev", "29/04/2022")
    printDaysBetween("18/5/2022", "29/04/2022")


if __name__ == "__main__":
    main()
