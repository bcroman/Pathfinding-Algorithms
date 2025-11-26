# Import Necessary Libraries
import time
import tracemalloc

# Import Core Files
from grid import Grid
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

# Function to Run an Algorithm and Measure Performance
def run_algorithm(name, func, grid, start, goal, output_file):
    tracemalloc.start() # Start memory tracking
    start_time = time.time() # Start time measurement

    path, explored = func(grid, start, goal) # Run the algorithm

    _, peak_memory = tracemalloc.get_traced_memory() # Get peak memory usage
    tracemalloc.stop() # Stop memory tracking

    elapsed = time.time() - start_time # Calculate elapsed time

    # Save the path to file
    if path:
        grid.save_path_to_file(output_file, path, start, goal)
        moves = len(path) - 1
    # No path found Error
    else:
        moves = None

    # Return performance metrics
    return {
        "time": elapsed,
        "explored": explored,
        "moves": moves,
        "memory": peak_memory / 1024,
    }

# Function to Display Results
def display_results_simple(results):
    print("\n==== Summary ====")
    # Display results in a simple table
    for name, r in results.items():
        # No path found case
        if r["moves"] is None:
            print(f"{name:<10}: No path")
        else:
            # Display performance metrics
            print(
                f"{name:<10}: "
                f"{r['time']:.6f}s | "
                f"{r['explored']} explored | "
                f"{r['moves']} moves | "
                f"{r['memory']:.2f}KB"
            )

# Function to Run Test on the Algorithms
def run_test(width, height, start, goal):
    grid = Grid(width, height, obstacle_ratio=0.2, weighted=True)

    # Force start and goal to be free
    grid.grid[start[1]][start[0]] = 0
    grid.grid[goal[1]][goal[0]] = 0

    # Save grid to file
    grid.save_to_file("grid_output.txt", start=start, goal=goal)

    print("\n--- Grid {}x{} ---".format(width, height))

    results = {}
    # Run Algorithms
    results["A*"] = run_algorithm("A*", astar, grid, start, goal, "astar.txt")
    results["BFS"] = run_algorithm("BFS", bfs, grid, start, goal, "bfs.txt")
    results["Dijkstra"] = run_algorithm("Dijkstra", dijkstra, grid, start, goal, "dijkstra.txt")

    # Display Results
    display_results_simple(results) 

# Run Main Code
if __name__ == "__main__":
    # Define start and goal positions
    start = (0, 0)
    goal = (19, 19)

    # Run Test
    run_test(20, 20, start, goal)
