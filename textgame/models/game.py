from .player import Player
from .. import save_game, save_exists, load_game

__all__ = [
    'Game'
]

from ..command import parse_args, get_command


class Game:
    def __init__(self, player: 'Player'):
        self.running = False
        self.player = player

    @classmethod
    def load(cls, overwrite=False) -> 'Game':
        if not overwrite and save_exists():
            return load_game()

        game = cls(Player(input('enter your player name: ').lower().strip()))
        game.save()

        return game

    def save(self):
        save_game(self)

    def _display_info(self):
        pass

    def _handle_player_input(self):
        self._display_info()
        cmd, *args = parse_args(input('\n] ').lower().strip())
        print()
        if command := get_command(cmd):
            command.execute(self, cmd, *args)

    def _process_single(self):
        self._handle_player_input()

    def play(self):
        self.running = True

        while self.running:
            self._process_single()
