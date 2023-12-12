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

# self.dog_image=load_image('images/dog.png',dog_width,dog_height)
# self.screen.blit(self.happiness_image, (padding,padding))

car = pg.image.load('images/White.png')
c = pg.transform.scale(car, (120,240))
x_c=(size[0]) // 2
y_c=(size[1]+400) // 2
c_rect=c.get_rect(center = (x_c,y_c))


# character=pg.image.load('Character.png')
# a=pg.transform.scale(character,(200,400))
# a_rect= character.get_rect(center = (size[1]// 2, size[1]// 2))
race=pg.Rect(300,0, 900, 750)
line_1=pg.Rect(450,500,15,135)
line_2=pg.Rect(600,500,15,135)
line_3=pg.Rect(750,500,15,135)
line_4=pg.Rect(900,500,15,135)
line_5=pg.Rect(1050,500,15,135)
lines=[line_1,line_2,line_3,line_4,line_5]
money=pg.Rect(0,0,70,25)
speed_car=30
gran=Race(line_1,line_2,line_3,line_4,line_5,money,speed_car)
m=random.randint(1,2)

f_speed=pg.font.Font('font.otf', 50) 
def texter(number,rectx,recty):
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

money_random=[375,525,675,825,975,1125]
money_random.append(random.randint(335,1000))
for i in range(500):
#     if money_random[i] >1200:
#         money_random[i]-random.randint(300,450)
#     elif money_random[i] <300:
#         money_random[i]+random.randint(300,450)
    money_random.append(money_random[random.randint(0,5)])

point=0

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
    # pg.draw.rect(screen, pg.Color('white'), line_5)


    keys = pg.key.get_pressed()
    if line_1.y>200:
            for i in lines:
                a=0
                for g in range(1000):  #g можно испльзовать как счетчик метров 
                    a+=335
                    line_x=pg.Rect(i.x,line_1.y-a,15,135)
                    if line_x.y<size[1] and line_x.y>-150:
                        pg.draw.rect(screen,pg.Color('white'),line_x)
    # if line_1.y>200:
    #     a=0
    #     for g in range(1000):
    #         a+=335
    #         line_copy_1=pg.Rect(450,line_1.y-a,15,135)
    #         line_copy_2=pg.Rect(600,line_1.y-a,15,135)
    #         line_copy_3=pg.Rect(750,line_1.y-a,15,135)
    #         line_copy_4=pg.Rect(900,line_1.y-a,15,135)
    #         line_copy_5=pg.Rect(1050,line_1.y-a,15,135)
    #         if line_copy_1.y<750 and line_copy_1.y>-150:
    #             pg.draw.rect(screen, pg.Color('white'), line_copy_1)
    #             pg.draw.rect(screen, pg.Color('white'), line_copy_2)
    #             pg.draw.rect(screen, pg.Color('white'), line_copy_3)
    #             pg.draw.rect(screen, pg.Color('white'), line_copy_4)
    #             pg.draw.rect(screen, pg.Color('white'), line_copy_5)
        # b=0
        # for j in money_random:
        #     b += 335  
        #     money_copy = pg.Rect(j, money.y - b, 50,50)
        #     if money_copy.y < 750 and money_copy.y > -150 and not c_rect.colliderect(money_copy):
        #         # pg.draw.rect(screen, pg.Color("green"), money_copy)
        #         pg.draw.ellipse(screen, pg.Color(255,223,0),money_copy)
        #         # print(j)
        #     if c_rect.colliderect(money_copy):
        #         point+=1 


    

    screen.blit(c,c_rect)
    if keys[pg.K_d]:
        c_rect.x += 20
        if c_rect.colliderect(wall_r):
            c_rect.x-=20
    if keys[pg.K_a]:
        c_rect.x -= 20
        if c_rect.colliderect(wall_l):
            c_rect.x+=20
    # if keys[pg.K_s]:
    #     if keys[pg.K_SPACE]:
    #         if speed_car<50:
    #             speed_car+=0.25
    #         elif speed_car<150 and speed_car>=50:
    #             speed_car+=0.05
    #         elif speed_car>=150:
    #             speed_car=150
    #             speed_car+=0.005
    #     else:
    #         if speed_car<5:
    #             speed_car+=2.5
    #         elif speed_car<15:
    #             speed_car+=1.5
    #         elif speed_car<27.5:
    #             speed_car+=0.5
    #         elif speed_car<30:
    #             speed_car+=0.25
    #         else:
    #             speed_car=30
    #     gran.minus()
    # else:
    #     speed_car=0

    if keys[pg.K_w]:
        if keys[pg.K_SPACE]:
            if speed_car<50:
                speed_car+=0.25
                print(speed_car)
            elif speed_car<150 and speed_car>=50:
                speed_car+=0.05
            elif speed_car>=150:
                speed_car=150
        else:
            if speed_car<5:
                speed_car+=2.5
            elif speed_car<15:
                speed_car+=1.5
            elif speed_car<27.5:
                speed_car+=0.5
            elif speed_car<30:
                speed_car+=0.25
            else:
                speed_car=30
        gran.plus(line_1,line_2,line_3,line_4,line_5,money,speed_car)
    else:
        if keys[pg.K_s]:
            if speed_car<100 and speed_car>0:
                speed_car-=1
        gran.plus(line_1,line_2,line_3,line_4,line_5,money,speed_car)

                






    texter('Speed:',200,100) # слово speed
    texter(f'{int(speed_car*2)}',200,150) # скорость
    texter(f'{int(point)}',1340,100) # очки
    pg.display.flip()
    clock.tick(fps)
