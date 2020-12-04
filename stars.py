import random 

def stars(mode, canvas):
     for i in range(25):
            x = random.randint(0, mode.width)
            y = random.randint(0, mode.height)
            canvas.create_oval(x - 1, y - 2, x + 1, y + 1, fill = 'white')