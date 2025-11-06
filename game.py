from factory.factory import Factory
from core.monster import Monster
from random import randrange
from battle import Battle
from core.player import Player

class Game:

    def __init__(self):
        self.monster = None
        self.player = None

    def start(self):

        play_game = True

        while play_game:

            self.show_menu()
            user_input = self.get_user_input()

            if user_input == 1:
                self.choose_random_monster()
                self.create_player()
                self.battle()
            else:
                break


    def show_menu(self):
        return print("Please enter '1' to start a battle or '-1' to exit the game : ")


    def choose_random_monster(self):
        """this function manages choosing a random monster"""
        monster_index = randrange(0, len(Monster.monster_types))
        monster_type = Monster.monster_types[monster_index]

        #this will receive a lambda function with that will create the specified character type
        self.monster = Factory.create()[monster_type]("monster")


    def create_player(self):
        """this function will create the player"""
        player_profession = Player.professions[randrange(0, len(Player.professions))]
        self.player = Player("yosef", player_profession)


    def get_user_input(self):

        while True:
            try:
              result = int(input())

              if result == -1 or result == 1:
                  return result

              print("number must be 1 or -1")

              self.show_menu()
            except:
                print("input must a integer")
                self.show_menu()


    def battle(self):
        battle_instance = Battle(self.player, self.monster)
        battle_instance.play_battle()



