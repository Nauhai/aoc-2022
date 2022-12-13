import solutions
import itertools
import functools


def parse_pairs(input_text):
    for pair in input_text.strip("\n").split("\n\n"):
        a, b = pair.split("\n")
        yield eval(a), eval(b)


def compare(a, b):
    # If both values are integers, the lower integer should come first
    if type(a) is int and type(b) is int:
        if a == b: return None
        return a < b

    # If exactly one value is an integer, convert it to a list
    if type(a) is int:
        a = [a]
    if type(b) is int:
        b = [b]

    # If both values are lists, compare the values of the lists
    for x, y in itertools.zip_longest(a, b):
        # If the left list runs out of items first, the input is in the right order
        if x is None:
            return True
    
        # If the right list runs out of items first, the input is not in the right order
        if y is None:
            return False

        c = compare(x, y)
        if c is None:
            continue

        return c


@solutions.solution(day=13, part=1)
def part_one(input_text):
    sum = 0
    for i, (a, b) in enumerate(parse_pairs(input_text)):
        if compare(a, b):
            sum += i+1
    return sum


@solutions.solution(day=13, part=2)
def part_two(input_text):
    packets = [[[2]], [[6]]]
    for a, b in parse_pairs(input_text):
        packets += [a, b]
    
    ordered = sorted(packets, key=functools.cmp_to_key(lambda a, b: -1 if compare(a, b) else 1))
    return (ordered.index([[2]])+1) * (ordered.index([[6]])+1)
