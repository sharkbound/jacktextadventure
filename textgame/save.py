from pathlib import Path
from typing import TYPE_CHECKING

from jsonpickle import dumps, loads

if TYPE_CHECKING:
    from .models.game import Game

__all__ = [
    'SAVE_FILE',
    'save',
    'load',
    'exists'
]

SAVE_FILE = Path('savedata.json')


def exists() -> bool:
    return SAVE_FILE.exists()


def load() -> 'Game':
    with open(SAVE_FILE) as save:
        return loads(save.read())


def save(game: 'Game'):
    with open(SAVE_FILE, 'w') as save:
        save.write(dumps(game, ))
