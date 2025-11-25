# algorithms/bfs.py
from collections import deque

def bfs(grid, start, goal):
    queue = deque([start])
    came_from = {start: None}
    explored = 0

    while queue:
        current = queue.popleft()
        explored += 1

        if current == goal:
            break

        for n in grid.neighbors(*current):
            if n not in came_from:
                queue.append(n)
                came_from[n] = current

    # reconstruct path
    if goal not in came_from:
        return None, explored

    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path, explored
