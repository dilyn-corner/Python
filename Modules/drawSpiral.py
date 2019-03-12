def drawSpiral(myTurtle,maxSide):
    for sideLength in range(1,maxSide,5):
        myTurtle.forward(sideLength)
        for turnAngle in range(91, 180, 10):
             myTurtle.right(turnAngle)
