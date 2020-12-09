import math
import enemy
from pygame import mixer

def projectile(mode, count, power, canvas): 
    #setting up variables needed to calucate x and y pos 
    yAccel = -9.8
    initialV = 10 
    degAngle = (count) * 3 
    angle = math.pi / 180 * (degAngle)
    time = 0
    Vy = initialV * math.sin(angle)
    Vx = initialV * math.cos(angle)
    totalTime = abs((2 * (Vy/ yAccel)))
    loop = 8
    xDist = Vx * totalTime * 24
    ovals = list()
    current = 1 
    newTime = 0
    while(time <= totalTime / 2):
        #x and y position on way up 
        yPos = mode.midY - 20 - 10 * (mode.count) + Vy * (time * 100) - yAccel * (time * 100) ** 2 / 2
        xPos = mode.midX + 35 + 1 * (mode.count) + Vx * time * 100
        if(yPos + loop < mode.midY + 50 - 10 * (mode.count)):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'white')
            ovals.append((xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop))
        time += .01
        loop += .1
    while(time > 0):
        #x and y position on way down 
        yPos = mode.midY - 12 - 10 * (mode.count) - Vy * (time * 75) - yAccel * (time * 75) ** 2 / 2
        xPos = mode.midX + 30 - (mode.count / 2) - Vx * time * 15
        if(yPos + loop < mode.height / 2 - 10):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'white')
            ovals.append((xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop))
        time -= .01
        if(loop > 5): 
            loop -= .15
        return(xPos)

def checkBlock(mode, count):
    #calculates which block is hit based on the count and turn 
    row = count
    col = mode.turn
    for i in range(-10, 10):
        r = row + i
        for j in range(-10, 10):
            c = col + j
            if(24 > r >= 0 and 24 > c >= 0):    
                if(mode.map[r][c] == 1):
                    mode.hit = True
                    mode.map[r][c] = 0
                    mode.myScore -= 1
    row = count  
    col = mode.turn
    if(0 > col  or col > 23 or 0 > row  or row > 23):
        pass
    elif(mode.map[row][col] == 6):
        mode.map[row][col] = 0
    if(mode.myScore == 0):
        mode.win == True
    return(row, col)

def calculateXY(mode, xy, count):
        spot = checkBlock(mode, count)
        current = 0
        smallest = enemy.dist(spot[0], spot[1], mode.enemySold[0][0], mode.enemySold[0][1])
        xDist = abs(spot[0] - mode.enemySold[0][0])
        yDist = abs(spot[1] - mode.enemySold[0][1])
        for i in range(len(mode.enemySold)): 
            temp = enemy.dist(spot[0], spot[1], mode.enemySold[i][0], mode.enemySold[i][1])
            if(temp < smallest):
                smallest = temp
                current = i 
                xDist = abs(spot[0] - mode.enemySold[i][0])
                yDist = abs(spot[1] + mode.enemySold[i][1])
        return (xDist, yDist)