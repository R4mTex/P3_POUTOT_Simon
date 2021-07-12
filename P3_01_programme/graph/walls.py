import pygame

# create a class that will represent our walls


class Wall(pygame.sprite.Sprite):

    # create a method for initialize Wall graph
    def __init__(self, pos_walls, screen):
        super().__init__()
        self.image = pygame.image.load('graph/pygame_images/walls.png')
        self.rect = self.image.get_rect()
        self.walls = pos_walls
        self.screen = screen

    # create a method for diplay our walls in the maze
    def display(self):
        for wall in self.walls:
            self.screen.blit(self.image, (wall.x * 40, wall.y * 40))
