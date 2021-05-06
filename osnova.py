from pygame import *
from random import randint

back = (200, 255, 255)
win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        
        if finish != True:
            window.fill(back)
        
    display.update()
    time.delay(25)
   