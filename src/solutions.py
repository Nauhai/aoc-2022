import functools
import time
import os
from collections import defaultdict
import traceback
import math


SOLUTIONS = defaultdict(lambda: {1: None, 2: None})


def solution(day, part):
    if day < 1 or 25 < day:
        raise ValueError("Day must be between 1 and 25")

    if part not in (1, 2):
        raise ValueError("Part must be 1 or 2")

    def solution_decorator(func):
        func.day = day
        func.part = part
        SOLUTIONS[day][part] = func

        @functools.wraps(func)
        def solution_wrapper(input):
            return func(input)

        return solution_wrapper

    return solution_decorator


def run_solution(day, part):
    if day < 1 or 25 < day:
        raise ValueError("Day must be between 1 and 25")

    if part not in (1, 2, 12):
        raise ValueError("Part must be 1, 2 or 12")

    if day not in SOLUTIONS:
        raise KeyError(f"Day {day:02} not registered")

    input_path = f"src/input/day{day:02}.txt"
    if not os.path.exists(input_path):
        raise FileExistsError(f"Cannot find input for day {day:02}")

    with open(input_path, 'r') as file:
        input_text = file.read()

        part1, part2 = SOLUTIONS[day][1], SOLUTIONS[day][2]
        match part:
            case 1: compute([part1], input_text)
            case 2: compute([part2], input_text)
            case 12: compute([part1, part2], input_text)


def compute(funcs, input):
    for func in funcs:
        if func is None:
            print("Solution waiting to be implemented...\n")
            continue

        print(f"----- Day {func.day:02} - Part {func.part} -----")

        try:
            start = time.perf_counter()
            result = func(input)
            counter = time.perf_counter() - start
            print(f"Returned result: {result}")
            print(f"In {prettify_counter(counter)}")
        except Exception as e:
            print(f"Raised an error: {traceback.format_exc()}")

        print("---------------------------\n")


def prettify_counter(elapsed_time):
    suffixes = ["ns", "ms", "s"]
    ns = elapsed_time * 10**6
    exp = int(math.log(ns, 1000))
    exp = min(exp, len(suffixes)-1)
    return str(round(ns / 1000**exp, 3)) + suffixes[exp]
