from sre_parse import State
import tkinter as tk
from tkinter import *
from tkinter import font
from turtle import bgcolor
from unittest import result

from matplotlib.ft2font import BOLD
from sudokusolver import solver
from puzzle import puzzle, solution
import time
from tkinter import messagebox
from tkinter.tix import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import tkinter.font as font


# import mp3play
import pygame

global board
# create the gui window
root = Tk()
root.title("Sudoku Solver")

# Set dimensions of the window
root.geometry("385x650")
root.configure(bg='white')

myFont = font.Font(family='Segoe UI')


label = Label(root, text="Fill in the numbers and click submit", font=(myFont, 12, 'bold'), background="white", borderwidth=0).grid(row=0, column=1, columnspan=10, pady=15)


# Label to represent unsolvable sudoku

errorLabel = Label(root, text="", fg="red")
errorLabel.grid(row=15, column=1, columnspan=10, pady=5)
errorLabel.config(background="white")

# Label to represent solvable sudoku

successLabel = Label(root, text="", fg="green")
successLabel.grid(row=15, column=1, columnspan=10, pady=5)
successLabel.config(background="white")
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
            e = Entry(root, width=5, fg="purple", font=('Roboto 10'), bg=bgcolor, readonlybackground=readonlycolor,
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
        messagebox.showinfo("Sudoku Results", "Correct Solution. Congratulations!" + recordSuccess())
        
     
        return True
    else:
        errorLabel.configure(text="Wrong Solution. Try again.")
        stopTimer()
        return False


# Function to update the cells and display the sudoku solution
def checkSolvable():
    board = getValues()
    sol = solver(board)
    if sol != "no":
        for rows in range(2, 11):
            for col in range(1, 10):
                cells[(rows, col)].config(state="normal")
                cells[(rows, col)].delete(0, "end")
                cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
        readOnly()

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
            cells[(rows, col)].config(fg="#023e8a", state="readonly")

# Function to play Sudoku's Game theme song
def play():
    changeIconAndCommand()
    gameThemeSong = 'playlist/hans1.mp3'

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(gameThemeSong)
    pygame.mixer.music.play(loops=0)


# Function to end the theme music.
def stop():
    changeIconAndCommand()
    pygame.mixer.music.stop()


def changeSolveButtonState():
    if solveBtn['state'] == DISABLED:

        solveBtn['state'] = NORMAL

    else:

        solveBtn['state'] = DISABLED


# Change the submit/play again button 
def changeSubmitButtonText():
    if submitBtn['text'] == 'Submit':
        submitBtn['text'] = 'Play Again'
        submitBtn['command'] = clearValues
        clearBtn['state'] = DISABLED
        pauseButton['state'] = DISABLED
        readOnly()
        

    else:
        submitBtn['text'] = 'Submit'
        submitBtn['command'] = compareSolution
        clearBtn['state'] = NORMAL
        pauseButton['state'] = NORMAL
        pause()
        reset()


# Start when the time isn't running
running = False

# time variables initially set to 0
hours, minutes, seconds = 0, 0, 0


# start the timer function
def start():
    global running
    if not running:
        update()
        running = True


# read only function
def readOnly():
    for row in range(2, 11):
            for col in range(1, 10):
               cells[(row, col)].config(state="readonly")
  

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
                

    # Make the board normal and the default values readonly
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


# function to stop the timer 
def stopTimer():
    global running
    if running:
        stopwatchLabel.after_cancel(updateTime)
        running = False
        print(updateTime[6:])

# Creating the list to record time
timeTaken = []

# record the time used to successfully solve the puzzle
def recordSuccess():  
    global currentTime, totalTime
    global previousTime

    # Call the function to stop the timer
    stopTimer()

    # Append the time taken to the list
    

    totalTime = int(updateTime[6:])
    
    if len(timeTaken) == 0:
        timeTaken.append(totalTime)
        previousTime = totalTime
        print('Since starting: ', totalTime)
        return ""


    elif len(timeTaken) != 0:
        previousTime = int(timeTaken[len(timeTaken)-1])
 
        totalSeconds = 0
        for item in range (0, len(timeTaken)):
            totalSeconds = totalSeconds + timeTaken[item]
        

        newTime = totalTime - totalSeconds
      
        timeTaken.append(newTime)
   

        if previousTime > newTime:
            results = "\nYou have improved from " + str(previousTime) + " to " + str(newTime) + " seconds.\nYour cognitive skills are on a rise!!! "
        
            return results
        
        elif previousTime <= newTime:

            results = "\nHowever, you have used more time compared to your previous attempt.\nYou can do better!"
            return results
                
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


# Change the pause/play button state
def changePauseState():
    if pauseButton['text'] == 'Play Game':
        pauseButton['text'] = 'Pause Game'
    else:
        pauseButton['text'] = 'Play Game'
        
# Change the icon and command of the play/stop music button
def changeIconAndCommand():
     if playBtn.image == photoimage1:
        playBtn.config(image=photoimage2)
        playBtn.image = photoimage2
        playBtn['command'] = stop
 
     else:
        playBtn.config(image=photoimage1)
        playBtn.image = photoimage1
        playBtn['command'] = play


# label to display time
stopwatchLabel = tk.Label(text='00:00:00', font=(myFont, 20))
stopwatchLabel.grid(row=1, column=0, columnspan=5, pady=20)
stopwatchLabel.config(background="white")


# start, pause, reset, quit buttons
pauseButton = tk.Button(text='Play Game', height=1, width=10, command=pause, background="#00b4d8", foreground="white", borderwidth=0, font=myFont)
pauseButton.grid(row=1, column=7, columnspan=2, pady=20)


# Create a tooltip
tip= Balloon(root)

# Defining music icons
icon1 = PhotoImage(file='images/music.png')
icon2 = PhotoImage(file='images/no-music.png')
photoimage1 = icon1.subsample(15, 15)
photoimage2 = icon2.subsample(15, 15)

# GUI Buttons

# Solution Button
submitBtn = Button(root, command=compareSolution, text="Submit", width=10, font=myFont, borderwidth=0.5)
submitBtn.grid(row=20, column=1, columnspan=5, pady=20)

# Clear Button
clearBtn = Button(root, command=clearValues, text="Clear", width=10, state=NORMAL, font=myFont, borderwidth=0.5)
clearBtn.grid(row=20, column=5, columnspan=5, pady=20)

# Play/Stop Music
playBtn = Button(root, command=play, text="Play Music", width=40, image=photoimage1, borderwidth=0, background="white") 
playBtn.image = photoimage1
playBtn.grid(row=20, column=3, columnspan=5, pady=20)

# Solve Button
solveBtn = Button(root, command=checkSolvable, text="Show solution", width=15, state=DISABLED, font=myFont, borderwidth=0.5)
solveBtn.grid(row=21, column=3, columnspan=5, pady=20)

# tooltip
tip.bind_widget(playBtn,balloonmsg="Play/Stop Music")

# Draw 9x9 Grid
draw9x9Grid()


if __name__ == '__main__':
    root.mainloop()