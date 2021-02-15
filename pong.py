#sara 
import pygame

from ball import Ball
from Paddles import Paddle

# creating main screen
screen = ---.Screen()
screen.title = ("Play the Pong Game!")
screen.setup(width=900, height = 500)
screen.bgcolor = ("black")

# right paddle
r_paddle = ()
r_paddle.speed(0)
r_paddle.shape("triangle")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=2)

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
        if event.type == pygame.KeyDOWN:
            


