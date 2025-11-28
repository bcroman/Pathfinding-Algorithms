# Import Necessary Libraries
import time
import tracemalloc

# Import Core Files
from grid import Grid
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

# Function to run one algorithm and record performance
def run_algorithm(name, func, grid, start, goal, output_file):
    # Start Measuring Time and Memory
    tracemalloc.start()
    start_time = time.time()

    path, explored = func(grid, start, goal) # Run the algorithm

    # Get memory usage
    _, peak_memory = tracemalloc.get_traced_memory()

    # Stop Measuring Time and Memory
    tracemalloc.stop()
    elapsed = time.time() - start_time

    # Save path to file if found
    if path:
        grid.save_path_to_file(output_file, path, start, goal)
        moves = len(path) - 1
    else:
        moves = None

    # Return performance metrics
    return {
        "time": elapsed,
        "explored": explored,
        "moves": moves,
        "memory": peak_memory / 1024,
    }

# Pretty-print a single run summary
def display_results_simple(results):
    print("\nSummary:")
    for name, r in results.items():
        # No path found
        if r["moves"] is None: 
            print(f"{name:<10}: No path")
        else:
            # Display Results
            print(
                f"{name:<10}: "
                f"{r['time']:.6f}s | "
                f"{r['explored']} explored | "
                f"{r['moves']} moves | "
                f"{r['memory']:.2f}KB"
            )

# Run a single test instance
def run_test(width, height, start, goal, obstacle_ratio=0.2, weighted=False):
    grid = Grid(width, height, obstacle_ratio=obstacle_ratio, weighted=weighted)

    # Ensure start and goal are free
    grid.grid[start[1]][start[0]] = 0
    grid.grid[goal[1]][goal[0]] = 0

    grid.save_to_file("grid_output.txt", start=start, goal=goal) # Save initial grid

    print(
        f"--- Grid {width}x{height} "
        f"| obstacles={grid.obstacle_ratio} "
        f"| weighted={grid.weighted} ---"
    )

    # Run Algorithms
    results = {}
    results["A*"] = run_algorithm("A*", astar, grid, start, goal, "astar.txt")
    results["BFS"] = run_algorithm("BFS", bfs, grid, start, goal, "bfs.txt")
    results["Dijkstra"] = run_algorithm("Dijkstra", dijkstra, grid, start, goal, "dijkstra.txt")
    return results

# Compute average of all runs
def compute_average(all_results):
    algorithms = ["A*", "BFS", "Dijkstra"]
    avg = {
        algo: {
            "time": 0,
            "explored": 0,
            "moves": 0,
            "memory": 0,
            "success": 0,   # number of successful runs
            "total": 0      # total runs attempted
        }
        for algo in algorithms
    }

    # Aggregate results
    for run in all_results:
        for algo in algorithms:
            avg[algo]["total"] += 1

            # If no path → failure
            if run[algo]["moves"] is None:
                continue

            # Completed Runs
            avg[algo]["success"] += 1
            avg[algo]["time"] += run[algo]["time"]
            avg[algo]["explored"] += run[algo]["explored"]
            avg[algo]["moves"] += run[algo]["moves"]
            avg[algo]["memory"] += run[algo]["memory"]

    # Compute averages
    for algo in algorithms:
        if avg[algo]["success"] == 0:
            # no successful runs
            avg[algo]["moves"] = None
        else:
            # calculate averages
            c = avg[algo]["success"]
            avg[algo]["time"] /= c
            avg[algo]["explored"] /= c
            avg[algo]["moves"] /= c
            avg[algo]["memory"] /= c

    return avg


# Print average results cleanly
def display_average_results(avg):
    print("\n====== AVERAGE RESULTS ======")

    # Display Results
    for algo, r in avg.items():
        success = r["success"]
        total = r["total"]
        rate = (success / total) * 100 if total > 0 else 0

        # No successful runs
        if r["moves"] is None:
            print(f"{algo:<10}: NO PATH in all runs | Success Rate: {rate:.1f}%")
        else:
            # Display Results
            print(
                f"{algo:<10}: "
                f"{r['time']:.6f}s | "
                f"{int(r['explored'])} explored | "
                f"{int(r['moves'])} moves | "
                f"{r['memory']:.2f}KB | "
                f"Success Rate: {rate:.1f}%"
            )

# Main execution
if __name__ == "__main__":
    start = (0, 0)
    goal = (199, 199)

    NUM_RUNS = 3
    all_results = []
    
    # Run multiple tests
    for i in range(NUM_RUNS):
        print(f"\nTest Run {i+1} Results ")
        result = run_test(200, 200, start, goal, obstacle_ratio=0.2, weighted=True)
        display_results_simple(result)
        all_results.append(result)

    # Compute & display averages
    avg = compute_average(all_results)
    display_average_results(avg)
