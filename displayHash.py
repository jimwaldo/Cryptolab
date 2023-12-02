import tkinter as tk
from tkinter import Label, Entry, Button
import hashlib

# Function to calculate SHA-256 hash
def calculate_hash():
    input_text = input_entry.get()
    sha256_hash = hashlib.sha256(input_text.encode()).hexdigest()
    hash_label.config(text=sha256_hash)

# Create the main window
window = tk.Tk()
window.title("SHA-256 Hash Calculator")

# Create a label and an entry field for input
input_label = Label(window, text="Enter a string:")
input_label.pack()
input_entry = Entry(window)
input_entry.pack()

# Create a button to trigger hash calculation
calculate_button = Button(window, text="Calculate Hash", command=calculate_hash)
calculate_button.pack()

# Create a label to display the hash result
hash_label = Label(window, text="", wraplength=400)
hash_label.pack()

# Start the tkinter main loop
window.mainloop()
