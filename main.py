"""
Demannu

A simple platformer with a human and a companion robot
By Farbod Rafezy

https://github.com/Farbod909/Demannu

MIT License

"""


import pygame
from models import Human
import colors

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Demannu')

background = pygame.Surface(game_display.get_size())
background = background.convert()
background.fill(colors.WHITE)

game_display.blit(background, (0, 0))
pygame.display.flip()

human = Human(initial_x=DISPLAY_WIDTH/2, initial_y=DISPLAY_HEIGHT/2)
human_sprite = pygame.sprite.RenderPlain(human)


def handle_key_down(key):
    if key == pygame.K_RIGHT:
        human.move_right()
    elif key == pygame.K_LEFT:
        human.move_left()
    elif key == pygame.K_UP:
        human.jump()


clock = pygame.time.Clock()

game_exit = False
while not game_exit:
    clock.tick(60)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            handle_key_down(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                human.stop_walking()

    dirty_rects = []

    game_display.blit(background, human.rect, human.rect)
    dirty_rects.append(human.rect)
    human_sprite.update()
    human_sprite.draw(game_display)
    dirty_rects.append(human.rect)
    pygame.display.update(dirty_rects)

pygame.quit()
quit()
