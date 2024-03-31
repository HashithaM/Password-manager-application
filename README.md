# Password-manager-application
This is a simple password manager application with saving and searching facilities
This code is a simple Password Manager application built using Tkinter, a standard GUI (Graphical User Interface) toolkit for Python. Let's break down its components:

Password Generator Function (generate_password):

This function generates a random password consisting of letters, numbers, and symbols. The length of the password varies between 8 to 10 characters for letters, and 2 to 4 characters each for symbols and numbers.
The pyperclip module is used to copy the generated password to the clipboard.
Save Password Function (save):

This function saves the website, email, and password entered by the user into a JSON file named "data.json".
It first checks if the website and password fields are not empty. If any of them are empty, it displays an error message.
If the fields are not empty, it prompts the user to confirm whether they want to save the entered details.
If the user confirms, it either creates a new JSON file or updates the existing one with the new data.
Find Password Function (find_password):

This function retrieves the password associated with a given website from the JSON file.
It first checks if the JSON file exists. If not, it displays an error message.
If the file exists, it checks if the entered website exists in the data. If it does, it retrieves the email and password associated with it and displays them. If not, it displays an error message.
User Interface Setup (UI SETUP):

It sets up the Tkinter window with a title "Password Manager" and padding.
It creates a canvas to display an image (a logo).
Labels, entry fields, and buttons are created for website, email, password entry, and password generation.
The buttons are associated with their respective functions (generate password, save password, find password).
Main Loop (window.mainloop()):

This starts the Tkinter event loop, which listens for user actions and updates the GUI accordingly.
Overall, this code provides a simple interface for generating, saving, and retrieving passwords associated with different websites.
