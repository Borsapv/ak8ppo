from tkinter import *
import zamestanecFunctions

#basic settings for form window
root = Tk()
root.title("Nový předmět")

def send_form():
    name = name_inpt.get()
    hours = hours_inpt.get()
    id = id_employee_inpt.get()

    zamestanecFunctions.add_subject(name, hours, id)

# set fields and buttons
name_lbl = Label(root, text="Jméno")
name_inpt = Entry(root)

hours_lbl = Label(root, text="Počet hodin")
hours_inpt = Entry(root)

id_employee_lbl = Label(root, text="ID_employee")
id_employee_inpt = Entry(root)



send_btn = Button(root, text="Uložit", command=send_form)


# place created fields on the screen - using grid system
name_lbl.grid(row=0, column=0)
name_inpt.grid(row=0, column=1, padx=20)

hours_lbl.grid(row=1, column=0)
hours_inpt.grid(row=1, column=1, padx=20)

id_employee_lbl.grid(row=2, column=0)
id_employee_inpt.grid(row=2, column=1, padx=20)


send_btn.grid(row=5, column=1)


#main loop
root.mainloop()