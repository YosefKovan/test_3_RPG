from random import randrange


class Dice:
    """
    Dice
    """
    def __init__(self, sides):
        self.sides = sides + 1

    def roll(self):
        return randrange(0, self.sides)

    @staticmethod
    def roll_twenty_dice():
        return randrange(0, 21)

    @staticmethod
    def roll_six_dice():
        return randrange(0, 7)