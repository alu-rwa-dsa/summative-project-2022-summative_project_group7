from tkinter import *
from solver import solver

# create the gui window
root = Tk()
root.title("Sudoku Solver")

# Set dimensions of the window
root.geometry("324x550")

label = Label(root, text="Fill in the numbers and click solve").grid(row=0, column=1, columnspan=10)

# Label to represent unsolvable sudoku

errorLabel = Label(root, text="", fg="red")
errorLabel.grid(row=15, column=1, columnspan=10, pady=5)

# Label to represent solvable sudoku

successLabel = Label(root, text="", fg="green")
successLabel.grid(row=15, column=1, columnspan=10, pady=5)

# Create a dict to store each cell of the input grid

cells = {}


# Function to validate our input numbers
def validateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = root.register(validateNumber)


# Draw the 3 by 3 regions
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e


# Draw the 9 by 9 Grid
def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"


# Function to clear values from the grid
def clearValues():
    errorLabel.configure(text="")
    successLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


# Function to get input from the user
def getValues():
    board = []
    errorLabel.configure(text="")
    successLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)


# Solve Button
btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

# Clear Button
btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)


# Function to update the cells and display the sudoku solution
def updateValues(s):
    sol = solver(s)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
        successLabel.configure(text="Sudoku Solved")
    else:
        errorLabel.configure(text="No Solution exists for this sudoku")



draw9x9Grid()
root.mainloop()
