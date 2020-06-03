
from Tkinter import *

def colourGuess():
    print "hello!!!!"


root = Tk()
root.config(bg='white')
root.title('Mastermind')


Horiz = 7
Vert = 10
canv = Canvas(root, width=50*Horiz, height=50*Vert, bg='white')
canv.pack()

#Stworzenie menu
def make_menus():
	menu = Menu(root)
	root.config(menu=menu)

	filemenu = Menu(menu)
	menu.add_cascade(label="File", menu=filemenu)
	filemenu.add_command(label="New Game", command=new_game())
	filemenu.add_command(label="Help", command=colourGuess)
	filemenu.add_command(label="Save", command=colourGuess)
	filemenu.add_command(label="Continue", command=colourGuess)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=colourGuess)

	welcom = Label(root, text='Welcome to play Mastermind', bg='white')
	welcom.pack(side='bottom')		

#Wybór kolorów
	colour_choice = Frame(root)

	b = Button(colour_choice, text='red', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	b = Button(colour_choice, text='blue', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	b = Button(colour_choice, text='yellow', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	b = Button(colour_choice, text='green', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	b = Button(colour_choice, text='brown', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	b = Button(colour_choice, text='orange', width=5, command=colourGuess)
	b.pack(side=LEFT,padx=2)

	colour_choice.pack(side=BOTTOM, fill=X)
	
def new_game():
	topw = Toplevel(root)
	Label(topw, text = 'Please enter the grid size (width x height, min = 4, max = 10):').pack(side=TOP)
	entry1 = Entry(topw, width = 2)
	entry1.pack(side=LEFT)
	Label(topw, text = 'x').pack(side=LEFT)
	entry2 = Entry(topw, width = 2)
	entry2.pack(side=LEFT)
	text_error = Label(topw, text = '')

make_menus()
root.mainloop()


