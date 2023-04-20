import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,R=255,G=0,B=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = R
        self.G = G
        self.B = B
        
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else:
            return False

  



pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
# firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

# while(run):
#     screen.fill((255, 255, 255))
#     if btn.isMouseOn():
#         btn.w = 200
#         btn.h = 300
#     else:
#         btn.w = 100
#         btn.h = 100
#     btn.draw(screen)
    
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False

#Exercise 1 ---------------------------------------------------
while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0] :
            btn.R = 75
            btn.G = 0
            btn.B = 130
        else:
            btn.R = 105
            btn.G = 105
            btn.B = 105
    else:
        btn.R = 225
        btn.G = 0
        btn.B = 0
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False



