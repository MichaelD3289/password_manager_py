from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new_data
            data.update(new_data)
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_passwords():
    website = website_entry.get().lower()
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="You have no saved passwords. Add some now!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"You don't have a saved password for {website}. Add one now!")


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
website_entry = Entry(width=25)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.insert(0, "michael.drummond328@gmail.com")
password_entry = Entry(width=25)


# Entries Grid
website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

# Buttons
add_btn = Button(text="Add", width=45, command=save_password)
generate_btn = Button(text="Generate Password", width=15, command=generate_password)
search_btn = Button(text="Search", width=15, command=search_passwords)

# Buttons Grid
add_btn.grid(row=4, column=1, columnspan=2)
generate_btn.grid(row=3, column=2)
search_btn.grid(row=1, column=2)

window.mainloop()
