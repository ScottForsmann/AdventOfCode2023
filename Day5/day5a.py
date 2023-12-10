def main():
    res = 0

    seedList = []

    # FORMAT WILL BE AS FOLLOWS
    # [curIndex, nextIndex, iRange]
    seedToSoil = []
    soilToFertilizer = []
    fertilizerToWater = []
    waterToLight = []
    lightToTemperature = []
    temperatureToHumidity = []
    humidityToLocation = []

    masterLists = [seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]
    mlI = 0
    incrimentIndex = False

    with open('day5Input.txt') as f:
        seedData = f.readline()
        seedText = seedData.split(':')[1]
        seedList = seedText.strip().split(' ')

        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()

            # Empty line
            if line == '':
                continue

            # Line indicates us to increment mapIndex
            if not line.split(' ')[0].isnumeric():
                if incrimentIndex:
                    mlI += 1
                else:
                    incrimentIndex = True

            # Make map
            else: # line is numeric data
                lineList = line.split(' ')
                for i in range(len(lineList)):
                    lineList[i] = int(lineList[i])

                curIndex, nextIndex, iRange = lineList

                masterLists[mlI].append([curIndex, nextIndex, iRange])

    resMinLocation = None

    for seed in seedList: ## FIX LATER
        curI = int(seed)

        mlI = 0
        while mlI < len(masterLists):
            for nextI, startI, iRange in masterLists[mlI]:
                if startI <= curI <= startI + iRange:
                    offset = curI - startI
                    curI = offset + nextI
                    break

            mlI += 1


        # There's a location!
        if mlI == len(masterLists):
            if not resMinLocation:
                resMinLocation = curI
            else:
                resMinLocation = min(resMinLocation, curI)

    return(resMinLocation)









if __name__ == "__main__":
    print(main())