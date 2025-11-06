from core.monster import Monster
from random import randrange

class Goblin(Monster):
    """
    Goblin
    """
    def __init__(self, name, weapon):
        super().__init__(name, 20, "goblin", randrange(5,11), randrange(5,11), 1, weapon)

    def attack(self):
        pass

    def speak(self):
        pass

    def run_away(self):
        pass

