import pygame
from models import Entity
import colors


class GameView:

    def __init__(self, game_display):
        self.game_display = game_display

    def fill(self, color):
        self.game_display.fill(color)

    def render_entity(self, entity: Entity):
        pygame.draw.rect(
            self.game_display, colors.BLACK,
            [entity.pos_x, entity.pos_y, entity.width, entity.height])

