from tkinter import *


root = Tk()

root.geometry("500x500")
root.title("Rock Paper Scissor")

rps = ["Rock" , "Paper" , "Scissors"]

def play(event):
    computer = choice(rps)
    player = event.widget.cget("text")

playerLabel = Label(frame3 , text=player , bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))

playerLabel.grid(row=0 , column=0)

computerLabel = Label(frame3 , text=computer , bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))

computerLabel.grid(row=0 , column=1)    


frame1 = Frame(root , bg="lightblue")
frame1.pack(fill=X)

titleLabel = Label(frame1 , text="Rock Paper Scissors" , font=("Arial" , 30) ,bg="yellow")
titleLabel.pack()


#frame 4
frame2 = Frame(root , bg="lightgreen")
frame2.pack(fill=X)

playerLabel = Label(frame2 , text="Player ", bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))
playerLabel.grid(row=0 , column=0)

computerLabel = Label(frame2 , text="Computer", bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))
computerLabel.grid(row=0 , column=1)


#frame 3
frame3 = Frame(root , bg="lightblue")
frame3.pack(fill=X)

playerLabel = Label(frame3 , text="Player : ________", bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))
playerLabel.grid(row=0 , column=0)

computerLabel = Label(frame3 , text="Computer : ________", bg="green" , relief=SUNKEN , borderwidth=5 , font=("Arial" , 20))
computerLabel.grid(row=0 , column=1)

#frame 4
 
frame4= Frame(root , bg="lightblue")
frame4.pack(fill=X)

rockButton = Button(frame4 , text="Rock" , bg="orange" , relief=RAISED , borderwidth=5 , font=("Arial" , 20))
rockButton.pack()
rockButton.bind("<Button-1>" , play)

rockButton = Button(frame4 , text="Paper" , bg="orange" , relief=RAISED , borderwidth=5 , font=("Arial" , 20))
rockButton.pack()
rockButton.bind("<Button-1>" , play)

rockButton = Button(frame4 , text="Scissors" , bg="orange" , relief=RAISED , borderwidth=5 , font=("Arial" , 20))
rockButton.pack()
rockButton.bind("<Button-1>" , play)


#frame 5

frame5 = Frame(root , bg="lightgreen")
frame5.pack(fill=X)


winnerLabel = Label(frame5 , text="__winner__", relief=RAISED , borderwidth=5 , font=("Arial , 35"))
winnerLabel.pack()


root.mainloop()