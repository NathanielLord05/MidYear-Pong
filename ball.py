#Tina 
# This file uses pygame to control the motion of the ball
import pygame
import random
BLACK = (0,1,1)

class Ball (pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0, width, height])

        
