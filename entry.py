from tkinter import *

root = Tk()


e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name: ", command=myClick)
myButton.pack()




root.mainloop()
