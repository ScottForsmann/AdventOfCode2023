def main():
    res = 0

    with open('day4Input.txt') as f:
        for line in f:
            lineList = line.split(':')
            gameInfo = lineList[0]

            myNumbers, winningNumbers = lineList[1].strip().split('|')

            myNumbersList = myNumbers.split()
            winningNumbersList = winningNumbers.split()

            myNumberSet = set(myNumbersList)
            winningNumbersSet = set(winningNumbersList)

            #print(myNumberSet, winningNumbersSet)

            curRes = 0
            for number in myNumberSet:
                if number in winningNumbersSet:
                    if not curRes:
                        curRes = 1
                    else:
                        curRes *= 2

            res += curRes

    return res

if __name__ == "__main__":
    print(main())