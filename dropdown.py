from tkinter import *


root = Tk()
root.title("Dropdown Menus")
root.geometry("600x600")


#Dropdown
def show():
    lbl = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options).pack()

btn = Button(root, text="Show Selection", command=show).pack()








root.mainloop()
