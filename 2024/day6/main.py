

def get_guard_position(lab_map, guard_symbol):
    for r in lab_map:
        if guard_symbol in r:
            return [lab_map.index(r), r.index(guard_symbol)]


def turn(cur_direction):
    match cur_direction:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'


def walk(direction, x_pos, y_pos):
    match direction:
        case '^':
            return [y_pos - 1, x_pos]
        case '>':
            return [y_pos, x_pos + 1]
        case 'v':
            return [y_pos + 1, x_pos]
        case '<':
            return [y_pos, x_pos - 1]


def patrol(lab_map):
    direction = '^'
    start_pos = get_guard_position(lab_map, direction)
    lab_map[start_pos[0]][start_pos[1]] = 'X'
    print(start_pos)

    current_pos = start_pos

    fields_walked = 1

    while True:
        y_pos, x_pos = current_pos

        try:
            match direction:
                case '^':
                    next_pos = lab_map[y_pos - 1][x_pos]
                case 'v':
                    next_pos = lab_map[y_pos + 1][x_pos]
                case '<':
                    next_pos = lab_map[y_pos][x_pos - 1]
                case '>':
                    next_pos = lab_map[y_pos][x_pos + 1]
                case _:
                    next_pos = None

            if next_pos == '.' or next_pos == 'X':
                current_pos = walk(direction, x_pos=x_pos, y_pos=y_pos)
                if next_pos == '.':
                    fields_walked += 1
                    lab_map[current_pos[0]][current_pos[1]] = 'X'
            elif next_pos == '#':
                direction = turn(direction)

        except IndexError:
            break

    return fields_walked


def main(file):
    with open(file, 'r') as f:
        raster = [list(y[0]) for y in [x.strip().split() for x in f.readlines()]]

    print(patrol(raster))


if __name__ == '__main__':
    main('input.txt')
