from core.orc import Orc
from core.player import Player
from core.goblin import Goblin


class Factory:

    @staticmethod
    def create():
        return {
            "player" : lambda name, profession : Player(name, profession),
            "orc" : lambda name : Orc(name),
            "goblin" : lambda name : Goblin(name)
        }