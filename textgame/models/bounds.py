from random import randint, randrange
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pos import Pos

__all__ = [
    'Bounds',
]


class Bounds:
    def __init__(self, size_x, size_y):
        self.size_y = size_y
        self.size_x = size_x

    def in_bounds(self, pos: 'Pos'):
        return 0 <= pos.x < self.size_x and 0 <= pos.y < self.size_y

    def random(self):
        return randrange(self.size_x), randrange(self.size_y)

    def __repr__(self):
        return f'<Bounds size_x={self.size_x} size_y={self.size_y}>'
