# create a class that will represent our item


class Item:

    # create a method for initialize item
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.is_drop = False
