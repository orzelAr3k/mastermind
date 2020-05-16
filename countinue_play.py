def continue_play():
    '''Kontynuacja gry - wczytanie z pliku'''
    global pegs
    global colours 
    global gameAnswer
    global gameBoard
    global tries
    global colourChoice2
    global whiteBoard 
    global blackBoard
    global choice
    
    f1 = open('savegame.txt','r')    
    text = f1.readlines()
    choice = 0 #only 'new game' could save game
    for i, line in enumerate(text):
        if i == 0:
            pegs = int(line)
        elif i == 1:
            colours = int(line)
        elif i == 2:
            gameAnswer = line[1:-1].split(',')
        elif i == 3:
            gameBoard = eval(line)
        elif i == 4:
            tries = int(line)
        elif i == 5:
            colourChoice2 = eval(line)
        elif i == 6:
            whiteBoard = line[1:-1].split(',')
        elif i == 7:
            blackBoard = line[1:-1].split(',')
    i = 1
    for index in gameBoard:#give player information of last play
        print i, index, "     black=", blackBoard[i-1], " white=", whiteBoard[i-1]
        i += 1
    return user_guess()