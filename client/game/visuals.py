import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def initialize_game():
    global SCREEN, CLOCK
    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    
    _draw_grid()

def _draw_grid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)