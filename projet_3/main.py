import pygame
from graph.game import Game
from models.logic import Logic
pygame.init()

# generate our game window
pygame.display.set_caption("Labyrinthe")
screen = pygame.display.set_mode((600, 600))

# import the background of our game
background = pygame.image.load('graph/pygame_images/bg.png')

# load our logic
logic = Logic()

# load our game
game = Game(logic, screen)

running = True

# loop as long as this condition is true
while running:

    # apply the background of our game
    screen.blit(background, (0, 0))

    # apply the image of our paths
    game.paths.display()

    # apply the image of our walls
    game.walls.display()

    # apply the image of our items
    game.items_im.display()

    # apply the image of our player
    screen.blit(game.player.image, game.player.rect)

    # apply the image of our guardian
    screen.blit(game.guardian.image, game.guardian.rect)

    # update screen
    pygame.display.flip()

    # if the player does events
    for event in pygame.event.get():

        # if the event is window closing
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detect if a player drops a key on the keyboard
        elif event.type == pygame.KEYDOWN:

            # which key was used + conditions
            if (event.key == pygame.K_RIGHT and
                    game.player.rect.x < 560 and
                    game.can_move(1, 0) and
                    game.take_item(1, 0) and
                    game.finish(1, 0)):
                game.player.move_right()

            elif (event.key == pygame.K_LEFT and
                    game.player.rect.x > 0 and
                    game.can_move(-1, 0) and
                    game.take_item(-1, 0) and
                    game.finish(-1, 0)):
                game.player.move_left()

            elif (event.key == pygame.K_UP and
                    game.player.rect.y > 0 and
                    game.can_move(0, -1) and
                    game.take_item(0, -1) and
                    game.finish(0, -1)):
                game.player.move_up()

            elif (event.key == pygame.K_DOWN and
                    game.player.rect.y < 560 and
                    game.can_move(0, 1) and
                    game.take_item(0, 1) and
                    game.finish(0, 1)):
                game.player.move_down()

        # conditions for close the game
        elif (game.guardian.rect.x == game.player.rect.x and
                game.guardian.rect.y == game.player.rect.y):
            running = False
