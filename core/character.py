from abc import ABC, abstractmethod
from dice import Dice


class Character(ABC):
    """
    Character
    """

    def __init__(self, name, hp, speed, power, armor_rating):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating


    def attack(self, attacked):

        attacker_dice_rol = Dice.roll_twenty_dice()

        if attacker_dice_rol + self.speed > attacked.armor_rating:
            #this will return the amount of harm that is caused
            attack_result = self.handle_attack_result(attacked)
            attacked.hp -= attack_result

            print(f"attack was successful: the attack caused {attack_result} harm!")
            print(f"the attacked current hp is {attacked.hp}")

        else:
            print("The attack was not successful!!!")



    @abstractmethod
    def handle_attack_result(self, attacked):
        pass

    @abstractmethod
    def speak(self):
        pass


