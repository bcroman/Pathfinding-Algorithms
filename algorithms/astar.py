# Import Necessary Libraries
import heapq
import math

# Function to Calculate Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Function to Perform A* Search
def astar(grid, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = 0

    # A* Search Loop
    while pq:
        priority, current = heapq.heappop(pq)
        explored += 1

        if current == goal:
            break

        for n in grid.neighbors(*current):
            nx, ny = n
            new_cost = cost_so_far[current] + (grid.grid[ny][nx] or 1)

            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost + heuristic(n, goal)
                heapq.heappush(pq, (priority, n))
                came_from[n] = current

    if goal not in came_from:
        return None, explored

    # reconstruct path
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    # Return path and explored count
    return path, explored
