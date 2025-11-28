import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    closed = set()
    explored = 0

    while pq:
        priority, current = heapq.heappop(pq)

        if current in closed:
            continue
        closed.add(current)
        explored += 1

        if current == goal:
            break

        for n in grid.neighbors(*current):
            nx, ny = n

            # Your grid uses -1 for walls
            cell_value = grid.grid[ny][nx]
            if cell_value == -1:
                continue  # Skip obstacle

            # Weight rules:
            # 0 → treat as weight 1
            # 1–5 → cost is weight itself
            step_cost = cell_value if cell_value > 0 else 1

            new_cost = cost_so_far[current] + step_cost

            if n not in cost_so_far or new_cost < cost_so_far[n]:
                w = 1
                cost_so_far[n] = new_cost
                priority = new_cost + w * heuristic(n, goal)
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

    return path, explored
