import sys
import solutions

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13


if __name__ == "__main__":
    print("Welcome to Advent of Code 2022!")

    if len(sys.argv) <= 1:
        print("No solution to run. Goodbye!")
        sys.exit()

    day = int(sys.argv[1])
    part = 12
    if len(sys.argv) > 2:
        part = int(sys.argv[2])

    print(f"Running solution for day {day} part {part}:")
    solutions.run_solution(day, part)
