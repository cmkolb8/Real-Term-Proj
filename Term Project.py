#Caitlin Kolb 
#using cmu graphics
from cmu_112_graphics import * 
from tkinter import * 
import raycasting as ry
import math 
import random
import move
import stars
import projectile 

#start screen mode 
class StartScreenMode(Mode): 
    def appStarted(mode):
        title = 'https://images.cooltext.com/5480353.png'
        mode.title = mode.loadImage(title)
        mode.instructionsColor = 'red3'
        mode.gameColor = 'red3'
        mode.instructionsOutline = 'red3'
        mode.gameOutline = 'red3'
    
    #checks if buttons were pressed 
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

    #creates highlight for when hovering over button 
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
        stars.stars(mode, canvas)
        canvas.create_rectangle(mode.width/2 - 75, (3/4) * mode.height, 
            mode.width/2 + 75, (3/4) * mode.height + 50, fill = mode.instructionsColor, outline = mode.instructionsOutline)
        canvas.create_text(mode.width/2, (3/4) * mode.height + 25, text = 'Start Game', fill = 'white', font='Times 26 bold')
        canvas.create_rectangle(mode.width/2 - 75, (2/3) * mode.height - 40, 
            mode.width/2 + 75, (2/3) * mode.height + 10, fill = mode.gameColor, outline = mode.gameOutline)
        canvas.create_text(mode.width/2, (2/3) * mode.height - 15, text = 'Instructions', fill = 'white', font='Times 26 bold')
        canvas.create_image(mode.width/2, 100, image = ImageTk.PhotoImage(mode.title))

#instructions page 
class InstructionsMode(Mode):
    def appStarted(mode):
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
        stars.stars(mode, canvas)
        canvas.create_rectangle(50, mode.height - 50, 150, mode.height - 80, fill = mode.backgroundColor, outline = mode.outlineColor)
        canvas.create_text(100, mode.height - 65, text = 'return', fill = 'white', font = 'Times 26 bold')

#sets up the scene, picks which side you are on 
class StoryMode(Mode):
    def appStarted(mode):
        mode.player = random.randint(0, 1)
        mode.time = 0
        mode.intro = False 
        mode.secondAl = True
        mode.thirdAl = False
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
        if(mode.time == 140):
            mode.app.setActiveMode(mode.app.setMode)

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

    #draws the story based on which was randomally generated
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        canvas.create_rectangle(mode.width - 150, mode.height - 50, mode.width - 75, mode.height - 25, fill = mode.color, outline = mode.outline)
        canvas.create_text(mode.width - 112, mode.height - 37, text = 'Skip', fill = 'white', font = 'Times 20 bold')
        stars.stars(mode, canvas)
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

class SetMode(Mode):
    def appStarted(mode):
        #beginning map, competely empty except for sides
        mode.map = [([0] * 24) for row in range(48)]
        for i in range(len(mode.map)):
            for j in range(len(mode.map[0])):
                mode.map[0][j] = 3
                mode.map[47][j] = 3
                mode.map[i][0] = 3
                mode.map[i][23] = 3
                mode.map[24][j] = 3
        mode.xPos = 22
        mode.yPos = 12
        mode.xDir = -1
        mode.yDir = 0
        mode.xCameraPlane = 0 
        mode.yCameraPlane = .66 
        mode.speed = .2
        mode.rotate = .02
        mode.finish = False
        mode.begin = False
        mode.imWidth = 64 
        mode.imHeight = 64
        mode.midX = mode.width / 2
        mode.midY = mode.height / 2
        mode.timer = 0
        mode.count = 1
        mode.power = 1
        mode.fire = False
        mode.keepTrack = 0
        mode.big = False
        mode.small = True
        mode.turn = 0
        mode.myScore = 10
        mode.enemyScore = 10
        mode.timerDelay = 100

    def mousePressed(mode, event):
        if(25 < event.x < 75 and mode.height - 50 > event.y > mode.height - 100):
            mode.big = True
            mode.small = False
            
        if(75 < event.x < 125 and mode.height - 50 > event.y > mode.height - 100):
            mode.big = False
            mode.small = True
        if(event.y > mode.height/2):
            midy = event.y // 2
            yDist = int((event.y + mode.xPos) / 2)
            dist = int((event.y - 200) // (150 / mode.xPos)) + 5
            xDist = int((event.x - 200) // (150 / mode.yPos)) 
            y = (midy // 8)
            x = (event.x // 16.67)
            xDist = int((x + mode.yPos) / 2)
            yDist = int((y + mode.xPos) / 2)
            mapOfX = int(xDist // mode.xPos + mode.xDir + mode.xCameraPlane)
            mapOfY = int(yDist // mode.xPos + mode.xDir + mode.yCameraPlane)
            if(event.x >= mode.width/2):
                x = mode.yPos + (event.x // (24 - mode.yPos))
            else: 
                x = mode.yPos - (event.x) // (24 - mode.yPos)
            y = mode.xPos + ((event.y // (24 - mode.xPos)))
            if(dist >= mode.xPos):
                dist = mode.xPos - 3
            if(mode.big):
                mode.map[dist][xDist] = 5
            else: 
                mode.map[dist][xDist] = 1


    def keyPressed(mode, event):
        if(event.key == "Left"):
            if(mode.begin == False):
                #this function math for rotating left (uses a rotation matrix)
                move.left(mode)
            else: 
                move.right(mode)
                mode.turn -= 1

        if(event.key == "Right"):
            if(mode.begin == False):
                move.right(mode)
            else: 
                move.left(mode)
                mode.turn += 1
            
        if(event.key == 'Up'):
            if(mode.begin == False):
            #checks if there is a block ahead, if not, walk forward
                move.up(mode)
            elif(mode.count < 23): 
                mode.count += 1

        if(event.key == 'Down'):
            if(mode.begin == False):
            #checks if there is a block behind, if not, walk backward
                move.down(mode)
            elif(mode.count > 0): 
                mode.count -= 1
            else: 
                pass

        if(event.key == 'd'):
             mode.begin = True
             mode.xDir = 1
             mode.yDir = 0
             mode.xPos = 2
             mode.yPos = 12
             mode.xCameraPlane = 0 
             mode.yCameraPlane = .66 
             for i in range(1, 22):
                mode.map[24][i] = 0
             for i in range(10):
                enemyRow = random.randint(25, 45)
                enemyCol = random.randint(3, 21)
                mode.map[enemyRow][enemyCol] = 1
                defense = random.randint(0, 5)
                for i in range(defense):
                    xRand = random.randint(-2, -1)
                    yRand = random.randint(-2, 2)
                    mode.map[enemyRow + xRand][enemyCol + yRand] = 6

        if(event.key == 'p'):
            if(mode.begin):
                mode.power += 10

        if(event.key == 'f'):
            mode.fire = True
            print(mode.fire)

    def redrawAll(mode, canvas):
        #this function has the math behind the raycasting in order to give a 3D apperance
        while(not mode.finish):
            ry.drawRayCaster(mode, canvas)

class MyModalApp(ModalApp):
    def appStarted(mode):
        mode.startScreenMode = StartScreenMode()
        mode.setMode = SetMode()
        mode.instructionsMode = InstructionsMode()
        mode.storyMode = StoryMode()
        mode.setActiveMode(mode.startScreenMode) 

app = MyModalApp(width = 500, height = 400)

