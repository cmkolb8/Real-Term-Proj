import math

def projectile(mode, count, power, canvas): 
    #setting up variables needed to calucate x and y pos 
    yAccel = -9.8
    initialV = 10 * power 
    degAngle = (count) * 3 
    angle = math.pi / 180 * (degAngle)
    time = 0
    Vy = initialV * math.sin(angle)
    Vx = initialV * math.cos(angle)
    totalTime = abs((2 * (Vy/ yAccel)))
    loop = 8
    while(time <= totalTime / 2):
        #x and y pos 
        yPos = mode.midY - 20 - 10 * (mode.count) + Vy * (time * 100) - yAccel * (time * 100) ** 2 / 2
        xPos = mode.midX + 35 + 1 * (mode.count) + Vx * time * 100
        if(yPos + loop < mode.midY + 50 - 10 * (mode.count)):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'white')
        time += .01
        loop += .1
    while(time > 0):
        yPos = mode.midY - 12 - 10 * (mode.count) - Vy * (time * 75) - yAccel * (time * 75) ** 2 / 2
        xPos = mode.midX + 30 - (mode.count / 2)- Vx * time * 15
        if(yPos + loop < mode.height / 2 - 10):
            canvas.create_oval(xPos - loop, yPos - (loop - 3), xPos + loop, yPos + loop, fill = 'white')
        time -= .01
        if(loop > 5): 
            loop -= .15

    
