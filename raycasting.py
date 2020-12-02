import math 
import random
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

#code adapted from https://www.mediafire.com/file/4155l5gz6fuxpbm/3D_Graphics_in_Tkinter_v1.00.py/file 
            if(mode.begin == True):
                topLeft = (mode.midX+50,mode.midY+50)
                topRight = (mode.midX+100,mode.midY+50)
                bottomLeft = (mode.midX+200,mode.midY+600)
                bottomRight = (mode.midX+1000,mode.midY+500)
                canvas.create_polygon(topLeft, bottomLeft, bottomRight, topRight, fill = 'gray25', outline = 'red4', width = 5)
                topRight, bottomRight = topLeft, bottomLeft
                topLeft = (topRight[0],mode.midY+100)
                bottomLeft = (mode.midX+200,mode.midY+1000)
                canvas.create_polygon(topLeft, bottomLeft, bottomRight, topRight,fill = 'gray25', outline = 'red4', width = 5)
            canvas.update()