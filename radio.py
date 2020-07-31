from tkinter import *

root = Tk()
root.title("Radio Buttons")

#r = IntVar()
#r.set("2")


def clicked(value):
    myLabel = Label(root, text = value).pack()





    
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set = ("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable = pizza, value=mode).pack(anchor=W)


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


myButton = Button(root, text= "Click Me!", command=lambda: clicked(pizza.get())).pack()




root.mainloop()
