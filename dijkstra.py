"""
Dijkstra's Search Algorithm
"""

class Dijkstra:
    def __init__(self,tester):
        self.solution = []
        self.found_items = set()
        self.adjacency_list = tester.get_list()
        self.start = tester.get_start()
        self.num_items = tester.get_num_of_items()

    def get_name(self):
        return "Dijkstra's Algorithm"

    def get_path(self):
        return self.solution

    def search(self):
        cur = (self.start[0],self.start[1])
        while len(self.found_items) < self.num_items:
            path, item_node = self.find(cur)
            cur = item_node
            self.found_items.add(item_node)
            self.solution += path[1:]

    def searchExtraCredit(self):
        cur = (self.start[0],self.start[1])
        while len(self.found_items) < self.num_items:
            path, item_node = self.find(cur)
            cur = item_node
            self.found_items.add(item_node)
            self.solution += path[1:]
        path, item_node = self.find(cur, (self.start[0],self.start[1]))
        self.solution += path[1:]

    def find(self, cur_start, item_to_find=None):
        """
        This function finds the path from the start node to the closest item as long as there is no item to find.
        Otherwise, it will find the shortest path to the item_to_find.

        Args:
            cur_start (int, int): The starting node for the search algorithm.
            item_to_find (int, int): The item for the search algorithm to find. I

        Returns:
            list, [int, int]: path to the nearest node that contains an item, node that contains the item
        """

        # Initialize a dictionary of distances to each node. Set them all to infinity.
        dist = {x: float('inf') for x in self.adjacency_list.keys()}
        # Initialize a dictionary of the node that came before each node. Set all values to None.
        last = {x: None for x in self.adjacency_list.keys()}
        # Set the distance to the start node to zero
        dist[cur_start] = 0
        # Initialize a list of nodes that have been checked.
        tested = set()
        # Initialize a list that acts as a queue. Add the start node to the queue.
        q = [(cur_start, 0)]


        # Keep running until the queue is empty
        while q:
            # Find the smallest distance to a node in the queue
            test_node, test_dist = q.pop(0)

            #Add the node to tested.
            tested.add(test_node)
            
            # Check if elem contains an item.
            if self.adjacency_list[test_node][0]:
                # If it does and the item is not in self.found_items
                if test_node not in self.found_items:
                    path = []
                    # Recreate the path to the node.
                    output = test_node
                    while test_node is not None:
                        path.insert(0, test_node)
                        test_node = last[test_node]
                    return path, output

            # Check through all the current nodes neighbors, if they haven't been tested, then add them to the queue.
            for node in self.adjacency_list[test_node][1]:
                if node in tested:
                    continue
                new_dist = test_dist + 1
                if new_dist < dist[node]:
                    dist[node] = new_dist
                    last[node] = test_node
                    q.append((node, new_dist))

        # Initialize a dictionary to keep track of path to the item.
        path = []
        cur_path = item_to_find

        # Recreate the path to the node.
        while cur_path is not None:
            path.insert(0, cur_path)
            cur_path = last[cur_path]
        return path, item_to_find