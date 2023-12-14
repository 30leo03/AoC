from math import gcd
from functools import reduce


def follow_instructions(instructions, current_node):
    for instruction in instructions:
        if instruction == "L":
            current_node = network[current_node][0]
        elif instruction == "R":
            current_node = network[current_node][1]
    return current_node


with open("data.txt", "r") as file:
    input = file.read().splitlines()

instructions = input[0]
inst_len = len(instructions)
network = {}
steps = 0

for line in input[2:]:
    node, connections = line.split(" = ")
    connections = connections[1:-1].split(", ")
    network[node] = connections

current_node = "AAA"
while current_node != "ZZZ":
    current_node = follow_instructions(instructions, current_node)
    steps += inst_len

print("Solution 1: ", steps)

# Part 2

current_nodes = [node for node in network if node[-1] == "A"]
steps_needed = []
steps = 0

while len(current_nodes) > 0:
    new_current_nodes = []
    steps += inst_len
    for current_node in current_nodes:
        new_node = follow_instructions(instructions, current_node)

        if new_node[-1] == "Z":
            steps_needed.append(steps)
        else:
            new_current_nodes.append(new_node)

    current_nodes = new_current_nodes


# find lcm between steps_needed numbers
def lcm(a, b):
    return a * b // gcd(a, b)


solution2 = reduce(lcm, steps_needed)

print("Solution 2: ", solution2)
