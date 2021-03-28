from tkinter import *
import zamestanecFunctions
import sqlite3

#basic settings for form window
root = Tk()
root.title("Nový zaměstnanec")


# Show all employees (ID, first name, last name)
def show_employees():

    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM zamestnanec")
    items = c.fetchall()

    employees = ""
    for item in items:
        employees += str(str(item[0]) + " " + str(item[1]) + " " + item[2] + '\n')

    item_lbl = Label(root, text=employees)
    item_lbl.grid_forget()
    item_lbl.grid(row=20, columnspan=2)



    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# Function to save a new employee
def send_form():
    first = name_inpt.get()
    last = last_name_inpt.get()
    work = mail_work_inpt.get()
    private = mail_private_inpt.get()
    phone = phone_number_inpt.get()

    zamestanecFunctions.add_employee(first, last, work, private, phone)

# Function to delete employee (by ID)
def delete_employee():

    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("DELETE from zamestnanec WHERE oid = " + chooser_inpt.get())
    show_employees()


    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# Function to show all subjects associated to employee
def show_employees_subject():

    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT * from predmet WHERE id_employee = " + chooser_inpt.get())
    subjects = c.fetchall()

    all_subjects = ""
    for subject in subjects:
        all_subjects += str(subject[1] + " " + str(subject[2]) + " hodin" + '\n')

    item_lbl = Label(root, text=all_subjects)
    item_lbl.grid_forget()
    item_lbl.grid(row=21, columnspan=2, pady=5)


    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# set fields and buttons
name_lbl = Label(root, text="Jméno")
name_inpt = Entry(root)

last_name_lbl = Label(root, text="Příjmení")
last_name_inpt = Entry(root)

mail_work_lbl = Label(root, text="Pracovní email")
mail_work_inpt = Entry(root)

mail_private_lbl = Label(root, text="Soukromý email")
mail_private_inpt = Entry(root)

phone_number_lbl = Label(root, text="Telefon")
phone_number_inpt = Entry(root)

save_btn = Button(root, text="Uložit", command=send_form)
save_btn.grid(row=5, column=0, columnspan=2, ipadx=100, pady=10)

show_btn = Button(root, text="Zobrazit všechny zaměstnance", command=show_employees)
show_btn.grid (row=6, column=0, columnspan=2, ipadx=34)

chooser_lbl = Label(root, text="Volba zaměstnance (ID)")
chooser_inpt = Entry(root)
chooser_lbl.grid(row=7, column=0)
chooser_inpt.grid(row=7, column=1)

delete_btn = Button(root, text="Smazat zvoleného zaměstnance", command=delete_employee)
delete_btn.grid (row=8, column=0, columnspan=2, ipadx=33, pady=5)

show_subjects_btn = Button(root, text="Předměty zvoleného zaměstnance", command=show_employees_subject)
show_subjects_btn.grid (row=9, column=0, columnspan=2, ipadx=27)

# place created fields on the screen - using grid system
name_lbl.grid(row=0, column=0)
name_inpt.grid(row=0, column=1, padx=20)

last_name_lbl.grid(row=1, column=0)
last_name_inpt.grid(row=1, column=1, padx=20)

mail_work_lbl.grid(row=2, column=0)
mail_work_inpt.grid(row=2, column=1, padx=20)

mail_private_lbl.grid(row=3, column=0)
mail_private_inpt.grid(row=3, column=1, padx=20)

phone_number_lbl.grid(row=4, column=0)
phone_number_inpt.grid(row=4, column=1, padx=20)





#main loop
root.mainloop()