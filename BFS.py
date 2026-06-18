"""
Breadth First Search (BFS)

Implementation of BFS to find the shortest path in an unweighted graph to collect all items in the warehouse.
"""
class BFS:
    def __init__(self, tester):
        self.solution = [] # Solution path as list of coordinate x and y
        self.found_items = set() # Hash set for O(1) lookup of collected items
        self.adjacency_list = tester.get_list() # Get warehouse layout as adjacency list from letter
        self.start = tester.get_start() # Start position in the layout from the warehouse
        self.num_items = tester.get_num_of_items() # The number of items that are in the layout

    def get_name(self):
        return "Breadth First Search"

    def get_path(self):
        return self.solution # Returns the computed solution path

    # Search logic to collect all items
    def search(self):
        self.solution = []
        self.found_items = set()
        cur = (self.start[0], self.start[1])

        while len(self.found_items) < self.num_items:
            path, item_node = self.find(cur)
            if not path or not item_node:  # If no path is found, break
                break
            cur = item_node  # Update current position to found item
            self.found_items.add(item_node)  # Mark item as collected
            self.solution += path[1:]  # Add path to solution

    # Extended search that includes returning to start position
    def searchExtraCredit(self):
        self.solution = []
        self.found_items = set()
        cur = (self.start[0], self.start[1])

        while len(self.found_items) < self.num_items:
            path, item_node = self.find(cur)
            if not path or not item_node:  # If no path is found, break
                break
            cur = item_node
            self.found_items.add(item_node)
            self.solution += path[1:]
        # Return to start
        path, _ = self.find(cur, (self.start[0], self.start[1]))
        if path:
            self.solution += path[1:]

    def find(self, cur_start, item_to_find=None):
        """
        Finds the shortest path from cur_start to either:
        - The closest unvisited item (if item_to_find is None)
        - The specific item_to_find (if provided)

        Args:
            cur_start (tuple): Starting position (x, y)
            item_to_find (tuple, optional): Specific target position to find

        Returns:
            tuple: (path, target_node) where path is list of positions and target_node is the found item position
        """
        # Initialize list to use as queue and visited set
        queue = [(cur_start, [cur_start])]  # List of tuples: (current_position, path_to_current)
        visited = {cur_start}  # Track visited positions
        while queue:
            # Remove first element (FIFO - First In First Out for BFS)
            current_pos, current_path = queue.pop(0)
            # First case: if we're looking for a specific position and found it
            if item_to_find and current_pos == item_to_find:
                return current_path, current_pos
            # Second case: if we're looking for any uncollected item and found one
            if not item_to_find and self.adjacency_list[current_pos][0] and current_pos not in self.found_items:
                return current_path, current_pos
            # Explore neighbors
            for next_pos in self.adjacency_list[current_pos][1]:
                if next_pos not in visited:
                    visited.add(next_pos)
                    new_path = current_path + [next_pos]
                    queue.append((next_pos, new_path))

        return None, None


if __name__ == "__main__":
    pass