from pathlib import Path
from typing import TYPE_CHECKING

from jsonpickle import dumps, loads

if TYPE_CHECKING:
    from .models.game import Game

__all__ = [
    'SAVE_FILE',
    'save_game',
    'load_game',
    'save_exists'
]

SAVE_FILE = Path('savedata.json')


def save_exists() -> bool:
    return SAVE_FILE.exists()


def load_game() -> 'Game':
    with open(SAVE_FILE) as save:
        return loads(save.read())


def save_game(game: 'Game'):
    with open(SAVE_FILE, 'w') as save:
        save.write(dumps(game, ))
