import solutions


def parse_stacks_moves(input_text):
    lines = input_text.strip().split("\n")
    stacks = []
    i_line = 0

    while (line := lines[i_line])[1] != '1':
        i_char = 0
        i_stack = 0
        while i_char < len(line):
            if line[i_char] == '[':
                while i_stack >= len(stacks):
                    stacks.append([])
                stacks[i_stack].insert(0, line[i_char+1])
            i_char += 4
            i_stack += 1
        i_line += 1
    
    i_line += 2

    moves = []
    while i_line < len(lines):
        line = lines[i_line].strip("move ")
        n, rest = line.split(" from ")
        a, b = rest.split(" to ")
        moves.append(map(int, (n, a, b)))
        i_line += 1
    
    return stacks, moves


@solutions.solution(day=5, part=1)
def part_one(input_text):
    stacks, moves = parse_stacks_moves(input_text)

    for n, a, b in moves:
        for _ in range(n):
            stacks[b-1].append(stacks[a-1].pop())

    return ''.join(s.pop() for s in stacks)


@solutions.solution(day=5, part=2)
def part_two(input_text):
    stacks, moves = parse_stacks_moves(input_text)

    for n, a, b in moves:
        stacks[b-1] += stacks[a-1][-n:]
        for _ in range(n):
            stacks[a-1].pop()

    return ''.join(s.pop() for s in stacks)
