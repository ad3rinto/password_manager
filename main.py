from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Agba")
window.config(pady=50, padx=50)
key_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, )
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

site_input = Entry(width=35)
site_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Username / Email:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", width=11)
password_button.grid(row=3, column=2)

add_to_list_button = Button(text="Add", width=33)
add_to_list_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
