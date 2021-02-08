#Nate

import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, height, width, color):
        super().__init__()

        self.paddle = pygame.pygame.Surface(width, height)
        self.paddle.fill(0, 0, 0)
        self.paddle.set_colorkey(0, 0, 0)

        pygame.draw.rect(self.paddle, color, ([Black, width, height])
        self.rect = self.image.get_rect()

        paddle1 = Paddle(WHITE, 10, 100)
        paddleA.rect.x = 20
        paddleA.rect.y = 200
        
        paddle2 = Paddle(WHITE, 10, 100)
        paddleB.rect.x = 670
        paddleB.rect.y = 200

    def UpOffScreen(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def DownOffScreen(self, pixels):
        self.rect.y += pixels

        if self.rect y > 400:
            self.rect.y = 400

        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                paddle1.moveUp(3)
            if keys[pygame.K_s]:
                paddle1.moveDown(3)
            if keys[pygame.K_UP]:
                paddle2.moveUp(3)
            if keys[pygame.K_DOWN]:
                paddle2.moveDown(3)  


    
