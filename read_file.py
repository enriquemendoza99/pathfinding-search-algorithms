"""
Read File

Opens a scenario gets the header and converts the body it into a 2D array

"""
graphing = True


class Layout:
    def __init__(self, letter, number):
        self.name = f"Scenario {letter}{number}"
        if graphing:
            filepath = f"scenarios_graph/scenario_{letter}{number}.txt"
        else:
            filepath = f"scenarios/scenario_{letter}{number}.txt"
        with open(filepath, 'r') as file:
            first_line = file.readline()
            header = first_line.strip()
            self.x_size, self.y_size, self.x_start, self.y_start, self.num_items = header.split()
            self.layout = [list(line.strip().replace(" ","")) for line in file]

    def print(self):
        print(f"Rows: {self.x_size} | Columns: {self.y_size} | x start: {self.x_start} | y start: {self.y_start} | number of items: {self.num_items}")
        for row in self.layout:
            print(''.join(row))

    def print_board(self):
        for row in self.layout:
            print(''.join(row))

    def get_name(self):
        return self.name

    def get_start_pos(self):
        return self.x_start, self.y_start

    def get_rows(self):
        return self.x_size

    def get_cols(self):
        return self.y_size

    def get_size(self):
        return self.x_size, self.y_size

    def get_num_of_items(self):
        return self.num_items

    def get_layout(self):
        return self.layout

    def get_position(self,x,y):
        return self.layout[x][y]


if __name__ == "__main__":
    #scenario_{a-d}{0-4}
    test_file = 'scenario_a0.txt'
    test = Layout("a",0)
    test.print()

