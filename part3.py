import sys
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,R=0,G=0,B=0):
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

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.info = self.text
                    self.text = ''

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def showinfo(self):
        return self.info
    
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class InputBox_age:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.error_displayed = False
        self.error_display_time = 0


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.info = self.text
                    self.text = ''
                    if not self.info.isnumeric():
                        self.error_displayed = True
                        self.error_display_time = pg.time.get_ticks()

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
                


    def showinfo(self):
        if not self.info.isnumeric():
            self.info = " ERROR "
        return self.info

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        if self.error_displayed:
            error = font.render('ERROR please enter number', True, (0,0,0))
            current_time = pg.time.get_ticks()
            if current_time - self.error_display_time < 5000:  # Display error for 5 seconds
                screen.blit(error, (440,250))
            else:
                self.error_displayed = False




run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))


font = pg.font.Font('freesansbold.ttf', 20) # font and fontsize
# text = font.render('FRA 142', True, (255, 255, 255), (0,0,0)) # (text,is smooth?,letter color,background color)
# textRect = text.get_rect() # text size
# textRect.center = (win_x // 2, win_y // 2)

COLOR_INACTIVE = pg.Color(230, 126, 34) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 130, 140, 32) # สร้าง InputBox1
input_box_age = InputBox_age(100, 300, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(475, 130, 140, 32) 
input_boxes = [input_box1, input_box_age, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

switch = 0


# -------------------------------------------


while(run):
    # screen.blit(text, textRect)
    screen.fill((255, 255, 255))


    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    
    Firstname = font.render('First  name', True, (0,0,0), (255, 255, 255))
    screen.blit(Firstname, (100,100))
    Lastname = font.render('Last  name', True, (0,0,0), (255, 255, 255))
    screen.blit(Lastname, (475,100))
    Age = font.render('Age', True, (0,0,0), (255, 255, 255))
    screen.blit(Age, (100,270))



    btn = Button(500,285,150,50) # สร้าง Object จากคลาส Button ขึ้นมา
    btn.R = 39
    btn.G = 174
    btn.B = 96
    btn.draw(screen)

    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0]:
            # showtext = font.render('Hello' +  input_box1.showinfo() + " " + input_box3.showinfo() + "You are" + input_box_age.showinfo() + "years old.", True, (255, 255, 255), (0,0,0))
            # screen.blit(showtext, (100,400))
            switch = 1


    if switch == 1:
        showtext = font.render('Hello  ' +  input_box1.showinfo() + " " + input_box3.showinfo() + "!  You are " + input_box_age.showinfo() + " years old.", True, (0,0,0))
        screen.blit(showtext, (100,400))



    Submit = font.render('Submit', True, (0,0,0))
    screen.blit(Submit, (538,300))

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()