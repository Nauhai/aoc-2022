import solutions


def parse_grid(input_text):
    grid = []
    for line in input_text.strip().split("\n"):
        grid.append([int(c) for c in line])
    return grid


@solutions.solution(day=8, part=1)
def part_one(input_text):
    grid = parse_grid(input_text)
    nb_l, nb_c = len(grid), len(grid[0])

    viewed = [None] * nb_l
    for l in range(nb_l):
        viewed[l] = [False] * nb_c

    visible = 0

    # Left to right
    for l in range(nb_l):
        max_h = -1
        for c in range(nb_c):
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not viewed[l][c]:
                    visible += 1
                    viewed[l][c] = True
    
    # Right to left
    for l in range(len(grid)):
        max_h = -1
        for c in range(nb_l)[::-1]:
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not viewed[l][c]:
                    visible += 1
                    viewed[l][c] = True

    # Top to bottom
    for c in range(nb_c):
        max_h = -1
        for l in range(nb_l):
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not viewed[l][c]:
                    visible += 1
                    viewed[l][c] = True
    # bottom to top
    for c in range(nb_c):
        max_h = -1
        for l in range(nb_l)[::-1]:
            h = grid[l][c]
            if h > max_h:
                max_h = h
                if not viewed[l][c]:
                    visible += 1
                    viewed[l][c] = True

    return visible


def get_scenic_score(grid, l, c):
    nb_l, nb_c = len(grid), len(grid[0])

    h = grid[l][c]
    total_view = 1

    # Right
    curr_view1 = 0
    for i in range(c+1, nb_c):
        curr_view1 += 1
        if grid[l][i] >= h:
            break
    total_view *= curr_view1

    # Left
    curr_view2 = 0
    for i in range(0, c)[::-1]:
        curr_view2 += 1
        if grid[l][i] >= h:
            break
    total_view *= curr_view2

    # Bottom
    curr_view3 = 0
    for j in range(l+1, nb_l):
        curr_view3 += 1
        if grid[j][c] >= h:
            break
    total_view *= curr_view3
    
    # Top
    curr_view4 = 0
    for j in range(0, l)[::-1]:
        curr_view4 += 1
        if grid[j][c] >= h:
            break
    total_view *= curr_view4

    return total_view


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
