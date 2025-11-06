from core.monster import Monster
from random import randrange

class Orc(Monster):
    """
    Orc
    """
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp, "orc", randrange(0,6), randrange(10,16), randrange(2,9), weapon)

    def attack(self):
        pass

    def speak(self):
        pass