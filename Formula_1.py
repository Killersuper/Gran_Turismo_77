import random
import pygame as pg
import time
from sprite import *
pg.init()

size=(1500,750)
screen = pg.display.set_mode(size)
pg.display.set_caption("Gran Turismo 7")
fps = 60
clock = pg.time.Clock()

car = pg.image.load('Yellow.png')
car_enemy_1 = pg.image.load('White.png')
car_enemy_2 = pg.image.load('Orange.png')
car_enemy_3 = pg.image.load('Green-yellow.png')
car_enemy_4 = pg.image.load('Green.png')
car_enemy_5 = pg.image.load('Red.png')


c = pg.transform.scale(car, (120,240))
c_enemy_1 = pg.transform.scale(car_enemy_1, (120,240))
c_enemy_2 = pg.transform.scale(car_enemy_2, (120,240))
c_enemy_3 = pg.transform.scale(car_enemy_3, (120,240))
c_enemy_4 = pg.transform.scale(car_enemy_4, (120,240))
c_enemy_5 = pg.transform.scale(car_enemy_5, (120,240))



c_rect= car.get_rect(center = (size[0]// 2+430, size[1]// 2+1290))
c_rect_enemy_1= car_enemy_1.get_rect(center = (size[0]// 2+50, size[1]// 2+1050))
c_rect_enemy_2= car_enemy_2.get_rect(center = (size[0]// 2+320, size[1]// 2+1290))
c_rect_enemy_3= car_enemy_3.get_rect(center = (size[0]// 2+620, size[1]// 2+1290))
c_rect_enemy_4= car_enemy_4.get_rect(center = (size[0]// 2+620, size[1]// 2+690))
c_rect_enemy_5= car_enemy_5.get_rect(center = (size[0]// 2+650, size[1]// 2+1050))



# character=pg.image.load('Character.png')
# a=pg.transform.scale(character,(200,400))
# a_rect= character.get_rect(center = (size[1]// 2, size[1]// 2))
race=pg.Rect(300,0, 900, 750)
line_1=pg.Rect(450,500,15,135)
line_2=pg.Rect(600,500,15,135)
line_3=pg.Rect(750,500,15,135)
line_4=pg.Rect(900,500,15,135)
line_5=pg.Rect(1050,500,15,135)
money_test=pg.Rect(size[0] // 2,size[1] // 2,70,25)
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

racers=[c_rect_enemy_1,c_rect_enemy_2,c_rect_enemy_3,c_rect_enemy_4,c_rect_enemy_5]

speed_car=30

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    screen.fill(pg.Color(52, 143, 26))
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
            money_test_copy=pg.Rect(x_money,money_test.y-y_money-a,70,25)
            pg.draw.rect(screen, pg.Color('white'), line_copy_1)
            pg.draw.rect(screen, pg.Color('white'), line_copy_2)
            pg.draw.rect(screen, pg.Color('white'), line_copy_3)
            pg.draw.rect(screen, pg.Color('white'), line_copy_4)
            pg.draw.rect(screen, pg.Color('white'), line_copy_5)
            
        # for i in range(70):
        #     money_test_copy=pg.Rect(size[0] // 2,size[1] // 2,70,25)
        #     pg.draw.rect(screen, pg.Color('green'),money_test_copy)
    screen.blit(c,c_rect)
    screen.blit(c_enemy_1,c_rect_enemy_1)
    screen.blit(c_enemy_2,c_rect_enemy_2)
    screen.blit(c_enemy_3,c_rect_enemy_3)
    screen.blit(c_enemy_4,c_rect_enemy_4)
    screen.blit(c_enemy_5,c_rect_enemy_5)
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

        if c_rect.colliderect(c_rect_enemy_2):
                speedx = 'left' if speedx == 'right' else 'right'
                speedy = 'up' if speedy == 'down' else 'down'
                c_rect_enemy_2.y+=10

        if keys[pg.K_SPACE]:
            if speed_car<50:
                speed_car+=0.25
                c_rect_enemy_1.y-=40
                c_rect_enemy_2.y-=20
                c_rect_enemy_3.y-=70
                c_rect_enemy_4.y-=30
                c_rect_enemy_5.y-=70
            elif speed_car<150 and speed_car>=50:
                speed_car+=0.05
                c_rect_enemy_1.y+=3
                c_rect_enemy_2.y+=10
                c_rect_enemy_3.y+=4
                c_rect_enemy_4.y+=7
                c_rect_enemy_5.y+=5
            elif speed_car>=150:
                speed_car=150
                speed_car+=0.005
                c_rect_enemy_1.y+=5
                c_rect_enemy_2.y+=12
                c_rect_enemy_3.y+=6
                c_rect_enemy_4.y+=9
                c_rect_enemy_5.y+=7
        else:
            c_rect_enemy_1.y-=40
            c_rect_enemy_2.y-=20
            c_rect_enemy_3.y-=70
            c_rect_enemy_4.y-=30
            c_rect_enemy_5.y-=70
            if speed_car<5:
                speed_car+=2.5
            elif speed_car<15:
                speed_car+=1.5
            elif speed_car<27.5:
                speed_car+=0.
            elif speed_car<30:
                speed_car+=0.25
            else:
                speed_car=30
        gran(line_1,line_2,line_3,line_4,line_5,money_test, speed_car)
    else:
        speed_car=0
        c_rect_enemy_1.y-=80
        c_rect_enemy_2.y-=40
        c_rect_enemy_3.y-=140
        c_rect_enemy_4.y-=60
        c_rect_enemy_5.y-=140

                






    speedometr('Speed:',1300,100)
    speedometr(f'{int(speed_car*2)}',1300,150)
    pg.display.flip()
    clock.tick(fps)

















