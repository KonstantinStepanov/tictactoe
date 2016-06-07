from tkinter import *
from tkinter.messagebox import askyesno
import random

degree = 3                        # Стандартный размер игры 3x3
#root = Tk()

coord = {}
label = {}
board = []

def onClick(event):             # Обработка нажатия игроком мышью на свободное поле
    label = event.widget
    row, col = coord[label]
    if board[row][col] == ' ':
        label.config(text='X')
        board[row][col] = 'X'
        finish()
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
    if len(clear_cells) > 0:
        return random.choice(clear_cells)
    else:
        return (-1, -1)

def compMove():                 # Вывод 0 (нуля) как результата хода компьютера
    row, col = computerMove()
    if row == -1:
        pass
    else:
        board[row][col] = '0'
        lab = label[(row, col)]
        lab.config(text='0')
        finish()
        

def draw():                           # Проверка на ничью
    for row in board:
        if ' ' in row:
            return False
    return True

def winner(mark):                # Определение победителя
    for row in board:
        if row.count(mark) == degree:
            return True
    for row in board:                          # Возможность выигрыша в режимах Специалист и Эксперт
        for col in range(degree):          #  если в горизонтальном ряду выбранны все клетки подряд кроме одной
            if row[col] != mark:
                break
            elif degree > 3 and row.count(mark) == (degree - 1):
                return True
    for row in board:                          
        for col in range(degree-1, -1, -1):            
            if row[col] != mark:
                break
            elif degree > 3 and row.count(mark) == (degree - 1):
                return True
    for col in range(degree):
        for row in board:
            if row[col] != mark:
                break
        else:
            return True
    for row in range(degree):     # Проверка первой диагонали
        col = row
        if board[row][col] != mark:
            break
    else:
            return True
    for row in range(degree):       # Проверка второй диагонали
        col = (degree - 1) - row
        if board[row][col] != mark:
            break
    else:
            return True

    
def finish():
     message = None
     if winner('X'):
         message = "Ты победил!"
     elif winner('0'):
         message = "Ты проиграл!"
     elif draw():
         message = "Ничья! Попробуй еще раз"

     if message:
         result = "Игра окончена:" + message                        # При выборе продолжения игры делает ход,
         if askyesno('Verify', result + '\n\nИграть еще раз?'):  # если первым в этот раз ходит компьютер
             newGame()                                                             # или ждет хода игрока.
         else:
             root.destroy()

def playGame():
    for r in range(degree):
        board.append([0] * degree)
        for k in range(degree):
            widget = Label(child, text=' ',relief=SUNKEN, width=10, height=5)
            widget.grid(row=r, column=k, sticky=NSEW)
            widget.bind('<Button-1>', onClick)
            coord[widget] = (r, k)
            label[(r, k)] = widget
            board[r][k] = ' '
            
def startGame():
    global child
    child = Toplevel(root)
    child.title('Крестики-нолики')
    playGame()
    button1 = Button(child, text='New Game', command=newGame)
    button1.grid()
    child.grab_set()
    child.focus_set()
    child.wait_window()

def degreeBeginner():
    global degree
    degree = 3
    startGame()
    
def degreeSpec():
    global degree
    degree = 5
    startGame()

def degreeExsp():
    global degree
    degree = 7
    startGame()

some_text = "Добро пожаловать!\n\nВыберите режим игры"
    
root = Tk()

root.title('Крестики нолики')
root.geometry('400x400+500+300')


lab = Label(root, text=some_text, font=('Arial', 20))
lab.grid(row=0, column=0, columnspan=12, rowspan=3)
lab2 = Label(root)
lab2.grid(row=3, column=0, rowspan=5)
button3 = Button(root, text='Новичок', font=('Arial',10), bg='white', fg='blue', command=degreeBeginner)
button3.grid(row=8, column=0, columnspan=4)
button4 = Button(root, text='Специалист', font=('Arial', 10), bg='white', fg='blue',command=degreeSpec)
button4.grid(row=8, column=4, columnspan=4)
button5 = Button(root, text='Эксперт', font=('Arial', 10), bg='white', fg='blue', command=degreeExsp)
button5.grid(row=8, column=8, columnspan=4)

root.mainloop()
