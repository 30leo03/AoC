import re

input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

pattern = re.compile(r':\s+((?:\d+\s+)+\d+)')
total_time = [int(x) for x in pattern.search(input_list[0]).group(1).split()]
distance_rec = [int(x) for x in pattern.search(input_list[1]).group(1).split()]

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






