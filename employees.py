from tkinter import *
import mysql.connector



# connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="testovaciHeslo1*",
    database="tajemnik"
)

# create a cursor
c = mydb.cursor()

# function to show stitky needs to be asigned
def unassigned_stitky():
    return

# function to show stitky related to assigned to emploeyy
def unassigned_stitky():
    return

# function to show employee detail
def employee_detail(employee_id):
    # SQL
    sql_cmd = "SELECT * FROM zamestnanci WHERE empl_id = %s"
    c.execute(sql_cmd, (employee_id,))
    details = c.fetchall()

    # First and last name for title
    for title in details:
        name = title[1] + " " + title[2]

    detail_screen = Tk()
    detail_screen.title(name)
    detail_screen.geometry("400x400")

    # show list of employees related to ID (should be one)
    for num, detail in enumerate(details):
        col2 = 0
        for det in detail:
            det_list = Label(detail_screen, text=det)
            det_list.grid(row=num, column=col2, padx=5, stick=W)
            col2 += 1


# show all employees
def show_all_employees():
    employees_screen = Tk()
    employees_screen.title("Seznam zaměstnanců")
    employees_screen.geometry("600x400")

    id_label = Label(employees_screen, text="ID")
    id_label.grid(row=0, column=0)

    c.execute("SELECT * FROM zamestnanci")
    employees = c.fetchall()
    rows = 1

    for index, emp in enumerate(employees):
        col = 0
        for em in emp:
            emp_list = Label(employees_screen, text=em)
            emp_list.grid(row=index + 1, column=col, padx=5, stick=W)
            col += 1
            rows += 1
    choose_lbl = Label(employees_screen, text="Zadejte ID").grid(row=rows, column=0, columnspan="2")

    choose_box = Entry(employees_screen, width="5")
    choose_box.grid(row=rows, column=2, columnspan="3")
    choose_btn = Button(employees_screen, text="Zobrazit zaměstnance", command=lambda: employee_detail(choose_box.get()))
    choose_btn.grid(row=rows, column=5, columnspan="3")



