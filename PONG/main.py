import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")


#-----------------
#-----------------


#create game objects
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 250

#create list of objects
sprite_list = pygame.sprite.Group()
sprite_list.add(paddleA)
sprite_list.add(paddleB)
sprite_list.add(ball)

run = True
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

#main loop
while run:
    clock.tick(60) #fps

    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #move paddles (P1 keys: q/a) (P2 keys: arrow up/down)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        paddleA.moveUp(5)
    if keys[pygame.K_a]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    sprite_list.update()

    #check if ball has collided with boundary
    if ball.rect.x >= 690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    #check if ball has collided with paddle
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    #render game
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #render sprite objects
    sprite_list.draw(screen)

    #render scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))

    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    pygame.display.flip()
    

pygame.quit()