import numpy as np

ALIVE = '*'
EMPTY = '-'

def count_neighbors(grid, y, x):
    neighbors = [
        (y + 1, x + 0),  # North
        (y + 1, x + 1),  # Northeast
        (y + 0, x + 1),  # East
        (y - 1, x + 1),  # Southeast
        (y - 1, x + 0),  # South
        (y - 1, x - 1),  # Southwest
        (y + 0, x - 1),  # West
        (y + 1, x - 1)   # Northwest
    ]
    count = 0
    for ny, nx in neighbors:
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
