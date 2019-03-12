def drawPolygon(myTurtle,sideLength,numSides):
    turnAngle=360/numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
def drawCircle(myTurtle,radius):
    circumference = 2*3.1415*radius
    myTurtle.up
    myTurtle.left(90)
    myTurtle.forward(radius)
    myTurtle.right(90)
    myTurtle.down
    circumference = 2*3.1415*radius
    sideLength = circumference/360
    drawPolygon(myTurtle,sideLength,360)

