
import copy


def read_map(file):
    with open(file, 'r') as f:
        return [list(line.rstrip('\n')) for line in f]


def get_guard_start(lab_map):
    directions = ['^', '>', 'v', '<']
    for y, row in enumerate(lab_map):
        for x, cell in enumerate(row):
            if cell in directions:
                return y, x, cell
    return None, None, None


def turn_right(direction):
    match direction:
        case '^': return '>'
        case '>': return 'v'
        case 'v': return '<'
        case '<': return '^'


def step_forward(direction, y, x):
    match direction:
        case '^': return y - 1, x
        case 'v': return y + 1, x
        case '<': return y, x - 1
        case '>': return y, x + 1


def simulate_guard(lab_map, start_y, start_x, start_dir):

    direction = start_dir
    y, x = start_y, start_x
    visited_states = set()
    visited_states.add((direction, y, x))
    fields_walked = 1

    while True:
        new_y, new_x = step_forward(direction, y, x)

        # Check bounds
        if not (0 <= new_y < len(lab_map) and 0 <= new_x < len(lab_map[0])):
            return fields_walked

        next_cell = lab_map[new_y][new_x]

        if next_cell == '#':
            direction = turn_right(direction)
        else:
            y, x = new_y, new_x
            fields_walked += 1

            state = (direction, y, x)
            if state in visited_states:
                return 'loop'
            visited_states.add(state)


def check_for_loop(lab_map, start_y, start_x, start_dir, test_y, test_x):
    temp_map = copy.deepcopy(lab_map)
    temp_map[test_y][test_x] = '#'
    result = simulate_guard(temp_map, start_y, start_x, start_dir)
    return result == 'loop'


def main(file):
    lab_map = read_map(file)
    start_y, start_x, start_dir = get_guard_start(lab_map)

    print(simulate_guard(lab_map, start_y, start_x, start_dir))

    lab_map[start_y][start_x] = '.'
    loop_counter = 0
    for y in range(len(lab_map)):
        for x in range(len(lab_map[0])):
            if (y, x) != (start_y, start_x) and lab_map[y][x] == '.':
                if check_for_loop(lab_map, start_y, start_x, start_dir, y, x):
                    loop_counter += 1

    print(loop_counter)

if __name__ == '__main__':
    main('input.txt')
