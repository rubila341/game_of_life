import numpy as np

ALIVE = '*'
EMPTY = '-'


def count_neighbors(grid, y, x):
    directions = [(dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if not (dy == 0 and dx == 0)]
    count = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < grid.height and 0 <= nx < grid.width:
            if grid[ny, nx] == ALIVE:
                count += 1
    return count


def game_logic(state, neighbors_count):
    if state == ALIVE:
        if neighbors_count < 2 or neighbors_count > 3:
            return EMPTY  # Die: Too few or too many
    else:
        if neighbors_count == 3:
            return ALIVE  # Regenerate
    return state


def update_grid(grid):
    new_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            neighbors_count = count_neighbors(grid, y, x)
            new_grid[y, x] = game_logic(grid[y, x], neighbors_count)
    return new_grid


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = np.full((height, width), EMPTY, dtype='<U1')

    def __getitem__(self, idx):
        y, x = idx
        return self.grid[y % self.height, x % self.width]

    def __setitem__(self, idx, value):
        y, x = idx
        self.grid[y % self.height, x % self.width] = value
