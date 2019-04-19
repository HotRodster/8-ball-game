"""
Rodney Berryman
CS II
DATE
ASSIGNMENT #

Example
"""
from graphics import*
import math
WIDTH = 654
HEIGHT = 600
def main():
    win = GraphWin("Example", WIDTH,HEIGHT)
    win.yUp()    

    dim = drawTable(win)
    playGame(win,dim)
    win.getMouse()
    win.close()

def drawTable(win):
    x0 = 0
    y0 = HEIGHT/2 - WIDTH*(32/114.0)
    xf = WIDTH
    yf = HEIGHT/2 + (32/114.0)*WIDTH
    rect = Rectangle(Point(x0,y0), Point(xf,yf))
    rect.setFill("brown")
    rect.setOutline("brown")

    x0 = (7/114.0)*WIDTH
    y0 = HEIGHT/2 - WIDTH * (32/114.0) + (7/114.0) * WIDTH
    xf = (107/114.0)*WIDTH
    yf = HEIGHT/2 + (32/114.0) * WIDTH - (7/114.0)*WIDTH
    rect2 = Rectangle(Point(x0,y0),Point(xf,yf))
    rect2.setFill("green")
    rect2.setOutline("green")

    x = x0
    y = y0
    radius = (2.5/114)*WIDTH
    pocket1 = Circle(Point(x,y),radius)
    pocket1.setFill("black")

    x = (xf - x0)/2 + x0
    y = y0
    pocket2 = Circle(Point(x,y),radius)
    pocket2.setFill("black")

    x = xf
    y = y0
    pocket3 = Circle(Point(x,y),radius)
    pocket3.setFill("black")

    x = x0
    y = yf
    pocket4 = Circle(Point(x,y),radius)
    pocket4.setFill("black")
    
    x = (xf - x0)/2 +x0
    y = yf
    pocket5 = Circle(Point(x,y),radius)
    pocket5.setFill("black")
    
    x = xf
    y = yf
    pocket6 = Circle(Point(x,y),radius)
    pocket6.setFill("black")
    
    rect.draw(win)
    rect2.draw(win)
    pocket1.draw(win)
    pocket2.draw(win)
    pocket3.draw(win)
    pocket4.draw(win)
    pocket5.draw(win)
    pocket6.draw(win)
    return [x0,y0,xf,yf]
    
def createBall(x,y,radius,color,win):
    ball = Circle(Point(x,y),radius)
    ball.setFill(color)
    ball.setOutline(color)
    ball.draw(win)
    return ball

def check(balls,velocities,dim):
    """
    num = 0
    for ball in balls:
        for i in range(len(balls)):
            if i != num:
                #check each ball
                #if in contact then change direction and speed
        num += 1
    """         
    x = balls.getCenter().getX()
    y = balls.getCenter().getY()
    radius = balls.getRadius()

    if x + radius >= dim[2] or x - radius <= dim[0]:
        velocities[0] *= -1

    if y + radius >= dim[3] or y - radius <= dim[1]:
        velocities[1] *= -1
    return velocities

def playGame(win,dim):
    x = 327
    y = 300
    #scratc
    radius = (1.125/114)*WIDTH
    color = "white"
    ball = createBall(x,y,radius,color,win)
    v = [3,3]
    point = win.checkMouse()
    while point == None:
        ball.move(v[0],v[1])
        v = check(ball,v,dim)
        time.sleep(1.0/60)
        point = win.checkMouse()
    
    

if __name__ == "__main__":
    main()
