import json
import pyttsx3
from difflib import get_close_matches
import tkinter.messagebox as tm
import tkinter as tk

data=json.load(open("python project\data.json"))
root = tk.Tk()
engine = pyttsx3.init()
# function which gives the result 

def extract(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        val = tm.askyesno("Help...","Did you mean %s"%get_close_matches(word,data.keys())[0])
        if val==True:
            return data[get_close_matches(word,data.keys())[0]]
        else:
            print("\nSorry....,Vidhan Sir I am Unable to Find")
            engine.say("Sorry Vidhan Sir, I am Unable to Find Your given word")
            engine.runAndWait()
            engine.stop()
            return None
    else:
        print("\nThe word doesnt Exit")
        engine.say("The word doesnt Exit")
        engine.runAndWait()
        engine.stop()
        return None

def callans(word):
    global data
    
    engine.setProperty("rate",125)
    # 125 parameter how fast you wnat to speek or listen 
    # 125 words per min 
    val2=True 
    while val2:
        to_search = word.lower()

        result_str = ""
        result1 = extract(to_search)
        if result1 == None:
            val2 = tm.askyesno("Hello...","Do you Want to continue...") 
            # c=input("Do you Want to continue...\nType: 'y' for Yes ans 'n' for No")
            if val2 == True:
                val2 = False
                pass
            else:
                exit()

        else: 
            for i in range(len(result1)):
                result_str+= result1[i]
                result_str+= " "
            x = result_str.split(". ")
            for i in x:
                print("\n",i)

            engine.say(result_str)
            engine.runAndWait()
            engine.stop()

            # c = input("Do you Want to continue...\nType: 'y' for Yes ans 'n' for No")
            val2 = tm.askyesno("Hello...","Do you Want to continue...")
            if val2==True:
                val2 = False
                pass
            else:
                exit()

def call():
    callans(searchvalue.get())


root.title("My Dictionary")
root.geometry("500x300+500+200")
root.minsize(500,300)
tk.Label(text = "Enter the Word that you want to Search",font = 40,pady=20).pack()
searchvalue = tk.StringVar()
# tk.Entry(root,textvariable = searchvalue).place(x=500,y=155,width=150,height=40)
tk.Entry(root,textvariable = searchvalue,font = 10).pack(pady=10)

tk.Button(text = "Search",font = 25,command=call).pack(padx=5,pady=10) 
root.mainloop()