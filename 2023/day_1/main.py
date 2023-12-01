
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


with open("data.txt") as f:
    data = f.read()

result = 0
for x in data.strip().split("\n"):
    fst = None
    lst = None
    for y in x:
        # check for digit and iterate through the string until last digit
        if y.isdigit():
            lst = y
            # only one digit?
            if fst is None:
                fst = y
    # exclude blanks and add first and last
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
            # check for key string at the end of word
            for key, value in spelled_numbers.items():
                if data.endswith(key):
                    # process as digit value
                    dig = str(value)
        # same as before
        if dig is not None:
            lst = dig
            if fst is None:
                fst = dig
    result += int(fst + lst)
print(result)
