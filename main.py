from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Agba")
window.config(pady=20, padx=20)
key_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, )
canvas.create_image(100, 100, image=key_img)
canvas.pack()

window.mainloop()
