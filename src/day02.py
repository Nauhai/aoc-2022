import solutions


SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

WINS = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

LOSES = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

DRAWS = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


def parse_rounds(input_text):
    return [(a, b) for a, b in [round.split(" ") for round in input_text.strip().split("\n")]]


@solutions.solution(day=2, part=1)
def part_one(input_text):
    score = 0
    for a, b in parse_rounds(input_text):
        score += SCORES[b] + (6 if WINS[a] == b else 3 if DRAWS[a] == b else 0)
    return score


@solutions.solution(day=2, part=2)
def part_two(input_text):
    score = 0
    for a, b in parse_rounds(input_text):
        match b:
            case "X": score += SCORES[LOSES[a]]
            case "Y": score += SCORES[DRAWS[a]] + 3
            case "Z": score += SCORES[WINS[a]] + 6
    return score
