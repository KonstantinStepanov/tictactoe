from tkinter import *

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
        
for r in range(0, degree):
    board.append([0] * degree)
    for k in range(0,degree):
        widget = Label(root, text=' ',relief=SUNKEN, width=10, height=5)
        widget.grid(row=r, column=k, sticky=NSEW)
        widget.bind('<Button-1>', onClick)
        coord[widget] = (r, k)
        label[(r, k)] = widget
        board[r][k] = ' '


root.title('Крестики нолики')
root.mainloop()
