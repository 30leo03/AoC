import re
from functools import reduce
import sys
from typing import List, Tuple


def calculate_distance(held, remaining):
    return remaining * held


input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

pattern = re.compile(r':\s+((?:\d+\s+)+\d+)')
total_time = [int(x) for x in pattern.search(input_list[0]).group(1).split()]
distance_rec = [int(x) for x in pattern.search(input_list[1]).group(1).split()]

new_total_time = ""
for t in total_time:
    new_total_time += str(t)
new_distance_rec = ""
for r in distance_rec:
    new_distance_rec += str(r)

record_beaters = []
for t in range(len(total_time)):
    possibilities = 0
    for i in range(1, total_time[t]):
        distance_travelled = (total_time[t] - i) * i
        if distance_travelled > distance_rec[t]:
            possibilities += 1
    record_beaters.append(possibilities)
result = 1
for w in record_beaters:
    result *= w

# Part 1
print(result)


def part_two():
    time = int(new_total_time)
    record = int(new_distance_rec)
    wins = 0
    for i in range(time + 1):
        if calculate_distance(i, time - i) > record:
            wins += 1
    return wins


# Part 2
print(part_two())
