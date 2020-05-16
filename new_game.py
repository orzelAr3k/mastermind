def new_game():    
    '''Nowa gra'''
    global choice 
    
    choice = 0
    check_user_input()
    game_board()
    game_answer()
    user_guess()
    
def read_me(): 
    '''README zasady gry'''
    f1 = open('ReadMe.txt', 'r')
    text = f1.readlines()
    for line in text:
        print line
    text_based_interface()
    test_input()