from Constants import HEIGHT, RECT_X, RECT_Y, WIDTH
from Ball import Ball
import pygame
import time

NUM = 0
class gen:
    def __init__(self) -> None:
        self.gen = 1
    def incre(self):
        self.gen = self.gen +1
while NUM <5:
    NUM = int(input("How many balls do you want > "))

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

BALLARRAY:list[Ball] = []
pygame.font.init()
FONT = pygame.font.SysFont('Comic Sans MS',30)
GEN = gen()

def init():
    for i in range(NUM):
        BALLARRAY.append(Ball(120))

def from_gen(copyarray):
    total = []
    for ind, ball in enumerate(copyarray):
        
        total.append({"fitness":ball.fitness,"index":ind})
    key_func = lambda x: x.get("fitness")
    total.sort(reverse=True,key=key_func)
    print(total[0:10])
    for i in range(NUM):
        BALLARRAY.append(Ball(120,fromother=True, ball1=copyarray[total[0]["index"]],ball2=copyarray[total[1]["index"]]))



def update_display(paused:bool):
    if not paused:
        WIN.fill((255,255,255))
        pygame.draw.rect(WIN,(0,0,0),pygame.Rect(RECT_X-20,RECT_Y-20,20,20))
        WIN.blit(FONT.render(f"Average Fitness {str(round(calc_avg(),2))}",False,(0,0,0)),(560,0))
        WIN.blit(FONT.render(f"Generation {GEN.gen}",False,(0,0,0)),(300,0))
        for i in BALLARRAY:
            i.draw(WIN)
            i.move()
            
        if len(BALLARRAY)>0 and BALLARRAY[0].done:
            copy = BALLARRAY.copy()
            BALLARRAY.clear()
            from_gen(copy)
            time.sleep(1)
            GEN.incre()
    else:
        WIN.fill((255,255,255))
        WIN.blit(FONT.render("DONE",False,(0,0,0)),(560,0))
        

    pygame.display.update()
    if paused:
        time.sleep(5)
        pygame.quit()



def FindPoint(x1, y1, x2,y2, x, y) :
    if (x > x1 and x < x2 and y > y1 and y < y2) :
        return True
    else :
        return False

def main():
    run = True
    init()
    clock = pygame.time.Clock()
    paused = False
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        paused = check_if_close()
        update_display(paused)

def check_if_close():

    for ball in BALLARRAY:
        
        if FindPoint(RECT_X-50,RECT_Y-50,RECT_X,RECT_Y,ball.x,ball.y):
            return True
    return False

def calc_avg():
    res = []
    sum = 0
    for ball in BALLARRAY:
        sum+= ball.fitness
    return sum/len(BALLARRAY)
        


if __name__ == "__main__":
    main()