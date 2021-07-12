from random import choice
from config import settings as constants
from config.settings import NAMES_ITEMS
from models.position import Position
from models.item import Item

# create a class that will represent our logic


class Map:
    # create a method for initialize our maze components
    def __init__(self, filename):
        self.filename = filename

        self._paths = list()
        self._walls = list()
        self._start = list()
        self._end = list()
        self.load_from_file()
        self.init_item_position()

    # create a method for initialize items in the maze
    def init_item_position(self):
        self.items = list()
        for name in NAMES_ITEMS:
            item = Item(name, choice(self._paths))
            self.items.append(item)

    # create some propertys for use methods like attributs
    @property
    def start(self):
        return self._start[0]

    @property
    def end(self):
        return self._end[0]

    @property
    def paths(self):
        return self._paths

    @property
    def walls(self):
        return self._walls

    # create a method to return the test : position in self._paths
    def __contains__(self, position):
        return position in self._paths

    # create a method for read the maze file and add values in some lists
    def load_from_file(self):
        with open(self.filename, "r") as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    if col == constants.PATH_CHAR:
                        self._paths.append(Position(x, y))
                    elif col == constants.START_CHAR:
                        self._start.append(Position(x, y))
                    elif col == constants.END_CHAR:
                        self._end.append(Position(x, y))
                    elif col == constants.WALL_CHAR:
                        self._walls.append(Position(x, y))
