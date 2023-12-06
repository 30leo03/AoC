
input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

symbol_set = set()
symbol_locations = set()
gear_locations = set()
# get indexes and symbols
for y, i in enumerate(input_list):
    for x, k in enumerate(i):
        if k != "." and not(k.isnumeric()):
            symbol_set.add(k)
            symbol_locations.add((x, y))
            if k == "*":
                gear_locations.add((x, y))
#print(gear_locations)

number_list = []
number_active = False
width = len(input_list[0])
for y, l in enumerate(input_list):
    for x, c in enumerate(l):
        if not number_active and (c == "." or c in symbol_set):
            continue
        elif not number_active and c.isnumeric():
            current_number = c  # first digit
            number_active = True
            new_x1 = x
        elif number_active and (c == "." or c in symbol_set):
            new_num = int(current_number)
            new_x2 = x - 1
            number_list.append((new_num, new_x1, new_x2, y))
            number_active = False
            current_number = ""
        elif number_active and c.isnumeric():
            current_number += c  # add to first digit
            if x == width - 1:  # add last digit and reset
                new_num = int(current_number)
                new_x2 = x
                number_list.append((new_num, new_x1, new_x2, y))    # indexed num with position in list
                number_active = False
                current_number = ""

part1_answer = 0
for number, x1, x2, Y in number_list:   # Y is index
    border_points = set()
    for y in range(Y-1, Y+2):
        for x in range(x1 - 1, x2 + 2):
            border_points.add((x, y))
    intersect_set = symbol_locations & border_points
    if len(intersect_set) > 0:
        part1_answer += number

part2_answer = 0
for gx, gy in gear_locations:
    gear_borders = set()
    gear_neighbors = []
    # compare/find neighbors on x- and y-axis
    for x in range(gx - 1, gx + 2):
        for y in range(gy - 1, gy + 2):
            gear_borders.add((x, y))
    for number, x1, x2, Y in number_list:   # find *(gear) nums
        if (x1, Y) in gear_borders or (x2, Y) in gear_borders:
            gear_neighbors.append(number)
    if len(gear_neighbors) == 2:
        N1, N2 = gear_neighbors
        part2_answer += N1 * N2

print(part1_answer)
print(part2_answer)
