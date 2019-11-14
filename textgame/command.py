from pathlib import Path
from shlex import split
from typing import TYPE_CHECKING, List, Dict, Union, Optional

if TYPE_CHECKING:
    from .models.game import Game


def parse_args(cmd: str) -> List[str]:
    try:
        return split(cmd)
    except:
        return cmd.split()


class Command:
    name: str = 'NO_NAME'
    help: str = 'NO_HELP'
    alias: List[str] = []

    def execute(self, game: 'Game', raw: str, *args: str):
        pass

    def __init_subclass__(cls, **kwargs):
        for name in [cls.name] + cls.alias:
            commands[name] = cls()


commands: Dict[str, Command] = {}


def load_commands(path: Union[str, Path]):
    if isinstance(path, str):
        path = Path(path)

    for file in path.iterdir():
        with open(file) as f:
            exec(f.read())


def get_command(cmd) -> Optional[Command]:
    return commands.get(cmd)
