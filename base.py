from tkinter import *

root = Tk()
root.title("New Window")




def open():
    
    top  = Toplevel()
    lbl = Label(top, text="hello world").pack()

btn = Button(root, text="Open New Window",command=open).pack()




root.mainloop()
