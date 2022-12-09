import solutions


def parse_grid(input_text):
    grid = []
    for line in input_text.strip().split("\n"):
        grid.append([int(c) for c in line])
    return grid


def find_visible_horizontal(grid, range_l, range_c):
    visible = set()
    for l in range_l:
        max_h = -1
        for c in range_c:
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not (l, c) in visible:
                    visible.add((l, c))
    return visible

def find_visible_vertical(grid, range_c, range_l):
    visible = set()
    for c in range_c:
        max_h = -1
        for l in range_l:
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not (l, c) in visible:
                    visible.add((l, c))
    return visible


def print_grid(grid, visible):
    for l in range(len(grid)):
        for c in range(len(grid[0])):
            if (l, c) in visible:
                print("#", end="")
            else:
                print(grid[l][c], end="")
        print()


@solutions.solution(day=8, part=1)
def part_one(input_text):
    grid = parse_grid(input_text)
    nb_l, nb_c = len(grid), len(grid[0])

    visible_left = find_visible_horizontal(grid, range(nb_l), range(nb_c))
    visible_right = find_visible_horizontal(grid, range(nb_l), range(nb_c)[::-1])
    visible_top = find_visible_vertical(grid, range(nb_c), range(nb_l))
    visible_bottom = find_visible_vertical(grid, range(nb_c), range(nb_l)[::-1])

    return len(visible_left.union(visible_right, visible_top, visible_bottom))


def get_viewing_distance_horizontal(grid, l, c, range_c):
    height = grid[l][c]
    distance = 0
    for i in range_c:
        distance += 1
        if grid[l][i] >= height:
            break
    return distance


def get_viewing_distance_vertical(grid, l, c, range_l):
    height = grid[l][c]
    distance = 0
    for i in range_l:
        distance += 1
        if grid[i][c] >= height:
            break
    return distance 


def get_scenic_score(grid, l, c):
    nb_l, nb_c = len(grid), len(grid[0])

    view_right = get_viewing_distance_horizontal(grid, l, c, range(c+1, nb_c))
    view_left = get_viewing_distance_horizontal(grid, l, c, range(0, c)[::-1])
    view_top = get_viewing_distance_vertical(grid, l, c, range(0, l)[::-1])
    view_bottom = get_viewing_distance_vertical(grid, l, c, range(l+1, nb_l))

    return view_left * view_right * view_top * view_bottom


@solutions.solution(day=8, part=2)
def part_two(input_text):
    grid = parse_grid(input_text)
    nb_l, nb_c = len(grid), len(grid[0])

    max_view = 0

    for l in range(nb_l):
        for c in range(nb_c):
            view = get_scenic_score(grid, l, c)
            if view > max_view:
                max_view = view
    
    return max_view
