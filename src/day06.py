import solutions


def all_unique(l):
    return len(set(l)) == len(l)


def find_first_n_differents(chars, n):
    for i in range(len(chars[:-n])):
        if all_unique(chars[i:i+n]):
            return i
    return -1


def find_marker(input_text, length):
    return find_first_n_differents(input_text, length) + length


@solutions.solution(day=6, part=1)
def part_one(input_text):
    return find_marker(input_text, 4)


@solutions.solution(day=6, part=2)
def part_two(input_text):
    return find_marker(input_text, 14)

