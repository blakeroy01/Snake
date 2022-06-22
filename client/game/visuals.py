import pygame
from game.fruit import FRUIT
from game.snake import SNAKE
BACKGROUNDCOLOR = (30, 47, 35)
GRIDCOLOR = (52, 98, 63)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200
blockSize = 20 #Set the size of the grid block

def initialize_game():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BACKGROUNDCOLOR)
    _draw_grid()

    # Fruit Generation Example 
    # Need to Randomly Generate Fruit Objects <------
    FR = FRUIT()
    FR.draw_fruit()
    FR1 = FRUIT()
    FR1.draw_fruit()
    FR2 = FRUIT()
    FR2.draw_fruit()
    SN = SNAKE()
    SN.draw_snake()

#Draw Map 
def _draw_grid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, GRIDCOLOR, rect, 1)
