import math


def createDirectionMap(mappings):
    directionMap = {}  # (left, right)
    for mapping in mappings:
        current, nxt = mapping.split(" = ")
        nxt = tuple(nxt.strip('()').split(', '))
        directionMap[current] = nxt
    return directionMap


def getData():
    data = open('data.txt').read().strip().split('\n')
    RL, mappings = open('data.txt').read().strip().split('\n\n')
    RLLEN = len(RL)
    return mappings.split('\n'), RL, RLLEN


def getStart(directionMap):
    startNodes = []
    for node in directionMap.keys():
        if node[-1] == 'A':
            startNodes.append(node)

    return startNodes

def getTraversesToZ(node, RLString, directionMap):
    count = 0
    RLLen = len(RLString)

    # Finds length to Z string from cur
    while node[-1] != 'Z':
        # Gets right/left
        rl = 0
        if RLString[count % RLLen] == "R":
            rl = 1

        node = directionMap[node][rl]
        count += 1

    return count


def getZEnding(directionMap):
    res = []
    for node in directionMap.keys():
        if node[-1] == "Z":
            res.append(node)
    return res

def main():
    mappings, RLString, RLLen = getData()
    directionMap = createDirectionMap(mappings)
    curNodes = getStart(directionMap)

    offsetsAndEnds = [] # Offsets and End Strings
    for node in curNodes:
        offsetsAndEnds.append(getTraversesToZ(node, RLString, directionMap))

    print(math.lcm(*offsetsAndEnds))


if __name__ == "__main__":
    main()