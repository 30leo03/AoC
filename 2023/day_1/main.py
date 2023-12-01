import re

# Create dict for spelled numbers
spelled_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}



def check_spelled(ref, item):
    spelled_values = []
    for key in ref:
        if key in item:
            print(f"Match for {key} in {item}")
            spelled_values.append(ref[key])
    # print(spelled_values)


def translate_spelled_to_numbers(input_string):
    spelled_out_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

    result = input_string.lower()

    for word, number in spelled_out_numbers.items():
        result = result.replace(word, number)

    return result


# with open("data.txt", "r") as raw_data:
#    data = [line.strip() for line in raw_data.readlines()]
#    all_numbers = []
#    total_sum = 0
#    #for x in range(0, len(data)):
#    #    numbers_in_string = []
#    #    check_spelled(ref=spelled_numbers, item=data[x])
#    #    for char in data[x]:
#    #        if char not in string.ascii_letters:
#    #            numbers_in_string.append(char)
#    #        # try to get the numbers in the right order
#    #        else:
#    #            pass
#    #    print(numbers_in_string)
#    #    all_numbers.append(numbers_in_string)
#    #for nums in all_numbers:
#    #    if len(nums) >= 1:
#    #        total_sum += int(nums[0] + nums[-1])
#    #print(total_sum)
#    all_split = []
#    for x in range(0, len(data)):
#        #print(data[x])
#        resolved = re.split(r'(\d+)', data[x])
#        resolved = [item for item in resolved if item or item.isdigit()]
#        all_split.append(resolved)
#    #print(all_split)
#    for i in range(0, len(all_split)):
#        for seq in all_split[i]:
#            if seq.isdigit():
#                print(seq)
#            else:
#                translated_string = translate_spelled_to_numbers(seq)
#                print(translated_string)
#        print("\n")


with open("data.txt") as f:
    data = f.read()

result = 0
for x in data.strip().split("\n"):
    fst = None
    lst = None
    for y in x:
        if y.isdigit():
            lst = y
            if fst is None:
                fst = y
    if fst is not None:
        result += int(fst + lst)

print(result)

result = 0
for x in data.strip().split("\n"):
    fst = None
    lst = None
    data = ""
    for c in x:
        dig = None
        if c.isdigit():
            dig = c
        else:
            data += c
            for key, value in spelled_numbers.items():
                if data.endswith(key):
                    # process as digit value
                    dig = str(value)
        if dig is not None:
            lst = dig
            if fst is None:
                fst = dig

    result += int(fst + lst)

print(result)
