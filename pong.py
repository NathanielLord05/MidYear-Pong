#sara 
import pygame

from ball import Ball
from Paddles import Paddle

# creating main screen
screen = ---.Screen() # unneccessary?
screen.title = ("Play the Pong Game!")
screen.setup(width=900, height = 500)
screen.bgcolor = ("black")

# right paddle
r_paddle = ()
r_paddle.speed(0) # unneccessary?
r_paddle.shape("triangle")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=2)

spriteLog = pygame.sprite.Group()

spriteLog.add(ball)
spriteLog.add(l_paddle)
spriteLog.add(r_paddle)

time = pygame.time.Clock()
player1Score = 0
player2Score = 0


running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_esc:
                running = False
        elif event.type == pygame.QUIT:
            running = False
            

    if pygame.sprite.collide_mask(ball, l_paddle) or pygame.sprite.collide_mask(ball, r_paddle):
        ball.bounce

    fontSize = pygame.font.Font(None, 69)
    player1text = font.render(str(player1Score)), 1, 255, 255, 255)
    screen.blit(text, 250, 10)
    player2text = font.render(str(player2Score)), 1, 255, 255, 255)
    screen.blit(text, 420, 10)
    scree.fill(BLACK)

    pygame.draw.line(screen, 255, 255, 255, [349, 0], [349, 500], 5)

    spriteLog.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()            


