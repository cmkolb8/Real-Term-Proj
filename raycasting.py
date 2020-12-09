from cmu_112_graphics import * 
import math 
import random
import shotGun
from tkinter import * 
import projectile 
import blockOption
import enemy
import topView
import stars
from pygame import mixer

#algorithm learned from https://lodev.org/cgtutor/raycasting3.html 
def drawRayCaster(mode, canvas):
    if(mode.top == True):
        topView.topView(mode, canvas)
    elif(mode.myScore == 0 and mode.begin):
            canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
            stars.stars(mode, canvas)
            canvas.create_text(mode.width / 2, mode.height / 2, text = 'Congratulations comrad, you have won the planet!', fill = 'white')
    elif(mode.enemyScore == 0 and mode.begin):
            canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
            stars.stars(mode, canvas)
            canvas.create_text(mode.width / 2, mode.height / 2, text = 'I am sorry, but you have lost the game and given up the hold of Zorga :(', fill = 'white')
    else: 
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
    if(mode.begin == False and mode.top == False):
        #draws the two options of block in lower left 
        blockOption.drawBlock(mode, canvas)
        
    #calls the draw function for the tank 
    if(mode.begin == True and mode.top == False):
        #draws the buttom part of the tank
       shotGun.bottomTank(mode, canvas)
       #draws the shot gun/ thing where the ball comes out of 
       shotGun.shotGun(mode, canvas)
       #draws the powerBar
       shotGun.powerBar(mode, canvas)
       canvas.create_text(400, 50, text = mode.myScore, fill = 'white', font='Times 26 bold')
       canvas.create_text(100, 50, text = mode.enemyScore, fill = 'firebrick4', font = 'Times 26 bold')

    #called when user presses f 
    if(mode.fire and mode.top == False):
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
            #this function draws the player's projectile 
            x = projectile.projectile(mode, mode.count, mode.power, canvas)
            #this function draws the enemey's projectile 
            enemy.outProjectile(mode, ang, count, xy, canvas)
            mode.timer += 1
            mixer.init()
            mixer.Sound.play(mode.cannon)
        if(not mode.hard):
            #this function checks where the enemy's projectile hit 
            enemy.shoot(mode, xy, count)
        elif(mode.hard and mode.shots == 0):
            #this function calculates the distance to the nearest soldier
            enemy.calculate(mode, xy, count)
            i = enemy.calculate(mode, xy, count)
        else: 
            i = enemy.calculate(mode, xy, count)
            #this function forces the enemy to shot at a soldier 
            enemy.knownShot(mode, i)
        if(not mode.hard):
            #this function checks where the player's projectile hit 
            projectile.checkBlock(mode, mode.count)
            #this function finds how far away the closes soldier is in terms of x and y cubes 
            dist = projectile.calculateXY(mode, xy, mode.count)
            canvas.create_text(200, 25, text = f' Your closest x: {dist[0]} cubes away, closest y: {dist[1]} cubes away', fill = 'gray', font = 'Times 14')
        else: 
            projectile.checkBlock(mode, mode.count)
        mode.timer = 0
        if(mode.hit):
            mixer.Sound.stop(mode.cannon)
            mixer.Sound.play(mode.explosion)
            tup = projectile.checkBlock(mode, mode.count)
            canvas.create_image(x, mode.height/ 2 - 20, image = ImageTk.PhotoImage(mode.fireImage))
        mode.hit = False
        mode.fire = False 

    canvas.update()