import itertools
import re


input_list = []
with open("data.txt") as data:
    for t in data:
        line = t.strip()
        input_list.append(line)

# Obtain all range digits first
seed_pattern = re.compile(r'seeds:\s+((?:\d+\s+)+\d+)')
seeds = seed_pattern.search(input_list[0]).group(1).split()

seed_ranges = [range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])) for i in range(0, len(seeds), 2)]
all_seeds = list(itertools.chain.from_iterable(seed_ranges))


def read_map(input_list, start_index):
    result = []
    i = start_index + 1  # Skip the map header
    while i < len(input_list) and input_list[i].strip() != "":
        result.append(list(map(int, input_list[i].split())))
        i += 1
    return result


def map_iterator(input_list):
    for i in range(1, len(input_list)):
        if input_list[i] == "seed-to-soil map:":
            yield read_map(input_list, i)
        elif input_list[i] == "soil-to-fertilizer map:":
            yield read_map(input_list, i)
        elif input_list[i] == "fertilizer-to-water map:":
            yield read_map(input_list, i)
        elif input_list[i] == "water-to-light map:":
            yield read_map(input_list, i)
        elif input_list[i] == "light-to-temperature map:":
            yield read_map(input_list, i)
        elif input_list[i] == "temperature-to-humidity map:":
            yield read_map(input_list, i)
        elif input_list[i] == "humidity-to-location map:":
            yield read_map(input_list, i)


# Use itertools.chain to combine the maps into a single iterator
all_maps = itertools.chain(map_iterator(input_list))

# Use next to get the next map from the iterator
seed_to_soil_map = next(all_maps)
soil_to_fertilizer_map = next(all_maps)
fertilizer_to_water_map = next(all_maps)
water_to_light_map = next(all_maps)
light_to_temperature_map = next(all_maps)
temperature_to_humidity_map = next(all_maps)
humidity_to_location_map = next(all_maps)

"""
Ranges:
[DESTINATION_START, SOURCE_START, LENGHT]
"""


def convert_source(num, range_list):
    line = next((line for line in range_list if line[1] <= num <= line[1] + line[2]), None)
    return line[0] + num - line[1] if line else num


location_numbers = all_seeds  # Start with the original seeds => change this depending on which part you wanna solve
# Apply the conversion iteratively instead of creating single lists
for conversion_map in [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map,
                        water_to_light_map, light_to_temperature_map, temperature_to_humidity_map,
                        humidity_to_location_map]:
    location_numbers = [convert_source(num, conversion_map) for num in location_numbers]


print(min(location_numbers))









