from collections import defaultdict


def delete_num(lines, r, c):
    numString = lines[r][c]

    originalC = c

    c -= 1
    while (0 <= c and c < len(lines[r])
    and lines[r][c].isnumeric()):
        numString = lines[r][c] + numString
        lines[r][c] = '.'
        c -= 1

    c = originalC + 1
    while (0 <= c and c < len(lines[r])
    and lines[r][c].isnumeric()):
        numString += lines[r][c]
        lines[r][c] = '.'
        c += 1

    return int(numString)


def check_if_num(lines, r, c):
    # Check if r, c is in bounds and a n
    if (0 <= r and r < len(lines)
    and 0 <= c and c < len(lines[r])
    and lines[r][c].isnumeric()):
        return True

    return False

def main():
    with open('day3Input.txt', 'r') as f:
        gear_ratio_sum = 0
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = list(lines[i].strip())

        lastLine = []

        adj_offsets = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                adj_offsets.append([i, j])

        for r in range(len(lines)):
            curLine = lines[r]
            for c in range(len(curLine)):
                # There may be an adjacent valid part number!
                if curLine[c] != '.' and not curLine[c].isnumeric():
                    adjacent_parts = []

                    for ro, co in adj_offsets:
                        nr, nc = ro + r, co + c
                        if check_if_num(lines, nr, nc):
                            adjacent_parts.append(delete_num(lines, nr, nc))

                    if len(adjacent_parts) == 2:
                        gear_ratio_sum += adjacent_parts[0] * adjacent_parts[1]

    return gear_ratio_sum

if __name__ == "__main__":
    print(main())