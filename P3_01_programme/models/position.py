# create a class which will represent a position


class Position:

    # create a method for initialize a position in x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # create a method for compare two positions
    def __eq__(self, other):
        if isinstance(other, Position):
            if other.x == self.x and other.y == self.y:
                return True
        return False

    # create a method for return a string
    def __repr__(self):
        return f"{self.x}/{self.y}"

    # create a method for return the hash value
    def __hash__(self):
        return hash(self.position)
