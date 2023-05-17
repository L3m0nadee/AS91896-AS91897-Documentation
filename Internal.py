import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Create the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x600")

MAX_NUMBER = 500
MIN_NUMBER = 1

# Labels for the input fields
name_label = ttk.Label(window, text="Full Name:")
receipt_label = ttk.Label(window, text="Receipt Number:")
items_label = ttk.Label(window, text="Items Hired:")
quantity_label = ttk.Label(window, text="Quantity:")

# Create the entry fields for the input data
name_entry = ttk.Entry(window)
receipt_entry = ttk.Entry(window)
items_entry = ttk.Entry(window)
quantity_entry = ttk.Entry(window)

# Create a button to submit the customer information
submit_button = ttk.Button(window, text="Submit", command=lambda: submit_info())

# Create a button to delete selected information
delete_button = ttk.Button(window, text="Delete", command=lambda: delete_info())

# Create a text widget to display errors
error_text = tk.Text(window, height=5)

# Create a Treeview widget
tree = ttk.Treeview(window)

# Define the columns for the Treeview
tree["columns"] = ("Name", "Receipt", "Items", "Quantity", "Time")

# Format the columns
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", width=150)
tree.column("Receipt", width=100)
tree.column("Items", width=150)
tree.column("Quantity", width=100)
tree.column("Time", width=150)

# Add column headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Full Name", anchor=tk.W)
tree.heading("Receipt", text="Receipt Number", anchor=tk.W)
tree.heading("Items", text="Items Hired", anchor=tk.W)
tree.heading("Quantity", text="Quantity", anchor=tk.W)
tree.heading("Time", text="Time", anchor=tk.W)

# Pack the Treeview widget
tree.pack()

# Add the labels, entry fields, submit button, delete button, and error box to the GUI window
name_label.pack(padx=10, pady=5)
name_entry.pack(padx=10, pady=5)
receipt_label.pack(padx=10, pady=5)
receipt_entry.pack(padx=10, pady=5)
items_label.pack(padx=10, pady=5)
items_entry.pack(padx=10, pady=5)
quantity_label.pack(padx=10, pady=5)
quantity_entry.pack(padx=10, pady=5)
submit_button.pack(pady=10)
delete_button.pack(pady=5)
error_text.pack()

# Function to handle the submission of the customer information
def submit_info():
    # Input Fields of data
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_entry.get()
    quantity = quantity_entry.get()

    # Clear the error box
    error_text.delete('1.0', tk.END)
    
    # Check if any input field is empty
    if not name or not receipt or not items or not quantity:
        # Display error message in the error box
        error_text.insert(tk.END, "Please fill in all the input boxes.\n")
        return

    # Check if the name contains only letters and spaces
    if not all(char.isalpha() or char.isspace() for char in name):
        # Display error message in the error box
        error_text.insert(tk.END, "Invalid name.\n")
        # Clear the name entry field
        name_entry.delete(0, tk.END)
        return

    # Check if the receipt number contains only numbers
    if not receipt.isdigit():
        # Display error message in the error box
        error_text.insert(tk.END, "Invalid receipt number.\n")
        # Clear the receipt entry field
        receipt_entry.delete(0, tk.END)
        return
    
    # Check if the items hired contain only letters
    if not items.isalpha():
        # Display error message in the error box
        error_text.insert(tk.END, "Invalid items hired.\nLetters only.\n")
        # Clear the items entry field
        items_entry.delete(0, tk.END)
        return

    # Check if the quantity is within the limit
    if not quantity.isdigit() or int(quantity) < MIN_NUMBER or int(quantity) > MAX_NUMBER:
        # Display error message in the error box
        error_text.insert(tk.END, f"Invalid Quantity.\nPlease enter a number between {MIN_NUMBER}-{MAX_NUMBER}.\n")
        # Clear the quantity entry field
        quantity_entry.delete(0, tk.END)
        return

    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert the data into the Treeview
    tree.insert("", tk.END, values=(name, receipt, items, quantity, current_time))

    # Clear the entry fields after submission
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    items_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function to handle the deletion of selected information
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        error_text.delete('1.0', tk.END)
        error_text.insert(tk.END, "No item selected.\n")
        return
    tree.delete(selected_item)

# Run the GUI window
window.mainloop()
