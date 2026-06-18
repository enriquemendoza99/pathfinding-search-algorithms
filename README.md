# Warehouse Pathfinding — Search Algorithm Comparison

A Python project implementing and comparing three graph search algorithms
— BFS, DFS, and Dijkstra's Algorithm — for finding paths through a
grid-based warehouse to collect all items.

## Highlights
- Implemented Breadth-First Search, Depth-First Search, and Dijkstra's
  Algorithm, each validated against 60 total scenarios (180/180 test
  runs passed)
- Identified a performance bottleneck in the Dijkstra implementation
  through comparative benchmarking
- Generated performance graphs comparing search time scaling across
  all three algorithms

## Project Structure
```
BFS.py                  — Breadth-First Search
dfs.py                   — Depth-First Search
dijkstra.py               — Dijkstra's Algorithm
example.py                 — Template for implementing a new algorithm
main.py                      — Single-scenario test harness (supports graphing)
test_all_algorithms.py        — Full comparison across all 20 scenarios
read_file.py                    — Parses scenario layout files
tester.py                        — Builds adjacency list and validates paths
scenarios/                         — Test scenario files (a0-a4, b0-b4, c0-c4, d0-d4)
scenarios_graph/                     — Larger scenario set used for performance graphing
graphs/                                — Saved performance comparison charts
TEST_RESULTS.md                          — Full results and performance analysis
```

## How to Run

1. Install dependencies:
```
pip install matplotlib bokeh
```

2. Run a single scenario — open `main.py` and set:
```python
algo = BFS.BFS        # or dijkstra.Dijkstra, or dfs.DFS_Algorithm
```
then run:
```
python main.py
```

3. Run all three algorithms against all 20 scenarios:
```
python test_all_algorithms.py
```

## Performance Graphing

`main.py` includes a matplotlib mode that plots search time against grid
size and against item count for a chosen algorithm.

**To generate a graph for one algorithm:**

1. Open `main.py` and set the algorithm to graph:
```python
algo = BFS.BFS        # or dijkstra.Dijkstra, or dfs.DFS_Algorithm
```
2. Set:
```python
test_all = True
graphing = True
```
3. Also set `graphing = True` at the top of `read_file.py` so it reads
   from `scenarios_graph/` (10 scenarios per letter instead of 5).
4. Run:
```
python main.py
```

This runs 40 scenarios (10 per letter) and produces two charts: search
time vs. grid size, and search time vs. item count, each with one line
per scenario type (a, b, c, d). Use the save icon in the matplotlib
window to export each chart as a PNG.

Repeat the steps above once per algorithm to generate all three charts
for comparison — see `graphs/` for the saved versions.

## Test Results

All three algorithms passed every scenario tested:

| Test Set | Scenarios | Algorithms | Total Runs Passed |
|----------|-----------|------------|----------------------|
| Standard scenarios | 20 | BFS, Dijkstra, DFS | 60 / 60 |
| Extended graphing scenarios | 40 | BFS, Dijkstra, DFS | 120 / 120 |

See `TEST_RESULTS.md` for the full breakdown including cells visited and
search time per scenario, plus an analysis of a performance bottleneck
found in the Dijkstra implementation.

## Scenario Types
- **Scenario a**: No obstacles, several items
- **Scenario b**: Multiple obstacles, fewer items
- **Scenario c**: Complex grid layout requiring optimized paths
- **Scenario d**: Single item in a corner of the grid

## Algorithm Notes

**BFS** explores all cells at the current distance before expanding
further, guaranteeing the shortest path on an unweighted grid.

**Dijkstra's Algorithm** reduces to BFS on an unweighted grid — every edge
costs 1, so both visit the same cells and find identical paths. In
practice, this implementation runs far slower than BFS (up to 150x on the
largest test grids) because it uses a plain list as its priority queue
rather than a heap, making each step an O(n) linear scan instead of
O(log n). This is a reminder that real-world performance depends as much
on the data structures used as on an algorithm's theoretical complexity.

**DFS** commits to exploring as deep as possible down one branch before
backtracking, rather than expanding outward evenly like BFS. This means
it visits far more cells than BFS or Dijkstra on the same scenarios, but
its cheap O(1) stack operations let it outscale the list-based Dijkstra
implementation on the largest grids despite the extra cells visited.
