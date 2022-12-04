import solutions


def parse_sections(input_text):
    for line in input_text.strip().split("\n"):
        yield (tuple(map(int, s.split("-"))) for s in line.split(","))


@solutions.solution(day=4, part=1)
def part_one(input_text):
    sum = 0
    for (l1, r1), (l2, r2) in parse_sections(input_text):
        if (l1 <= l2 and r2 <= r1) or (l2 <= l1 and r1 <= r2):
            sum += 1
    return sum


@solutions.solution(day=4, part=2)
def part_two(input_text):
    sum = 0
    for (l1, r1), (l2, r2) in parse_sections(input_text):
        if (l1 <= l2 and (l2 <= r1 or r2 <= r1)) or (l2 <= l1 and (l1 <= r2 or r1 <= r2)):
            sum += 1
    return sum
