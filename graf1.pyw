from tkinter import *

degree = 3   # Стандартный размер игры 3x3
root = Tk()

coord = {}
label = {}
board = []
for r in range(0, degree):
    board.append([0] * degree)
    for k in range(0,degree):
        widget = Label(root, text=' ',relief=SUNKEN, width=10, height=5)
        widget.grid(row=r, column=k, sticky=NSEW)
        coord[widget] = (r, k)
        label[(r, k)] = widget
        board[r][k] = ' '
        

root.title('Крестики нолики')
root.mainloop()
