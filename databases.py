from tkinter import *
import sqlite3



root = Tk()
root.title("Databases")
root.geometry("700x700")



#Databases




#Create table
'''c.execute("""CREATE TABLE addresses (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")
'''

#Create Submit Function for databases
def submit():
    #Create a database of connect to one
    conn = sqlite3.connect('adddress_book.db')
    
    #Create cursor
    c = conn.cursor()
    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            }


    
    #Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



    #Create text Boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20)

    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1)

    address = Entry(root, width=30)
    address.grid(row=2, column=1)

    city = Entry(root, width=30)
    city.grid(row=3, column=1)

    state = Entry(root, width=30)
    state.grid(row=4, column=1)

    zipcode = Entry(root, width=30)
    zipcode.grid(row=5, column=1)


#Create text boxes labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)


#Create Submit Button
submit_button = Button(root, text="Add Record To Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create a Query Button
query_btn = Button(root, text="Show  Records", command = query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
            






#Commit changes
conn.commit()

#Close Connections
conn.close()
              











root.mainloop()
