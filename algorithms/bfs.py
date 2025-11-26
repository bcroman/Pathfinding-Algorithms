# Import Necessary Libraries
from collections import deque

# Function to Perform Breadth-First Search
def bfs(grid, start, goal):
    queue = deque([start])
    came_from = {start: None}
    explored = 0

    # BFS Loop
    while queue:
        current = queue.popleft()
        explored += 1

        # Goal check
        if current == goal:
            break

        # Explore neighbors
        for n in grid.neighbors(*current):
            if n not in came_from:
                queue.append(n)
                came_from[n] = current

    # reconstruct path
    if goal not in came_from:
        return None, explored

    # Reconstruct Path
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    # Return path and explored count
    return path, explored
