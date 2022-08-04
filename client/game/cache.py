
PLAYERS = {}

def add_player(player):
    PLAYERS[player.id] = player
    print(PLAYERS , 'cache')

def remove_player(player):
    pass

def get_player(id):
    return PLAYERS[id]
    
def display_players():
    pass