#!/usr/bin/python
# Adventures In Python - Koch Curve 1

import turtle
screen = turtle.getscreen()
screen.screensize = (1500,1000)

turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()

def draw_koch(l, i=0):
    if( i > 0 ):
        draw_koch(l, i-1)
        turtle.forward(l)
    turtle.left(60)
    if( i > 0 ):
        draw_koch(l, i-1)
        turtle.forward(l)
    turtle.right(120)
    if( i > 0 ):
        draw_koch(l, i-1)
        turtle.forward(l)
    turtle.left(60)
    if( i > 0 ):
        draw_koch(l, i-1)


turtle.penup()
turtle.setx(-900)
turtle.sety(-300)
turtle.pendown()
turtle.width(2)#

length = 5
recurse = 5
draw_koch(length, recurse)

turtle.exitonclick()
