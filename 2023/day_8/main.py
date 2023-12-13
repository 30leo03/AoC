
input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

directions = input_list[0] + input_list[1]
step_strings = [input_list[x] for x in range(2, len(input_list)) if input_list[x]]
variables = {}
for step in step_strings:
    str_step = step[6:16]
    step_tuple = tuple(map(str.strip, str_step[1:-1].split(',')))
    indice = step.split()[0]
    variables[indice] = step_tuple


def stop(pos, goal):
    return pos == goal


at_end = False
iterations = 0
current = "AAA"
end = "ZZZ"
while not at_end:
    direction = directions[iterations % len(directions)]
    if direction == "R":
        current = variables[current][1]
    elif direction == "L":
        current = variables[current][0]
    iterations += 1
    at_end = stop(current, end)

print(iterations)

