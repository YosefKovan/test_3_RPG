from random import randrange


class Dice:
    """
    Dice
    """

    @staticmethod
    def roll_twenty_dice():
        return randrange(0, 21)

    @staticmethod
    def roll_six_dice():
        return randrange(0, 7)