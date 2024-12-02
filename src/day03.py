import solutions
from string import ascii_letters


PRIORITIES = {a: b for a, b in zip(ascii_letters, range(1, len(ascii_letters)+1))}


def parse_sacks(input_text):
    return [s.strip() for s in input_text.strip().split("\n")]


@solutions.solution(day=3, part=1)
def part_one(input_text):
    sacks = parse_sacks(input_text)
    priorities_sum = 0
    for s in sacks:
        half = len(s)//2
        left, right = s[:-half], s[half:]
        for item in left:
            if item in right:
                priorities_sum += PRIORITIES[item]
                break
    return priorities_sum


@solutions.solution(day=3, part=2)
def part_two(input_text):
    sacks = parse_sacks(input_text)
    groups = [sacks[i:i + 3] for i in range(0, len(sacks), 3)]
    priorities_sum = 0
    for s1, s2, s3 in groups:
        for item in s1:
            if item in s2 and item in s3:
                priorities_sum += PRIORITIES[item]
                break
    return priorities_sum
