import tkinter as tk
from tkinter import *
from sudokusolver import solver
from puzzle import puzzle, solution
import time
from tkinter import messagebox

# import mp3play
import pygame

global board
# create the gui window
root = Tk()
root.title("Sudoku Solver")

# Set dimensions of the window
root.geometry("370x550")

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
    errorLabel.configure(text="")
    out = (P.isdigit() or P == "") and len(P) < 2 and P != "0"
    if not out:
        errorLabel.configure(text="Invalid Input!Enter numbers from 1-9")
        return False
    return out


reg = root.register(validateNumber)


# Draw the 3 by 3 regions
def draw3x3Grid(row, column, bgcolor, readonlycolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, fg="purple", font=('Lato 10'), bg=bgcolor, readonlybackground=readonlycolor,
                      justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e


# Draw the 9 by 9 Grid
def draw9x9Grid():
    color = "white"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color, color)
            if color == "#caf0f8":
                color = "white"
            else:
                color = "#caf0f8"
    populateGrid(puzzle)


# Function to clear values from the grid
def clearValues():
    errorLabel.configure(text="")
    successLabel.configure(text="")
    if submitBtn['text'] == 'Play Again':
        changeSubmitButtonText()
        changeSolveButtonState()
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")
    populateGrid(puzzle)


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
    return board


def compareSolution():
    changeSolveButtonState()
    changeSubmitButtonText()
    board = getValues()
    if board == solution:
        # successLabel.configure(text="Correct Solution. Congratulations!")
        messagebox.showinfo("Sudoku Results", "Correct Solution. Congratulations!")

        return True
    else:
        errorLabel.configure(text="Wrong Solution. Try again.")
        return False


# Function to update the cells and display the sudoku solution
def checkSolvable():
    board = getValues()
    sol = solver(board)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows - 2][col - 1])

        successLabel.configure(text="Sudoku Solved")

    else:
        errorLabel.configure(text="No Solution exist for this sudoku")


# Function to set default puzzle values on the grid

def populateGrid(puzzle):
    for rows in range(2, 11):
        for col in range(1, 10):
            val = puzzle[rows - 2][col - 1]
            if val != 0:
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, val)
                cells[(rows, col)].config(fg="#023e8a", state="readonly")


# Function to play Sudoku's Game theme song
def play():
    gameThemeSong = 'playlist/hans1.mp3'

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(gameThemeSong)
    pygame.mixer.music.play(loops=0)


# Function to end the theme music.
def stop():
    pygame.mixer.music.stop()


def changeSolveButtonState():
    if solveBtn['state'] == DISABLED:

        solveBtn['state'] = NORMAL

    else:

        solveBtn['state'] = DISABLED


def changeSubmitButtonText():
    if submitBtn['text'] == 'Submit':
        submitBtn['text'] = 'Play Again'
        submitBtn['command'] = clearValues
        clearBtn['state'] = DISABLED

    else:
        submitBtn['text'] = 'Submit'
        submitBtn['command'] = compareSolution
        clearBtn['state'] = NORMAL


# Start when the time isn't running
running = False

# time variables initially set to 0
hours, minutes, seconds = 0, 0, 0


def start():
    global running
    if not running:
        update()
        running = True


# pause function
def pause():
    global running
    if running:

        # cancel updating of time using after_cancel()
        stopwatchLabel.after_cancel(updateTime)
        running = False
        changePauseState()
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].config(state="readonly")


    elif not running:
        update()
        running = True
        changePauseState()
        for row in range(2, 11):
            for col in range(1, 10):
                val = puzzle[row - 2][col - 1]
                if val != 0:
                    cells[(row, col)].config(fg="#023e8a", state="readonly")

                else:
                    cells[(row, col)].config(state="normal")

                # reset function


def reset():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatchLabel.after_cancel(updateTime)
        running = False
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatchLabel.config(text='00:00:00')


# update stopwatch function
def update():
    # update seconds with (addition) compound assignment operator

    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatchLabel.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use updateTime variable to cancel or pause the time using after_cancel
    global updateTime
    updateTime = stopwatchLabel.after(1000, update)


def changePauseState():
    if pauseButton['text'] == 'play':
        pauseButton['text'] = 'pause'
    else:
        pauseButton['text'] = 'play'


# label to display time
stopwatchLabel = tk.Label(text='00:00:00', font=('Arial', 20))
stopwatchLabel.grid(row=1, column=0, columnspan=5, pady=20)

# start, pause, reset, quit buttons
# start_button = tk.Button(text='start', height=2, width=7, font=('Arial', 10), command=start)
# start_button.grid(row=1, column=3, columnspan=5, pady=20)
pauseButton = tk.Button(text='play', height=1, width=7, font=('Arial', 10), command=pause)
pauseButton.grid(row=1, column=6, columnspan=2, pady=20)
resetButton = tk.Button(text='reset', height=1, width=7, font=('Arial', 10), command=reset)
resetButton.grid(row=1, column=8, columnspan=2, pady=20)
# quit_button = tk.Button(text='quit', height=2, width=7, font=('Arial', 10), command=root.quit)
# quit_button.grid(row=1, column=8, columnspan=2, pady=20)


# GUI Buttons

# Solution Button
submitBtn = Button(root, command=compareSolution, text="Submit", width=10)
submitBtn.grid(row=20, column=1, columnspan=5, pady=20)

# Clear Button
clearBtn = Button(root, command=clearValues, text="Clear", width=10, state=NORMAL)
clearBtn.grid(row=20, column=5, columnspan=5, pady=20)

# Play Music
playBtn = Button(root, command=play, text="Play Music", width=10)
playBtn.grid(row=21, column=1, columnspan=5, pady=20)

# Stop Music
StopBtn = Button(root, command=stop, text="Stop Music", width=10)
StopBtn.grid(row=21, column=5, columnspan=5, pady=20)

# Solve Button
solveBtn = Button(root, command=checkSolvable, text="Show solution", width=10, state=DISABLED)
solveBtn.grid(row=22, column=3, columnspan=5, pady=20)

draw9x9Grid()


if __name__ == '__main__':
    root.mainloop()
