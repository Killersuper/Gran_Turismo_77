import pygame as pg
import random


class Race(pg.sprite.Sprite):
    def __init__(self,line_1,line_2,line_3,line_4,line_5,money):
        pg.sprite.Sprite.__init__(self)
        line_1.y+=30
        line_2.y+=30
        line_3.y+=30
        line_4.y+=30
        line_5.y+=30
        money.y+=30
    