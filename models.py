GRAVITY_ACCELERATION = 0.6


class Entity:

    def __init__(
            self,
            initial_x: int, initial_y: int,
            width: int, height: int):
        self.pos_x = initial_x - (width / 2)
        self.pos_y = initial_y - (height / 2)
        self.width = width
        self.height = height


class GravityEntity(Entity):

    def __init__(
            self,
            initial_x: int, initial_y: int,
            width: int, height: int):
        super().__init__(initial_x, initial_y, width, height)
        self.accel_y = GRAVITY_ACCELERATION
