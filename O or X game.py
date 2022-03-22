import tkinter.messagebox as tm 
from tkinter import *
from turtle import left


def checker (buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        score()
    elif buttons["text"] == " " and click ==False:
        buttons["text"] = "O"
        click = True
        score()


def score():
    c = False

# -------------------WIning points Condition for "X" ---------------------------
    # All Rows for x
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.configure(background="powder blue")
        b2.configure(background="powder blue")
        b3.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True


    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.configure(background="powder blue")
        b5.configure(background="powder blue")
        b6.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.configure(background="powder blue")
        b8.configure(background="powder blue")
        b9.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    # All column for x
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.configure(background="powder blue")
        b4.configure(background="powder blue")
        b7.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.configure(background="powder blue")
        b5.configure(background="powder blue")
        b8.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.configure(background="powder blue")
        b6.configure(background="powder blue")
        b9.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    # All digonals
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.configure(background="powder blue")
        b5.configure(background="powder blue")
        b9.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.configure(background="powder blue")
        b5.configure(background="powder blue")
        b7.configure(background="powder blue")
        n = float(playerx.get())
        playerx.set(n+2)
        tm.showinfo("Gave Over","Player 'X' Won the Match")
        c = True
    
# -------------------WIning points Condirion for "O"---------------------------

    # All Rows for x
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.configure(background="#47ffaf")
        b2.configure(background="#47ffaf")
        b3.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.configure(background="#47ffaf")
        b5.configure(background="#47ffaf")
        b6.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.configure(background="#47ffaf")
        b8.configure(background="#47ffaf")
        b9.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    # All column for x
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.configure(background="#47ffaf")
        b4.configure(background="#47ffaf")
        b7.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.configure(background="#47ffaf")
        b5.configure(background="#47ffaf")
        b8.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.configure(background="#47ffaf")
        b6.configure(background="#47ffaf")
        b9.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    # All digonals
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.configure(background="#47ffaf")
        b5.configure(background="#47ffaf")
        b9.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.configure(background="#47ffaf")
        b5.configure(background="#47ffaf")
        b7.configure(background="#47ffaf")
        n = float(playero.get())
        playero.set(n+2)
        tm.showinfo("Gave Over","Player 'O' Won the Match")
        c = True

    # Condition For tie
    elif b1["text"] != " " and b2["text"] != " " and b3["text"] != " " and b4["text"] != " " and b5["text"] != " " and b6["text"] != " " and b7["text"] != " " and b8["text"] != " " and b9["text"] != " ":
        b2.configure(background="#ff5447")
        b3.configure(background="#ff5447")
        b1.configure(background="#ff5447")
        b4.configure(background="#ff5447")
        b5.configure(background="#ff5447")
        b6.configure(background="#ff5447")
        b7.configure(background="#ff5447")
        b8.configure(background="#ff5447")
        b9.configure(background="#ff5447")
        n1 = float(playero.get())
        n2 = float(playerx.get())

        playero.set(n1+1)
        playerx.set(n2+1)

        tm.showinfo("Game Over","Match is tie")
        c = True

    if c:
        val = tm.askyesno("Restart","Do you want to restart the game")
        if val:
            reset()

def reset():
    global count
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "

    b1.configure(background="gainsboro")
    b2.configure(background="gainsboro")
    b3.configure(background="gainsboro")
    b4.configure(background="gainsboro")
    b5.configure(background="gainsboro")
    b6.configure(background="gainsboro")
    b7.configure(background="gainsboro")
    b8.configure(background="gainsboro")
    b9.configure(background="gainsboro")
    
    nm.configure(text = count)
    count+=1



def newgame():
    global count
    count = 1
    reset()
    playero.set(0)
    playerx.set(0)

    # i dont know why this for loop fails but i will resolve it after compiting
    # for i in range(3):
    #     for j in range(3):
    #         n = "b" + str(i+j+1)
    #         n["text"] = " "

root = Tk()
root.geometry("1350x700+100+30")
root.minsize(1350,700)
root.title("'O' or 'X' Game")
# We can also use hash code here 
root.configure(background="#ced95d")

Tops = Frame(root,bg = "#ced95d" ,pady =2,width = 1350,height = 100,relief=RIDGE)
Tops.grid(row=0,column=0)

# Heading of the game 
head = Label(Tops,font = "arial 50 bold",text = "Tic Tac Toe Game",bd = 21,bg = "#ced95d",fg = "white",justify=CENTER)
head.grid(row=0,column=0)

count = 1
nm = Label(Tops,font = "arial 50 bold",text = "0",bd = 5,bg = "Cadet Blue",fg = "White",justify=LEFT,relief=RIDGE)
nm.grid(row=0,column=2)

# This is main Frame with width = 1350,height = 600.
MainFrame = Frame(root,bg = "Powder Blue" ,bd=10,width = 1350,height = 600,relief=RIDGE)
MainFrame.grid(row=1,column=0,padx=15)

# Left Frame or we can say left box
LeftFrame = Frame(MainFrame,bd = 10,bg = "Cadet Blue",width = 750,height = 500,relief=RIDGE,padx=10,pady=2)
LeftFrame.pack(side=LEFT) 

# Right Frame or we can say right box
RightFrame = Frame(MainFrame,bd = 10,bg = "Cadet Blue",width = 560,height = 500,relief=RIDGE,padx=10,pady=2)
RightFrame.pack(side=RIGHT)

#  right sub boxes
RightFrame1 = Frame(RightFrame,bd = 10,bg = "Cadet Blue",width = 560,height = 200,relief=RIDGE,padx=10,pady=2)
RightFrame1.grid(row=0,column=0)

RightFrame2 = Frame(RightFrame,bd = 10,bg = "Cadet Blue",width = 560,height = 200,relief=RIDGE,padx=10,pady=2)
RightFrame2.grid(row=1,column=0)

#  Reset and Newgame Button
btnReset = Button(RightFrame2,text="Reset",font = "arial 38 bold",height=1,width=20,bg = "gainsboro",command=reset)
btnReset.grid(row = 0,column=0,padx=6,pady=10)
  
btnNewgame = Button(RightFrame2,text="New Game",font = "arial 38 bold",height=1,width=20,bg = "gainsboro",command=newgame)
btnNewgame.grid(row = 1,column=0,padx=6,pady=10)

# variable assignment
playerx = IntVar()
playero = IntVar()

playerx.set(0)
playero.set(0)

buttons = StringVar()
click = True




# Here I am using dnested for loop for making grid of 3 X 3
# for i in range(3):
#     for j in range(3):
#         n = "button" + str(i+j)
#         n = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(n))
#         n.grid(row = i,column=j,sticky=S+N+E+W)

b1 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b1),padx = 1)
b1.grid(row = 0,column=0,sticky=S+N+E+W)

b2 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b2),padx = 1)
b2.grid(row = 0,column=1,sticky=S+N+E+W)

b3 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b3),padx = 1)
b3.grid(row = 0,column=2,sticky=S+N+E+W)

b4 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b4),padx = 1)
b4.grid(row = 1,column=0,sticky=S+N+E+W)

b5 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b5),padx = 1)
b5.grid(row = 1,column=1,sticky=S+N+E+W)

b6 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b6),padx = 1)
b6.grid(row = 1,column=2,sticky=S+N+E+W)

b7 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b7),padx = 1)
b7.grid(row = 2,column=0,sticky=S+N+E+W)

b8 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b8),padx = 1)
b8.grid(row = 2,column=1,sticky=S+N+E+W)

b9 = Button(LeftFrame,text=" ",font = "Times 26 bold",height=3,width=8,bg = "gainsboro",command=lambda:checker(b9),padx = 1)
b9.grid(row = 2,column=2,sticky=S+N+E+W)

# Score of player 1 who is taking "X"
lblplayerx = Label(RightFrame1,font = "arial 40 bold",text = "Player X",bg = "Cadet Blue",fg = "white",justify=CENTER)
lblplayerx.grid(row=0,column=0,sticky=W)

txtplayerx = Entry(RightFrame1,font = "arial 40 bold",bd = 2,textvariable=playerx,width=14,justify=LEFT).grid(row = 0,column=1)

# Score of player 2 who is taking "O"
lblplayero = Label(RightFrame1,font = "arial 40 bold",text = "Player O",bg = "Cadet Blue",fg = "white",justify=CENTER)
lblplayero.grid(row=1,column=0,sticky=W)

txtplayero = Entry(RightFrame1,font = "arial 40 bold",bd = 2,textvariable=playero,width=14,justify=LEFT).grid(row = 1,column=1)

root.mainloop()