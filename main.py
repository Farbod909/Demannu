"""
Demannu

A simple platformer with a human and a companion robot
By Farbod Rafezy

https://github.com/Farbod909/Demannu

MIT License

"""


import pygame
from Human import Human
from views import GameView
import colors

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Demannu')

clock = pygame.time.Clock()

game_view = GameView(game_display)
human = Human(
    initial_x=DISPLAY_WIDTH/2,
    initial_y=DISPLAY_HEIGHT/2,
    width=10, height=40)


def handle_key_down(key):
    if key == pygame.K_RIGHT:
        human.change_direction_to_right()
    elif key == pygame.K_LEFT:
        human.change_direction_to_left()
    elif key == pygame.K_UP:
        human.jump()

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            handle_key_down(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                human.stop_walking()

    human.apply_physics()

    game_view.fill(colors.WHITE)
    game_view.render_entity(human)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
