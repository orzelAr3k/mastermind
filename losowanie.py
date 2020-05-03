def game_answer():
    global colourChoice2
    global gameAnswer
    global gameBoard
    # lista kolorow
    colourChoice = ["czerwony", "niebieski", "zolty", "zielony",
                    "brazowy", "pomaranczowy", "rozowy", "fioletowy"]
    colourChoice1 = colourChoice[0:(colours)] #wybieranie ile kolorow bedziemy uzywac
    colourChoice2 = colourChoice1[:]
    for i in range (0, pegs):
        i = random.choice(colourChoice1)
        colourChoice1.remove(i)
        gameAnswer.append(i)
    print gameAnswer