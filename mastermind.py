#created by GuanJun(username:jg495)
#This file include AI function

'''LIBRARY IMPORT'''
import random
import sys

'''VARIABLR GLOBAL'''
global pegs
global colours
global colourChoice1
colourChoice1 = []
global colourChoice2
colourChoice2 = []
global gameAnswer
gameAnswer = []
global userGuess
global gameBoard
gameBoard = []
global tries
tries = 0
global whiteBoard 
whiteBoard = []
global blackBoard
blackBoard = []
global white
global black
global choice

def text_based_interface():    
    '''text-based interface'''
    print ' ---------------'
    print ' |   new game  |'
    print ' |    help     |' 
    print ' |    save     |' 
    print ' |  continue   |'
    print ' |     AI      |'
    print ' ---------------'
    
def test_input():
    '''test the user input value '''
    user_input0 = raw_input('What do you want to do?\n')
    user_input = user_input0.lower()
    
    if user_input == 'new game':
        new_game()
    elif user_input == 'help':
        read_me()
    elif user_input == 'save':
        sys.stderr.write('only could save in the game\n')
        return test_input()
    elif user_input == 'continue':
        continue_play()
    elif user_input == 'ai':
        compVsComp()    
    else:
        sys.stderr.write('invalid input\n')
        return test_input()

def check_user_input():            
    '''get the input from user'''
    global pegs
    global colours
    global choice
        
    try: 
        pegs = input("please enter how many pegs you want?(from 3 to 8):  ")
        if pegs < 3 or pegs > 8:
            print "please enter the number between 3 to 8, start again please"
            if choice == 0:
                return new_game()
            else:
                return compVsComp()    
                
        colours = input('how many colours you want from 3 to 8:  ')
        if colours < 3 or colours > 8:
            print "please enter the number between 3 to 8, start again please"
            if choice == 0:
                return new_game()
            else:
                return compVsComp()    
                
        elif colours < pegs:
            txt="Your colours' number cannot less than your pegs' number\n"
            sys.stderr.write(txt)
            if choice == 0:
                return new_game()
            else:
                return compVsComp()    
    except:
        if choice == 0 or choice == 1:
            sys.exit()
        else:
            sys.stderr.write('invaild input,please enter number \n')
            if choice == 0:
                return new_game()
            else:
                return compVsComp()
                 

def game_board():
    global pegs

    matrix = []
    print 'You only have 10 attempts to guess!Come On!'
    for i in range(0, 10):
        coloumn = []
        for j in range (0, pegs):
            coloumn.append("0")
        matrix.append(coloumn)
    for i in matrix:
        print i    
    return matrix
    
def game_answer():
    '''get random answer as codemaker '''
    global colourChoice2
    global gameAnswer
    global gameBoard
  
    colourChoice = ["red", "blue", "yellow", "green", 
                    "brown", "orange", "pink", "purple"] 
    colourChoice1 = colourChoice[0:(colours)]
    colourChoice2 = colourChoice1[:]
    for i in range (0, pegs):
        i = random.choice(colourChoice1)
        colourChoice1.remove(i)
        gameAnswer.append(i)
    
    
def user_guess():   
    '''ask user to guess the colours and get input from user''' 
    global colourChoice2
    global gameAnswer
    global gameBoard
    global tries
    global userGuess
    global pegs
    
  
    while tries < 10    :
        userGuess = []
        c = 0
        while c < pegs:
            c += 1
            print ("please guess a colour between"), colourChoice2
            i = raw_input()
            i = i.lower()
            if i == 'save':  
                save_game()
            elif i in colourChoice2:
                userGuess.append(i)
            else:
                sys.stderr.write('invalid input\n')
                c -= 1
        check_Answer()

        tries += 1
        user_guess()

    print "Fail~~, Play Again!"
    sys.exit()

def check_Answer():
    '''check the userGuess and the gameAswer'''
    '''black=colour and position is right; white=colour is 
    right but position is wrong'''
    global gameAnswer
    global userGuess
    global whiteBoard 
    global blackBoard
    global gameBoard
    global white
    global black
    global choice

    black = 0
    white = 0
    userGuessM = []
    c = 0
    checkAnswer = gameAnswer[:]
    userGuess2 = userGuess[:]
    for i in range (0, pegs):
        if    userGuess2[i] == checkAnswer[i]:
            black = black+1
            checkAnswer[i] = 0    
    for element in userGuess2:
        if element in userGuess2[c+1:len(userGuess2)]:
            userGuess2[c] = 1
        c += 1
    for i in range (0, pegs):
        if    userGuess2[i] in checkAnswer:
            white = white+1
            
    if black == pegs: 
        whiteBoard.append(white)
        blackBoard.append(black)
        gameBoard.append(userGuess)
        if choice == 0:
            i = 1
            for index in gameBoard:
                print i, index, "     black=", blackBoard[i-1], " white=", whiteBoard[i-1]
                i += 1     
            print"Congratulation!You Win!"
            
        else: 
            gameBoard.append(userGuessM)
            i = 0
            for element in gameBoard:
                i += 1
            print i-1, userGuess, "    black=", black, " white=", white
            print 'OMG!Codebreaker Win!!!'
            
        sys.exit()    
        
    else:
   
        i = 1
        if choice == 0:
            whiteBoard.append(white)
            blackBoard.append(black)
            userGuessM = userGuess[:]
            gameBoard.append(userGuessM)
            for index in gameBoard:
                print i, index, "     black=", blackBoard[i-1], " white=", whiteBoard[i-1]
                i += 1     
        else:
            gameBoard.append(userGuessM)
            for element in gameBoard:
                i += 1
            print i-1, userGuess, "    black=", black, " white=", white
            
                
            
def new_game():    
    '''the main function for new game'''
    global choice 
    
    choice = 0
    check_user_input()
    game_board()
    game_answer()
    user_guess()
    
def read_me(): 
    '''read the 'readMe' from another file'''
    f1 = open('ReadMe.txt', 'r')
    text = f1.readlines()
    for line in text:
        print line
    text_based_interface()
    test_input()

def save_game():
    '''save game'''
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

def continue_play():
    '''continue play the game,restore data from the savegame File'''
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
    choice = 0 
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
    for index in gameBoard:
        print i, index, "     black=", blackBoard[i-1], " white=", whiteBoard[i-1]
        i += 1
    return user_guess()
        


def compVsComp():
    '''AI'''
    global choice
    
    choice = 1
    check_user_input()    
    game_board()
    game_answer()
    computerGuess()

def computerGuess():  
    '''computer codebreaker'''  
    global colourChoice2
    global gameBoard
    global pegs
    global colours
    global userGuess
    global white 
    global black
    global tries

    print   'computer codebreaker will guess the colours between', colourChoice2
    userGuess = []
    userGuess1 = []
    random_check = []
    black = 0
    black1 = 0
    white1 = 0
    f = 0
    s = 1
    x = 0
    c = 1
    '''used when pegs = colours'''
    if pegs == colours:      
        while tries < 10:
            if tries == 0:
                userGuess = compGuess()
                random_check.append(userGuess)
                check_Answer()
                tries += 1
            if black == 0 and tries == c:
                userGuess = compGuess()
                while userGuess in random_check:
                    userGuess = compGuess()
                random_check.append(userGuess)
                check_Answer()
                x = tries
                c += 1
                tries += 1
            else:
                if black-black1 == 2 and tries != 1 and tries != x:
                    black1 = black
                    f += 1
                    s = f+1
                if s == pegs and black-black1 != 2:
                    f += 1
                    s = f+1
                    if f == pegs-1: 
                        f = 0
                        s = 1
                userGuess1 = userGuess[:]
                userGuess[s] = userGuess1[f]
                userGuess[f] = userGuess1[s]
                s += 1
                check_Answer()
                tries += 1
        
    else:
        '''used when pegs < colours'''
        while tries < 10:    
            if tries == 0:
                userGuess = compGuess()
                random_check.append(userGuess)
                check_Answer()
                tries += 1
            else:
                if white + black == pegs:
                    if black == 0 and tries == c:
                        userGuess = compGuess()
                        while userGuess in random_check:
                            userGuess = compGuess()
                        random_check.append(userGuess)
                        check_Answer()
                        x = tries
                        c += 1
                        tries += 1
                    else:
                        if black-black1 == 2 and tries != 1 and tries != x:
                            black1 = black
                            f += 1
                            s = f+1
                        if s == pegs and black - black1 != 2:
                            f += 1 
                            s = f+1
                            if f == pegs-1:
                                f = 0
                                s = 1
                        userGuess1 = userGuess[:]
                        userGuess[s] = userGuess1[f]
                        userGuess[f] = userGuess1[s]
                        s += 1
                        check_Answer()
                        tries += 1    
                elif white + black == 0:
                    for element in userGuess:
                        colourChoice2.remove(element)
                    userGuess = compGuess()
                    while userGuess in random_check:
                        userGuess = compGuess()
                    random_check.append(userGuess)
                    check_Answer()
                    tries += 1
                else:
                    userGuess = compGuess()    
                    while userGuess in random_check:
                        userGuess = compGuess()
                    random_check.append(userGuess)
                    check_Answer()
                    tries += 1    
                    
    print "Fail~~, computer codemaker win"
    sys.exit()

def compGuess():
    ''' used for AI to generate random list'''
    global colourChoice2
    
    userGuess = []
    colourChoice3 = colourChoice2[:]
    for i in range (0, pegs):
        i = random.choice(colourChoice3)
        colourChoice3.remove(i)
        userGuess.append(i)
    return userGuess
     
'''call main function'''
text_based_interface()
test_input()



    
    
    


