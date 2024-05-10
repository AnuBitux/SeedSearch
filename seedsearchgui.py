import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_directory():
    directory_path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory_path)

def start_tool():
    directory_path = directory_entry.get()
    if directory_path:
        command = f'/opt/Tools/Recovery/SeedSearch/ssve/bin/python3 /opt/Tools/Recovery/SeedSearch/seedsearch.py -d {directory_path}'
        os.system(command)
        root.destroy()


# Create main window
root = tk.Tk()
root.title("BIP39 Mnemonic Search")

# Create widgets
directory_label = tk.Label(root, text="Directory to scan:")
directory_label.grid(row=0, column=0, padx=10, pady=5)

directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=10, pady=5)

select_button = tk.Button(root, text="Select Directory", command=select_directory, bg="black", fg="blue")
select_button.grid(row=0, column=2, padx=10, pady=5)

start_button = tk.Button(root, text="GO!", command=start_tool, bg="black", fg="blue")
start_button.grid(row=1, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
