from tkinter import *
import random

degree = 3   # Стандартный размер игры 3x3
root = Tk()

coord = {}
label = {}
board = []

def onClick(event):
    label = event.widget
    row, col = coord[label]
    if board[row][col] == ' ':
        label.config(text='X')
        board[row][col] = 'X'

def newGame():
    for row, col in label.keys():
        label[(row, col)].config(text=' ')
        board[row][col] = ' '

def computerMove():
    clear_cells = []
    for row in degree:
        for col in degree:
            if board[row][col] == ' ':
                clear_cells.append((row, col))
    return random.choice(clear_cells)
        
for r in range(0, degree):
    board.append([0] * degree)
    for k in range(0,degree):
        widget = Label(root, text=' ',relief=SUNKEN, width=10, height=5)
        widget.grid(row=r, column=k, sticky=NSEW)
        widget.bind('<Button-1>', onClick)
        coord[widget] = (r, k)
        label[(r, k)] = widget
        board[r][k] = ' '

button1 = Button(root, text='New Game', command=newGame)
button1.grid()

root.title('Крестики нолики')
root.mainloop()
