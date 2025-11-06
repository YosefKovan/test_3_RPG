from core.character import Character
from random import randrange
from dice import Dice

class Monster(Character):
    """
    Monster
    """
    monster_types = ["goblin", "orc"]
    weapons = ["knife", "ax", "sword"]
    weapon_affect = {"knife" : 0.5, "sword" : 1, "ax" : 1.5}


    def __init__(self, name, hp, monster_type, speed, power, armor_rating):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = monster_type
        self.weapon = Monster.weapons[randrange(0, len(Monster.weapons))]

    def handle_attack_result(self, attacked):
        return (Dice.roll_six_dice() + self.power) * Monster.weapon_affect[self.weapon]


    def speak(self):
        print(f"monster named : {self.name} and of type : {self.type}")