import pygame as pg
class Lines_go(pg.sprite.Sprite):
    def __init__(self,lines,coins,speed):
        pg.sprite.Sprite.__init__(self)
        self.lines=lines
        self.coins=coins
        self.speed=speed

        for i in self.lines:
            i.y+=self.speed
        self.coins.y+=self.speed
