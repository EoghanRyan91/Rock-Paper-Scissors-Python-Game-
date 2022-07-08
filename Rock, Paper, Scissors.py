# Eoghan Ryan - ETF9831 - Event Driven Programming

# Rock Paper Scissors Game

# Import Modules

from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Main Window Code

root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# Picture Variables 

rockIMG = ImageTk.PhotoImage(Image.open("userRock.png"))
paperIMG = ImageTk.PhotoImage(Image.open("userPaper.png"))
scissorIMG = ImageTk.PhotoImage(Image.open("userScissors.png"))
rockIMG_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paperIMG_comp = ImageTk.PhotoImage(Image.open("Paper.png"))
scissorIMG_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# Inserting Pictures Into The Program

userLabel = Label(root, image=scissorIMG, bg="#9b59b6")
compLabel = Label(root, image=scissorIMG_comp, bg="#9b59b6")
compLabel.grid(row=1, column=0)
userLabel.grid(row=1, column=4)


# Keeping Track of Scores

playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators

userIndicator = Label(root, font=50, text="YOU", bg="#9b59b6", fg="white")
compIndicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
userIndicator.grid(row=0, column=3)
compIndicator.grid(row=0, column=1)

# Messages/Alerts

msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# Update Message Code

def updateMessage(x):
    msg['text'] = x

# Update Score Code

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update Computer Score

def updateComputerScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check Winner Score

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose!")
            updateComputerScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass


# Update Choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # Computer

    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        compLabel.configure(image=rockIMG_comp)
    elif compChoice == "paper":
        compLabel.configure(image=paperIMG_comp)
    else:
        compLabel.configure(image=scissorIMG_comp)


# Player

    if x == "rock":
        userLabel.configure(image=rockIMG)
    elif x == "paper":
        userLabel.configure(image=paperIMG)
    else:
        userLabel.configure(image=scissorIMG)

    checkWin(x, compChoice)


# Buttons

rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
