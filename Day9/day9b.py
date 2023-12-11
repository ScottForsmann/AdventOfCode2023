def read_data():
    data = open('data.txt').read().split('\n')
    for i in range(len(data)):
        data[i] = list(map(int, data[i].split()))

    print(f"Data: {data}")
    return data


def check_valid_zero_sequence(sequence):
    for num in sequence:
        if num != 0:
            return False
    return True


def generate_zero_sequences(sequence):
    new_sequences = [sequence]
    while not check_valid_zero_sequence(new_sequences[-1]):
        temp = []
        for i in range(1, len(new_sequences[-1])):
            difference = new_sequences[-1][i] - new_sequences[-1][i - 1]
            temp.append(difference)
        if not temp:
            temp = [0]
        new_sequences.append(temp)
    return new_sequences


def create_row_of_first_cols(zeroed_sequence):
    res = []
    for r in zeroed_sequence:
        res.append(r[0])
    return res


def extrapolate_next(sequence):
    zeroed_sequence = generate_zero_sequences(sequence)
    first_cols = create_row_of_first_cols(zeroed_sequence)

    cur_num = 0
    for i in range(len(first_cols) - 1, -1, -1):
        cur_num = first_cols[i] - cur_num

    return cur_num

def main():
    data = read_data()
    count = 0
    for sequence in data:
        count += extrapolate_next(sequence)

    print(f"Sum of extrapolated values: {count}")

if __name__ == "__main__":
    main()
