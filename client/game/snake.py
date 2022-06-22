import random as rand
from pygame.math import Vector2
import game.visuals as vs
import pygame 
class SNAKE:
    def __init__(self):

        self.body = [Vector2(15,8),Vector2(16,8),Vector2(17,8)]

    def draw_snake(self):
        for body in self.body:
            x_pos = body.x * vs.blockSize
            y_pos = body.y * vs.blockSize
            body_rect = pygame.Rect(x_pos ,y_pos,vs.blockSize,vs.blockSize)
            pygame.draw.rect(vs.SCREEN,(138,201,38),body_rect)