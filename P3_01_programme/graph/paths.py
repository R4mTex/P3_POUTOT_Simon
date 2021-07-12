import pygame

# create a class that will represent our paths


class Path(pygame.sprite.Sprite):

    # create a method for initialize Path graph
    def __init__(self, pos_paths, screen):
        super().__init__()
        self.image = pygame.image.load('graph/pygame_images/paths.png')
        self.rect = self.image.get_rect()
        self.paths = pos_paths
        self.screen = screen

    # create a method for diplay our paths in the maze
    def display(self):
        for path in self.paths:
            self.screen.blit(self.image, (path.x * 40, path.y * 40))
