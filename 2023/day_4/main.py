import re
import math

input_list = []
value = 1
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

pattern = re.compile(r'Card\s+(\d+):\s+((?:\d+\s+)+)\|\s+((?:\d+\s+)+\d+)')

all_scores = []
for i in range(len(input_list)):
    #print("###########")
    match = pattern.search(input_list[i])

    current_points = 0
    if match:
        card_number = match.group(1)
        winning_numbers = match.group(2).split()
        check_numbers = match.group(3).split()
        for num in winning_numbers:
            if num in check_numbers:
                if current_points == 0:
                    current_points += 1
                elif current_points > 0:
                    current_points *= 2
        #print(current_points)
        all_scores.append(current_points)
# Part 1
print(sum(all_scores))


