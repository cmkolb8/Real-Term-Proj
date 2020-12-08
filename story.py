def tellStory(mode, canvas, time):
     if(mode.player == 0):
            if(0 < mode.time < 40):
               canvas.create_text(mode.width/2, mode.height/2, text = 'Your kind has inhabited the planet of Zorga for over 17 trillion years.'
                ' You have had a peaceful existance.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)
            elif(40 < mode.time < 60):
                canvas.create_text(mode.width/2, mode.height/2, text = 'But everything has changed.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 
            elif(60 < mode.time < 110):
                canvas.create_text(mode.width/2, mode.height/2, text = "Creatures have arrived. They call themselves 'humans'. If you are not able to defend your land, you will be taken over.", fill = 'firebrick3', font = "Times 26 bold", width = mode.width - 50) 
            elif(110 < mode.time < 140): 
                canvas.create_text(mode.width/2, mode.height/2, text = "I have faith in you. Do me proud. Protect Zorga.", fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)
     else: 
            if(0 < mode.time < 40):
               canvas.create_text(mode.width/2, mode.height/2, text = 'Upon your recent space mission you have discovered a new planet.'
                ' An exciting discovery indeed. The only issue...', fill = 'firebrick3', font = "Times 26 bold", width = mode.width - 50)
            elif(40 < mode.time < 60):
                canvas.create_text(mode.width/2, mode.height/2, text = 'It is already inhabited.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50)    
            elif(60 < mode.time < 110):
                canvas.create_text(mode.width/2, mode.height/2, text = 'You must fight the inhabitants to gain this new territory. But beware,'
                 ' losing could have dire consequences.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 
            elif(110 < mode.time < 140):
                canvas.create_text(mode.width/2, mode.height/2, text = 'Good luck comrade. Bring us home some new land.', fill = 'firebrick3', font = 'Times 32 bold', width = mode.width - 50) 