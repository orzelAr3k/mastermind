def test_input():
    '''Sprawdzenie poprawności podaneko kodu gracza '''
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