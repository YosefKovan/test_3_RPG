from core.monster import Monster
from random import randrange

class Orc(Monster):
    """
    Orc
    """
    def __init__(self, name):
        super().__init__(name, 50, "orc", randrange(0,6), randrange(10,16), randrange(2,9))

