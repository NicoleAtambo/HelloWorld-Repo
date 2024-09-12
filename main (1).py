# # Nicole, Ugo and Bryan
# #OOPS Implemented
# #1st Part(Classes)
# import os.path
# import random
# import string

# class Password:
#     def __init__(self, username, password, website):
#         self.username = username
#         self.password = password
#         self.website = website

#     def __str__(self):
#         return f"UserName: {self.username}\nPassword: {self.password}\nWebsite: {self.website}\n"

# class PasswordManager:
#     def __init__(self):
#         self.passwords = []

#     def check_existence(self):
#         if os.path.exists("info.txt"):
#             pass
#         else:
#             file = open("info.txt", 'w')
#             file.close()

#     def save_password(self, password):
#         # This function will allow the user to input new password and save it in the txt file
#         file = open("info.txt", 'a')

#         file.write(" \n")
#         file.write(str(password))
#         file.write(" \n")
#         file.write("\n")
#         file.close()

#     def read_passwords(self):
#         file = open('info.txt', 'r')
#         content = file.read()
#         file.close()
#         print(content)

#     def find_password_by_username(self, username):
#         with open('info.txt', 'r') as file:
#             lines = file.readlines()
#             for i in range(0, len(lines), 4):
#                 # Check if the username matches
#                 if lines[i+1].strip() == f"UserName: {username}":
#                     return lines[i+3].strip()[len("Password: "):]
#             return None

# class RandomWebsite:
#     def __init__(self, length):
#         self.length = length

#     def generate_website(self):
#         # generate a random website name
#         letters = string.ascii_lowercase
#         website = ''.join(random.choice(letters) for i in range(self.length))
#         return f"http://www.{website}.com"

# class EncryptedPassword(Password):
#     def __init__(self, username, password, website, key):
#         super().__init__(username, password, website)
#         self.key = key

#     def decrypt_password(self):
#         # decrypt the password using the key
#         return self.password - self.key

#     def encrypt_password(self):
#         #this is to hide the password so that it can be read during decryption
#         # encrypt the password using the key
#         self.password = self.password + self.key
# #2nd Part(Password Generation)
# def generate_strong_password():
#     length = 16
#     letters = string.ascii_letters
#     digits = string.digits
#     special_chars = string.punctuation

#     # shuffle the characters and choose a random subset
#     characters = random.sample(letters + digits + special_chars, length)

#     # convert the subset to a string and return it
#     password = ''.join(characters)
#     return password
# #3rd Part(Main Program)
# if __name__ == "__main__":
#     pm = PasswordManager()
#     pm.check_existence()
#     rw = RandomWebsite(8)

#     while True:
#         print("What do you want to do?")
#         print("1. Save new password")
#         print("2. Read saved passwords")
#         # print("3. See forgotten password")
#         print("3. Generate a strong password")
#         print("4. Quit")

#         choice = input("Enter your choice (1/2/3/4/5): ")

#         if choice == '1':
#             username = input("Please enter the user name: ")
#             password = input("Please enter the password here: ")
#             website = rw.generate_website()
#             p = Password(username, password, website)
#             pm.save_password(p)
#         elif choice == '2':
#             pm.read_passwords()
        
#         elif choice == '3':
#             password = generate_strong_password()
#             print(f'Your new password is:(password)')
#             username = input("Please enter the user name: ")
#             website = rw.generate_website()
#             p = Password(username, password, website)
#             pm.save_password(p)
#         elif choice == '4':
#             print("Thanks For Using The YBNL Generator")
#             break
#         else:
#             print("Invalid coice, please try again.")

#DESKTOP APP VERSION

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


