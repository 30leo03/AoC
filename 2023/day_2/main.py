import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

with open("data.txt") as data:
    input_text = [x.strip() for x in data.readlines()]

pattern = re.compile(r"Game (\d+):((?:[^;]+;?)+)")
games_content_tot = []

for line in input_text:
    match = pattern.search(line)
    if match:
        game_number = match.group(1)
        game_content = match.group(2).split(';')
        game_content = [[tuple(x.strip().split(',')) for x in pull.split(',')] for pull in game_content if pull]
        for p in game_content:
            # convert each single pull of each hand into a tuple (int, str)
            for i in range(len(p)):
                old_tuple = p[i]
                new_tuple = tuple(map(lambda x: (int(x.split()[0]) if x.split()[0].isdigit() else x.strip(),
                                                 x.split()[1]), old_tuple[0].split(',')))
                p[i] = new_tuple[0]     # get rid of outer tuple. can't find the error in the previous code :(
        games_content_tot.append((game_number, game_content))


def possible_pull(pull):
    col_red = 0
    col_gre = 0
    col_blu = 0
    for hand in pull:
        if hand[1] == 'red':
            col_red += hand[0]
        elif hand[1] == 'green':
            col_gre += hand[0]
        elif hand[1] == 'blue':
            col_blu += hand[0]
    if col_red > RED_MAX or col_gre > GREEN_MAX or col_blu > BLUE_MAX:
        return False
    else:
        return True


def check_min_required_pow(game):
    min_red = 0
    min_gre = 0
    min_blu = 0
    for pull in game:
        for hand in pull:
            if hand[1] == 'red' and hand[0] > min_red:
                min_red = hand[0]
            elif hand[1] == 'green' and hand[0] > min_gre:
                min_gre = hand[0]
            elif hand[1] == 'blue' and hand[0] > min_blu:
                min_blu = hand[0]
    return min_red*min_gre*min_blu


id_sum = 0
min_pow = 0

for game_number, pulls in games_content_tot:
    should_add = True
    # this does not seem smart but well I do not care
    for p in pulls:
        if not possible_pull(p):
            should_add = False
    if should_add:
        id_sum += int(game_number)
    # confusing ahh argument
    min_pow += check_min_required_pow(game=pulls)

print(id_sum)
print(min_pow)

