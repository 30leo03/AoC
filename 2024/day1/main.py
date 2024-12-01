
def main(file):
    with open(file) as f:
        lines = f.readlines()

    data = [[int(x) for x in line.strip().split()] for line in lines]

    sorted_data = list(zip(
        sorted([x[0] for x in data]),
        sorted([x[1] for x in data])
    ))

    total_distance = 0

    for pair in sorted_data:
        total_distance += abs(pair[0] - pair[1])

    print(f"The total distance between the lists is: {total_distance}")

    right_list = [x[1] for x in sorted_data]
    similarity_score = 0

    for x in sorted_data:
        similarity_score += right_list.count(x[0]) * x[0]

    print(f"The similarity score between the lists is: {similarity_score}")


if __name__ == "__main__":
    main("input.txt")

