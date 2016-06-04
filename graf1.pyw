from tkinter import *

degree = 3   # Стандартный размер игры 3x3
root = Tk()
rows = []
for r in range(0, degree):
    cols = []
    for k in range(0,degree):
        widget = Label(root, text=' ',relief=SUNKEN, width=10, height=5)
        widget.grid(row=r, column=k, sticky=NSEW)
        cols.append(widget)
    rows.append(cols)

root.title('Крестики нолики')
root.mainloop()
