from tkinter import *
import sqlite3



root = Tk()
root.title("Databases")
root.geometry("700x700")



#Databases

#Create a database of connect to one
conn = sqlite3.connect('adddress_book.db')


#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE addresses (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")




#Commit changes
conn.commit()

#Close Connections
conn.close()





root.mainloop()
