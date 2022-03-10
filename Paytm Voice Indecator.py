from tkinter import *
import pyttsx3
import tkinter.messagebox as tm

def pay():
    x = amountvar.get()
    if x==0:
        tm.showerror("Error","Please Enter Amount")
    else:
        val = tm.askyesnocancel("Alert","Do you want you Continue you Payment of %d"%(x))
        if val:    
            print(x)
            engine = pyttsx3.init()
            engine.setProperty("rate",130)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            
            engine.say('Attention! Mr Vidhan Rathore %d ruppes is credited in your account'%(amountvar.get()))
            engine.runAndWait()
        else:
            tm.showwarning("Retry","Your Payment has Canceled")





root = Tk()
root.title("My Paytm Voice")
Label(text = "Paytm Voice Indicator",font = "serif 25 bold").pack(fill= X)
root.geometry("500x300+500+200")
root.minsize(500,300)

# Label for message
amount = Label(root,text="Enter Your Amount",font = "serif 15 bold")
amount.pack(pady = 10)

# input box
amountvar = IntVar()
Entry(root, textvariable=amountvar,font="serif 15").pack()

# button
Button(text = "Pay" ,command = pay,font = "_ 12 bold",padx= 10,pady=0).pack(padx= 10,pady=10)
# amountvar = 0





root.mainloop()