from tkinter import *
import random

degree = 3   # Стандартный размер игры 3x3
root = Tk()

coord = {}
label = {}
board = []

def onClick(event):             # Обработка нажатия игроком мышью на свободное поле
    label = event.widget
    row, col = coord[label]
    if board[row][col] == ' ':
        label.config(text='X')
        board[row][col] = 'X'
        compMove()

def newGame():                  # Очистка игрового поля и старт новой игры
    for row, col in label.keys():
        label[(row, col)].config(text=' ')
        board[row][col] = ' '

def computerMove():           # Рандомный выбор незанятой позиции для хода компьютера
    clear_cells = []
    for row in range(degree):
        for col in range(degree):
            if board[row][col] == ' ':
                clear_cells.append((row, col))
    return random.choice(clear_cells)

def compMove():                 # Вывод 0 (нуля) как результата ходя компьютера
    row, col = computerMove()
    board[row][col] = '0'
    label[(row, col)].config(text='0')

def draw():                           # Проверка на ничью
    for row in board:
        if ' ' in row:
            return False
    return True

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
