import solutions


def are_adjacent(knot1, knot2):
    x, y = knot1
    return knot2 in (
        (x, y),
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
        (x, y+1),
        (x-1, y+1),
        (x-1, y)
    )


def parse_moves(input_text):
    moves = []
    for line in input_text.strip().split("\n"):
        dir, units = line.split(" ")
        moves.append((dir, int(units)))
    return moves


def move(knot, dir):
    x, y = knot
    match dir:
        case 'U': return x, y-1
        case 'D': return x, y+1
        case 'L': return x-1, y
        case 'R': return x+1, y


def follow(knot1, knot2):
    x1, y1 = knot1
    x2, y2 = knot2

    h_dist = x1 - x2
    v_dist = y1 - y2

    nx, ny = knot1

    # T..H
    if h_dist > 1:
        nx = x1-1
    
    # H..T
    if h_dist < -1:
        nx = x1+1
    
    # T
    # .
    # H
    if v_dist > 1:
        ny = y1-1

    # H
    # .
    # T
    if v_dist < -1:
        ny = y1+1

    return nx, ny


def print_grid(rope, range_x, range_y):
    for y in range_y:
        for x in range_x:
            if (x, y) in rope:
                print(rope.index((x, y)), end="")
            elif (x, y) == (0, 0):
                print("s", end="")     
            else:
                print(".", end="")
        print()
    

@solutions.solution(day=9, part=1)
def part_one(input_text):
    moves = parse_moves(input_text)
    positions = {(0, 0)}

    head = (0, 0)
    tail = (0, 0)

    for dir, units in moves:
        for _ in range(units):
            head = move(head, dir)
            if not are_adjacent(head, tail):
                tail = follow(head, tail)
                positions.add(tail)
    
    return len(positions)


@solutions.solution(day=9, part=2)
def part_two(input_text):
    moves = parse_moves(input_text)
    positions = {(0, 0)}

    rope = [(0, 0)] * 10
    for dir, units in moves:
        for _ in range(units):
            rope[0] = move(rope[0], dir)
            for i in range(1, len(rope)):
                prev, next = rope[i-1], rope[i]
                if not are_adjacent(prev, next):
                    rope[i] = follow(prev, next)
            positions.add(rope[-1])

    return len(positions)
