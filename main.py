from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Email: {email}\n"
                                                      f"Password: {password}\n"
                                                      f"Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

logo_canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", background="white")
email_label = Label(text="Email/Username:", background="white")
password_label = Label(text="Password:", background="white")

# Labels Grid
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=45)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.insert(0, "michael.drummond328@gmail.com")
password_entry = Entry(width=25)
generate_btn = Button(text="Generate Password", width=15, command=generate_password)

# Entries Grid
website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=45, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()