import math 
import random 

def outProjectile(mode, ang, count, xy, canvas):
    #establishes necessary variables for the physics 
    yAccel = -9.8
    initialV = 10
    angle = math.pi / 180 * (ang)
    Vy = initialV * math.sin(angle)
    Vx = initialV * math.cos(angle)
    totalTime = abs((2 * (Vy/ yAccel)))
    loop = 5
    xDist = Vx * totalTime * 24
    time = totalTime / 2
    current = 0
    newTime = 0
    while(time > 0):
        #physics of x and y pos on way up 
        row = shoot(mode, xy, count)
        yPos = mode.midY - 15 - 10 * (count) - Vy * (time * 75) - yAccel * (time * 75) ** 2 / 2
        xPos =  mode.midX + 60 + xy * (count) + xy * (Vx * time * 15)
        if(yPos + loop < mode.height / 2 - 10):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'red')
        time -= .01
        loop += .025
    while(time <= totalTime / 2):
        #x and y pos on way down
        if(xy < 0):
            yPos = mode.midY - 20 - 10 * (count) + Vy * (time * 100) - yAccel * (time * 100) ** 2 / 2
            xPos = mode.midX + 50 - xy * (count) - xy * (Vx * time * 15)
        else: 
            yPos = mode.midY - 20 - 10 * (count) + Vy * (time * 100) - yAccel * (time * 100) ** 2 / 2
            xPos = mode.midX + 70 - xy * (count) - xy * (Vx * time * 15)
        if(yPos + loop < mode.midY + 125 - 10 * (count)):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'red')
        time += .01
        loop += .1

#randomally shots, used for easy and first shot of hard 
def shoot(mode, xy, count):
    #calculates which block it hits 
    row = count - 1
    if(xy < 0):
        col = random.randint(12, 23)
    else: 
        col = random.randint(1, 12)
    if(mode.map[row][col] == 1):
        mode.map[row][col] = 0
        mode.enemyScore -= 1
    if(mode.enemyScore == 0):
        mode.lose == True
    return (row, col)

#distance formula
def dist(x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2) ** .5

#calculates which soldiers is closest
def calculate(mode, xy, count):
        spot = shoot(mode, xy, count)
        current = 0
        smallest = dist(spot[0], spot[1], mode.soldiers[0][0], mode.soldiers[0][1])
        for i in range(len(mode.soldiers)): 
            temp = dist(spot[0], spot[1], mode.soldiers[i][0], mode.soldiers[i][1])
            if(temp < smallest):
                smallest = temp
                current = i 
        mode.shots += 1
        return i

#shoots second ball at closest soldier during hard mode 
def knownShot(mode, i):
    row = mode.soldiers[i][0]
    col = mode.soldiers[i][1]
    mode.map[row][col] = 0
    mode.enemyScore -= 1
    if(mode.enemyScore == 0):
        mode.lose == True
    mode.shots = 0      
