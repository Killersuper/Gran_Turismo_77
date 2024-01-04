# import random
# class Coins:
#     def __init__(self):
#         self.coins_image=load_image('images/money.png',50,50)
#         self.rect_coins=self.coins_image.get_rect()
#         self.rect_coins.center=(size[0]//2,size[1]//2)

#     def update(self):
#         self.l=[375,525,675,825,975,1125]
#         self.c=0
#         for f in range(1000):
#             self.c+=335
#             self.rect_coins=self.coins_image.get_rect()
#             self.rect_coins.center=(self.l[random.randint(0,5)],size[1]-self.c)
#             if self.rect_coins[1]<size[1] and self.rect_coins[1]>-150:
#                 screen.blit(self.coins_image,self.rect_coins)
# class Toy(pg.sprite.Sprite):
#     def __init__(self):
#         pg.sprite.Sprite.__init__(self)
#         self.toy1_image=load_image('images/toys/blue bone.png', TOY_SIZE,TOY_SIZE)
#         self.toy2_image=load_image('images/toys/red bone.png',TOY_SIZE,TOY_SIZE)
#         self.toy3_image=load_image('images/toys/ball.png',TOY_SIZE,TOY_SIZE)
#         self.toys=[self.toy1_image,self.toy2_image,self.toy3_image]
#         self.image=self.toys[random.randint(0,2)]
#         self.rect = self.image.get_rect()
#         n=random.randint(130,SCREEN_WIDTH-130)
        
#         self.rect.center = [n,0]

#         self.speed=random.randint(1,5)
#     def update(self):
#         # print(1)

#         self.rect.y+=self.speed

#     def draw(self,screen):
#         screen.blit(self.image, self.rect) 
        

        # class Coins:
#     def __init__(self):
#         self.coins_image=load_image('images/money.png',50,50)
#         self.rect_coins=self.coins_image.get_rect()
#         self.rect_coins.center=(size[0]//2,size[1]//2)

#     def update(self):
#         self.l=[375,525,675,825,975,1125]
#         self.c=0
#         for f in range(1000):
#             self.c+=335
#             self.rect_coins=self.coins_image.get_rect()
#             self.rect_coins.center=(self.l[random.randint(0,5)],size[1]-self.c)
#             if self.rect_coins[1]<size[1] and self.rect_coins[1]>-150:
#                 screen.blit(self.coins_image,self.rect_coins)



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
color=['red', 'white', 'black', 'green', 'blue']



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
        if self.keys[pg.K_d]:
            self.rect_car.x += 20
            # if self.rect_car.colliderect(self.wall_r):
            #     self.rect_car.x-=20
        if self.keys[pg.K_a]:
            self.rect_car.x -= 20
            # if self.rect_car.colliderect(self.wall_l):
            #     self.rect_car.x+=20

class Coin(pg.sprite.Sprite):
    def __init__(self,speed):
        self.speed=speed

        self.coin_image=load_image('images/money.png',50,50)
        self.rect_coin=self.coin_image.get_rect()
        self.rect_coin.center=(lines[random.randint(0,5)],0)

    def update(self):
        self.rect_coin.y+=self.speed

    def draw(self):
        screen.blit(self.coin_image,self.rect_coin)

        
        
class Road:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
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
            pg.draw.rect(screen, pg.Color(self.color), line)

class Free_ride_1: # СОБИРАТЬ МОНЕТКИ
    pass

class Racing_2: # ГОНКИ
    pass

sp_coin=[]
sp_road=[]

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
        r=Road(5,color[random.randint[0,4]])
        sp_road.append(r)


    for coin in sp_coin:
        coin.update()
        coin.draw()

    if random.randint(1,100)==5:
        c=Coin(2)       
        sp_coin.append(c)

    pg.display.flip()
    clock.tick(fps)