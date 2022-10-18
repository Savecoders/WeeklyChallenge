

AtheleteState = {
    "Jump": '|',
    "Run": '_',
}


def checkRace(AtheleteState: dict, RaceTrack: str) -> bool:
    # Runway is the track that the athelete will run on
    RaceTrack = [*RaceTrack]

    if len(AtheleteState) != len(RaceTrack):
        return False

    for i in range(len(AtheleteState)):
        if AtheleteState[i] == RaceTrack[i]:
            continue
        else:
            return False

    return True


def main():
    print(checkRace([AtheleteState['Run'], AtheleteState['Jump'],
          AtheleteState['Run'], AtheleteState['Jump'], AtheleteState['Run']], '_|_|_'))


if __name__ == "__main__":
    main()
