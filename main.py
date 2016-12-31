"""
Demannu

A simple platformer with a human and a companion robot
By Farbod Rafezy

https://github.com/Farbod909/Demannu

MIT License

"""

import pygame
from models import Human
from resource_manager import load_png


DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

pygame.init()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Demannu')

city_bg = load_png('cityBackground.png')[0]
city_bg = pygame.transform.scale(city_bg, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
background = pygame.Surface(game_display.get_size())
background = background.convert()
background.blit(city_bg, (0, 0))

game_display.blit(background, (0, 0))
pygame.display.flip()

human = Human(initial_x=DISPLAY_WIDTH/2, initial_y=DISPLAY_HEIGHT/2)
human_sprite = pygame.sprite.RenderPlain(human)

clock = pygame.time.Clock()

game_exit = False
while not game_exit:
    clock.tick(60)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                human.move_right()
            elif event.key == pygame.K_LEFT:
                human.move_left()
            elif event.key == pygame.K_UP:
                human.jump()
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
