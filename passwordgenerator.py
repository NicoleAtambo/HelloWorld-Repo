#password generator
import os.path
import random
import string
import tkinter as tk
from tkinter import messagebox

class Password:
    def __init__(self, username, password, website):
        self.username = username
        self.password = password
        self.website = website

    def __str__(self):
        return f"UserName: {self.username}\nPassword: {self.password}\nWebsite: {self.website}\n"

class PasswordManager:
    def __init__(self):
        self.passwords = []

    def check_existence(self):
        if os.path.exists("info.txt"):
            pass
        else:
            file = open("info.txt", 'w')
            file.close()

    def save_password(self, password):
        file = open("info.txt", 'a')
        file.write(" \n")
        file.write(str(password))
        file.write(" \n")
        file.write("\n")
        file.close()

    def read_passwords(self):
        file = open('info.txt', 'r')
        content = file.read()
        file.close()
        return content

    def find_password_by_username(self, username):
        with open('info.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                if lines[i+1].strip() == f"UserName: {username}":
                    return lines[i+3].strip()[len("Password: "):]
            return None

class RandomWebsite:
    def __init__(self, length):
        self.length = length

    def generate_website(self):
        letters = string.ascii_lowercase
        website = ''.join(random.choice(letters) for i in range(self.length))
        return f"http://www.{website}.com"

class EncryptedPassword(Password):
    def __init__(self, username, password, website, key):
        super().__init__(username, password, website)
        self.key = key

    def decrypt_password(self):
        return self.password - self.key

    def encrypt_password(self):
        self.password = self.password + self.key

def generate_strong_password():
    length = 16
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    characters = random.sample(letters + digits + special_chars, length)
    password = ''.join(characters)
    return password

def save_password():
    username = username_entry.get()
    password = password_entry.get()
    website = rw.generate_website()
    p = Password(username, password, website)
    pm.save_password(p)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo("Password Saved", "Password saved successfully!")

def read_passwords():
    passwords_text.delete(1.0, tk.END)
    content = pm.read_passwords()
    passwords_text.insert(tk.END, content)

def generate_and_save_password():
    password = generate_strong_password()
    username = username_entry.get()
    website = rw.generate_website()
    p = Password(username, password, website)
    pm.save_password(p)
    username_entry.delete(0, tk.END)
    messagebox.showinfo("Strong Password Generated", f"Your new password is: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Create instances of the PasswordManager and RandomWebsite classes
pm = PasswordManager()
pm.check_existence()
rw = RandomWebsite(8)

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="User Name:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Create buttons for actions
save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

generate_button = tk.Button(root, text="Generate Strong Password", command=generate_and_save_password)
generate_button.pack()

read_button = tk.Button(root, text="Read Saved Passwords", command=read_passwords)
read_button.pack()

# Create a text widget for displaying saved passwords
passwords_text = tk.Text(root, height=10, width=40)
passwords_text.pack()

# Start the main event loop
root.mainloop()


