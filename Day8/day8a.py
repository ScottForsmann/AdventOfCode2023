def createDirectionMap(mappings):
    directionMap = {}  # (left, right)
    for mapping in mappings:
        current, nxt = mapping.split(" = ")
        nxt = tuple(nxt.strip('()').split(', '))
        directionMap[current] = nxt
    return directionMap

def main():
    RL, mappings = open('data.txt').read().strip().split('\n\n')
    RLLEN = len(RL)
    mappings = mappings.split('\n')
    directionMap = createDirectionMap(mappings)

    cur = 'AAA'
    end = 'ZZZ'
    count = 0
    while cur != end:
        i = 0
        if RL[count % RLLEN] == "R":
            i = 1

        cur = directionMap[cur][i]
        count += 1

    print(count)

if __name__ == "__main__":
    main()