import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Constants
MAX_NUMBER = 500
MIN_NUMBER = 1

# Error class
class Error(Exception):
    pass

# List to store submissions
submissions = []

# Function that makes the submission true
def submit_info():
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_entry.get()
    quantity = quantity_entry.get()

    try:
        # IF statements for error messages
        if not name:
            raise Error("Please fill in the Customer's Full Name.")

        if not receipt:
            raise Error("Please fill in the Receipt Number.")

        if not items:
            raise Error("Please fill in the Items Hired.")

        if not quantity:
            raise Error("Please fill in the Quantity of Items hired.")

        if not receipt.isdigit():
            raise Error("Invalid receipt number. Digits only.")

        if not quantity.isdigit() or int(quantity) < MIN_NUMBER or int(quantity) > MAX_NUMBER:
            raise Error(f"Invalid Quantity. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.")

        # Check if receipt number already exists
        for submission in submissions:
            if submission["Receipt"] == receipt:
                raise Error("Duplicate receipt number. Please enter a unique receipt number.")

        # Shows current time in Treeview
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        index = len(submissions) + 1  # Get the next index value
        submission = {
            "Index": index,
            "Name": name,
            "Receipt": receipt,
            "Items": items,
            "Quantity": quantity,
            "Time": current_time
        }
        submissions.append(submission)
        tree.insert("", tk.END, values=(index, name, receipt, items, quantity, current_time))

        # Clears Entry fields when submitted
        name_entry.delete(0, tk.END)
        receipt_entry.delete(0, tk.END)
        items_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

    except Error as error:
        messagebox.showerror("Error", str(error))

#  Deleting information
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select the item returned.")
        return
    index = int(tree.item(selected_item, "values")[0])
    del submissions[index - 1]  # Remove submission from the list
    tree.delete(selected_item)

#  Customer's full name entry
def validate_name_entry(text):
    if any(char.isdigit() or (not char.isalnum() and char != " ") for char in text):
        messagebox.showerror("Error", "Numbers and symbols are not allowed in the Customer's Full Name.")
        return False
    return True

#  Receipt number entry
def validate_receipt_entry(text):
    if any(char.isalpha() or (not char.isdigit()) for char in text):
        messagebox.showerror("Error", "Only digits are allowed in the Receipt Number.")
        return False
    return True

# Items hired entry
def validate_items_entry(text):
    if any(char.isdigit() or (not char.isalpha() and not char.isspace()) for char in text):
        messagebox.showerror("Error", "Numbers and symbols are not allowed in the Items Hired.")
        return False
    return True

#  Quantity entry
def validate_quantity_entry(text):
    if text == "":
        # Allow an empty entry (deleting a single digit)
        return True
    if not text.isdigit() or int(text) < MIN_NUMBER or int(text) > MAX_NUMBER:
        messagebox.showerror("Error", f"Invalid Quantity. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.")
        return False
    return True

# Creates the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x700")

# Configure a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), foreground="blue")  # Set label font and color
style.configure("TButton", font=("Helvetica", 12), foreground="white", background="green")  # Set button font, foreground, and background colors
style.configure("Treeview", font=("Helvetica", 12), background="white", fieldbackground="white")  # Set Treeview font, foreground, and background colors

# Title label
title_label = ttk.Label(window, text="List of Items Hired", font=("Helvetica", 16, "bold"), foreground="purple")  # Set title label font and color
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels
name_label = ttk.Label(window, text="Full Name:", foreground="red")  # Set label color
receipt_label = ttk.Label(window, text="Receipt Number:", foreground="red")  # Set label color
items_label = ttk.Label(window, text="Items Hired:", foreground="red")  # Set label color
quantity_label = ttk.Label(window, text="Quantity of Items hired:", foreground="red")  # Set label color

# Entries
name_entry = ttk.Entry(window, font=("Helvetica", 12))
receipt_entry = ttk.Entry(window, font=("Helvetica", 12))
items_entry = ttk.Entry(window, font=("Helvetica", 12))
quantity_entry = ttk.Entry(window, font=("Helvetica", 12))

# Bind the validation functions to the entry widgets
name_entry["validate"] = "key"
name_entry["validatecommand"] = (window.register(validate_name_entry), "%P")
receipt_entry["validate"] = "key"
receipt_entry["validatecommand"] = (window.register(validate_receipt_entry), "%P")
items_entry["validate"] = "key"
items_entry["validatecommand"] = (window.register(validate_items_entry), "%P")
quantity_entry["validate"] = "key"
quantity_entry["validatecommand"] = (window.register(validate_quantity_entry), "%P")

# Submit and Delete button
submit_button = ttk.Button(window, text="Submit", command=submit_info)
delete_button = ttk.Button(window, text="Return Items", command=delete_info)

# Tree view
tree = ttk.Treeview(window, show="headings", selectmode="browse", height=10)
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
submit_button.grid(row=6, column=0, columnspan=2, pady=10)
delete_button.grid(row=7, column=0, columnspan=2, pady=5)

# Configuring grid weights
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# Runs the GUI
window.mainloop()
