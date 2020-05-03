def check_Answer():
 '''Sprawdzenie odpowiedzi gracza z kodem'''
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
            
    if black == pegs: #!!WYGRANA!!
        whiteBoard.append(white)
        blackBoard.append(black)
        gameBoard.append(userGuess)
        if choice == 0:#wybor gracza
            i = 1
            for index in gameBoard:
                print i, index, "     black=", blackBoard[i-1], " white=", whiteBoard[i-1]
                i += 1     
            print"Congratulation!You Win!"
            
        else: #sprawdzenie zgodnosci
            gameBoard.append(userGuessM)
            i = 0
            for element in gameBoard:
                i += 1
            print i-1, userGuess, "    black=", black, " white=", white
            print 'OMG!Codebreaker Win!!!'
            
        sys.exit()    
        
    else:
    #wyswietlenie odpowiedzi
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
            
