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

#function to clear fields
def clear_fields():
    course_abbr_box.delete(0, END)
    course_name_box.delete(0, END)
    weeks_box.delete(0, END)
    hours_p_box.delete(0, END)
    hours_c_box.delete(0, END)
    hours_s_box.delete(0, END)
    completion_type_box.delete(0, END)
    language_box.delete(0, END)
    max_students_box.delete(0, END)

#function to create stitky from new course into the database, commit changes and clear form.
def create_stitky():
    if hours_c_box.get():
        Q1 = "INSERT INTO stitky (course_name, course_type, language, hours, completion_type, students) VALUES (%s, %s, %s, %s, %s, %s)"
        course_name = "Cvičení z " + course_abbr_box.get()
        hours = int(weeks_box.get())*int(hours_c_box.get())
        course_type = "cvičení"
        stitky_values = (course_name, course_type, language_box.get(), hours, completion_type_box.get(), max_students_box.get())
        c.execute(Q1, stitky_values)

    if hours_p_box.get():
        Q2 = "INSERT INTO stitky (course_name, course_type, language, hours, completion_type, students) VALUES (%s, %s, %s, %s, %s, %s)"
        course_name = "Přednášky z " + course_abbr_box.get()
        hours = int(weeks_box.get()) * int(hours_p_box.get())
        course_type = "přednášky"
        stitky_values = (course_name, course_type, language_box.get(), hours, completion_type_box.get(), max_students_box.get())
        c.execute(Q2, stitky_values)

    if int(hours_s_box.get()) > 0:
        Q3 = "INSERT INTO stitky (course_name, course_type, language, hours, completion_type, students) VALUES (%s, %s, %s, %s, %s, %s)"
        course_name = "Semináře z " + course_abbr_box.get()
        hours = int(weeks_box.get()) * int(hours_s_box.get())
        course_type = "semináře"
        stitky_values = (course_name, course_type, language_box.get(), hours, completion_type_box.get(), max_students_box.get())
        c.execute(Q3, stitky_values)

    mydb.commit()
    clear_fields()

#function to add a new course into the database, commit changes and clear form.
def add_course():
    sql_cmd = "INSERT INTO courses (course_abbr, course_name, weeks, hours_p, hours_c, hours_s, completion_type, language, max_students) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (course_abbr_box.get(), course_name_box.get(), weeks_box.get(), hours_p_box.get(), hours_c_box.get(), hours_s_box.get(), completion_type_box.get(), language_box.get(),max_students_box.get())

    c.execute(sql_cmd, values)

    create_stitky()

    mydb.commit()
    clear_fields()

#function to show all courses in new form.
def show_courses():
    employees_screen = Tk()
    employees_screen.title("Seznam předmětů")
    employees_screen.geometry("600x400")

    c.execute("SELECT * FROM courses")
    courses_table = c.fetchall()

    for index, cou in enumerate(courses_table):
        col = 0
        for co in cou:
            emp_list = Label(employees_screen, text=co)
            emp_list.grid(row=index+1, column=col, padx=5, stick=W)
            col += 1

#function to show all stitky related to a selected course.
def show_course_stitky():
    # get ID zadane uzivatelem
    # vytvorit novy screen
    # select * from stitky where id
    #
    #
    #
    return

    c.execute("SELECT * FROM stitky")
    table = c.fetchall()
    for col in table:
        print(col)


def show_stitky():
    c.execute("SELECT * FROM stitky")
    table = c.fetchall()
    for col in table:
        print(col)

#create a title label
title_label = Label(root, text="Předměty", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#create main form (labels, entry boxes and buttons)
course_abbr_label = Label(root, text="Zkratka").grid(row=1, column=0, sticky=W, padx=10)
course_name_label = Label(root, text="Název").grid(row=2, column=0, sticky=W, padx=10)
weeks_label = Label(root, text="Počet týdnů").grid(row=3, column=0, sticky=W, padx=10)
hours_p_label = Label(root, text="Hodin přednášek").grid(row=4, column=0, sticky=W, padx=10)
hours_c_label = Label(root, text="Hodin cvičení").grid(row=5, column=0, sticky=W, padx=10)
hours_s_label = Label(root, text="Hodin seminářů").grid(row=6, column=0, sticky=W, padx=10)
completion_type_label = Label(root, text="Způsob zakončení").grid(row=7, column=0, sticky=W, padx=10)
language_label = Label(root, text="Jazyk").grid(row=8, column=0, sticky=W, padx=10)
max_students_label = Label(root, text="Kapacita studentů").grid(row=9, column=0, sticky=W, padx=10)

course_abbr_box = Entry(root)
course_abbr_box.grid(row=1, column=1, pady=5)
course_name_box = Entry(root)
course_name_box.grid(row=2, column=1, pady=5)
weeks_box = Entry(root)
weeks_box.grid(row=3, column=1, pady=5)
hours_p_box = Entry(root)
hours_p_box.grid(row=4, column=1, pady=5)
hours_c_box = Entry(root)
hours_c_box.grid(row=5, column=1, pady=5)
hours_s_box = Entry(root)
hours_s_box.grid(row=6, column=1, pady=5)
completion_type_box = Entry(root)
completion_type_box.grid(row=7, column=1, pady=5)
language_box = Entry(root)
language_box.grid(row=8, column=1, pady=5)
max_students_box = Entry(root)
max_students_box.grid(row=9, column=1, pady=5)

add_course_btn = Button(root, text="Přidat předmět", command=add_course)
add_course_btn.grid(row=10, column=0, padx=10, pady=10)
show_courses_btn = Button(root, text="Zobrazit všechny", command=show_courses)
show_courses_btn.grid(row=11, column=0, sticky=W, padx=10)

show_stitky()

root.mainloop()