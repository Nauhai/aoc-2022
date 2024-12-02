import solutions


def compute_calories(input_text):
    input_list = input_text.split("\n")

    calories = []
    current_cal = 0
    for cal in input_list:
        if cal == "":
            calories.append(current_cal)
            current_cal = 0
            continue

        current_cal += int(cal.strip())
    calories.append(current_cal)

    return calories


@solutions.solution(day=1, part=1)
def part_one(input_text):
    return max(compute_calories(input_text))


@solutions.solution(day=1, part=2)
def part_two(input_text):
    return sum(sorted(compute_calories(input_text), reverse=True)[:3])
