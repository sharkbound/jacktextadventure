from textgame import load_commands, Game, Bounds

load_commands('textgame/commands/')

bounds = Bounds(10, 10)

game = Game.load()
game.play()
