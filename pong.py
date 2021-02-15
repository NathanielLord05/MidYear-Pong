#sara 
import pygame

from ball import Ball
from Paddles import Paddle

# creating main screen
screen = screen.Screen()
screen.title = ("Play the Pong Game!")
screen.setup(width=900, height = 500)
screen.bgcolor = ("black")

# right paddle
r_paddle = ()
r_paddle.speed(0)
r_paddle.shape("rectangle")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=2)

# left paddle 
l_paddle = screen2.Screen()
l_paddle.shape("rectangle")
l_paddle.color("black")
l_paddle.speed(0)
l_paddle.shapesize(stretch_len = 3, stretch_wid = 5)



spriteLog = pygame.sprite.Group()

spriteLog.add(ball)
spriteLog.add(paddleA)
spriteLog.add(paddleB)

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
            


