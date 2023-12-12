import random
import pygame as pg
import time
from New_sprite import*

pg.init()
fps = 60
clock = pg.time.Clock()
size=(1500,750)
screen = pg.display.set_mode(size)
pg.display.set_caption("Gran Turismo 7")

def load_image(file,width,height):
    image= pg.image.load(file)
    image=pg.transform.scale(image,(width,height))
    return image

race=pg.Rect(300,0, 900, 750)
line_1=pg.Rect(450,500,15,135)
line_2=pg.Rect(600,500,15,135)
line_3=pg.Rect(750,500,15,135)
line_4=pg.Rect(900,500,15,135)
line_5=pg.Rect(1050,500,15,135)
lines=[line_1,line_2,line_3,line_4,line_5]


max_speed=300 #TODO
acc=10

class Road:
    def __init__(self,mode,coins,rect_coins): #coins
        self.mode=mode
        self.speed=0
        self.coins=coins
        self.rect_coins=rect_coins
    def trassa(self):
        if line_1.y>200:
            for i in lines:
                a=0
                for g in range(1000):  #g можно испльзовать как счетчик метров  TODO
                    a+=335
                    self.line_z=pg.Rect(i.x,line_1.y-a,15,135)
                    if self.line_z.y<size[1] and self.line_z.y>-150:
                        pg.draw.rect(screen,pg.Color('white'),self.line_z)
            if self.mode=='free_ride':
                c=0
                for f in range(1000):
                    c+=335
                    self.rect_coins=self.coins.get_rect()
                    self.rect_coins.center=(size[0]//2,size[1]-c)
                    if self.rect_coins[1]<size[1] and self.rect_coins[1]>-150:
                        screen.blit(self.coins,self.rect_coins)
                        
                        
    def go(self,rect_car):
        self.rect_car=rect_car
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_d]:
            self.rect_car.x += 20
            if self.rect_car.colliderect(self.wall_r):
                self.rect_car.x-=20
        if self.keys[pg.K_a]:
            self.rect_car.x -= 20
            if self.rect_car.colliderect(self.wall_l):
                self.rect_car.x+=20
        if self.keys[pg.K_w]:
            if self.keys[pg.K_f]:
                acc_x=2
            else:
                acc_x=1
            if self.speed<=50:
                self.speed+=10
            elif self.speed>50 and self.speed<=100:
                self.speed+=acc*1.5*acc_x
            elif self.speed>100 and self.speed<=max_speed:
                self.speed+=acc*2*acc_x
            else:
                self.speed=max_speed 
        else:  
            if self.keys[pg.K_SPACE]:
                if self.speed<100 and self.speed>0:
                    self.speed-=1



    def draw(self):
        screen.fill(pg.Color(52, 143, 26))
        pg.draw.rect(screen, pg.Color(182, 187, 193), race)
        self.wall_l=pg.draw.line(screen, pg.Color('black'), (300, 0), (300, 750), 6)
        self.wall_r=pg.draw.line(screen, pg.Color('black'), (1200, 0), (1200, 750), 6)
        pg.draw.rect(screen, pg.Color('white'), line_1)
        pg.draw.rect(screen, pg.Color('white'), line_2)
        pg.draw.rect(screen, pg.Color('white'), line_3)
        pg.draw.rect(screen, pg.Color('white'), line_4)
        pg.draw.rect(screen, pg.Color('white'), line_5)


class Free_ride():
    def __init__(self):
        self.line_1=lines[0]
        self.line_2=lines[1]
        self.line_3=lines[2]
        self.line_4=lines[3]
        self.line_5=lines[4]
        self.race=race
        self.car=load_image('images/Yellow.png',120,240)
        self.rect_car=self.car.get_rect()
        self.rect_car.center=(size[0]//2,size[1]-size[1]//4)
        self.coins=load_image('images/money.png',50,50)
        self.rect_coins=self.coins.get_rect()
        self.rect_coins.center=(size[0]//2,size[1]//2)
        self.road=Road('free_ride',self.coins,self.rect_coins)
        

    def update(self):
        # self.lines_go=Lines_go(lines,self.road.rect_coins,self.road.speed)
        for i in lines:
            i.y+=self.road.speed
        self.rect_coins.y+=self.road.speed

        
    def draw(self):
        self.road.go(self.rect_car)
        self.road.draw()
        self.road.trassa()
        screen.blit(self.car,self.rect_car)


class Racing:
    pass

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    free_ride=Free_ride()
    free_ride.draw()
    free_ride.update()

    pg.display.flip()
    clock.tick(fps)

#ПРОБЛЕМА №1: нельзя использовать while, из-за чего не работает ускорение машины
#ПРОБЛЕМА №2: моенты не двигаются