def get_data():
    data = open('data.txt').read().split('\n')
    return data


def get_rows_cols(data):
    galaxy_rows = set()
    galaxy_cols = set()
    empty_cols = set()
    empty_rows = set()

    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == '#':
                galaxy_rows.add(r)
                galaxy_cols.add(c)
        if r not in galaxy_rows:
            empty_rows.add(r)

    for c in range(len(data[0])):
        if c not in galaxy_cols:
            empty_cols.add(c)

    return galaxy_rows, galaxy_cols, empty_rows, empty_cols


def get_all_galaxy_coordinates(data):
    galaxy_coordinates = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == '#':
                galaxy_coordinates.append((r, c))

    return galaxy_coordinates


def get_all_pairs(l):
    perms = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            perms.append((l[i], l[j]))

    return perms


def expand_universe(data):
    galaxy_rows, galaxy_cols, empty_rows, empty_cols = get_rows_cols(data)
    # Expand columns first, then rows

    # ACCIDENTALLY DELETED THIS

    return data


def calculate_shortest_path_sum(data):
    galaxy_coordinates = get_all_galaxy_coordinates(data)
    galaxy_permutations = get_all_pairs(galaxy_coordinates)

    sum_lengths = 0
    for g1, g2 in galaxy_permutations:
        sum_lengths += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return sum_lengths



def main():
    data = get_data()
    data = expand_universe(data)

    res = calculate_shortest_path_sum(data)
    print(res)

if __name__ == "__main__":
    main()