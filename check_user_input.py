def check_user_input():            
    '''Pobranie wejścia od gracza'''
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
            if choice == 0:# used for 'new game'
                return new_game()
            else:#used for AI
                return compVsComp()
                 
#game board  "pegs,coloumn,matrix"
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
    
