#draws tank/ shooting 
def bottomTank(mode, canvas):
    #draws bottom of tank/ platform 
    left = (0, mode.height + 10)
    botLeft= (0, mode.height)
    botRight = (mode.width, mode.height)
    right = (mode.midX + 100, mode.midY + 125)
    canvas.create_rectangle(0, mode.height, mode.width, mode.height + 100, fill = 'black')
    canvas.create_polygon(left, botLeft, right, botRight, fill = 'darkolivegreen', outline = 'darkgreen', width = 5)
    canvas.create_rectangle(0, mode.height + 100, mode.width, mode.height, fill = 'black')

def shotGun(mode, canvas):
    #code adapted from https://www.mediafire.com/file/4155l5gz6fuxpbm/3D_Graphics_in_Tkinter_v1.00.py/file 
    #draws the shooting part
    topLeft = (mode.midX + 50, mode.midY + 50 - 10 * (mode.count))
    topRight = (mode.midX + 100, mode.midY + 50 - 10 * (mode.count))
    bottomLeft = (mode.midX + 200, mode.midY + 600 - 10 * (mode.count))
    bottomRight = (mode.midX + 1000, mode.midY + 500)
    canvas.create_polygon(topLeft, bottomLeft, bottomRight, topRight, fill = 'DarkGreen', outline = 'red4', width = 3)
    topRight, bottomRight = topLeft, bottomLeft
    topLeft = (topRight[0], mode.midY + 100 - 10 * (mode.count))
    bottomLeft = (mode.midX + 200, mode.midY + 1000 - 10 * (mode.count))
    canvas.create_polygon(topLeft, bottomLeft, bottomRight, topRight,fill = 'DarkGreen', outline = 'red4', width = 3)

def powerBar(mode, canvas):
    #shows a power bar 
    topLeft = (mode.midX + 77, mode.midY + 75 - 10 * (mode.count))
    topRight = (mode.midX + 115, mode.midY + 75 - 10 * (mode.count))
    bottomLeft = (mode.midX + 110, mode.midY + 150 - 10 * (mode.count))
    bottomRight = (mode.midX + 220, mode.midY + 150 - 10 * (mode.count))
    canvas.create_polygon(topLeft, bottomLeft, bottomRight, topRight, fill = 'darkseagreen', outline = 'red4', width = 3)
