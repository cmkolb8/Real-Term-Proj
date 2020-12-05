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
        
