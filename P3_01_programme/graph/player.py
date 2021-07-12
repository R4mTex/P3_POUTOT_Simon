import pygame

# create a class that will represent our player


class MacGyver(pygame.sprite.Sprite):

    # create a method for initialize MacGyver graph
    def __init__(self, pos_start):
        super().__init__()
        self.image = pygame.image.load('graph/pygame_images/macgyver.png')
        self.rect = self.image.get_rect()
        self.velocity = 40
        self.rect.x = pos_start.x * self.velocity
        self.rect.y = pos_start.y * self.velocity

    # create a method to move right
    def move_right(self):
        self.rect.x += self.velocity

    # create a method to move left
    def move_left(self):
        self.rect.x -= self.velocity

    # create a method to move up
    def move_up(self):
        self.rect.y -= self.velocity

    # create a method to move down
    def move_down(self):
        self.rect.y += self.velocity
