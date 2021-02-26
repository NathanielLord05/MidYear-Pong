#Nate

import pygame

BLACK = (0, 0, 0)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, height, width, color):
        super().__init__()

        self.image = pygame.pygame.Surface(width, height)
        # self.image.fill(BLACK)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, ([0, 0, width, height]))
        self.rect = self.image.get_rect()

        paddle1 = Paddle(WHITE, 10, 100)
        l_paddle.rect.x = 20
        l_paddle.rect.y = 200
        
        paddle2 = Paddle(WHITE, 10, 100)
        r_paddle.rect.x = 670
        r_paddle.rect.y = 200

    def UpOffScreen(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def DownOffScreen(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        l_paddle.moveUp(3)
                    if event.key == pygame.K_s:
                        l_paddle1.moveDown(3)
                    if event.key == pygame.K_UP:
                        r_paddle2.moveUp(3)
                    if event.key == pygame.K_DOWN:
                        r_paddle1.moveDown(3)



    
