#Tina 
# This file uses pygame to control the motion of the ball
import pygame
import random
BLACK = (0,0,0)
WHITE = (255,255,255)

class Ball (pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()

        # set the color of the ball and its position
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        self.image.set_colorkey(BLACK)

        # create ball shape (temporarily a rectanlge)
        pygame.draw.rect(self.image, color, [0,0, width, height])

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8,8)


        
