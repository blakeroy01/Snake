# will serve as an interface between main and game
from .player import Player
from .apple import Apple
from .visuals import draw_grid, draw_apple, draw_snakes, draw_main_menu, draw_end_menu

# Get an apple for this game
def new_apple(x, y):
    return Apple(x, y)

# Player starting coordinates are on the server
def new_player(length=1):
    return Player([], length)