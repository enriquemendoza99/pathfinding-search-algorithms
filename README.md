# Warehouse Pathfinding — Search Algorithm Comparison

A Python project implementing and comparing three graph search algorithms: 
BFS, DFS, and Dijkstra's Algorithm, for finding paths through a
grid-based warehouse to collect all items.

## Project Structure
BFS.py                  — Breadth-First Search

dfs.py                   — Depth-First Search (debugged and rewritten)

dijkstra.py               — Dijkstra's Algorithm

example.py                 — Template for implementing a new algorithm

main.py                      — Single-scenario test harness (supports graphing)

test_all_algorithms.py        — Full comparison across all 20 scenarios

read_file.py                    — Parses scenario layout files

tester.py                        — Builds adjacency list and validates paths

scenarios/                         — Test scenario files (a0-a4, b0-b4, c0-c4, d0-d4)

scenarios_graph/                     — Larger scenario set used for performance graphing

TEST_RESULTS.md                        — Full results and bug writeup

## How to Run

1. Install dependencies:
pip install matplotlib bokeh

2. Run a single scenario — open `main.py` and set:
```python
algo = BFS.BFS        # or dijkstra.Dijkstra, or dfs.DFS_Algorithm
```
then run:
python main.py

3. Run all three algorithms against all 20 scenarios:
python test_all_algorithms.py

## Performance Graphing

`main.py` includes an optional matplotlib mode that plots how search time,
grid size, and path length scale for each algorithm.

To use it:

1. Open `main.py` and set:
```python
test_all = True
graphing = True
```
2. Also set `graphing = True` at the top of `read_file.py` so it reads
   from the `scenarios_graph/` folder instead of `scenarios/`.
3. Run:
python main.py

This runs every scenario (10 per letter when graphing is on) and opens
matplotlib windows plotting search time against grid size and against
item count, with one line per scenario type (a, b, c, d).

## Test Results
All three algorithms pass all 20 scenarios for both standard search and
extra credit (60/60 total runs). See `TEST_RESULTS.md` for the full
breakdown with cells visited and search time per scenario, plus a detailed
writeup of the three bugs found and fixed in the DFS implementation.

## Scenario Types
- **Scenario a**: No obstacles, several items
- **Scenario b**: Multiple obstacles, fewer items
- **Scenario c**: Complex grid layout requiring optimized paths
- **Scenario d**: Single item in a corner of the grid

## Algorithm Notes

**BFS** explores all cells at the current distance before expanding
further, guaranteeing the shortest path on an unweighted grid.

**Dijkstra's Algorithm** reduces to BFS on an unweighted grid — every edge
costs 1, so both algorithms find identical paths. Dijkstra is slower in
practice due to priority-queue overhead that provides no benefit here.

**DFS** commits to exploring as deep as possible down one branch before
backtracking. It originally crashed on large grids due to Python's
recursion limit, then ran out of memory after an initial fix attempt due
to storing full path copies per branch, and failed on some small grids
because it required one continuous walk without revisiting any cell. All
three issues were fixed by rewriting the search with an explicit stack and
parent-pointer path reconstruction.
