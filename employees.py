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

# function to show stitky related to assigned to employee
def assigned_stitky():
    return


# function to assign stitek to employee
def assign_stitek(employee_id, assign_box):
    sql_cmd = "UPDATE stitky SET empl_id = %s WHERE stitek_ID = %s"
    c.execute(sql_cmd, (employee_id, assign_box,))

    test_sql_cmd = "SELECT * FROM stitky WHERE empl_id = %s"
    c.execute(test_sql_cmd, (employee_id,))
    assigned = c.fetchall()
    for ass in assigned:
        print(ass)

    mydb.commit()

# function to show stitky needs to be assigned
def unassigned_stitky(screen, num, employee_id):
    num += 1
    volne_stitky_lbl = Label(screen, text="Nepřiřazené štítky").grid(row=num, column=0, columnspan=2, pady=15)

    c.execute("SELECT * FROM stitky")
    table = c.fetchall()
    for st_num, stitek in enumerate(table):
        col3 = 0
        num += 1
        for stit in stitek:
            stit_list = Label(screen, text=stit)
            stit_list.grid(row=num, column=col3, padx=5, stick=W)
            col3 += 1

    num += 1
    # button to assign stitek
    assign_lbl = Label(screen, text="ID štítku")
    assign_lbl.grid(row=num, column=0, columnspan="2", stick=W)
    assign_box = Entry(screen, width="5")
    assign_box.grid(row=num, column=2, stick=W)
    assign_btn = Button(screen, text="Potvrdit", command=lambda: assign_stitek(employee_id, assign_box.get()))
    assign_btn.grid(row=num, column=3, columnspan="2", stick=W)


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
    detail_screen.geometry("600x400")

    # show list of employees related to ID (should be one)
    for num, detail in enumerate(details):
        col2 = 0
        for det in detail:
            det_list = Label(detail_screen, text=det)
            det_list.grid(row=num, column=col2, padx=5, stick=W)
            col2 += 1

    unassigned_stitky(detail_screen, num, employee_id)

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



