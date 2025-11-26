# Import Necessary Librariess
import heapq

# Dijkstra's Algorithm Implementation
def dijkstra(grid, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    explored = 0

    # Main Loop
    while pq:
        cost, current = heapq.heappop(pq)
        explored += 1

        if current == goal:
            break

        # Explore Neighbors
        for n in grid.neighbors(*current):
            nx, ny = n
            new_cost = cost_so_far[current] + (grid.grid[ny][nx] or 1)

            # Update Costs and Paths
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                heapq.heappush(pq, (new_cost, n))
                came_from[n] = current

    # Check if Goal was Reached
    if goal not in came_from:
        return None, explored

    # path reconstruction
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    # Return Path and Explored Nodes Count
    return path, explored
