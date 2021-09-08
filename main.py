

import math
from Constants import HEIGHT, RECT_X, RECT_Y, WIDTH
from Ball import Ball
import pygame
import time

NUM = int(input("Num of balls"))

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

BALLARRAY = []
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS',30)

def init():
    for i in range(NUM):
        BALLARRAY.append(Ball(50))



def update_display():
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN,(0,0,0),pygame.Rect(RECT_X-20,RECT_Y-20,20,20))
    WIN.blit(FONT.render(str(round(calc_avg(),2)),False,(0,0,0)),(800,0))
    for i in BALLARRAY:
        i.draw(WIN)
        i.move()
    if len(BALLARRAY)>0 and BALLARRAY[0].done:
        BALLARRAY.clear()
        time.sleep(1)
        init()
    
    
    pygame.display.update()



def main():
    run = True
    init()
    clock = pygame.time.Clock()

    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        update_display()
        
def calc_avg():
    res = []
    sum = 0
    for ball in BALLARRAY:
        sum+= ball.fitness
    return sum/len(BALLARRAY)
        



main()