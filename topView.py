def topView(mode, canvas): 
    for i in range(48):
        for j in range(24):
            posColors = [[0,0,0], [0, 100, 0], [150, 0 ,0], [0,100, 100], [0,150,0], [100,30, 100], [150, 0 ,0], [0,0,150]]
            color = posColors[mode.map[i][j]]
            #picks the right color of each spot on the map 
            for k, l in enumerate(color):
                color[k] = int(l / 2)
                col = '#%02x%02x%02x' % (color[0], color[1], color[2])
                #canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
                canvas.create_rectangle(i * (mode.width / 48), j * (mode.height / 24), i * (mode.width / 48) + (mode.width / 48), j * (mode.height / 24) + (mode.height / 24), fill = col) 