import re

REGEX_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"


def multiply(matches):
    total_sum = 0

    for match in matches:
        nums = re.findall(r"\d+", match)
        x, y = map(int, nums)
        total_sum += x * y

    return total_sum


def part_one(data):
    matches = re.findall(REGEX_PATTERN, data)

    return multiply(matches)


def part_two(data):
    regex_do = r"do\(\)"
    regex_dont = r"don't\(\)"

    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", data)
    tokens = [token for token in tokens if token.strip()]

    print(tokens)

    enabled = True
    instructions_to_perform = []

    for token in tokens:
        if re.match(regex_do, token):
            enabled = True
        elif re.match(regex_dont, token):
            enabled = False
        elif re.match(REGEX_PATTERN, token):
            if enabled:
                instructions_to_perform.append(token)

    return multiply(instructions_to_perform)


def main(file):
    with open(file, 'r') as f:
        data = f.read()

    print(part_one(data))
    print(part_two(data))


if __name__ == "__main__":
    main("input.txt")