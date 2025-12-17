import tkinter as tk
import random
import string
from tkinter import messagebox


def generate_password():
    length = entry_length.get()

    if length == "":
        messagebox.showerror("Error", "Please enter password length")
        return

    length = int(length)

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")
root.config(bg="#f4f6f8")


tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8"
).pack(pady=20)


frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(pady=10, padx=20)

tk.Label(frame, text="Enter Password Length", bg="white").pack(pady=5)

entry_length = tk.Entry(frame, width=20)
entry_length.pack(pady=5)

tk.Button(
    frame,
    text="Generate Password",
    bg="#4CAF50",
    fg="white",
    width=20,
    command=generate_password
).pack(pady=15)


tk.Label(root, text="Generated Password", bg="#f4f6f8").pack(pady=5)

entry_password = tk.Entry(root, width=35, font=("Arial", 12))
entry_password.pack(pady=5)

root.mainloop()
