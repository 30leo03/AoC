
def problem_dampener(level):
    for j in range(len(level)):
        edited_level = level[:j] + level[j+1:]
        if is_linear(edited_level):
            return True
    return False

def is_linear(level):
    is_increasing = all(1 <= (level[i + 1] - level[i]) <= 3 for i in range(len(level) - 1))
    is_decreasing = all(1 <= (level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))
    return is_increasing or is_decreasing

def main(file):
    with open(file) as f:
        lines = f.readlines()

    data = [[int(x) for x in line.strip().split()] for line in lines]

    safe_count = 0
    unsafe_levels = []

    for level in data:
        if is_linear(level):
            safe_count += 1
        else:
            unsafe_levels.append(level)

    print(f"The amount of safe levels is: {safe_count}.")

    for level in unsafe_levels:
        if problem_dampener(level):
            safe_count += 1

    print(f"The amount of new safe levels where the Problem Dampener can remove a single level from unsafe reports is: {safe_count}.")


if __name__ == "__main__":
    main("input.txt")