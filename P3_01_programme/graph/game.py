from models.position import Position
from graph.player import MacGyver
from graph.guardian import Guardian
from graph.paths import Path
from graph.walls import Wall
from graph.items_im import Items_im

# create a class that will represent our game


class Game:

    # create a method for initialize our components
    def __init__(self, logic, screen):
        print("Hello MacGyver,\nTo get out of here you must collect the 3 items hidden in the maze before presenting "
              "in front of the guard, so that he can let you pass.\nGood luck !")
        self.macgyver_bag = 0
        self.logic = logic
        self.paths = Path(self.logic.get_map().paths, screen)
        self.walls = Wall(self.logic.get_map().walls, screen)
        self.items_im = Items_im(self.logic.get_map().items, screen)
        self.player = MacGyver(self.logic.get_map().start)
        self.guardian = Guardian(self.logic.get_map().end)

    # create a method for don't moving in the walls
    def can_move(self, x, y):
        for position_walls in self.walls.walls:
            futur_position = Position(int(self.player.rect.x / 40) + x, int(self.player.rect.y / 40) + y)
            if futur_position == position_walls:
                return False
        return True

    # create a method for taking items in the maze
    def take_item(self, x, y):
        for item in self.items_im.items:
            futur_position = Position(int(self.player.rect.x / 40) + x, int(self.player.rect.y / 40) + y)
            if futur_position == item.pos and self.macgyver_bag < 3 and not item.is_drop:
                self.macgyver_bag += 1
                print(f"You have {item.name} in your backpack.")
                item.is_drop = True
        return True

    # create a method for leaving the maze
    def finish(self, x, y):
        position_guardian = Position(int(self.guardian.rect.x / 40), int(self.guardian.rect.y / 40))
        futur_position = Position(int(self.player.rect.x / 40) + x, int(self.player.rect.y / 40) + y)
        if futur_position == position_guardian and self.macgyver_bag == 3:
            print("Congratulations ! You are out of the maze.")
        elif futur_position == position_guardian and self.macgyver_bag != 3:
            print("Sorry, you succumbed because you don't have all items in your possession.")
        return True
