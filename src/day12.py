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


def get_neighbors(coords, grid_width, grid_height):
    x, y = coords
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            yield nx, ny


def find_path(grid, start, end_pred, reachable_pred):
    width = len(grid[0])
    height = len(grid)

    queue = deque([(start, 0)])
    seen = {start}

    while len(queue) > 0:
        (x, y), length = queue.popleft()

        if end_pred((x, y)):
            return length
        
        for ncoords in get_neighbors((x, y), width, height):
            if ncoords not in seen and reachable_pred((x, y), ncoords, grid):
                queue.append((ncoords, length+1))
                seen.add(ncoords)


def is_reachable(from_coords, to_coords, grid):
    fx, fy = from_coords
    tx, ty = to_coords
    return grid[ty][tx] - grid[fy][fx] <= 1
    

@solutions.solution(day=12, part=1)
def part_one(input_text):
    grid, start, end = parse_grid(input_text)
    end_pred = lambda c: c == end
    return find_path(grid, start, end_pred, is_reachable)


@solutions.solution(day=12, part=2)
def part_two(input_text):
    grid, _, end = parse_grid(input_text)
    end_pred = lambda c: grid[c[1]][c[0]] == ord('a')
    reachable_pred = lambda f, t, g: is_reachable(t, f, g)
    return find_path(grid, end, end_pred, reachable_pred)
