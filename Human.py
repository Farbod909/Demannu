from models import GravityEntity


WALKING_SPEED = 5
JUMP_SPEED = 6


class Human(GravityEntity):

    def __init__(
            self,
            initial_x: int, initial_y: int,
            width: int, height: int):
        super().__init__(initial_x, initial_y, width, height)
        self.speed_x = 0
        self.speed_y = 0

    def change_direction_to_right(self):
        self.speed_x = WALKING_SPEED

    def change_direction_to_left(self):
        self.speed_x = -WALKING_SPEED

    def advance_position(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

    def apply_gravity(self):
        self.speed_y += self.accel_y

    def apply_physics(self):
        self.apply_gravity()
        self.advance_position()

    def jump(self):
        self.speed_y = -JUMP_SPEED

    def stop_walking(self):
        self.speed_x = 0
