"""
Test script to run BFS, Dijkstra, and DFS against all 20 scenarios
and print a clean comparison table.

Place this file in the same folder as main.py and run:
python test_all_algorithms.py
"""
import sys
import time
from read_file import Layout
from tester import Tester
import BFS, dfs, dijkstra

scenarios = [(letter, num) for letter in ["a", "b", "c", "d"] for num in range(5)]

algorithms = [
    ("BFS", BFS.BFS),
    ("Dijkstra", dijkstra.Dijkstra),
    ("DFS", dfs.DFS_Algorithm),
]

results = {name: [] for name, _ in algorithms}

# Suppress DFS debug prints during testing
import io
import contextlib

for letter, num in scenarios:
    layout = Layout(letter, num)
    tester = Tester(layout)
    scenario_name = f"{letter}{num}"
    for algo_name, algo_class in algorithms:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                algo = algo_class(tester)
                start = time.time()
                algo.search()
                duration = time.time() - start
                path = algo.get_path()
            complete, visited, items, bonus = tester.test_path(path)
            results[algo_name].append((scenario_name, complete, visited, round(duration, 4)))
        except Exception as e:
            results[algo_name].append((scenario_name, "ERROR", str(e)[:40], 0))

print(f"\n{'Scenario':<10}{'BFS':<20}{'Dijkstra':<20}{'DFS':<20}")
print("-" * 70)
for i, (letter, num) in enumerate(scenarios):
    scenario_name = f"{letter}{num}"
    row = f"{scenario_name:<10}"
    for algo_name, _ in algorithms:
        _, complete, visited, duration = results[algo_name][i]
        status = "PASS" if complete is True else str(complete)[:6]
        row += f"{status} ({visited}c, {duration}s)".ljust(20)
    print(row)

print("\n=== SUMMARY ===")
for algo_name, _ in algorithms:
    passed = sum(1 for r in results[algo_name] if r[1] is True)
    print(f"{algo_name}: {passed}/20 scenarios passed")