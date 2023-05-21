import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Constants
MAX_NUMBER = 500
MIN_NUMBER = 1

# Function that makes the submission true 
def submit_info():
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_entry.get()
    quantity = quantity_entry.get()

    # IF statements for error messages
    if not name:
        messagebox.showerror("Error", "Please fill in the Customer's Full Name.")
        return
    
    if not receipt:
        messagebox.showerror("Error", "Please fill in the Receipt Number.")
        return
    
    if not items:
        messagebox.showerror("Error", "Please fill in the Items Hired.")
        return
    
    if not quantity:
        messagebox.showerror("Error", "Please fill in the Quantity of Items hired.")
        return


    if not all(char.isalpha() or char.isspace() for char in name):
        messagebox.showerror("Error", "Invalid name. Letters and spaces only.")
        name_entry.delete(0, tk.END)
        return

    if not receipt.isdigit():
        messagebox.showerror("Error", "Invalid receipt number. Digits only.")
        receipt_entry.delete(0, tk.END)
        return

    if not all(char.isalpha() or char.isspace() for char in items):
        messagebox.showerror("Error", "Invalid items hired. Letters only.")
        items_entry.delete(0, tk.END)
        return

    if not quantity.isdigit() or int(quantity) < MIN_NUMBER or int(quantity) > MAX_NUMBER:
        messagebox.showerror("Error", f"Invalid Quantity. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.")
        quantity_entry.delete(0, tk.END)
        return

    # Shows current time in Treeview
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    index = len(tree.get_children()) + 1  # Get the next index value
    tree.insert("", tk.END, values=(index, name, receipt, items, quantity, current_time))

    # Clears Entry fields when submitted
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    items_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# Function for deleting information
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select the item returned.")
        return
    tree.delete(selected_item)

# Creates the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x700")

# Configure a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("Treeview", font=("Helvetica", 12))

# Title label
title_label = ttk.Label(window, text="List of Items Hired", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels
name_label = ttk.Label(window, text="Full Name:")
receipt_label = ttk.Label(window, text="Receipt Number:")
items_label = ttk.Label(window, text="Items Hired:")
quantity_label = ttk.Label(window, text="Quantity of Items hired:")

# Entries
name_entry = ttk.Entry(window, font=("Helvetica", 12))
receipt_entry = ttk.Entry(window, font=("Helvetica", 12))
items_entry = ttk.Entry(window, font=("Helvetica", 12))
quantity_entry = ttk.Entry(window, font=("Helvetica", 12))

# Submit and Delete button
submit_button = ttk.Button(window, text="Submit", command=submit_info)
delete_button = ttk.Button(window, text="Return", command=delete_info)

# Tree view
tree = ttk.Treeview(window, show="headings", selectmode="browse")
tree["columns"] = ("Column", "Name", "Receipt", "Items", "Quantity", "Time")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Column", width=100)
tree.column("Name", width=200)
tree.column("Receipt", width=150)
tree.column("Items", width=200)
tree.column("Quantity", width=150)
tree.column("Time", width=200)
tree.heading("Column", anchor=tk.CENTER)
tree.heading("Name", text="Full Name", anchor=tk.CENTER)
tree.heading("Receipt", text="Receipt Number", anchor=tk.CENTER)
tree.heading("Items", text="Items Hired", anchor=tk.CENTER)
tree.heading("Quantity", text="Quantity of Items Hired", anchor=tk.CENTER)
tree.heading("Time", text="Time", anchor=tk.CENTER)
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Labels, Entries, Submit and Delete button for GUI
name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
receipt_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
receipt_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
items_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
items_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
quantity_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
submit_button.grid(row=2, column=0, columnspan=2, pady=10)
delete_button.grid(row=3, column=0, columnspan=2, pady=5)

# Configuring grid weights
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# Runs the GUI
window.mainloop()
