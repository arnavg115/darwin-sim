import time
from Constants import HEIGHT, RECT_X, RECT_Y, WIDTH
import pygame
import math
from random import randint
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
        self.reached = False

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
            self.calc_dist()
            self.if_dist()
            self.increment +=1
        else:
            self.done = True
    
    def calc_dist(self):
        dist = math.sqrt(math.pow((RECT_X-self.x),2)+math.pow(RECT_Y-self.y,2))
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
    
    def if_dist(self):
        if self.fitness > 0.95:
            print("done")

            exit()



