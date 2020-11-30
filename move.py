import math 
def left(mode):
    yDir = mode.yDir 
    xDir = mode.xDir
    #uses rotation matrix in order to rotate
    mode.yDir = mode.xDir * math.sin(mode.rotate) + mode.yDir * math.cos(mode.rotate)
    mode.xDir = mode.xDir * math.cos(mode.rotate) - yDir * math.sin(mode.rotate)
    planex = mode.xPlane
    #changes plane with the rotation matrix
    #mode.xPlane = -1 * (mode.yPlane * math.sin(mode.rotate)) + mode.xPlane * math.cos(mode.rotate)
    #mode.yPlane = planex * math.sin(mode.rotate) + mode.yPlane * math.cos(mode.rotate)

def right(mode):
    yDir = mode.yDir
    xDir = mode.xDir
    mode.yDir = mode.xDir * math.sin(-1 * mode.rotate) + mode.yDir * math.cos(-1 * mode.rotate)
    mode.xDir = mode.xDir * math.cos(-1 * mode.rotate) - yDir * math.sin(-1 * mode.rotate)
    planex = mode.xPlane
    mode.xPlane = -1 * (mode.yPlane * math.sin(-1 * mode.rotate)) + mode.xPlane * math.cos(-1 * mode.rotate)
    mode.yPlane = planex * math.sin(-1 * mode.rotate) + mode.yPlane * math.cos(-1 * mode.rotate)

def up(mode):
    #checks if there is a block ahead, if not moves forward
    if(mode.map[int(mode.xPos + mode.xDir * mode.speed)][int(mode.yPos)] == 0):
        mode.xPos += mode.xDir * mode.speed 
    if(mode.map[int(mode.xPos)][int(mode.yPos + mode.yDir * mode.speed)] == 0):
        mode.yPos += mode.yDir * mode.speed

def down(mode):
     #checks if there is a block behind, if not moves backward
    if(mode.map[int(mode.xPos - mode.xDir * mode.speed)][int(mode.yPos)] == 0):
        mode.xPos -= mode.xDir * mode.speed 
    if(mode.map[int(mode.xPos)][int(mode.yPos - mode.yDir * mode.speed)] == 0):
        mode.yPos -= mode.yDir * mode.speed 
    