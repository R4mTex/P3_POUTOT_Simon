import pygame

# create a class that will represent our guardian


class Guardian(pygame.sprite.Sprite):

    # create a method for initialize Guardian graph
    def __init__(self, pos_end):
        super().__init__()
        self.image = pygame.image.load('graph/pygame_images/guardian.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_end.x * 40
        self.rect.y = pos_end.y * 40
