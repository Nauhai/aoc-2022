import solutions


def parse_instructions(input_text):
    for line in input_text.strip().split("\n"):
        if line.startswith("addx"):
            instr, val = line.split(" ")
            yield instr, int(val)
        else:
            yield line


def advance_cycle_1(cycle, num, X, signal_strengths):
    for _ in range(num):
        cycle += 1
        if cycle in signal_strengths:
            signal_strengths[cycle] = X
    return cycle


@solutions.solution(day=10, part=1)
def part_one(input_text):
    signal_strengths = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}

    cycle = 0
    X = 1
    for instr in parse_instructions(input_text):
        match instr:
            case "addx", val:
                cycle = advance_cycle_1(cycle, 2, X, signal_strengths)
                X += val
            case "noop":
                cycle = advance_cycle_1(cycle, 1, X, signal_strengths)
    
    return sum(k * v for k, v in signal_strengths.items())


def draw_pixel(cycle, X):
    pixel = "."
    if cycle%40 in (X-1, X, X+1):
        pixel = "#"
    
    if (cycle+1)%40 == 0:
        pixel += "\n"
    
    return pixel


def advance_cycle_2(cycle, num, X, image):
    for _ in range(num):
        image += draw_pixel(cycle, X)
        cycle += 1
    return cycle, image


@solutions.solution(day=10, part=2)
def part_two(input_text):
    image = "\n"

    cycle = 0
    X = 1
    
    for instr in parse_instructions(input_text):
        match instr:
            case "addx", val:
                cycle, image = advance_cycle_2(cycle, 2, X, image)
                X += val
            case "noop":
                cycle, image = advance_cycle_2(cycle, 1, X, image)
    
    return image[:-1]
