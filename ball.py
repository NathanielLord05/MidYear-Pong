#Tina 
# This file uses pygame to control the motion of the ball
import pygame
import random
BLACK = (0,0,0)
WHITE = (255,255,255)

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # set the color of the ball and its position
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        self.image.set_colorkey(BLACK)

        # create ball shape (temporarily a rectanlge)
        pygame.draw.rect(self.image, color, [0,0, width, height])
        self.v = [random.randint(4,8), random.randint(-8,8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.v[0]
        self.rect.y += self.v[1]

    def bounce(self):
        self.v[0] = -self.v[0]
        self.v[1] = random.randint(-8,8)




        
