from tkinter import *

#basic settings for form window
root = Tk()
root.title("Nový zaměstnanec")

def send_form():
    return

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

send_btn = Button(root, text="Uložit", command=send_form)


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

send_btn.grid(row=5, column=1)


#main loop
root.mainloop()