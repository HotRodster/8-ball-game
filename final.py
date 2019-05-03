"""
Rodney Berryman
CS II
DATE
ASSIGNMENT #

Example
"""
from graphics import*
import time
import math
WIDTH = 654.0
HEIGHT = 600.0
TIMEMOD = 100
def main():
    win = GraphWin("Example", WIDTH,HEIGHT)
    win.yUp()    

    
    dim = drawTable(win)
    playGame(win,dim)
    win.getMouse()
    win.close()

def drawTable(win):
    brown = color_rgb(101,53,51)
    x0 = 0
    y0 = HEIGHT/2 - WIDTH*(32/114.0)
    xf = WIDTH
    yf = HEIGHT/2 + (32/114.0)*WIDTH
    rect = Rectangle(Point(x0,y0), Point(xf,yf))
    rect.setFill(brown)
    rect.setOutline(brown)

    green = color_rgb(11,135,127)
    x0 = (7/114.0)*WIDTH
    y0 = HEIGHT/2 - WIDTH * (32/114.0) + (7/114.0) * WIDTH
    xf = (107/114.0)*WIDTH
    yf = HEIGHT/2 + (32/114.0) * WIDTH - (7/114.0)*WIDTH
    rect2 = Rectangle(Point(x0,y0),Point(xf,yf))
    rect2.setFill(green)
    rect2.setOutline(green)

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
    savedIndexes = []
    num = 0
    radius = balls[0].getRadius()
    for ball in balls:
        if num not in savedIndexes:
            x = ball.getCenter().getX()
            y = ball.getCenter().getY()
            v1x0 = velocities[num][0]
            v1y0 = velocities[num][1]
            if x + radius >= dim[2] or x - radius <= dim[0]:
                velocities[num][0] *= -1
            if y + radius >= dim[3] or y - radius <= dim[1]:
                velocities[num][1] *= -1
            
            for i in range(len(balls)):
    
                if i != num:
                    v2x0 = velocities[i][0]
                    v2y0 = velocities[i][1]
                    newX = balls[i].getCenter().getX()
                    newY = balls[i].getCenter().getY()
                    distance = ((x-newX)**2 + (y-newY)**2)**0.5
                    if distance <= 2*radius:
                        v1x = v2x0
                        v1y = v2y0
                        v2x = v1x0
                        v2y = v1y0
                        velocities[num][0] = v1x
                        velocities[num][1] = v1y
                        velocities[i][0] = v2x
                        velocities[i][1] = v2y
                        savedIndexes.append(i) 
                    
        num += 1
        
    
    return velocities

def drawBalls(win):
    space = 1.0
    radius = (1.125/114)*WIDTH
    main = createBall(0.28*WIDTH,HEIGHT/2,radius,"white",win)
    b1 = createBall(0.72 *WIDTH, HEIGHT/2,radius,"yellow",win)
    b10 = createBall(b1.getCenter().getX() + 2*radius + space,
                     HEIGHT/2 + radius + space,radius,"blue",win)
    b11 = createBall(b10.getCenter().getX(),HEIGHT/2 - radius - space, radius,
                     "red",win)
    b6 = createBall(b11.getCenter().getX() + 2*radius +space,
                    HEIGHT/2 + 2*radius +space, radius,"green",win) #change to green
    b8 = createBall(b6.getCenter().getX(), HEIGHT/2, radius, "black",win)
    b9 = createBall(b6.getCenter().getX(), HEIGHT/2 -2*radius - space,
                    radius,"yellow",win)
    b5 = createBall(b9.getCenter().getX() + 2*radius + space,
                    HEIGHT/2 - 3*radius - 2*space,radius,"orange",win)
    b12 = createBall(b5.getCenter().getX(), HEIGHT/2 - radius - space, radius,
                     "purple",win)
    b7 = createBall(b5.getCenter().getX(), HEIGHT/2 +radius + space, radius,
                    "brown",win)
    b13 = createBall(b5.getCenter().getX(), HEIGHT/2 + 3*radius +2*space, radius,
                     "orange",win)
    b2 = createBall(b5.getCenter().getX() + 2*radius + space,
                    HEIGHT/2 - 2*radius - space,radius, "blue",win)
    b3 = createBall(b2.getCenter().getX(), HEIGHT/2 + 2*radius + space, radius,
                    "red",win)
    b4 = createBall(b2.getCenter().getX(), HEIGHT/2 + 4*radius + 2*space, radius
                    ,"purple",win)
    b14 = createBall(b2.getCenter().getX(), HEIGHT/2, radius, "green", win) #change to green
    b15 = createBall(b2.getCenter().getX(),HEIGHT/2 - 4*radius - 2*space, radius
                     ,"brown",win)


    return [main,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]

def findVelocity(ball,win):
    point = win.getMouse()
    x0 = ball.getCenter().getX()
    xf = point.getX()
    y0 = ball.getCenter().getY()
    yf = point.getY()

    vx = xf - x0
    vy = yf - y0
    return vx,vy
    

def playGame(win,dim):
    balls = drawBalls(win)
    vx0, vy0 = findVelocity(balls[0],win)
    vx0 /= TIMEMOD
    vy0 /= TIMEMOD
    velocities = [[vx0,vy0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
                  [0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    radius = (1.125/114)*WIDTH
    
    point = win.checkMouse()
    a = 0.005*9.8/TIMEMOD**2
    while point == None:
        num = 0
        for ball in balls:
            ball.move(velocities[num][0],velocities[num][1])
            num += 1
        
        velocities = check(balls,velocities,dim)
        time.sleep(1.0/TIMEMOD)
        for v in velocities:
            if v[0]**2 + v[1]**2 > 0:
                ax = a*v[0]/math.sqrt(v[0]**2 + v[1]**2)
                ay = a*v[1]/math.sqrt(v[0]**2 + v[1]**2)

                if v[0] > 0 and v[0] - ax <0:
                    v[0] = 0
                elif v[0] < 0 and v[0] - ax > 0:
                    v[0] = 0
                else:
                    v[0] -= ax

                if v[1] > 0 and v[1] - ay <0:
                    v[1] = 0
                elif v[1] < 0 and v[1] - ay > 0:
                    v[1] = 0
                else:
                    v[1] -= ay

                  
        
        point = win.checkMouse()
        

if __name__ == "__main__":
    main()
