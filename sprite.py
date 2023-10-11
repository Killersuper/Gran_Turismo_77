import pygame as pg
import random


class Race(pg.sprite.Sprite):
    def __init__(self,line_1,line_2,line_3,line_4,line_5,money,speed_car):
        pg.sprite.Sprite.__init__(self)
        line_1.y+=speed_car
        line_2.y+=speed_car
        line_3.y+=speed_car
        line_4.y+=speed_car
        line_5.y+=speed_car
        money.y+=speed_car
    
