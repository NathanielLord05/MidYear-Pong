#Nate

import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, height, width, color):
        super().__init__()

        self.paddle = pygame.pygame.Surface(width, height)
        self.paddle.fill(0, 0, 0)
        self.paddle.set_colorkey(0, 0, 0)

        pygame.draw.rect(self.paddle, color, ([Black, width, height])
        
