import sys
sys.path.append('C:/Users/Joseph H. Hendrickso/AppData/Local/Programs/Python/Python37/Tools')
sys.path.append('C:/Users/Joseph H. Hendrickso/Documents/python')
from joe_turtle_utilities import *
from graphics import *
from turtle import *
import random 
import math

def draw_square(size,x,y):
    up()
    goto(x,y)
    seth(90)
    width(1)
    color("green")
    down()
    begin_fill()
    fd(size)
    seth(0)
    fd(size)
    seth(-90)
    fd(size)
    seth(180)
    fd(size)
    end_fill()



def draw_balls(x1,x2,y):
    up()
    goto (x1,y)
    seth(90)
    color("yellow")
    down()
    begin_fill()
    circle(20)
    end_fill()
    up()
    goto (x2,y)
    seth(-90)
    color("yellow")
    down()
    begin_fill()
    circle(20)
    end_fill()
    


def ornament(x,y,rad):
    
    up()
    #goto(-300-50,200)
    goto(x-rad,y)
    seth(-90)
    down()
    begin_fill()
    color("blue")
    circle(50)
    end_fill()

    


    #snowflake(4, 6, -300, 200)
    snowflake(rad*8/110, 6, x, y)

    up()
    goto(x,y+rad)
    down()
    color("white")
    seth(90)
    fd(400)
  
 




def main():
    st()
    mkscreen([-500,-500],[500,500])
    home()
    clear()
    bgcolor("black")
    ht()

 

    ornament(-300,200,50)
    ornament(-150,200,50)
    ornament(-450,300,50)



    
    box_size = 100
    x = -500 + 2*box_size
    y = -500
    x1 = x
    
    for i in range(6):
        draw_square(box_size,x,y)
        x = x + box_size
    
    draw_balls(x1,x,y+box_size)
    
    x = -500 + 3*box_size
    y = -500 + box_size
    x1 = x
    
    
    for i in range(4):
        draw_square(box_size,x,y)
        x = x + box_size
    
    draw_balls(x1,x,y+box_size)
    
        
    x = -500 + 3.5*box_size
    y = -500 + 2*box_size
    x1 = x
    
    for i in range(3):
        draw_square(box_size,x,y)
        x = x + box_size
    
    draw_balls(x1,x,y+box_size)
    
    x = -500 + 4*box_size
    y = -500 + 3*box_size
    x1 = x
    
    for i in range(2):
        draw_square(box_size,x,y)
        x = x + box_size
    
    draw_balls(x1,x,y+box_size)
    
    x = -500 + 4.5*box_size
    y = -500 + 4*box_size
    x1 = x
    
    for i in range(1):
        draw_square(box_size,x,y)
        x = x + box_size
    
    draw_balls(x1,x,y+box_size)
    
    star_size = 100
    x = x1 + 0.5*box_size -10
    y = -500 + 5*box_size+star_size
    
    up()
    goto(x,y)
    down()
    draw_star(star_size)



  

main()


