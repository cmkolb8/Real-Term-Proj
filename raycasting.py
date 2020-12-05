import math 
import random
import shotGun
from tkinter import * 
import projectile 
import blockOption
import enemy

#algorithm learned from https://lodev.org/cgtutor/raycasting3.html 
def drawRayCaster(mode, canvas):
    for x in range(mode.width):
        xMap = int(mode.xPos)
        yMap = int(mode.yPos)
        hit = 0 
        xCamera = 2.0 * x / mode.width - 1.0
        xRayDir = mode.xDir + xCamera * mode.xCameraPlane 
        yRayDir = mode.yDir + xCamera * mode.yCameraPlane + .0000001 #so don't divde by zero
        #calculate distance to next x and y edge (sqaure border)
        xDeltaDist = math.sqrt(1.0 + (yRayDir * yRayDir) / ((xRayDir * xRayDir)))
        yDeltaDist = math.sqrt(1.0 + (xRayDir * xRayDir) / ((yRayDir * yRayDir)))
        
        #calculate the steps (which direction to go in) and the initall distance 
        #x and y distance of the ray 
        if (yRayDir < 0):
            ySideDist = (mode.yPos - yMap) * yDeltaDist  
            yStep = -1        
        else: 
            ySideDist = (yMap + 1.0 - mode.yPos) * yDeltaDist
            yStep = 1

        if(xRayDir < 0):
            xSideDist = (mode.xPos - xMap) * xDeltaDist 
            xStep = -1

        else: 
            xSideDist = (xMap + 1.0 - mode.xPos) * xDeltaDist 
            xStep = 1
            
        while(hit == 0):
            #go to next map square in x or y direction 
            if(xSideDist > ySideDist):
                side = True 
                ySideDist += yDeltaDist
                yMap += yStep

            else: 
                side = False
                xSideDist += xDeltaDist
                xMap += xStep

                #check if ray has hit the wall
            if(mode.map[xMap][yMap] > 0):
                    hit = 1

            #(xMap - mode.xPos + (1 - xStep / 2) = number of sqaures the ray has crossed in x dir 
            #calculates distance projected on camera direction (simply using the perpindicualar to the camera plane)
            if (side == False):
                perpWallDist = (xMap - mode.xPos + (1.0 - xStep) / 2.0) / xRayDir
            else: 
                perpWallDist = (yMap - mode.yPos + (1.0 - yStep) / 2.0) / yRayDir
            
            lineHeight = abs(int(mode.height  / (perpWallDist + .0000001)))
            start = -1 * lineHeight / 2.0 + mode.height / 2.0
            otherStart = -2 * lineHeight / 2.0 + mode.height / 2.0
            end = lineHeight / 2.0 + mode.height / 2.0
            otherEnd = lineHeight / 4.0 + mode.height / 4.0
            if(start < 0):
                start = 0 
            if(end >= mode.height):
                end = mode.height - 1
            
            #colors 
            posColors = [[0,0,0], [0, 100, 0], [150, 0 ,0], [0,100, 100], [0,150,0], [100,30, 100], [150, 0 ,0], [0,0,150]]
            color = posColors[mode.map[xMap][yMap]]
            #picks the right color of each spot on the map 
            if(side == True):
                for i, j in enumerate(color):
                        color[i] = int(j / 2)
            col = '#%02x%02x%02x' % (color[0], color[1], color[2])
            if(mode.map[xMap][yMap] == 5):
                canvas.create_line(x, start - 10, x, end, fill = col)
            else:
                canvas.create_line(x, start, x, end, fill = col)

#is called when mouse is pressed to shoot 
def possible(mode, canvas):
    #draws the enemy's blocks
    if(mode.begin == False):
        blockOption.drawBlock(mode, canvas)

    #calls the draw function for the tank 
    if(mode.begin == True):
        shotGun.bottomTank(mode, canvas)
        shotGun.shotGun(mode, canvas)
        shotGun.powerBar(mode, canvas)
        canvas.create_text(400, 50, text = mode.myScore, fill = 'white', font='Times 26 bold')

    #called when user presses f 
    if(mode.fire):
        three = False 
        while(not three):
            ang = random.randint(3, 70)
            if(ang % 3 == 0):
                three = True
        count = random.randint(2, 24)
        direc = False 
        while(not direc):
            xy = random.randint(-1, 1)
            if(xy != 0):
                direc = True
        while(mode.timer < 15):
            #class projectile draw 
            projectile.projectile(mode, mode.count, mode.power, canvas)
            enemy.outProjectile(mode, ang, count, xy, canvas)
            mode.timer += 1
        #shoots ball
        enemy.shoot(mode, xy, count)
        projectile.checkBlock(mode, mode.count)
        mode.timer = 0
        mode.fire = False 

    canvas.update()