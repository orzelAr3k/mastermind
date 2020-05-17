def user_guess():   
    '''Prośba o podanie koloru i liczby przez gracza''' 
    global colourChoice2
    global gameAnswer
    global gameBoard
    global tries
    global userGuess
    global pegs
    
#user have 10 attempts to try    
    while tries < 10    :
        userGuess = []
        c = 0
        while c < pegs:
            c += 1
            print ("please guess a colour between"), colourChoice2
            i = raw_input()
            i = i.lower()
            if i == 'save':  #save the game if the player want 
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