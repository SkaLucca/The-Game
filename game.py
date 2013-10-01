import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 800, 600
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if pygame.key.get_pressed()[K_d] and not pygame.key.get_pressed()[K_a]:
                speed[0] = 1
            elif pygame.key.get_pressed()[K_a] and not pygame.key.get_pressed()[K_d]:
                speed[0] = -1
            else:
                speed[0] = 0
    ballrect = ballrect.move(speed)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
