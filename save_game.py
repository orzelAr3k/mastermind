def save_game():
    '''Zapisanie gry'''
    global pegs
    global colours 
    global gameAnswer
    global gameBoard
    global tries
    global colourChoice2
    global whiteBoard 
    global blackBoard
    
    f1 = open('savegame.txt','w')
    f1.write("%s\n" % pegs)
    f1.write("%s\n" % colours)
    f1.write(' ')
    for i in gameAnswer:
        f1.write("%s," % i)
    f1.write('\n')
    f1.write("%s\n" % gameBoard)
    f1.write("%s\n" % tries)
    f1.write("%s\n" % colourChoice2)
    f1.write("%s\n" % whiteBoard)
    f1.write("%s\n" % blackBoard)
    f1.close()
    sys.exit()

def literable(a, b):
    pass