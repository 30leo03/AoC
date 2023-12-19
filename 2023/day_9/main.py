
input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip().split()
        input_list.append(line)
sequences = [[int(n) for n in l] for l in input_list]


def done(seq):
    if sum(seq) == 0:
        return True
    else:
        return False


def calc_difference(seq):
    new_seq = []
    for n in range(0, len(seq)):
        if n+1 < len(seq):
            new_seq.append(abs(seq[n+1] - seq[n]))
    return new_seq


def extrapolate(matrix):
    # add a 0 to the first list
    matrix[0].append(0)
    # add the last item of the last seq to the next seq
    for i in range(1, len(matrix)):
        if matrix[i][-1] > 0:
            new_last_val = matrix[i-1][-1] + matrix[i][-1]
        else:
            new_last_val = matrix[i-1][-1] - matrix[i][-1]
        matrix[i].append(new_last_val)
    last_element_sign = matrix[-1][-1]
    if matrix[-1][-2] <= 0:
        last_element_sign *= -1
    print(last_element_sign)
    return last_element_sign


result = []
for s in sequences:
    cur_seq = s
    ext_matrix = []
    while not done(cur_seq):
        ext_matrix.append(cur_seq)
        cur_seq = calc_difference(cur_seq)
    ext_matrix.append(cur_seq)
    ext_matrix = [sublist for sublist in reversed(ext_matrix)]
    result.append(extrapolate(ext_matrix))

# Part 1
print(sum(result))














