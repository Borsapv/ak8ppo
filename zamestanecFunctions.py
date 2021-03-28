import sqlite3
from tkinter import *


# Save a new employee entry
def add_employee(name,last_name,mail_work,mail_private,phone_number):
    # connection to database
    conn = sqlite3.connect("tajemnik.db")

    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO zamestnanec(name, last_name, mail_work, mail_private, phone_number) VALUES(?,?,?,?,?)", (name, last_name, mail_work, mail_private, phone_number))

    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# Save a new subject entry
def add_subject(name, hours, id):
    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO predmet(name, pocet_hodin, id_employee) VALUES(?,?,?)",
              (name, hours, id))

    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# Show all from zamestnanec table
def show_all_employees():

    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM zamestnanec")
    items = c.fetchall()

    for item in items:
        item_lbl = Label(root, text=item)
        item_lbl.pack()


    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

# Show all from zamestnanec table
def show_all_subjects():
    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    conn.execute("PRAGMA foreign_keys = 1")
    # create cursor
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM predmet")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit commands
    conn.commit()

    # Close connection
    conn.close()