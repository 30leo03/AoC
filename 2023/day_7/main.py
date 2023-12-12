

SYMBOLS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

TYPES = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1
}


input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)
bet_list = []
for bet in input_list:
    components = bet.split()
    bet = (components[0], int(components[1]))
    bet_list.append(bet)


def get_type(hand):
    alg = []
    game = None
    for c in hand:
        amt = hand.count(c)
        alg.append(amt)
    alg_set = list(set(alg))
    try:
        if alg_set[0] == 5:
            game = TYPES["Five of a kind"]
        elif sum(alg_set) == 5 and alg_set[0] == 4 or alg_set[1] == 4:
            game = TYPES["Four of a kind"]
        elif sum(alg_set) == 5 and alg_set[0] == 2 or alg_set[0] == 3:
            game = TYPES["Full house"]
        elif sum(alg_set) == 4:
            game = TYPES["Three of a kind"]
        elif alg.count(2) == 4:
            game = TYPES["Two pair"]
        elif sum(alg) == 7 and sum(alg_set) == 3:
            game = TYPES["One pair"]
        elif sum(alg) == 5 and sum(alg_set) == 1:
            game = TYPES["High card"]
    except IndexError:
        game = 1
    return game


def char_to_value(value_dict, char):
    return value_dict[char]


def reorder(same_type_list):
    # create another sorting number for every card value
    new_list = []
    for q in range(0, len(same_type_list)):
        hand = same_type_list[q][1][0]
        # order num conversion
        order_hash = []
        for char in hand:
            order_hash.append(char_to_value(SYMBOLS, char))
        new_hand_cs = (same_type_list[q][0], same_type_list[q][1], order_hash)
        new_list.append(new_hand_cs)
    new_list = sorted(new_list, key=lambda x: x[2])
    return new_list


hand_type = [(get_type(hand[0]), (str(hand[0]), int(hand[1]))) for hand in bet_list]
ordered_hands = sorted(hand_type, key=lambda x: x[0])
hc_list = []
op_list = []
tp_list = []
tk_list = []
fh_list = []
fk_list = []
fik_list = []
for i in range(len(ordered_hands)):
    if ordered_hands[i][0] == 1:
        hc_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 2:
        op_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 3:
        tp_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 4:
        tk_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 5:
        fh_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 6:
        fk_list.append(ordered_hands[i])
    elif ordered_hands[i][0] == 7:
        fik_list.append(ordered_hands[i])


def first_part(list_in_order):
    result = 0
    for p in range(len(list_in_order)):
        placed_bet = list_in_order[p][1][1]
        result += placed_bet * (p+1)
    return result


all_lists = [hc_list, op_list, tp_list, tk_list, fh_list, fk_list, fik_list]
ordered_db_lists = []
for array in all_lists:
    if array:
        ordered_db_lists.extend(reorder(array))
# Part 1
print(first_part(ordered_db_lists))



