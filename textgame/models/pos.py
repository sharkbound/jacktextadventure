from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bounds import Bounds

__all__ = [
    'Pos',
    'randpos',
    'filled_pos'
]


class Pos:
    __slots__ = ['x', 'y']

    def __init__(self, x, y, add=True):
        self.y = y
        self.x = x

        if add:
            filled_pos.add(self)

    @property
    def astuple(self):
        return self.x, self.y

    def move(self, xoff=0, yoff=0):
        if self in filled_pos:
            filled_pos.remove(self)

        return Pos(self.x + xoff, self.y + yoff)

    def __eq__(self, other):
        return (
                (isinstance(other, Pos) and self.astuple == other.astuple)
                or (isinstance(other, tuple) and self.astuple == other)
        )

    def __hash__(self):
        return hash(self.astuple)

    def __repr__(self):
        return f'{{x={self.x}, y={self.y}}}'


filled_pos = set()


def randpos(bounds: 'Bounds') -> Pos:
    while (xy := bounds.random()) in filled_pos:
        pass
    return Pos(*xy)
