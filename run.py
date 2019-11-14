from textgame.command import load_commands
from textgame.models import Game

load_commands('textgame/commands/')

game = Game.load()
game.play()
