import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Demannu')

WALKING_SPEED = 5
GRAVITY_ACCELERATION = 0.6

speed_x = 0
speed_y = 0
accel_y = GRAVITY_ACCELERATION
pos_x = DISPLAY_WIDTH / 2
pos_y = DISPLAY_HEIGHT / 2

clock = pygame.time.Clock()

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_x = WALKING_SPEED
            elif event.key == pygame.K_LEFT:
                speed_x = -WALKING_SPEED
            elif event.key == pygame.K_UP:
                speed_y = -6
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                speed_x = 0

    pos_x += speed_x
    pos_y += speed_y

    speed_y += accel_y

    # if pos_y >= 500 and 0 <= pos_x <= 400:
    #     pos_y = 500
    #
    # if pos_y >= 300 and 400 < pos_x <= 800:
    #     pos_y = 300

    game_display.fill((255, 255, 255))
    pygame.draw.rect(game_display, (0, 0, 0), [pos_x, pos_y, 10, 40])
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
