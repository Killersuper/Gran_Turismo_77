import random
import pygame as pg
import time
from sprite import *
pg.init()

size=(1500,750)
screen = pg.display.set_mode(size)
pg.display.set_caption("Gran Turismo 7")
fps = 0
clock = pg.time.Clock()


car = pg.image.load('Green-yellow.png')
c = pg.transform.scale(car, (120,240))
c_rect= car.get_rect(center = (size[0]// 2+430, size[1]// 2+1290))


# character=pg.image.load('Character.png')
# a=pg.transform.scale(character,(200,400))
# a_rect= character.get_rect(center = (size[1]// 2, size[1]// 2))
race=pg.Rect(300,0, 900, 750)
line_1=pg.Rect(450,500,15,135)
line_2=pg.Rect(600,500,15,135)
line_3=pg.Rect(750,500,15,135)
line_4=pg.Rect(900,500,15,135)
line_5=pg.Rect(1050,500,15,135)
money=pg.Rect(0,0,70,25)
gran=Race
m=random.randint(1,2)

f_speed=pg.font.Font('font.otf', 50) 
def speedometr(number,rectx,recty):
    speed = f_speed.render(number, True, pg.Color('black'))
    speed_rect = speed.get_rect(center=(rectx,recty))
    screen.blit(speed, speed_rect)

if m == 1:
    speedx = 'right'
else:
    speedx = 'left'

if m == 1:
    speedy = 'down'
else:
    speedy = 'up'

y_money=random.randint(335,1000)
x_money=random.randint(350,1150)

money_random=[]
for i in range(500):
    money_random.append(random.randint(335,1000))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill(pg.Color(81, 141, 240))
    pg.draw.rect(screen, pg.Color(182, 187, 193), race)
    wall_l=pg.draw.line(screen, pg.Color('black'), (300, 0), (300, 750), 6)
    wall_r=pg.draw.line(screen, pg.Color('black'), (1200, 0), (1200, 750), 6)
    pg.draw.rect(screen, pg.Color('white'), line_1)
    pg.draw.rect(screen, pg.Color('white'), line_2)
    pg.draw.rect(screen, pg.Color('white'), line_3)
    pg.draw.rect(screen, pg.Color('white'), line_4)
    pg.draw.rect(screen, pg.Color('white'), line_5)


    keys = pg.key.get_pressed()
    
    if line_1.y>200:
        a=0
        for i in range(1000):
            a=a+335
            line_copy_1=pg.Rect(450,line_1.y-a,15,135)
            line_copy_2=pg.Rect(600,line_1.y-a,15,135)
            line_copy_3=pg.Rect(750,line_1.y-a,15,135)
            line_copy_4=pg.Rect(900,line_1.y-a,15,135)
            line_copy_5=pg.Rect(1050,line_1.y-a,15,135)
            if line_copy_1.y<750 and line_copy_1.y>-150:
                pg.draw.rect(screen, pg.Color('white'), line_copy_1)
                pg.draw.rect(screen, pg.Color('white'), line_copy_2)
                pg.draw.rect(screen, pg.Color('white'), line_copy_3)
                pg.draw.rect(screen, pg.Color('white'), line_copy_4)
                pg.draw.rect(screen, pg.Color('white'), line_copy_5)
        b=0
        for j in money_random:
            b=b+335  
            money_copy=pg.Rect(j,money.y-b,50,50)
            if money_copy.y<750 and money_copy.y>-150 and not c_rect.colliderect(money_copy):
                pg.draw.ellipse(screen, pg.Color(255,223,0),money_copy)


    

    screen.blit(c,c_rect)
    # pg.draw.rect(screen, pg.Color('red'),test)
    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        c_rect.x += 20
        # if c_rect.colliderect(wall_r):
        #     c_rect.x-=20
    if keys[pg.K_a]:
        c_rect.x -= 20
        # if c_rect.colliderect(wall_l):
        #     c_rect.x+=20
    if keys[pg.K_w]:
        if keys[pg.K_SPACE]:
            if fps<100:
                fps+=0.5
            elif fps<300 and fps>=100:
                fps+=0.1
            elif fps>=300:
                fps=300
                fps+=0.01
        else:
            if fps<10:
                fps+=5
            elif fps<30:
                fps+=3
            elif fps<45:
                fps+=1
            elif fps<60:
                fps+=0.5
            else:
                fps=60
        gran(line_1,line_2,line_3,line_4,line_5,money)
    else:
        fps=0

                






    speedometr('Speed:',1300,100)
    speedometr(f'{int(fps)}',1300,150)
    pg.display.flip()
    clock.tick(fps)
