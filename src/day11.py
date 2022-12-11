import solutions
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, int|str]
    test_val: int
    cases: tuple[int, int]
    inspections: int = 0

    def get_target(self, item):
        return self.cases[item % self.test_val == 0]

    def receive(self, item):
        self.items.append(item)


def parse_monkeys(input_text):
    monkeys = []

    for monkey in input_text.strip().split("\n\n"):
        lines = monkey.split("\n")
        items = [int(item) for item in lines[1].lstrip("Starting items:").split(", ")]
        operation = lines[2].lstrip("Operation: new = old").split(" ")
        test_val = int(lines[3].lstrip("Test: divisible by"))
        true_case = int(lines[4].lstrip("If true: throw to monkey"))
        false_case = int(lines[5].lstrip("If false: throw to monkey"))
        
        monkeys.append(Monkey(items, operation, test_val, (false_case, true_case)))
    
    return monkeys


def play_round(monkeys, reduce_func):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)

            match monkey.operation:
                case "+", val: item += (item if val == "old" else int(val))
                case "*", val: item *= (item if val == "old" else int(val))
            
            item = reduce_func(item)
            monkeys[monkey.get_target(item)].receive(item)
            monkey.inspections += 1


def play_rounds(n, monkeys, reduce_func):
    for _ in range(n):
        play_round(monkeys, reduce_func)


def get_monkey_business(monkeys):
    a, b = sorted(map(lambda m: m.inspections, monkeys), reverse=True)[:2]
    return a * b


@solutions.solution(day=11, part=1)
def part_one(input_text):
    monkeys = parse_monkeys(input_text)

    play_rounds(20, monkeys, lambda x: x//3)

    return get_monkey_business(monkeys)


@solutions.solution(day=11, part=2)
def part_two(input_text):
    monkeys = parse_monkeys(input_text)

    divisor = 1
    for monkey in monkeys:
        divisor *= monkey.test_val

    play_rounds(10000, monkeys, lambda x: x%divisor)
    
    return get_monkey_business(monkeys)
