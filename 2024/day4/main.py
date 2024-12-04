def xmas_sliding_window(grid, target="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    target_len = len(target)
    occurrences = []

    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-rihgt diagonal
        (-1, -1), # up-left diagonal
        (1, -1),  # Down-left diagonal
        (-1, 1),  # Up-right diagonal
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                word = []
                positions = []
                for i in range(target_len):
                    nr, nc = r + i * dr, c + i * dc
                    if is_valid(nr, nc):
                        word.append(grid[nr][nc])
                        positions.append((nr, nc))
                    else:
                        break
                if "".join(word) == target:
                    occurrences.append({"word": "".join(word), "start": (r, c), "direction": (dr, dc), "positions": positions})

    return occurrences


def xmas_patterns(grid):
    occurrences = []
    pattern_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)] # x-shape in coords

    def is_valid_pattern(start_r, start_c):
        try:
            chars = [grid[start_r + dr][start_c + dc] for dr, dc in pattern_positions] #get chars in x shape pos

            # Diagonal from top-left to bottom-right
            diag1 = [chars[0], chars[2], chars[4]]
            # Diagonal from top-right to bottom-left
            diag2 = [chars[1], chars[2], chars[3]]

            valid_diag1 = diag1 == list('MAS') or diag1 == list('SAM')
            valid_diag2 = diag2 == list('MAS') or diag2 == list('SAM')

            return valid_diag1 and valid_diag2
        except IndexError:
            return False

    for r in range(len(grid) - 2):
        for c in range(len(grid[0]) - 2):
            if is_valid_pattern(r, c):
                positions = [(r + dr, c + dc) for dr, dc in pattern_positions]
                occurrences.append({
                    "start": (r, c),
                    "location": positions
                })

    return occurrences


def main(file):
    with open(file, 'r') as f:
        data = [[x for x in line.strip()] for line in f.readlines()]

    xmas_found = xmas_sliding_window(data, target="XMAS")
    print(f"Number of XMAS occurrences: {len(xmas_found)}")

    xmas_patterns_found = xmas_patterns(data)
    print(f"Number of X-shaped MAS patterns: {len(xmas_patterns_found)}")


if __name__ == '__main__':
    main("input.txt")
