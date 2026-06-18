"""
this is an example of how search
"""




class Algorithm_Name:
    def __init__(self,tester):
        self.solution = []
        self.found_items = set()
        self.adjacency_list = tester.get_list()
        self.start = tester.get_start()
        self.num_items = tester.get_num_of_items()

    def get_name(self):
        return "Algorithm Name"

    def search(self):
        pass

    def searchExtraCredit(self):
        pass

    def get_path(self):
        return self.solution


if __name__ == "__main__":
    pass