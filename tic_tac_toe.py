from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        c = buttons[row][0]['text']
        if all(buttons[row][i]['text'] == c for i in range(3)) and c!= "":
            for i in range(3):
                buttons[row][i].config(bg="green")
            return True

    for column in range(3):
        c = buttons[0][column]['text']
        if all(buttons[i][column]['text'] == c for i in range(3)) and c!= "":
            for i in range(3):
                buttons[i][column].config(bg="green")
            return True

    c = buttons[0][0]['text'] 
    if all(buttons[i][i]['text'] == c for i in range(3) ) and c != "":
        for i in range(3):
                buttons[i][i].config(bg="green")
        return True

    c = buttons[0][2]['text']
    if all(buttons[i][2-i]['text'] == c for i in range(3)) and c!= "":
        for i in range(3):
                buttons[i][2 - i].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
               return True
    return

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0 for i in range(3)] for i in range(3)]

label = Label(text=player.upper() + " turn", font=('consolas',20))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game, bg = "red")
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()