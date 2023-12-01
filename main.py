from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = site_input.get()
    username_value = username_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or len(username_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Opps", message="You cant leave fields blank")
    else:

        is_ok = messagebox.askokcancel(title=website_value,
                                       message=f"These are the details entered: \nEmail: {username_value}\nPassword:"
                                               f"{password_value}\nIs it ok to save?")

        if is_ok:
            print(f"site: {website_value}, username: {username_value}, password: {password_value}")
            f = open("data.txt", "a")
            f.write(f"site: {website_value}| username: {username_value}| password: {password_value}\n")
            f.close()
            site_input.delete(0, END)
            password_input.delete(0, END)


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
site_input.focus()
site_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Username / Email:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(END, "aad3rinto@gmail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", width=11, command=generate_password)
password_button.grid(row=3, column=2)

add_to_list_button = Button(text="Add", width=33, command=save)
add_to_list_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
