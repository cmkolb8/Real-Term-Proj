def drawBlock(mode, canvas):
    canvas.create_rectangle(25, mode.height - 50, 75, mode.height - 100, outline = 'white')
    canvas.create_rectangle(75, mode.height - 50, 125, mode.height - 100, outline = 'white')
    canvas.create_rectangle(30, mode.height - 55, 70, mode.height - 95, fill = 'magenta2')
    canvas.create_rectangle(90, mode.height - 65, 110, mode.height - 90, fill = 'darkGreen')