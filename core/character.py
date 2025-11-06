from abc import ABC, abstractmethod


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

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def speak(self):
        pass