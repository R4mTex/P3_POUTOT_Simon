from models.character import MacGyver
from models.map import Map

# create a class that will represent our logic


class Logic:

    # initialize the map and Macgyver
    def __init__(self):
        self.map = Map('models/map.txt')
        self.macgyver = MacGyver(self.map)

    # create a method for return return a value
    def get_map(self):
        return self.map

    # create a method for return return a value
    def get_macgyver(self):
        return self.macgyver
