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
import topView
import story 

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

    #checks if pressed the button 
    def mousePressed(mode, event):
        if(50 <= event.x <= 150 and mode.height - 80 <= event.y <= mode.height - 50):
              mode.app.setActiveMode(mode.app.startScreenMode)

    #highlights the button if hover over it 
    def mouseMoved(mode, event):  
        if(50 <= event.x <= 150 and mode.height - 80 <= event.y <= mode.height - 50):
            mode.backgroundColor = 'red'
            mode.outlineColor = 'white'
        else: 
            mode.backgroundColor = 'red3'
            mode.outlineColor = 'red3'

    #draws the button and instructions
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        stars.stars(mode, canvas)
        canvas.create_rectangle(50, mode.height - 50, 150, mode.height - 80, fill = mode.backgroundColor, outline = mode.outlineColor)
        canvas.create_text(100, mode.height - 65, text = 'return', fill = 'white', font = 'Times 26 bold')
        canvas.create_text(mode.width / 2, mode.height / 2, text ='Walk around your side setting up 10 targets (the green blocks).'
                ' Then use the pink blocks to create a defense for your green blocks. Once your side is ready, click d and the match will begin.' 
                ' Use the arrow keys to move around your tank and p to increase the power.'
                ' When you think you are able to hit one of the enemys green blocks, hit f to fire.'
                ' The first team to destroy all the other teams green blocks wins!', fill = 'firebrick3', font = 'Times 20 bold', width = mode.width - 50)

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

    #sets each writing for a certain time 
    def timerFired(mode):
        mode.time += 1
        if(40 < mode.time < 60):
            mode.intro = False
            mode.secondAl = True
        elif(60 < mode.time < 100):
            mode.secondAl = False 
            mode.thirAl = True
        if(mode.time == 140):
            mode.app.setActiveMode(mode.app.setPickMode)

    #checks if hit the button 
    def mousePressed(mode, event):  
        if(mode.width - 150 <= event.x <= mode.width - 75 
            and mode.height - 50 <= event.y <= mode.height - 25):
            mode.app.setActiveMode(mode.app.setPickMode)

    #chekc if button was hovered over 
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
        story.tellStory(mode, canvas, mode.time)

class SetPickMode(Mode):
    def appStarted(mode):
        mode.instructionsColor = 'red3'
        mode.gameColor = 'red3'
        mode.instructionsOutline = 'red3'
        mode.gameOutline = 'red3'

    #creates highlight for when hovering over button 
    def mouseMoved(mode, event):  
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (1/4) * mode.height <= event.y <= (1/4) * mode.height + 50):
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

    def mousePressed(mode, event):  
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (1/4) * mode.height <= event.y <= (1/4) * mode.height + 50):
            mode.app.setActiveMode(mode.app.setEasyMode)
            mode.gameColor = 'red3'
            mode.gameOutline = 'red3'
        if(mode.width/2 - 75 <= event.x <= mode.width/2 + 75 
            and (2/3) * mode.height - 40 <= event.y <= (2/3) * mode.height + 10):
            mode.app.setActiveMode(mode.app.setHardMode)
            mode.gameColor = 'red3'
            mode.gameOutline = 'red3'

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        #draws the stars
        stars.stars(mode, canvas)
        canvas.create_rectangle(mode.width/2 - 75, (1/4) * mode.height, 
            mode.width/2 + 75, (1/4) * mode.height + 50, fill = mode.instructionsColor, outline = mode.instructionsOutline)
        canvas.create_text(mode.width/2, (1/4) * mode.height + 25, text = 'Easy', fill = 'white', font='Times 26 bold')
        canvas.create_rectangle(mode.width/2 - 75, (2/3) * mode.height - 40, 
            mode.width/2 + 75, (2/3) * mode.height + 10, fill = mode.gameColor, outline = mode.gameOutline)
        canvas.create_text(mode.width/2, (2/3) * mode.height - 15, text = 'Hard', fill = 'white', font='Times 26 bold')

class SetEasyMode(Mode):
    def appStarted(mode):
        #beginning map, competely empty except for sides
        mode.map = [([0] * 24) for row in range(48)]
        for i in range(len(mode.map)):
            for j in range(len(mode.map[0])):
                mode.map[0][j] = 3
                mode.map[47][j] = 3
                mode.map[i][0] = 3
                mode.map[i][23] = 3
        #establishes variables for raycasting 
        mode.xPos = 22
        mode.yPos = 12
        mode.xDir = -1
        mode.yDir = 0
        mode.xCameraPlane = 0 
        mode.yCameraPlane = .66
        mode.speed = .2
        mode.rotate = .02

        #variables needed for when different buttons are pressed 
        mode.finish = False
        mode.begin = False
        mode.fire = False
        mode.big = False
        mode.small = True
        mode.win = False
        mode.lose = False
        
        #varibles to used in projectile and enemy functions 
        mode.midX = mode.width / 2
        mode.midY = mode.height / 2
        mode.timer = 0
        mode.count = 1
        mode.power = 1
        mode.turn = 12
        mode.myScore = 10
        mode.mySold = list()
        mode.enemyScore = 0
        mode.timerDelay = 250
        mode.sold = 0
        mode.top = False
        mode.fireImg = mode.loadImage('fire.jpg')
        mode.hard = False

    def mousePressed(mode, event):
        if(25 < event.x < 75 and mode.height - 50 > event.y > mode.height - 100):
            mode.big = True
            mode.small = False
            
        #calucates where the block should be placed based on current position and eventx/y
        if(75 < event.x < 125 and mode.height - 50 > event.y > mode.height - 100):
            mode.big = False
            mode.small = True
        if(event.y > mode.height/2):
            dist = int((event.y - 200) // (150 / mode.xPos)) + 5
            x = (event.x // 16.67)
            xDist = int((x + mode.yPos) / 2)
            if(dist >= mode.xPos):
                dist = mode.xPos - 3
            if(mode.big and (xDist > 13 or xDist < 11)):
                mode.map[int(dist)][int(xDist)] = 5
            elif(mode.small and (xDist > 13 or xDist < 11) and mode.sold < 10): 
                mode.enemyScore += 1
                mode.sold += 1
                mode.mySold.append((dist, xDist))
                mode.map[dist][xDist] = 1
    
    def keyPressed(mode, event):
        if(event.key == "Left"):
            if(mode.begin == False):
                #this function math for rotating left (uses a rotation matrix)
                move.left(mode)
            else: 
                if(mode.turn > -10):
                #this function math for rotating right (uses a rotation matrix)
                    move.right(mode)
                    mode.turn -= 1

        if(event.key == "Right"):
            if(mode.begin == False):
                move.right(mode)
            else: 
                if(mode.turn < 30):
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

        #when d is pressed, player turns around and enemy's defense is drawn
        if(event.key == 'd' and mode.sold > 0):
             mode.begin = True
             mode.xDir = 1
             mode.yDir = 0
             mode.xPos = 2
             mode.yPos = 12
             mode.xCameraPlane = 0 
             for i in range(1, 22):
                mode.map[24][i] = 0
             #puts enemy soldiers
             for i in range(10):
                enemyRow = random.randint(25, 45)
                enemyCol = random.randint(3, 21)
                mode.map[enemyRow][enemyCol] = 1
                #puts enemy blocks around soldiers 
                defense = random.randint(1, 5)
                for i in range(defense):
                    xRand = random.randint(-2, -1)
                    yRand = random.randint(-1, 1)
                    mode.map[enemyRow + -1][enemyCol + yRand] = 6

        #increases power of shot
        if(event.key == 'p'):
            if(mode.begin):
                mode.power += 10

        #fires 
        if(event.key == 'f' and mode.begin):
            mode.fire = True

        if(event.key == 't' and mode.begin):
            mode.top = True  
 
        if(event.key == 'r' and mode.begin and mode.top):
            mode.top = False

    def redrawAll(mode, canvas):
        while(not mode.finish):
            #this function has the math behind the raycasting in order to give a 3D apperance
            ry.drawRayCaster(mode, canvas)
            #this function calls neccessary functions when certain keys are pressed
            ry.possible(mode, canvas) 

class SetHardMode(SetEasyMode):
    def appStarted(mode):
        super().appStarted()
        mode.hard = True
        mode.shots = 0
        mode.soldiers = list()
        mode.myScore = 20

    def keyPressed(mode, event):
        super().keyPressed(event)

        if(event.key == 'd' and mode.sold > 0):
             mode.begin = True
             mode.xDir = 1
             mode.yDir = 0
             mode.xPos = 2
             mode.yPos = 12
             mode.xCameraPlane = 0 
             for i in range(1, 22):
                mode.map[24][i] = 0
             #puts enemy soldiers
             for i in range(10):
                enemyRow = random.randint(25, 45)
                enemyCol = random.randint(3, 21)
                mode.map[enemyRow][enemyCol] = 1
                print(1)
                mode.soldiers.append((enemyRow, enemyCol))
                #puts enemy blocks around soldiers 
                defense = random.randint(1, 5)
                for i in range(defense):
                    xRand = random.randint(-2, -1)
                    yRand = random.randint(-1, 1)
                    mode.map[enemyRow + -1][enemyCol + yRand] = 6

class MyModalApp(ModalApp):
    def appStarted(mode):
        mode.startScreenMode = StartScreenMode()
        mode.setEasyMode = SetEasyMode()
        mode.instructionsMode = InstructionsMode()
        mode.storyMode = StoryMode()
        mode.setActiveMode(mode.startScreenMode) 
        mode.setPickMode = SetPickMode()
        mode.setHardMode = SetHardMode()

app = MyModalApp(width = 500, height = 400)