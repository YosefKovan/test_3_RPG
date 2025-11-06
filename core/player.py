from core.character import Character
from random import randrange
from dice import Dice

class Player(Character):
    """
    Player
    """
    professions = ["doctor", "fighter"]

    def __init__(self, name, profession):
        super().__init__(name, 50 if profession != "doctor" else 60, randrange(5, 11), randrange(5, 11), randrange(5, 16))
        self.profession = profession

    def handle_attack_result(self, attacked):
        return Dice.roll_six_dice() + self.power

    def speak(self):
        print(f"{self.name} with the profession {self.profession}")