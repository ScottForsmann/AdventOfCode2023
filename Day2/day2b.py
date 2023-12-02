with open('day2Input.txt', 'r') as f:
    neededCubesSum = 0

    for line in f:
        gameStartI = -1

        # Start iterating after 'Game '
        for i in range(5, len(line)):
            c = line[i]
            if c == ':':
                gameStartI = i + 2
                break

        # Clean line w/ only game data
        line = line[gameStartI:]

        reveals = line.split(';')
        gameColorMax = {'red': 0, 'green': 0, 'blue': 0}

        for reveal in reveals:
            curCubes = 0

            for numAndColor in reveal.split(','):
                numAndColor = numAndColor.strip()

                colorString = ""
                numberString = ""

                for c in numAndColor:
                    if c.isnumeric():
                        numberString += c
                    elif c != ' ':
                        colorString += c

                gameColorMax[colorString] = max(int(numberString), gameColorMax[colorString])

        powerOfCubes = 1
        for numberOfCubes in gameColorMax.values():
            powerOfCubes *= numberOfCubes

        neededCubesSum += powerOfCubes

    print(neededCubesSum)
