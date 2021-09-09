import math
from random import randint

from Ball import Ball
import pygame
import time

WIDTH = 900
HEIGHT = 500
RECT_X=890
RECT_Y=490
NUM = 0
class gen:
    def __init__(self) -> None:
        self.gen = 1
    def incre(self):
        self.gen = self.gen +1
while NUM <5:
    NUM = int(input("How many balls do you want > "))

class Ball:
    def __init__(self,length,fromother:bool= False, ball1= None,ball2= None) -> None:

        if fromother:
            self.genes = self.gen_from_parents(ball1,ball2)
        else:
            self.genes = self.generate_genes(length)
        self.x =15
        self.y =15
        self.increment = 0
        self.done = False
        self.fitness = 0

    def generate_genes(self,length:int):
        rep = []

        for i in range(length):
            rep.append([randint(-30,30), randint(-30,30)])
        return rep
    
    def draw(self,canvas):
        pygame.draw.circle(canvas,(0,255,255),(self.x, self.y),10,0)
    
    def move(self):
        if self.increment < len(self.genes):
            if (self.x + self.genes[self.increment][0]) > 15 and (self.x + self.genes[self.increment][0]) < (WIDTH-15):
                self.x += self.genes[self.increment][0]
            else:
                self.x += -1*self.genes[self.increment][0]
            if (self.y + self.genes[self.increment][1]) > 15 and (self.y + self.genes[self.increment][1]) < (HEIGHT-15):
                self.y += (self.genes[self.increment][1])
            else:
                self.y += (-1*self.genes[self.increment][1])
            self.calc_fitness()
            self.increment +=1
        else:
            self.done = True
    
    def calc_dist(self):
        return math.sqrt(math.pow((RECT_X-self.x),2)+math.pow(RECT_Y-self.y,2))

    def calc_fitness(self):
        dist = self.calc_dist()
        self.fitness = 1- (dist/math.sqrt(math.pow((RECT_X-0),2)+math.pow(RECT_Y-0,2)))
    
    
    def gen_from_parents(self,ball, ball1):
        res = []
        for i in range(len(ball.genes)):

            if randint(1,6) == 1:
                res.append([randint(-30,30), randint(-30,30)])
            else:
                if randint(1,2) == 1:
                    res.append(ball.genes[i])
                else:
                    res.append(ball1.genes[i])    
            
        return res

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