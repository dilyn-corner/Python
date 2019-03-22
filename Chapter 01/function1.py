def drawFunction1(myTurtle,maxSide):
    for x in range(1,maxSide):
        myTurtle.forward(x)
        myTurtle.left(90)
        myTurtle.forward(x**2)
        myTurtle.right(90)

