# trying to fix it because I have no idea what's happening, sorry sara </3
import pygame

# importing ball and paddle files
from ball import Ball
from paddles import Paddle
pygame.init()
pygame.mixer.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# creating main screen
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by Stressed High School Students")

BACKGROUND_MUSIC = pygame.mixer.Sound('rainbowconnection.mp3')

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 15, 15)
ball.rect.x = 345
ball.rect.y = 195

spriteLog = pygame.sprite.Group()

spriteLog.add(ball)
spriteLog.add(paddleA)
spriteLog.add(paddleB)

FPS = pygame.time.Clock()
player1Score = 0
player2Score = 0

run = True
while run:
    BACKGROUND_MUSIC.play()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                BACKGROUND_MUSIC.stop()
        elif event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    
    spriteLog.update()
    
    if ball.rect.x >= 690:
        player1Score += 1
        ball.v[0] = -ball.v[0]
    if ball.rect.x <= 0:
        player2Score += 1
        ball.v[0] = -ball.v[0]
    if ball.rect.y > 490:
        ball.v[1] = -ball.v[1]
    if ball.rect.y < 0:
        ball.v[1] = -ball.v[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    WIN.fill(BLACK)
    pygame.draw.line(WIN, WHITE, [349, 0], [349, 500], 5)
    spriteLog.draw(WIN)

    font = pygame.font.Font(None, 74)
    text = font.render(str(player1Score), 1, WHITE)
    WIN.blit(text, (250,10))
    text = font.render(str(player2Score), 1, WHITE)
    WIN.blit(text, (420,10))


    if player1Score >= 20:
        spriteLog.remove(ball)
        WIN.fill(BLACK)
        text = font.render(str(player1Score), False, WHITE)
        text = font.render(("Player 1 won!"), False, WHITE)
        WIN.blit(text, (180,100))

    elif player2Score >= 20:
        spriteLog.remove(ball)
        WIN.fill(BLACK)
        text = font.render(str(player2Score), True, WHITE)
        text = font.render(("Player 2 won!"), True, WHITE)
        WIN.blit(text, (180,100))
    spriteLog.update()

    pygame.display.flip()

    FPS.tick(60)

pygame.quit()