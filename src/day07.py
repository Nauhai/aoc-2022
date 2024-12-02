import solutions
from collections import namedtuple


class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.size = 0
        self.children = {}


File = namedtuple("File", ["size"])


def parse_fs(input_text):
    fs = {"/": Directory(None)}
    current_dir = fs["/"]
    for line in input_text.strip().split("\n"):
        if line.startswith("$"):
            cmd = line[2:].split(" ")
            if cmd[0] == "cd":
                match cmd[1]:
                    case "/": current_dir = fs["/"]
                    case "..": current_dir = current_dir.parent
                    case d: current_dir = current_dir.children[d]
        else:
            a, b = line.split(" ")
            if a == "dir":
                current_dir.children[b] = Directory(current_dir)
            else:
                current_dir.children[b] = File(int(a))
    return fs


def get_size(item):
    if type(item) is File:
        return item.size
    
    if type(item) is Directory:
        if item.size == 0:
            for child in item.children.values():
                item.size += get_size(child)
        return item.size


def get_sum_small_sizes(dir):
    sum = 0
    for child in dir.children.values():
        if type(child) is Directory:
            sum += get_sum_small_sizes(child)
    
    if (size := get_size(dir)) <= 100000:
        sum += size
    
    return sum


def get_big_sizes(dir, treshold):
    size = get_size(dir)
    if size < treshold:
        return []
    
    sizes = [size]
    for child in dir.children.values():
        if type(child) is Directory:
            sizes += get_big_sizes(child, treshold)
    return sizes


@solutions.solution(day=7, part=1)
def part_one(input_text):
    fs = parse_fs(input_text)
    return get_sum_small_sizes(fs['/'])


@solutions.solution(day=7, part=2)
def part_two(input_text):
    fs = parse_fs(input_text)
    missing_space = 30000000 - 70000000 + get_size(fs['/'])
    return min(get_big_sizes(fs['/'], missing_space))
