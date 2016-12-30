import pygame
from resource_manager import load_png


class Human(pygame.sprite.Sprite):

    GRAVITY_ACCELERATION = 0.6
    WALK_SPEED = 5
    JUMP_SPEED = 6

    def __init__(self, initial_x, initial_y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('charRightStill.png')
        self.area = pygame.display.get_surface().get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.rect.center = (initial_x, initial_y)

    def move_right(self):
        self.vel_x = Human.WALK_SPEED

    def move_left(self):
        self.vel_x = -Human.WALK_SPEED

    def update(self):
        self._apply_gravity()
        new_pos = self.rect.move(self.vel_x, self.vel_y)
        self.rect = new_pos
        pygame.event.pump()

    def _apply_gravity(self):
        self.vel_y += Human.GRAVITY_ACCELERATION

    def jump(self):
        self.vel_y = -Human.JUMP_SPEED

    def stop_walking(self):
        self.vel_x = 0
