#!/usr/bin/python
# Recursive N point stars

import turtle

turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()

def star_n(size, p=6, n=6, i=0):

    ang1 = 360.0 / p # 60
    ang2 = ang1 * 2  # 120
    ang3 = 180 - (ang1/2)

    if ( n > 0 ):

        turtle.forward( size / 3.0 )

        if ( i > 0 ):
            #print i, “ Recursing turn right ”, ang3
            turtle.right( ang3 )
            star_n(size / 2.5, p, p, i-1)
            turtle.left( ang3 )

        turtle.left( ang2 )
        turtle.forward( size / 3.0 )
        turtle.right( ang1 )
        star_n( size, p, n-1, i)

size = 200
sides = 5
recurse = 3
points = sides

star_n(size, sides , points, recurse)

turtle.exitonclick()
