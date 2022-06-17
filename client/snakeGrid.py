import sys
import time
import pygame


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

global SCREEN, CLOCK
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)
drawGrid()

def gameLoop():
    game_over = False
    X = WINDOW_WIDTH/2
    Y = WINDOW_HEIGHT/2

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if X >= WINDOW_WIDTH or X < 0 or Y >= WINDOW_HEIGHT or Y < 0:
            game_over = True
        pygame.display.update()
        CLOCK.tick(10)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()
gameLoop()