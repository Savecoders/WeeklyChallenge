

def timeToMiles(days, hours, minute, seconds) -> int:

    daysInMiliseconds = days * 24 * 60 * 60 * 1000
    hoursInMiliseconds = hours * 60 * 60 * 1000
    minutesInMiliseconds = minute * 60 * 1000
    secondsInMiliseconds = seconds * 1000

    return (daysInMiliseconds + hoursInMiliseconds + minutesInMiliseconds + secondsInMiliseconds) / 1609.34


def main():
    print(timeToMiles(1, 1, 1, 1))


if __name__ == "__main__":
    main()
