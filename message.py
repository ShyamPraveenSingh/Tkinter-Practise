from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Messages Box")

def popup():
    messagebox.askyesno("This is a popup", "Hello World")
    Label(root, text=response).pack()

Button(root, text="Popup", command = popup).pack()





root.mainloop()
