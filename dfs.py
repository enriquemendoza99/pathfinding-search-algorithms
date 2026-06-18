"""
DFS Algorithm
"""

class DFS_Algorithm:
    def __init__(self, tester):
        self.solution = []  # Solution path as list of (x, y) coordinates
        self.found_items = set()  # Hash set for O(1) lookup of collected items
        self.adjacency_list = tester.get_list()  # Warehouse layout as adjacency list
        self.start = tester.get_start()  # Start position in the warehouse
        self.num_items = tester.get_num_of_items()  # Number of items in the layout

    def get_name(self):
        return "DFS Algorithm"

    def get_path(self):
        return self.solution

    def search(self):
        self.solution = []
        self.found_items = set()
        cur = (self.start[0], self.start[1])

        while len(self.found_items) < self.num_items:
            path, item_node = self.find(cur)
            if not path or item_node is None:
                break
            cur = item_node
            self.found_items.add(item_node)
            self.solution += path[1:]

    def searchExtraCredit(self):
        self.search()
        if len(self.found_items) == self.num_items and self.solution:
            cur = self.solution[-1]
            start_pos = (self.start[0], self.start[1])
            path, _ = self.find(cur, start_pos)
            if path:
                self.solution += path[1:]

    def find(self, cur_start, item_to_find=None):
        """
        Iteratively finds a path to the nearest unvisited item (or to
        item_to_find if given) using an explicit stack instead of
        recursion, avoiding Python's recursion limit on large grids.
        Uses parent pointers instead of full path copies to keep memory
        usage proportional to cells visited.

        Args:
            cur_start (tuple): Starting position (x, y)
            item_to_find (tuple, optional): Specific target position to find

        Returns:
            tuple: (path, target_node)
        """
        stack = [cur_start]
        visited = {cur_start}
        parent = {cur_start: None}

        target = None
        while stack:
            current_pos = stack.pop()

            if item_to_find and current_pos == item_to_find:
                target = current_pos
                break

            if not item_to_find and self.adjacency_list[current_pos][0] \
                    and current_pos not in self.found_items:
                target = current_pos
                break

            for next_pos in self.adjacency_list[current_pos][1]:
                if next_pos not in visited:
                    visited.add(next_pos)
                    parent[next_pos] = current_pos
                    stack.append(next_pos)

        if target is None:
            return None, None

        # Reconstruct the path by walking parent pointers back to the start
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        return path, target

if __name__ == "__main__":
    pass