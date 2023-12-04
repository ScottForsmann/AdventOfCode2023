from collections import defaultdict

def main():
    res = 0
    cardInstances = defaultdict(int)

    with open('day4Input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i]

            lineList = line.split(':')
            gameInfo = lineList[0]

            myNumbers, winningNumbers = lineList[1].strip().split('|')

            myNumbersList = myNumbers.split()
            winningNumbersList = winningNumbers.split()

            myNumberSet = set(myNumbersList)
            winningNumbersSet = set(winningNumbersList)

            matchingCards = 0
            for number in myNumberSet:
                if number in winningNumbersSet:
                    matchingCards += 1

            for j in range(1, matchingCards+1):
                cardInstances[i + j] += 1 + cardInstances[i]

            res += cardInstances[i] + 1

    return res

if __name__ == "__main__":
    print(main())