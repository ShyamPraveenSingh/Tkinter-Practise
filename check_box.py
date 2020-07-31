from tkinter import *


root=Tk()
root.title("Check")
root.geometry("700x700")


def show():
    myLabel = Label(root, text=var.get()).pack()
    




var = StringVar()


c = Checkbutton(root, text="Check me out",variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()




myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()
