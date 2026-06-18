"""
Tester

The test class creates an adjacency list. The list is a  dict in the following form:
{(x,y): [is_item, [adjacent_nodes]] , ...}
   is_item is a boolean
   adjacent_nodes ia a list of [x,y] nodes


The following commands are available for a search algorithm: (README)
get_list()
get_start()
get_number_of_items()
test_path(path)           - You can test paths of actions. Input path should be a list of [x,y] coordinates
   returns:  "All items found  |  Cells visited  |  Number of items found  |  Was extra credit completed"

Samuel Landis
"""
from bokeh.layouts import layout


class Tester:
    def __init__(self, layout): #private
        # Initialize the Tester class with the layout, number of items and starting position
        self.layout = layout.get_layout()
        self.num_items = int(layout.get_num_of_items())
        self.x_start, self.y_start  = layout.get_start_pos()
        self.x_start = int(self.x_start)
        self.y_start = int(self.y_start)
        self.diagonal = False
        self.adjacency_list = self.create_list()
        self.size = int(layout.get_rows()) * int(layout.get_cols())

    def create_list(self): #private
        out = {}
        for ii in range(0,len(self.layout)):
            for jj in range(0, len(self.layout[0])):
                lst = []
                if self.valid_position(ii,jj):
                    #check through all combos
                    if self.valid_position(ii+1,jj):
                        lst.append(((ii+1),jj))
                    if self.valid_position(ii-1,jj):
                        lst.append(((ii-1),jj))
                    if self.valid_position(ii,jj+1):
                        lst.append((ii, (jj+1)))
                    if self.valid_position(ii,jj-1):
                        lst.append((ii,(jj-1)))
                    if self.diagonal:
                        if self.valid_position(ii+1,jj+1):
                            lst.append(((ii+1),(jj+1)))
                        if self.valid_position(ii+1,jj-1):
                            lst.append(((ii+1),(jj-1)))
                        if self.valid_position(ii-1,jj-1):
                            lst.append(((ii-1),(jj-1)))
                        if self.valid_position(ii-1,jj+1):
                            lst.append(((ii-1),(jj+1)))
                out[(ii,jj)] = [self.check_for_item(ii,jj),lst]
        return out

    def get_list(self): #public
        return self.adjacency_list

    def check_for_item(self,x,y): #private
        # Check if the current cell contains an item
        return self.layout[x][y] == "$"

    def valid_position(self, x, y): #private
        """
        Checks if the specified (x, y) coordinates are within bounds and not a wall.
        Parameters:
        - x (int): The x-coordinate to validate.
        - y (int): The y-coordinate to validate.
        Returns:
        - bool: True if the position is valid and not a wall, otherwise False.
        """
        if (y < len(self.layout[0])) and (y >= 0) and (x < len(self.layout)) and (x >= 0):
            return self.layout[x][y] != "x"
        return False

    def test_path(self, path): #public
        #path should be a list of [x,y] cords
        found = set()
        visits = 0
        x = self.x_start
        y = self.y_start
        for move in path:
            if move in self.adjacency_list[(x,y)][1]:
                x = move[0]
                y = move[1]
                if self.check_for_item(x,y):
                    if not (x,y) in found:
                        found.add((x,y))
                visits += 1
            else:
                break
        bonus = (x == self.x_start) and (y == self.y_start) and (len(found) == int(self.num_items))
        return len(found) == int(self.num_items), visits, len(found), bonus

    def get_num_of_items(self): #public
        # Retrieves the number of items
        return self.num_items

    def get_start(self): #public
        # Retrieves the starting coordinates
        return [self.x_start, self.y_start]

    def get_size(self):
        # Retrieves the size of the grid (cols * rows)
        return self.size