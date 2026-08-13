#!/usr/bin/python
# Sierpinski Triangle

 import turtle
 
 turtle.speed(0)
 turtle.hideturtle()
 turtle.delay(0)
 print “Delay ”, turtle.delay()
 
 
 def sierpinski(side, i=1):
     if ( i > 0 ):
         sierpinski(side/2, i-1)
 
     turtle.forward(side)
     turtle.left(120)
 
     if ( i > 0 ):
         sierpinski(side/2, i-1)
 
     turtle.forward(side)
     turtle.left(120)
 
     if ( i > 0 ):
         sierpinski(side/2, i-1)
 
     turtle.forward(side)
     turtle.left(120)
 
 sierpinski(400,6)
 
 turtle.exitonclick()
