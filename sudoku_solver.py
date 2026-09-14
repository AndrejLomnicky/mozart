import tkinter as tk

sudoku = []


def create_sudoku(sudoku):
    fr = open('sudoku.txt', 'r')
    for row in fr:
        row = row.strip()
        temp = []
        for char in row:
            temp.append(int(char))
        sudoku.append(temp)

def checkit(x, y, number):

    for i in range(9):
        if sudoku[x][i] == number:
            return False


    for i in range(9):
        if sudoku[i][y] == number:
            return False


    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if sudoku[i][j] == number:
                return False

    return True

def sudoku_solver():
    global sudoku
    for y in range(0,9):
        for x in range(0,9):
            if sudoku[y][x] == 0:
                for i in range(1,10):
                    if checkit(y, x, i):
                        sudoku[y][x] = i
                        if sudoku_solver():
                            return True
                        sudoku[y][x] = 0
                return False
    return True

def show_grid(grid):
    root = tk.Tk()
    root.title("Vyriešené sudoku")
    root.configure(background="black")

    for y in range(9):
        for x in range(9):
            value = grid[y][x]
            cell = tk.Label(root,text=str(value),width=2,height=1,font=("Arial", 20),borderwidth=1,relief="solid", background="white")

            padx = (5 if x % 3 == 0 else 1, 5 if x == 8 else 1)
            pady = (5 if y % 3 == 0 else 1, 5 if y == 8 else 1)

            cell.grid(row=y, column=x, padx=padx, pady=pady)

    root.mainloop()


create_sudoku(sudoku)
sudoku_solver()
show_grid(sudoku)