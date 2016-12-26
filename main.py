import pygame
from Human import Human
from views import GameView

pygame.init()


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Demannu')

clock = pygame.time.Clock()

game_view = GameView(game_display)
human = Human(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2, 10, 40)

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                human.change_direction_to_right()
            elif event.key == pygame.K_LEFT:
                human.change_direction_to_left()
            elif event.key == pygame.K_UP:
                human.jump()
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                human.stop_walking()

    human.apply_physics()

    game_view.fill((255,255,255))
    game_view.render_entity(human)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
