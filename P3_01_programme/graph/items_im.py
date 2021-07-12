import pygame

# create a class that will represent our items


class Items_im(pygame.sprite.Sprite):

    # create a method for initialize Item graph
    def __init__(self, pos_items, screen):
        super().__init__()
        self.image = pygame.image.load('graph/pygame_images/items.png')
        self.rect = self.image.get_rect()
        self.items = pos_items
        self.screen = screen

    # create a method for diplay our items in the maze
    def display(self):
        for item in self.items:
            if not item.is_drop:
                self.screen.blit(self.image, (item.pos.x * 40, item.pos.y * 40))
