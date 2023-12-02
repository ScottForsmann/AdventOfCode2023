with open('day2Input.txt', 'r') as f:
    validGameSum = 0

    for line in f:
        # Get game num
        gameNum = ""
        gameStartI = -1

        # Start iterating after 'Game '
        for i in range(5, len(line)):
            c = line[i]

            if c.isnumeric():
                gameNum += c
            elif c == ':':
                gameStartI = i + 2
                break

        # It starts as a valid game
        validGameSum += int(gameNum)
        validGame = True

        # Clean line w/ only game data
        line = line[gameStartI:]

        reveals = line.split(';')
        for reveal in reveals:
            for numAndColor in reveal.split(','):
                numAndColor = numAndColor.strip()

                colorString = ""
                numberString = ""

                for c in numAndColor:
                    if c.isnumeric():
                        numberString += c
                    elif c != ' ':
                        colorString += c

                if (colorString == 'red' and int(numberString) > 12
                        or colorString == 'green' and int(numberString) > 13
                        or colorString == 'blue' and int(numberString) > 14):
                    validGameSum -= int(gameNum)
                    validGame = False
                    break

            if not validGame:
                break

    print(validGameSum)
