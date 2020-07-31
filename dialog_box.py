from tkinter import *
from tkinter import filedialog


root = Tk()
root.title("Dialog Box")
root.geometry("400x600")




root.filename = filedialog.askopenfilename(initialdir="/home/shyam", title="Select files")


root.mainloop()
