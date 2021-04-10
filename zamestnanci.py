from tkinter import *
import mysql.connector

#basic settings for form window
root = Tk()
root.title("Nový zaměstnanec")
root.geometry("300x400")

#connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="testovaciHeslo1*",
    database="tajemnik"
)

#create a cursor
c = mydb.cursor()

#function to cleare form
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    work_email_box.delete(0, END)
    private_email_box.delete(0, END)
    phone_number_box.delete(0, END)

#function to add a new employee into the database, commit changes and clear form.
def add_employee():
    sql_cmd = "INSERT INTO zamestnanci (first_name, last_name, work_mail, private_mail, phone_num) VALUES (%s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), work_email_box.get(), private_email_box.get(), phone_number_box.get())

    c.execute(sql_cmd, values)

    mydb.commit()
    clear_fields()

#function to show all employees
def show_employees():
    employees_screen = Tk()
    employees_screen.title("Seznam zaměstnanců")
    employees_screen.geometry("600x400")

    id_label = Label(employees_screen, text="ID")
    id_label.grid(row=0, column=5)

    c.execute("SELECT * FROM zamestnanci")
    employees = c.fetchall()

    for index, emp in enumerate(employees):
        col = 0
        for em in emp:
            emp_list = Label(employees_screen, text=em)
            emp_list.grid(row=index+1, column=col, padx=5, stick=W)
            col += 1

'''
#function to search employee
def search_employee():
    return
'''

#create a title label
title_label = Label(root, text="Zaměstnanci", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#create main form (labels, entry boxes and buttons)
first_name_label = Label(root, text="Jméno").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Příjmení").grid(row=2, column=0, sticky=W, padx=10)
work_email_label = Label(root, text="Pracovní email").grid(row=3, column=0, sticky=W, padx=10)
private_email_label = Label(root, text="Soukromý email").grid(row=4, column=0, sticky=W, padx=10)
phone_number_label = Label(root, text="Telefonní číslo").grid(row=5, column=0, sticky=W, padx=10)

first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)
last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)
work_email_box = Entry(root)
work_email_box.grid(row=3, column=1, pady=5)
private_email_box = Entry(root)
private_email_box.grid(row=4, column=1, pady=5)
phone_number_box = Entry(root)
phone_number_box.grid(row=5, column=1, pady=5)

add_employee_btn = Button(root, text="Přidat zaměstnance", command=add_employee)
add_employee_btn.grid(row=6, column=0, padx=10, pady=10)
clear_fields_btn = Button(root, text="Vymazat", command=clear_fields)
clear_fields_btn.grid(row=6, column=1)
show_employees_btn = Button(root, text="Zobrazit všechny", command=show_employees)
show_employees_btn.grid(row=7, column=0, sticky=W, padx=10)

''' #Vyhrazeno do budoucna
search_employee_btn = Button(root, text="vyhledat zaměstnance", command=search_employee)
search_employee_btn.grid (row=7, column=1)
'''

root.mainloop()