import pygame as pg
import random


class Race(pg.sprite.Sprite):
    def __init__(self,line_1,line_2,line_3,line_4,line_5,money,speed_car):
        pg.sprite.Sprite.__init__(self)
        self.line_1=line_1
        self.line_2=line_2
        self.line_3=line_3
        self.line_4=line_4
        self.line_5=line_5
        self.money=money
        self.speed_car=speed_car
    def plus(self,line_1,line_2,line_3,line_4,line_5,money,speed_car):
        line_1.y+=speed_car
        line_2.y+=speed_car
        line_3.y+=speed_car
        line_4.y+=speed_car
        line_5.y+=speed_car
        money.y+=speed_car
    
    def minus(self):
        self.line_1.y-=self.speed_car
        self.line_2.y-=self.speed_car
        self.line_3.y-=self.speed_car
        self.line_4.y-=self.speed_car
        self.line_5.y-=self.speed_car
        self.money.y-=self.speed_car

