import random
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk


window = ThemedTk (theme = "equilux")
window.configure(themebg = "equilux")

window.geometry("460x185")

window.title("Colour game")

colours = ["Red" , "Blue", "Green" , "Brown", "Yellow", "Pink", "Black", "Orange", "White", "Purple"]
score = 0
time = 30

def startGame(event):
    if time == 30:
        countdown()
    nextColour()

def countdown():
    global time
    if time > 0:
        time -= 1
        lbl3.config(text= "Time left: " + str(time))
        lbl3.after(1000,countdown)

def nextColour():
    global score
    global time
    if time > 0:
        if txt.get().lower() == colours[1].lower():
            score += 1

            lbl2.config(text="Score: " +str(score))

            random.shuffle(colours)
            lbl4.config(fg= str(colours[1]), text= str(colours[0]))
    txt.delete(0, "end")
lbl = ttk.Label(window, text="Type in the colour of the words, and not the word text!")
lbl.place(x=50,y=30)

lbl2 = ttk.Label(window, text="Score: " +str(score))
lbl2.place(x=50,y=50)

lbl3 = ttk.Label(window, text="Time left: " +str(time))
lbl3.place(x=50,y=70)

lbl4 = Label(window, text="PINK", fg="BLUE",font=("Arial", 40))
lbl4.place(x=180,y=90)


txt = ttk.Entry(window,width=37, font=("Arial", 20))
txt.place(x= 0, y=150)

window.bind("<Return>", startGame)

window.mainloop()