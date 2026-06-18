"""
Main file

This is the main file to test search algorithms.
"""
import BFS
import dijkstra
import BFS
import dfs
from tester import Tester
from read_file import Layout
import time
import matplotlib.pyplot as plt


def run_test(algorithm, letter, number):
    layout = Layout(letter, number)
    tester = Tester(layout)
    current_algorithm = algorithm(tester)
    print(f"\nTesting {current_algorithm.get_name()} with {layout.get_name()}... ", end="")
    start_time = time.time()
    current_algorithm.search()
    end_time = time.time()
    duration = end_time - start_time
    path = current_algorithm.get_path()
    complete, visited, items, bonus = tester.test_path(path)
    print(f"\nComplete: {complete}")
    complete_text = "| All items found" if complete else f"| Search failed | Number of items found: {items}"
    print(f"{complete_text}  |  Cells visited: {visited}  | Search time: {duration} |")
    lst_for_graph[letter].append((False, duration, tester.get_size(), tester.get_num_of_items(), visited, current_algorithm.get_name()))
    if test_extra_credit:
        print("Testing Extra Credit... ", end="")
        current_algorithm = algorithm(tester)
        start_time = time.time()
        current_algorithm.searchExtraCredit()
        end_time = time.time()
        duration = end_time - start_time
        path = current_algorithm.get_path()
        complete, visited, items, bonus = tester.test_path(path)
        complete_text = "" if complete else f" | Search failed | Number of items found: {items}"
        bonus_text = "| Extra credit completed" if bonus else "| No extra credit "
        print(f"{bonus_text}{complete_text} | Search time: {duration} |")
        lst_for_graph[letter].append((True, duration, tester.get_size(), tester.get_num_of_items(), visited, current_algorithm.get_name()))

lst_for_graph = {"a":[],"b":[],"c":[],"d":[]}
test_all = True
test_extra_credit = True
graphing = True


#YOUR ALGORITHM HERE
algo = dijkstra.Dijkstra
#algo = BFS.BFS
#algo = dfs.DFS_Algorithm



print("Starting test code...")
if test_all:
    for char in ["a","b","c","d"]:
        if not graphing:
            for num in range(0,5):
                run_test(algo, char, num)
        else:
            for num in range(0,10):
                run_test(algo, char, num)
else:
    run_test(algo, "a", 0)

#TODO: Calculate additional time for extra credit

if graphing:
    names = {1: "Search Time (Seconds)", 2: "Grid Size", 3: "Items", 4: "Path Length"}
    graphs = [(1, 2), (1, 3)]
    for tup in graphs:
        plt.figure()
        x_idx, y_idx = tup
        for key in lst_for_graph.keys():
            data = [(x[x_idx], x[y_idx]) for x in lst_for_graph[key] if not x[0]]
            if data and ((key == "a") or (y_idx != 2)):
                data.sort(key=lambda x: x[0])
                y, x = zip(*data)
                plt.plot(x, y, marker='o', label=f"Scenario {key}")

        plt.title(lst_for_graph["a"][0][5])
        #plt.xscale('log')
        #plt.yscale('log')
        plt.xlabel(names[y_idx])
        plt.ylabel(names[x_idx])
        plt.legend()
        plt.show()