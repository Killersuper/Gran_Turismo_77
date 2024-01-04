import random
import pygame as pg
import time

pg.init()
fps = 60
clock = pg.time.Clock()
size=(1500,750)
screen = pg.display.set_mode(size)
pg.display.set_caption("Gran Khidirismo")
lines=[375,525,675,825,975,1125]




def load_image(file,width,height):
    image= pg.image.load(file)
    image=pg.transform.scale(image,(width,height))
    return image

class Car: 
    def __init__(self):
        self.car_image= load_image('images/Yellow.png',120,240)
        self.rect_car=self.car_image.get_rect()
        self.rect_car.center=(size[0]//2,size[1]-size[1]//4)
    def update(self):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_d] and self.rect_car.x<1070:
            self.rect_car.x += 20

        if self.keys[pg.K_a] and self.rect_car.x>310:
            self.rect_car.x -= 20


    def draw(self):
        screen.blit(self.car_image,self.rect_car)


class Coin(pg.sprite.Sprite):
    def __init__(self,speed, number):
        self.speed=speed
        self.number=number
        self.coin_image=load_image('images/money.png',50,50)
        self.rect_coin=self.coin_image.get_rect()
        self.rect_coin.center=(lines[random.randint(0,5)],0)

    def update(self):
        self.rect_coin.y+=self.speed

    def draw(self):
        screen.blit(self.coin_image,self.rect_coin)
    
    def faster(self):
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_w]:
            self.speed+=self.number
        elif self.keys[pg.K_s]:
            self.speed-=self.number
        elif self.keys[pg.K_SPACE] and self.speed>0:
            self.speed-=self.number
        
        
class Road:
    def __init__(self,speed):
        self.speed=speed
        self.race=pg.Rect(300, 0, 900, 750)
        self.line_1=pg.Rect(450,-135,15,135)
        self.line_2=pg.Rect(600,-135,15,135)
        self.line_3=pg.Rect(750,-135,15,135)
        self.line_4=pg.Rect(900,-135,15,135)
        self.line_5=pg.Rect(1050,-135,15,135)
        self.all_lines=[self.line_1,self.line_2,self.line_3,self.line_4,self.line_5]

    def update(self):
        for line in self.all_lines:
            line.y += self.speed

    def draw(self):
        pg.draw.rect(screen, pg.Color(182, 187, 193), self.race)
        self.wall_l=pg.draw.line(screen, pg.Color('black'), (300, 0), (300, 750), 6)
        self.wall_r=pg.draw.line(screen, pg.Color('black'), (1200, 0), (1200, 750), 6)
        
        for line in self.all_lines:
            pg.draw.rect(screen, pg.Color('white'), line)

class Free_ride_1: # СОБИРАТЬ МОНЕТКИ
    pass

class Racing_2: # ГОНКИ
    pass

sp_coin=[]
sp_road=[]

car=Car()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill(pg.Color(52, 143, 26))

    for road in sp_road:
        road.update()
        road.draw()
    
    if random.randint(1,50)==5:    
        r=Road(5)
        sp_road.append(r)

    print(len(sp_road))

    for coin in sp_coin:
        coin.update()
        coin.draw()
        coin.faster()

    if random.randint(1,20)==5:
        c=Coin(2,1)       
        sp_coin.append(c)







    car.update()
    car.draw()

    pg.display.flip()
    clock.tick(fps)