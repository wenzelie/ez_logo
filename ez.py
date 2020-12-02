from turtle import *

pensize(20)
speed(0)
hideturtle()

def ez(s):
    penup()
    goto(0,0)
    pendown()
    right(30)
    forward(s)
    right(120)
    forward(s)
    left(120)
    forward(s)
    right(120)
    forward(2*s)
    left(120)
    forward(s)

if __name__==__main__:
    ez(100)
