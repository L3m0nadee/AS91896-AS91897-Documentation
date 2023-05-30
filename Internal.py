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

# Function to submit customer information
def submit_info():
    # Get values from entry fields
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_combobox.get()
    quantity = quantity_entry.get()

    try:
        # Validation checks for input fields
        if not name:
            raise Error("Please fill in the Customer's Full Name.")

        if not receipt:
            raise Error("Please fill in the Receipt Number.")

        if not items:
            raise Error("Please select an item.")

        if not quantity:
            raise Error("Please fill in the Quantity of Items hired.")

        # Check if receipt number already exists
        for submission in submissions:
            if submission["Receipt"] == receipt:
                raise Error("Duplicate receipt number. Please enter a unique receipt number.")

        # Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        index = len(submissions) + 1  # Get the next index value

        # Create submission dictionary
        submission = {
            "Index": index,
            "Name": name,
            "Receipt": receipt,
            "Items": items,
            "Quantity": quantity,
            "Time": current_time
        }

        # Add submission to the list
        submissions.append(submission)

        # Insert values into the treeview
        tree.insert("", tk.END, values=(index, name, receipt, items, quantity, current_time))

        # Clear entry fields after submission
        name_entry.delete(0, tk.END)
        receipt_entry.delete(0, tk.END)
        items_combobox.set('')
        quantity_entry.delete(0, tk.END)

        # Sort the treeview by receipt number
        tree_sort_by_receipt()

    except Error as error:
        # Display error message in a messagebox
        messagebox.showerror("Error", str(error))



# Function to delete selected information from the treeview
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select the item returned.")
        return
    index = int(tree.item(selected_item, "values")[0])
    submission = submissions[index - 1]
    submissions.remove(submission)  # Remove submission from the list
    tree.delete(selected_item)
    clear_entry_fields()

# Function that clears all the entries when you click the return button
def clear_entry_fields():
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    items_combobox.set('')
    quantity_entry.delete(0, tk.END)

# Function to handle deletion of selected item from the treeview using the Backspace key
def delete_selected_item(event):
    delete_info()

# Validation function for customer name entry
def validate_name_entry(text):
    if any(char.isdigit() or (not char.isalnum() and char != " ") for char in text):
        messagebox.showerror("Error", "Numbers and symbols are not allowed in the Customer's Full Name.")
        return False
    return True

# Validation function for receipt number entry
def validate_receipt_entry(text):
    if any(char.isalpha() or (not char.isdigit()) for char in text):
        messagebox.showerror("Error", "Only digits are allowed in the Receipt Number.")
        return False
    return True

# Validation function for quantity entry
def validate_quantity_entry(text):
    if text == "":
        # Allow an empty entry (deleting a single digit)
        return True
    if not text.isdigit() or int(text) < MIN_NUMBER or int(text) > MAX_NUMBER:
        messagebox.showerror("Error", f"Invalid Quantity. Please enter a number between {MIN_NUMBER}-{MAX_NUMBER}.")
        return False
    return True

# Function to sort the treeview by receipt number
def tree_sort_by_receipt():
    tree_data = [(tree.item(item)["values"], item) for item in tree.get_children()]
    tree_data.sort(key=lambda x: x[0][2])  # Sort by receipt number
    for i, (values, item) in enumerate(tree_data):
        tree.move(item, "", i)

# Create the GUI window
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
quantity_entry = ttk.Entry(window, font=("Helvetica", 12))

# Combobox for items
items_combobox = ttk.Combobox(window, font=("Helvetica", 12), state="readonly")
items_combobox['values'] = ('Entertainment', 'Cups', 'Furniture', 'Catering', 'LED products', 'Themes and Accessories')
items_combobox.current(0)  # Set the default selection

# Bind the validation functions to the entry widgets
name_entry["validate"] = "key"
name_entry["validatecommand"] = (window.register(validate_name_entry), "%P")
receipt_entry["validate"] = "key"
receipt_entry["validatecommand"] = (window.register(validate_receipt_entry), "%P")
quantity_entry["validate"] = "key"
quantity_entry["validatecommand"] = (window.register(validate_quantity_entry), "%P")

# Submit and Delete buttons
submit_button = ttk.Button(window, text="Submit", command=submit_info)
delete_button = ttk.Button(window, text="Return Items", command=delete_info)

# Treeview
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

# Labels, Entries, Submit and Delete buttons for the GUI
name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
receipt_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
receipt_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
items_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
items_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="w")
quantity_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
quantity_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
submit_button.grid(row=2, column=0, columnspan=2, pady=10)
delete_button.grid(row=3, column=0, columnspan=2, pady=5)

# Configure grid weights
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

# Allow pressing backspace inside the treeview
window.bind("<BackSpace>", delete_selected_item)

# Run the GUI
window.mainloop()
