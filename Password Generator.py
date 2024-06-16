import tkinter as tk
from tkinter import messagebox
import random
import string

MAX_LENGTH = 16


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def on_generate():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return
        elif length > MAX_LENGTH:
            messagebox.showerror("Error", f"Password length must be less than or equal to {MAX_LENGTH}.")
            return

        password = generate_password(length)

        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def copy_to_clipboard():
    password = output_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Info", "Password copied to clipboard!")

    length_entry.delete(0, tk.END)
    output_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.resizable(0, 0)

tk.Label(root, text="Enter desired length (max 16):").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=30)
output_entry.grid(row=2, column=1, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
