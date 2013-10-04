import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 1000, 800
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('The Game')
ball = pygame.image.load("happypizza.jpg")
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
            if pygame.key.get_pressed()[K_w] and not pygame.key.get_pressed()[K_s]:
                speed[1] = -1
            elif pygame.key.get_pressed()[K_s] and not pygame.key.get_pressed()[K_w]:
                speed[1] = 1
            elif pygame.key.get_pressed()[K_SPACE]:
                speed[1] = -1
            else:
                speed[1] = 0    
    if(ballrect.y > height):
        ballrect.y = height
    ballrect = ballrect.move(speed)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
