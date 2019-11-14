__all__ = [
    'Player'
]


class Player:
    def __init__(self, name: str, max_hp: int = 100):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.xp = 0
        self.level = 0
        self.xp_next_level_up = 5

    @property
    def alive(self):
        return self.hp > 0

    @property
    def dead(self):
        return not self.alive

    def hurt(self, dmg):
        """
        hurts the player, returns if they are dead
        """
        self.hp = max(self.hp - dmg, 0)
        return self.dead

    def heal(self, hp):
        """
        heals the player, restore `hp` health
         """
        self.hp = min((self.hp + hp), self.max_hp)
