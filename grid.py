# Import Necessary Libraries
import random

# Define the Grid Class
class Grid:
    # Initialize the Grid
    def __init__(self, width, height, obstacle_ratio=0.2, weighted=False):
        self.width = width
        self.height = height
        self.weighted = weighted
        self.obstacle_ratio = obstacle_ratio
        
        # Generate the grid with obstacles and weights
        self.grid = self._generate_grid(obstacle_ratio)

    # Generate the Grid with Obstacles and Weights
    def _generate_grid(self, obstacle_ratio):
        grid = []
        # Populate the grid
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Decide if cell is an obstacle or free/weighted
                if random.random() < obstacle_ratio:
                    row.append(-1)  # obstacle
                else:
                    if self.weighted:
                        row.append(random.randint(1, 5))  # real weights
                    else:
                        row.append(0)  # free cell
            grid.append(row)
        return grid

    # Check if Position is Within Bounds
    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    # Check if Position is Passable
    def passable(self, x, y):
        return self.grid[y][x] != -1

    # Get Neighbors of a Position
    def neighbors(self, x, y):
        steps = [(1,0), (-1,0), (0,1), (0,-1)]
        result = []
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.passable(nx, ny):
                result.append((nx, ny))
        return result
    
    # Save the Grid to a File
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

    # Save the Path to a File
    def save_path_to_file(self, filename, path, start, goal):
        """Save the grid with the path drawn using '*'."""
        path_set = set(path)

        with open(filename, "w") as f:
            for y in range(self.height):
                row_str = ""
                for x in range(self.width):

                    if (x, y) == start:
                        row_str += "S "
                    elif (x, y) == goal:
                        row_str += "G "
                    elif (x, y) in path_set:
                        row_str += "* "
                    else:
                        cell = self.grid[y][x]
                        if cell == -1:
                            row_str += "# "
                        else:
                            row_str += f"{cell} "
                f.write(row_str + "\n")
