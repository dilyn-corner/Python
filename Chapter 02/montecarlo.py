import math 
import random
import turtle

def montePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2,-2,2,2)

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    inCircle=0
    drawingT.up()
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x**2 + y**2)

        drawingT.goto(x,y)
        
        if d<=1:
            inCircle = inCircle+1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = inCircle/numDarts * 4

    wn.exitonclick()

    return pi 
