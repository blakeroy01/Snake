from tkinter.tix import WINDOW
import pygame 
from pygame.math import Vector2
import game.visuals as vs
import random as rand
class FRUIT:
    def __init__(self):
        self.x = rand.randint(0,vs.blockSize - 1)
        self.y = rand.randint(0,vs.blockSize - 1)
        self.pos = Vector2(self.x ,self.y) 

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * vs.blockSize, self.pos.y * vs.blockSize ,vs.blockSize,vs.blockSize)
        pygame.draw.rect(vs.SCREEN,(200,66,14),fruit_rect)
