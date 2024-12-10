from itertools import product


def calculate_lines_part_one(lines):
    valid_results = []

    for line in lines:
        goal_result = line[0]
        operands = line[1:]

        n = len(operands) - 1
        operators = product(['+', '*'], repeat=n)

        for ops in operators:
            cur_result = operands[0]

            for i, op in enumerate(ops):
                next_operand = operands[i + 1]
                if op == '+':
                    cur_result += next_operand
                elif op == '*':
                    cur_result *= next_operand

            if cur_result == goal_result:
                valid_results.append(cur_result)
                break

    return sum(valid_results)


def calculate_lines_part_two(lines):
    valid_results = []

    for line in lines:
        goal_result = line[0]
        operands = line[1:]

        n = len(operands) - 1
        operators = product(['+', '*', '||'], repeat=n)

        for ops in operators:
            cur_result = operands[0]

            for i, op in enumerate(ops):
                next_operand = operands[i + 1]
                if op == '+':
                    cur_result += next_operand
                elif op == '*':
                    cur_result *= next_operand
                elif op == '||':
                    cur_result = int(str(cur_result) + str(next_operand))  # Concatenate numbers

            if cur_result == goal_result:
                valid_results.append(cur_result)
                break

    return sum(valid_results)


def main(file):
    with open(file, 'r') as f:
        data = [[int(parts[0].rstrip(':'))] + list(map(int, parts[1:])) for line in f if
                (parts := line.strip().split())]

    print(calculate_lines_part_one(data))
    print(calculate_lines_part_two(data))



if __name__ == '__main__':
    main("input.txt")
