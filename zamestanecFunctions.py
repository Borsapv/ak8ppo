import sqlite3

def set_connection():
    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    # create cursor
    c = conn.cursor()

def close_connection():
    # Commit commands
    conn.commit()

    # Close connection
    conn.close()

def add_employee(name,last_name,mail_work,private_work,phone_number):
    # connection to database
    conn = sqlite3.connect("tajemnik.db")
    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO tajemnik VALUES(?,?,?,?,?)", (name, last_name, mail_work, private_work, phone_number))

    # Commit commands
    conn.commit()

    # Close connection
    conn.close()


