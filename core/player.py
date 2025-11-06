from core.character import Character
from random import randrange

class Player(Character):
    """
    Player
    """
    def __init__(self, name, profession):
        super().__init__(name, 50 if profession != "doctor" else 60, randrange(5, 11), randrange(5, 11), randrange(5, 16))
        self.profession = profession

    def attack(self):
        pass

    def speak(self):
        pass