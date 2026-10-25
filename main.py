import json
import secrets
import string
from tkinter import *
from tkinter import messagebox

import keyring
import pyperclip
from keyring.errors import KeyringError


SERVICE_NAME = "hashitham-password-manager"
PASSWORD_LENGTH = 16
PASSWORD_ALPHABET = string.ascii_letters + string.digits + "!#$%&()*+"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():
    while True:
        password = "".join(secrets.choice(PASSWORD_ALPHABET) for _ in range(PASSWORD_LENGTH))
        if (any(char.islower() for char in password)
                and any(char.isupper() for char in password)
                and any(char.isdigit() for char in password)
                and any(char in "!#$%&()*+" for char in password)):
            break

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Save the credential for {email} in the operating system's secure credential vault?",
    )
    if not is_ok:
        return

    credential = json.dumps({"email": email, "password": password})
    try:
        keyring.set_password(SERVICE_NAME, website, credential)
    except KeyringError as error:
        messagebox.showerror(title="Credential vault error", message=str(error))
        return

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ------------------- Find password ---------------------------------- #


def find_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showinfo(title="Oops", message="Enter a website before searching.")
        return

    try:
        stored_credential = keyring.get_password(SERVICE_NAME, website)
    except KeyringError as error:
        messagebox.showerror(title="Credential vault error", message=str(error))
        return

    if stored_credential is None:
        messagebox.showinfo(title="Error", message=f"No detail for {website} exists!")
        website_entry.delete(0, END)
        return

    try:
        credential = json.loads(stored_credential)
        email = credential["email"]
        password = credential["password"]
    except (json.JSONDecodeError, KeyError, TypeError):
        messagebox.showerror(title="Credential vault error", message="The stored record is invalid.")
        return

    pyperclip.copy(password)
    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword copied to the clipboard.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user@example.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search",width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()


# File not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
#     print("This is try part")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("This is file not found part")
# except KeyError as error_message:
#     print(f"That key {error_message}does not exist")
#     print("This is key error part")
# else:
#     content = file.read()
#     print(content)
#     print("This is else part")
# finally:
#     file.close()
#     print("This is finally part")
    # raise TypeError("This is an error that I made up")

# height = float(input("Height :"))
# weight = int(input("Weight :"))

# if height > 3:
#     raise TypeError("Human height should not be over than 3 meters.")

# bmi = weight / height ** 2
# print(bmi)


# fruits = ["Apple", "Pear", "Orange"]

# # TODO: Catch the exception and make sure the code runs without crashing.


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         # post["Likes"] = 0
#         # total_likes += 0
#         pass


# print(total_likes)

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# import pandas

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry only letters in the alphabet please !")
#         generate_phonetic()
#     else:
#         print(output_list)


# generate_phonetic()


