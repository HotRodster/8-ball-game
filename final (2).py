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
    win = GraphWin("Pool", WIDTH,HEIGHT)
    win.yUp()    

    
    dim,holes = drawTable(win)
    playGame(win,dim,holes)
    win.getMouse()
    win.close()


def checkHole(holes,balls,velocities):
    bottomh = [holes[0],holes[1],holes[2]]
    toph = [holes[3],holes[4],holes[5]]
    radius = balls[0].getRadius()
    hr = holes[0].getRadius()
    n = 0
    s = 2
    for ball in balls:
        x = ball.getCenter().getX()
        y = ball.getCenter().getY()
        for hole in toph:
            hx = hole.getCenter().getX()
            hy = hole.getCenter().getY()
            if x - radius >= hx - hr - s and x + radius <= hx + hr +s:
                if y > hy - radius:
                    ball.undraw()
                    del balls[n]
                    del velocities[n]
        for hole in bottomh:
            hx = hole.getCenter().getX()
            hy = hole.getCenter().getY()
            if x - radius >= hx - hr - s and x + radius <= hx + hr + s:
                if y < hy + radius:
                    ball.undraw()
                    del balls[n]
                    del velocities[n]
        n += 1
    return balls,velocities



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
    holes = [pocket1, pocket2, pocket3, pocket4, pocket5, pocket6]
    return [x0,y0,xf,yf], holes
    
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
                        v1 = (v1x0**2 + v1y0**2)**0.5
                        v2 = (v2x0**2 + v2y0**2)**0.5
                        m1 = (newY - y) / (newX - x)
                        if m1 == 0:
                            v1x = v2x0
                            v1y = v2y0
                            v2x = v1x0
                            v2y = v1y0
                        elif v1 == 0:
                            m2 = -1/m1
                            a2 = math.atan(m2)
                            a1 = math.atan(m1)
                            v2 /= 2
                            v1 = v2
                            v1y = v1 * math.sin(a1)
                            v1x = v1 * math.cos(a1)
                            v2y = v2 * math.sin(a2)
                            v2x = v2 * math.cos(a2)
                        elif v2 == 0:
                            m2 = -1/m1
                            a2 = math.atan(m2)
                            a1 = math.atan(m1)
                            v1 /= 2
                            v2 = v1
                            v1y = v1*math.sin(a1)
                            v1x = v1*math.cos(a1)
                            v2y = v2*math.sin(a2)
                            v2x = v2*math.cos(a2)
                        else:
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

def checkTouch(start,balls):
    for ball in balls:
        x 
"""
def checkTouch(balls,radius):
    num = 0
    for j in range(len( balls )):
        x = balls[j].getCenter().getX()
        y = balls[j].getCenter().getY()
        for i in range(len(balls)):
            if i != j:
                newX = balls[i].getCenter().getX()
                newY = balls[i].getCenter().getY()
                distance = ((x-newX)**2 + (y-newY)**2)**0.5
                if distance <= 2*radius:
                    return True
        #num += 1
    return False
"""
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

    balls = [main,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    return balls

def findVelocity(ball,win):
    point = win.getMouse()
    x0 = ball.getCenter().getX()
    xf = point.getX()
    y0 = ball.getCenter().getY()
    yf = point.getY()

    vx = xf - x0
    vy = yf - y0
    return vx,vy

def checkWall(ball,dim):
    x = ball.getCenter().getX()
    y = ball.getCenter().getY()
    radius = ball.getRadius()
    if x + radius >= dim[2] or x - radius <= dim[0]:
        return True

    if y + radius >= dim[3] or y - radius <= dim[1]:
        return True

def changeWall(ball,dim,velocities,num):
    x = ball.getCenter().getX()
    y = ball.getCenter().getY()
    radius = ball.getRadius()
    while x + radius >= dim[2]:
        x = ball.getCenter().getX()
        y = ball.getCenter().getY()
        if velocities[num][0] > 0:
            velocities[num][0] *= -1
        else:
            ball.move(velocities[num][0],velocities[num][1])
    while x - radius <= dim[0]:
        x = ball.getCenter().getX()
        y = ball.getCenter().getY()
        if velocities[num][0] < 0:
            velocities[num][0] *= -1
        else:
            ball.move(velocities[num][0],velocities[num][1])
    while y + radius >= dim[3]:
        x = ball.getCenter().getX()
        y = ball.getCenter().getY()
        if velocities[num][1] > 0:
            velocities[num][1] *= -1
        else:
            ball.move(velocities[num][0],velocities[num][1])
    while y - radius <= dim[1]:
        x = ball.getCenter().getX()
        y = ball.getCenter().getY()
        if velocities[num][1] < 0:
            velocities[num][1] *= -1
        else:
            ball.move(velocities[num][0],velocities[num][1])

    return velocities


def oneRound(balls,vx0,vy0,a,dim,holes,radius):
    velocities = [[vx0/TIMEMOD,vy0/TIMEMOD],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
                  [0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    value = 40
    while value != 0:
        if checkTouch(balls,radius):
            velocities = check(balls,velocities,dim)
            p = 0
            while checkTouch(balls,radius):
                num = 0
                for ball in balls:
                    if velocities[num][0] != 0 or velocities[num][1] != 0:
                        if checkWall(ball,dim):
                            velocities = changeWall(ball,dim,velocities,num)
                        else:
                            ball.move(velocities[num][0],velocities[num][1])
                            checkHole(holes,balls,velocities)
                    
                
                    num +=1
        else:
            num = 0
            for ball in balls:
                if velocities[num][0] != 0 or velocities[num][1] != 0:
                    if checkWall(ball,dim):
                        velocities = changeWall(ball,dim,velocities,num)
                    else:
                        ball.move(velocities[num][0],velocities[num][1])
                        checkHole(holes,balls,velocities)
                
                num +=1


        value = 0
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
                value += (v[0] + v[1])
    print "DONE"
    
def playGame(win,dim,holes):
    balls = drawBalls(win)
    radius = (1.125/114)*WIDTH
    a = 0.05*9.8/TIMEMOD**2
    
    while len(balls) != 1:
        vx0, vy0 = findVelocity(balls[0],win)
        oneRound(balls,vx0,vy0,a,dim,holes,radius)
        

if __name__ == "__main__":
    main()
