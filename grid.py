# grid.py
import random

class Grid:
    def __init__(self, width, height, obstacle_ratio=0.2, weighted=False):
        self.width = width
        self.height = height
        self.weighted = weighted
        
        self.grid = self._generate_grid(obstacle_ratio)

    def _generate_grid(self, obstacle_ratio):
        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if random.random() < obstacle_ratio:
                    row.append(-1)  # obstacle
                else:
                    if self.weighted:
                        row.append(random.randint(1, 5))  # real weights
                    else:
                        row.append(0)  # free cell
            grid.append(row)
        return grid

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, x, y):
        return self.grid[y][x] != -1

    def neighbors(self, x, y):
        steps = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.passable(nx, ny):
                result.append((nx, ny))
        return result
    
    def save_to_file(self, filename, start=None, goal=None):
        with open(filename, "w") as f:
            for y in range(self.height):
                row_str = ""
                for x in range(self.width):
                    cell = self.grid[y][x]
                    if start and (x, y) == start:
                        row_str += "S "   # Start
                    elif goal and (x, y) == goal:
                        row_str += "G "   # Goal
                    elif cell == -1:
                        row_str += "# "   # Obstacle
                    else:
                        row_str += f"{cell} "  # Free or weighted cell
                f.write(row_str + "\n")
