from textgame import Command, Game, commands


class Quit(Command):
    name = 'quit'
    help = 'saves then quits the game'

    def execute(self, game: 'Game', raw: str, *args: str):
        game.save()
        game.running = False


class ListCommands(Command):
    name = 'help'
    alias = ['?']
    help = 'shows this help message'

    def execute(self, game: 'Game', raw: str, *args: str):
        longest_command_name_len = max(*map(len, commands), len('COMMAND')) + 1
        longest_command_alias_len = max(*map(len, (' '.join(c.alias) for c in commands.values())), len('ALIAS')) + 1
        seen = set()

        header = f'{"COMMAND":^{longest_command_name_len}} | {"ALIAS":^{longest_command_alias_len}} | HELP'

        print(header)
        print('-' * len(header))

        for command in commands.values():
            for alias in [command.name] + command.alias:
                if alias in seen:
                    continue
                print(
                    f'{alias:<{longest_command_name_len}} | {" ".join(command.alias):<{longest_command_alias_len}} | {command.help}')
                seen.add(alias)
