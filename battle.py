from dice import Dice

class Battle:

    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.attacker = None
        self.attacked = None


    def play_battle(self):
       """this function will manage the battle play"""

       #this will decide the initial attacker
       self.attacker, self.attacked = self.get_attacker_and_defender()
       battle_round = 1

       while self.attacked.hp > 0:

           if battle_round != 1:
               self.swap_players()

           self.battle_round(battle_round)
           battle_round += 1


       self.print_battle_result()


    def battle_round(self, battle_round):
        print(f"Current round is : {battle_round}")
        print(f"the attacker is : {self.attacker.name} and the attacked character is : {self.attacked.name}")
        self.attacker.attack(self.attacked)


    def get_attacker_and_defender(self):
        """this function will return who is the attacker and who is the defender"""
        player_result = Dice.roll_six_dice() + self.player.speed
        monster_result = Dice.roll_six_dice() + self.monster.speed

        #if the monster is greater than the monster will be the attacker else
        # (player is greater or equal the player will be the attacker)
        return (self.monster, self.player) if player_result < monster_result else (self.player, self.monster)


    def swap_players(self):
        self.attacker, self.attacked = self.attacked, self.attacker


    def print_battle_result(self):

        if self.player.hp < 0:
            print(f"player {self.player.name} won the battle")
        else:
            print(f"player {self.monster.name} won the battle")