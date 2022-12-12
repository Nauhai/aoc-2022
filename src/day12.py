import solutions
from collections import deque


def parse_grid(input_text):
    grid = []
    start = (-1, -1)
    end = (-1, -1)

    for y, line in enumerate(input_text.strip().split("\n")):
        grid.append([])
        for x, c in enumerate(line):
            if c == 'S':
                c = 'a'
                start = x, y
            elif c == 'E':
                c = 'z'
                end = x, y
            grid[y].append(ord(c))
    
    return grid, start, end


def are_valid_coords(coords, width, height):
    x, y = coords
    return 0 <= x < width and 0 <= y < height


def is_reachable(from_coords, to_coords, grid):
    fx, fy = from_coords
    tx, ty = to_coords
    return grid[ty][tx] - grid[fy][fx] <= 1


def find_path(grid, start, end):
    width = len(grid[0])
    height = len(grid)

    queue = deque([[start]])
    seen = {start}

    while len(queue) > 0:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for ncoords in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if are_valid_coords(ncoords, width, height) and ncoords not in seen and is_reachable((x, y), ncoords, grid):
                queue.append(path + [ncoords])
                seen.add(ncoords)
    

@solutions.solution(day=12, part=1)
def part_one(input_text):
    return len(find_path(*parse_grid(input_text)))-1


@solutions.solution(day=12, part=2)
def part_two(input_text):
    grid, _, end = parse_grid(input_text)
    width = len(grid[0])
    height = len(grid)

    min_length = 1000000
    for y in range(height):
        for x in range(width):
            if grid[y][x] == ord('a'):
                path = find_path(grid, (x, y), end)
                if path and (length := len(path)-1) < min_length:
                    min_length = length
    
    return min_length
