from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Click Success")
    myLabel.pack()

myButton = Button(root, text = "Click Me", padx=50, command=myClick, fg = "red")

myButton.pack()


root.mainloop()
