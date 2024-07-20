import random
from chip import Chip
from player import Player
        
class Game:
    def __init__(self, players) -> None:
        self.turn_counter = 0
        self.players = players

    def turn(self):
        # A turn involves init seeding, seeding, bidding & drawing
        # init seeding: players take turns to add a chip to live_chips
        # seeding: players take turns to add a chip to live_chips list or initiate bidding.
        # bidding: players take turns to bid on how many chips they think they can draw before choosing
        # a skull.
        # drawing: the player with the highest bet will start drawing cards until they reach a skull or reach the bet size
        
        self.turn_counter += 1
        bidding = False

        # init seeding
        print('INIT SEED ' +'-'*20)
        for player in self.players:
            # print([(player, player.chips, player.live_chips) for player in self.players])
            # add to live chip
            player.play_chip()

        # seeding
        print('SEEDING ' +'-'*20)
        while bidding == False:
            for player in self.players:
                if input(f"{player} would you like to initiate betting? y/n ") == 'y':
                    bidding = True
                    player.current_bid = input(f"{player} how much are you bidding? ")
                    break # break the seed as soon as someone initiates betting
                else:
                    player.play_chip()

        # bidding
        print('BIDDING' +'-'*20)
        # start with the player after the one who intiaalised the bid
        while bidding == True:
            pass



def initialise():
    # create player list
    available_players = {
        'Sandra': '👩', 
        'Gregory': '👨', 
        'Betty': '👵', 
        'Stephan': '👷'
    }
    players = []
    # for the amount of players (usually 4) create a players list
    for player in available_players.items():
        players.append(
            Player(
                player[0], # player name
                player[1], # player emoji
                {
                    1: Chip("flower"),
                    2: Chip("flower"),
                    3: Chip("flower"),
                    4: Chip("skull")
                },  # standard chipset
                0          # points
            )
        )
    
    game = Game(players)
    return game


if __name__ == "__main__":
    # initialise the game
    game = initialise()

    game.turn()
