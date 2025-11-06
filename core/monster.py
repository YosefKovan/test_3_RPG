from core.character import Character

class Monster(Character):
    """
    Monster
    """
    def __init__(self, name, hp, monster_type, speed, power, armor_rating, weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = monster_type
        self.weapon = weapon

