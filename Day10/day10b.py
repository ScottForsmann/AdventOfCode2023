# CODE DOESN'T WORK

def read_data():
    data = open('data.txt').read().split('\n')
    return data


def get_start(data):
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "S":
                return r, c


def populate_pipe_dict(data):
    # Connect pipe_dict[char] : [[xOffset, yOffset]]
    pipe_dict = {
        '|': [[0, -1], [0, 1]],
        '-': [[-1, 0], [1, 0]],
        'L': [[0, -1], [1, 0]],
        'J': [[0, -1], [-1, 0]],
        '7': [[-1, 0], [0, 1]],
        'F': [[0, 1], [1, 0]],
    }

    return pipe_dict


def get_inverted_direction(direction):
    x, y = direction
    return [-x, -y]


def get_next_direction(pipe_dict, cur_pipe, last_direction):
    inverted_direction = get_inverted_direction(last_direction)

    for direction in pipe_dict[cur_pipe]:
        if direction != inverted_direction:
            return direction


def check_valid_pipe(pipe, pipe_dict, last_direction):
    if pipe == '.':
        return False

    inverted_direction = get_inverted_direction(last_direction)
    if pipe != 'S' and (pipe not in pipe_dict or inverted_direction not in pipe_dict[pipe]):
        return False

    return True


def get_max_loop_size(data, start_row, start_col):
    pipe_dict = populate_pipe_dict(data)
    start_offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    valid_start_directions = []

    # Valid Start Directions
    for offset in start_offsets:
        nr, nc = start_row + offset[1], start_col + offset[0]

        if (0 <= nr < len(data)
        and 0 <= nc < len(data[nr])
        and check_valid_pipe(data[nr][nc], pipe_dict, offset)
        ):
            valid_start_directions.append(offset)

    # Iterate through pipes
    for direction in valid_start_directions:
        valid_loop_pipes = {(start_row, start_col)}

        last_direction = direction
        cur_row, cur_col = start_row + direction[1], start_col + direction[0]

        while cur_row != start_row or cur_col != start_col:
            # Find current direction pipe goes
            cur_direction = get_next_direction(pipe_dict, data[cur_row][cur_col], last_direction)
            nr, nc = cur_direction[1] + cur_row, cur_col + cur_direction[0]
            valid_loop_pipes.add((cur_row, cur_col))

            if (0 <= nr < len(data)
            and 0 <= nc < len(data[nr])
            and check_valid_pipe(data[nr][nc], pipe_dict, cur_direction)
            ):
                if data[nr][nc] == 'S':
                    return get_s_shape(pipe_dict, direction, cur_direction), valid_loop_pipes
                else:
                    last_direction = cur_direction
                    cur_row, cur_col = nr, nc
            else:
                break


def get_s_shape(pipe_dict, start_dir, end_dir):
    for char in pipe_dict:
        if start_dir in pipe_dict[char] and end_dir in pipe_dict[char]:
            return char


def count_contained_area(data, valid_loop_pipes):
    inside_count = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if (r, c) in valid_loop_pipes:
                continue

            crosses = 0
            r2, c2 = r, c

            while r2 < len(data) and c2 < len(data[r]):
                pipe2 = data[r2][c2]
                if (r2, c2) in valid_loop_pipes and pipe2 != "L" and pipe2 != "7":
                    crosses += 1

                r2 += 1
                c2 += 1

            if crosses % 2 == 1:
                inside_count += 1

    return inside_count

def main():
    data = read_data()
    start_row, start_col = get_start(data)
    s_shape, valid_loop_pipes = get_max_loop_size(data, start_row, start_col)

    # Fix s_shape to be correct for counting parity
    data[start_row] = data[start_row][:start_col] + s_shape + data[start_row][start_col+1:]

    contained_area = count_contained_area(data, valid_loop_pipes)
    print(contained_area)


if __name__ == "__main__":
    main()