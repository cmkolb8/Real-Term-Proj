from cmu_112_graphics import * 
from tkinter import * 
import math 
import random
import decimal

#start screen mode 
class StartScreenMode(Mode): 
    def appStarted(mode):
        title = 'https://images.cooltext.com/5480353.png'
        mode.title = mode.loadImage(title)
        mode.instructionsColor = 'red3'
        mode.gameColor = 'red3'
        mode.instructionsOutline = 'red3'
        mode.gameOutline = 'red3'

    def mousePressed(mode, event):  
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (3/4) * mode.height <= event.y <= (3/4) * mode.height + 50):
            mode.app.setActiveMode(mode.app.storyMode)
            mode.gameColor = 'red3'
            mode.gameOutline = 'red3'
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (2/3) * mode.height - 40 <= event.y <= (2/3) * mode.height + 10):
            mode.app.setActiveMode(mode.app.instructionsMode)
            mode.gameColor = 'red3'
            mode.gameOutline = 'red3'

    def mouseMoved(mode, event):  
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (3/4) * mode.height <= event.y <= (3/4) * mode.height + 50):
            mode.instructionsColor = 'red'
            mode.instructionsOutline = 'white'
        else: 
            mode.instructionsColor = 'red3'
            mode.instructionsOutline = 'red3'
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (2/3) * mode.height - 40 <= event.y <= (2/3) * mode.height + 10):
            mode.gameColor = 'red'
            mode.gameOutline = 'white'
        else: 
            mode.gameColor = 'red3'
            mode.gameOutline = 'red3'

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        #draws the stars
        for i in range(25):
            x = random.randint(0, mode.width)
            y = random.randint(0,mode.height)
            canvas.create_oval(x - 1, y - 2, x + 1, y + 1, fill = 'white')
        canvas.create_rectangle(mode.width/2 - 75, (3/4) * mode.height, 
            mode.width/2 + 75, (3/4) * mode.height + 50, fill = mode.instructionsColor, outline = mode.instructionsOutline)
        canvas.create_text(mode.width/2, (3/4) * mode.height + 25, text = 'Start Game', fill = 'white', font='Times 26 bold')
        canvas.create_rectangle(mode.width/2 - 75, (2/3) * mode.height - 40, 
            mode.width/2 + 75, (2/3) * mode.height + 10, fill = mode.gameColor, outline = mode.gameOutline)
        canvas.create_text(mode.width/2, (2/3) * mode.height - 15, text = 'Instructions', fill = 'white', font='Times 26 bold')
        canvas.create_image(mode.width/2, 100, image = ImageTk.PhotoImage(mode.title))

#set up your side mode
class SetMode(Mode):
    def appStarted(mode):
        mode.map = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        mode.xPos = 22
        mode.yPos = 12
        mode.xDir = -1
        mode.yDir = 0
        mode.xPlane = 0 
        mode.yPlane = .66 
        mode.finish = False
        mode.speed = .2
        mode.rotate = .05
        mode.x = 0
        mode.y = 0
        mode.color = 'black'

#https://lodev.org/cgtutor/raycasting3.html used this to help learn raycasting 
    def drawRayCaster(mode, canvas):
        while(not mode.finish):
            for x in range(mode.width):
                xMap = int(mode.xPos)
                yMap = int(mode.yPos)
                hit = 0 
                xCamera = 2.0 * x / mode.width - 1.0
                xRayDir = mode.xDir + xCamera * mode.xPlane 
                yRayDir = mode.yDir + xCamera * mode.yPlane + .0000001 #so don't divde by zero
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
                    end = lineHeight / 2.0 + mode.height / 2.0
                    if(start < 0):
                        start = 0 
                    if(end >= mode.height):
                        end = mode.height - 1
                    
                    #colors 
                    posColors = [[0,0,0], [0,100, 100], [150, 0 ,0], [0,150,0], [0,0,150], [100,30, 100]]
                    color = posColors[mode.map[xMap][yMap]]
                    if(side == True):
                        for i, j in enumerate(color):
                            color[i] = int(j / 2 )
                    col = '#%02x%02x%02x' % (color[0], color[1], color[2])
                    canvas.create_line(x, start, x, end, fill = col)
            canvas.update()

    def mousePressed(mode, event):
        if(event.y > mode.height/2):
            midy = event.y // 2
            yDist = int((event.y + mode.xPos) / 2)
            dist = int((event.y - 200) // (150 / mode.xPos)) + 5
            xDist = int((event.x - 200) // (150 / mode.yPos)) 
            y = (midy // 8)
            x = (event.x // 16.67)
            xDist = int((x + mode.yPos) / 2)
            yDist = int((y + mode.xPos) / 2)
            mapOfX = int(xDist // mode.xPos + mode.xDir + mode.xPlane)
            mapOfY = int(yDist // mode.xPos + mode.xDir + mode.xPlane)
            if(event.x >= mode.width/2):
                x = mode.yPos + (event.x // (24 - mode.yPos))
            else: 
                x = mode.yPos - (event.x) // (24 - mode.yPos)
            y = mode.xPos + ((event.y // (24 - mode.xPos)))
            if(dist >= mode.xPos):
                dist = mode.xPos - 3
            print(dist)
            print(xDist)
            print(mode.map[dist][xDist])
            mode.map[dist][xDist] = 5

    def keyPressed(mode, event):
        if(event.key == "Left"):
            yDir = mode.yDir 
            xDir = mode.xDir
            mode.yDir = xDir * math.sin(mode.rotate) + mode.yDir * math.cos(mode.rotate)
            mode.xDir = mode.xDir * math.cos(mode.rotate) - yDir * math.sin(mode.rotate)
            planex = mode.xPlane
            mode.xPlane = -1 * (mode.yPlane * math.sin(mode.rotate)) + mode.xPlane * math.cos(mode.rotate)
            mode.yPlane = planex * math.sin(mode.rotate) + mode.yPlane * math.cos(mode.rotate)

        if(event.key == "Right"):
            yDir = mode.yDir
            xDir = mode.xDir
            mode.yDir = xDir * math.sin(-1 * mode.rotate) + mode.yDir * math.cos(-1 * mode.rotate)
            mode.xDir = mode.xDir * math.cos(-1 * mode.rotate) - yDir * math.sin(-1 * mode.rotate)
            planex = mode.xPlane
            mode.xPlane = -1 * (mode.yPlane * math.sin(-1 * mode.rotate)) + mode.xPlane * math.cos(-1 * mode.rotate)
            mode.yPlane = planex * math.sin(-1 * mode.rotate) + mode.yPlane * math.cos(-1 * mode.rotate)
            
        if(event.key == 'Up'):
            if(mode.map[int(mode.xPos + mode.xDir * mode.speed)][int(mode.yPos)] == 0):
                print(int(mode.xPos - mode.xDir * mode.speed))
                print(int(mode.yPos))
                print(mode.map[int(mode.xPos + mode.xDir * mode.speed)][int(mode.yPos)])
                mode.xPos += mode.xDir * mode.speed 
            if(mode.map[int(mode.xPos)][int(mode.yPos + mode.yDir * mode.speed)] == 0):
                mode.yPos += mode.yDir * mode.speed

        if(event.key == 'Down'):
            if(mode.map[int(mode.xPos - mode.xDir * mode.speed)][int(mode.yPos)] == 0):
                mode.xPos -= mode.xDir * mode.speed 
            if(mode.map[int(mode.xPos)][int(mode.yPos - mode.yDir * mode.speed)] == 0):
                mode.yPos -= mode.yDir * mode.speed 

    def redrawAll(mode, canvas):
        mode.drawRayCaster(canvas)

#sets up the scene, picks which side you are on 
class StoryMode(Mode):
    def appStarted(mode):
        mode.player = random.randint(0, 1)
        mode.time = 0
        mode.intro = False 
        mode.secondAl = True
        mode.thirdAl = False
        planet = 'hiclipart.com.png'
        mode.planet = mode.loadImage(planet)
        mode.size = 1/4
        mode.sizey = mode.scaleImage(mode.planet, mode.size)
        mode.color = 'red3'
        mode.outline = 'red3'

    def timerFired(mode):
        mode.time += 1
        if(40 < mode.time < 60):
            mode.intro = False
            mode.secondAl = True
        elif(60 < mode.time < 100):
            mode.secondAl = False 
            mode.thirAl = True
        if(mode.time == 160):
            mode.app.setActiveMode(mode.app.setMode)
        #if(140 < mode.time < 200):
       # mode.size += 10
        #if(140 < mode.time < 200):
        #    mode.size += 10

    def mousePressed(mode, event):  
        if(mode.width - 150 <= event.x <= mode.width - 75 
            and mode.height - 50 <= event.y <= mode.height - 25):
            mode.app.setActiveMode(mode.app.setMode)

    def mouseMoved(mode, event):  
        if(mode.width - 150 <= event.x <= mode.width - 75 
            and mode.height - 50 <= event.y <= mode.height - 25):
            mode.color = 'red'
            mode.outline = 'white'
        else: 
            mode.color = 'red3'
            mode.outline = 'red3'

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        canvas.create_rectangle(mode.width - 150, mode.height - 50, mode.width - 75, mode.height - 25, fill = mode.color, outline = mode.outline)
        canvas.create_text(mode.width - 112, mode.height - 37, text = 'Skip', fill = 'white', font = 'Times 20 bold')
        for i in range(25):
            x = random.randint(0, mode.width)
            y = random.randint(0,mode.height)
            canvas.create_oval(x - 1, y - 2, x + 1, y + 1, fill = 'white')
        if(mode.player == 0):
            if(0 < mode.time < 40):
               canvas.create_text(mode.width/2, mode.height/2, text = 'Your kind has inhabited the planet of Zorga for over 17 trillion years. You have had a peaceful existance.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)
            elif(40 < mode.time < 60):
                canvas.create_text(mode.width/2, mode.height/2, text = 'But everything has changed.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 
            elif(60 < mode.time < 110):
                canvas.create_text(mode.width/2, mode.height/2, text = "Creatures have arrived. They call themselves 'humans'. If you are not able to defend your land, you will be taken over.", fill = 'firebrick3', font = "Times 26 bold", width = mode.width - 50) 
            elif(110 < mode.time < 140): 
                canvas.create_text(mode.width/2, mode.height/2, text = "I have faith in you. Do me proud. Protect Zorga.", fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)
        else: 
            if(0 < mode.time < 40):
               canvas.create_text(mode.width/2, mode.height/2, text = 'Upon your recent space mission you have discovered a new planet. An exciting discovery indeed. The only issue...', fill = 'firebrick3', font = "Times 26 bold", width = mode.width - 50)
            elif(40 < mode.time < 60):
                canvas.create_text(mode.width/2, mode.height/2, text = 'It is already inhabited.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)    
            elif(60 < mode.time < 110):
                canvas.create_text(mode.width/2, mode.height/2, text = 'You must fight the inhabitants to gain this new territory. But beware, losing could have dire consequences.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 
            elif(110 < mode.time < 140):
                canvas.create_text(mode.width/2, mode.height/2, text = 'Good luck comrade. Bring us home some new land.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 
        if(140 < mode.time):
            canvas.create_image(mode.width/2, mode.height/2, image = ImageTk.PhotoImage(mode.sizey))

#instructions page 
class InstructionsMode(Mode):
    def appStarted(mode):
        instructionsBackground = 'https://c4.wallpaperflare.com/wallpaper/66/989/201/fantasy-art-fantasy-city-battlegrounds-of-eldhelm-video-games-wallpaper-preview.jpg'
        mode.instructionsBackground = mode.loadImage(instructionsBackground)
        mode.backgroundColor = 'red3'
        mode.outlineColor = 'red3'

    def mousePressed(mode, event):
        if(50 <= event.x <= 150 and mode.height - 80 <= event.y <= mode.height - 50):
              mode.app.setActiveMode(mode.app.startScreenMode)

    def mouseMoved(mode, event):  
        if(50 <= event.x <= 150 and mode.height - 80 <= event.y <= mode.height - 50):
            mode.backgroundColor = 'red'
            mode.outlineColor = 'white'
        else: 
            mode.backgroundColor = 'red3'
            mode.outlineColor = 'red3'

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        for i in range(25):
            x = random.randint(0, mode.width)
            y = random.randint(0, mode.height)
            canvas.create_oval(x - 1, y - 2, x + 1, y + 1, fill = 'white')
        canvas.create_rectangle(50, mode.height - 50, 150, mode.height - 80, fill = mode.backgroundColor, outline = mode.outlineColor)
        canvas.create_text(100, mode.height - 65, text = 'return', fill = 'white', font = 'Times 26 bold')

class MyModalApp(ModalApp):
    def appStarted(mode):
        mode.startScreenMode = StartScreenMode()
        mode.setMode = SetMode()
        mode.instructionsMode = InstructionsMode()
        mode.storyMode = StoryMode()
        mode.setActiveMode(mode.startScreenMode) 
    
app = MyModalApp(width = 500, height = 400)

