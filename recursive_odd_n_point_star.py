#!/usr/bin/python
# Recursive Odd Pointed Stars

import turtle
import math

turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()

def odd_star(side, i=0, n=5, p=5):

    ang0 = (360.0 / p) # interior angle of the n sided polygon
    ang1 = ang0 * 2.0
    ang2 = 90 - ( ang0 / 2 )
    ang3 = - ( ang0 - ( 2 * ang2 ))

    if (n  > 0):
        turtle.forward(side)
        if ( i > 0):
            turtle.left( ang3 )
            odd_star( side/2.5 , i-1, p, p)
            turtle.right( ang3 )
        turtle.right( ang1 )
        odd_star(side, i, n -1 , p)

side=200
recurse=5
sides=5
points=sides

odd_star(side, recurse, sides, points)

turtle.exitonclick()
