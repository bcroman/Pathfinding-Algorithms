# main.py
import time
from grid import Grid
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

def run_test(width, height, start, goal):
    grid = Grid(width, height, obstacle_ratio=0.2, weighted=True)

    # Force start and goal to be free
    grid.grid[start[1]][start[0]] = 0
    grid.grid[goal[1]][goal[0]] = 0

    # Save grid to file
    grid.save_to_file("grid_output.txt", start=start, goal=goal)

    print("\n--- Grid {}x{} ---".format(width, height))

    # BFS
    t1 = time.time()
    p1, e1 = bfs(grid, start, goal)
    t_bfs = time.time() - t1

    # Dijkstra
    t2 = time.time()
    p2, e2 = dijkstra(grid, start, goal)
    t_dij = time.time() - t2

    # A*
    t3 = time.time()
    p3, e3 = astar(grid, start, goal)
    t_astar = time.time() - t3

    # Results
    print("BFS:      time={:.6f}s explored cells={}".format(t_bfs, e1))
    print("Dijkstra: time={:.6f}s explored cells={}".format(t_dij, e2))
    print("A*:       time={:.6f}s explored cells={}".format(t_astar, e3))

if __name__ == "__main__":
    # Define start and goal positions
    start = (0, 0)
    goal = (19, 19)

    # Run Test
    run_test(20, 20, start, goal)
