import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Constants
MAX_NUMBER = 500
MIN_NUMBER = 1

#Function that makes the submission true 
def submit_info():
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_entry.get()
    quantity = quantity_entry.get()

    #Function for Error box 
    error_text.configure(state="normal")
    error_text.delete("1.0", tk.END)
    error_text.configure(state="disabled")

    # If statements for error messages 
    if not name or not receipt or not items or not quantity:
        error_text.configure(state="normal")
        error_text.insert(tk.END, "Please fill in all the input boxes.\n")
        error_text.configure(state="disabled")
        return

    if not all(char.isalpha() or char.isspace() for char in name):
        error_text.configure(state="normal")
        error_text.insert(tk.END, "Invalid name.\n")
        error_text.configure(state="disabled")
        name_entry.delete(0, tk.END)
        return

    if not receipt.isdigit():
        error_text.configure(state="normal")
        error_text.insert(tk.END, "Invalid receipt number.\n")
        error_text.configure(state="disabled")
        receipt_entry.delete(0, tk.END)
        return

    if not all(char.isalpha() or char.isspace() for char in name):
        error_text.configure(state="normal")
        error_text.insert(tk.END, "Invalid items hired.\nLetters only.\n")
        error_text.configure(state="disabled")
        items_entry.delete(0, tk.END)
        return

    if not quantity.isdigit() or int(quantity) < MIN_NUMBER or int(quantity) > MAX_NUMBER:
        error_text.configure(state="normal")
        error_text.insert(
            tk.END, f"Invalid Quantity.\nPlease enter a number between {MIN_NUMBER}-{MAX_NUMBER}.\n"
        )
        error_text.configure(state="disabled")
        quantity_entry.delete(0, tk.END)
        return

    # Shows current time in Treeview
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tree.insert("", tk.END, values=(name, receipt, items, quantity, current_time))

    # Clears Entry fields when submitted
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    items_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function for deleting information
def delete_info():
    selected_item = tree.selection()
    if not selected_item:
        error_text.configure(state="normal")
        error_text.delete("1.0", tk.END)
        error_text.insert(tk.END, "No item selected.\n")
        error_text.configure(state="disabled")
        return
    tree.delete(selected_item)

# Creates the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x600")

# Labels
name_label = ttk.Label(window, text="Full Name:")
receipt_label = ttk.Label(window, text="Receipt Number:")
items_label = ttk.Label(window, text="Items Hired:")
quantity_label = ttk.Label(window, text="Quantity:")

# Entries
name_entry = ttk.Entry(window)
receipt_entry = ttk.Entry(window)
items_entry = ttk.Entry(window)
quantity_entry = ttk.Entry(window)

#Submit and Delete button
submit_button = ttk.Button(window, text="Submit", command=submit_info)
delete_button = ttk.Button(window, text="Delete", command=delete_info)

# Error Box
error_text = tk.Text(window, height=5)
error_text.configure(state="disabled")

#Tree view
tree = ttk.Treeview(window)
tree["columns"] = ("Name", "Receipt", "Items", "Quantity", "Time")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", width=150)
tree.column("Receipt", width=100)
tree.column("Items", width=150)
tree.column("Quantity", width=100)
tree.column("Time", width=150)
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="Full Name", anchor=tk.W)
tree.heading("Receipt", text="Receipt Number", anchor=tk.W)
tree.heading("Items", text="Items Hired", anchor=tk.W)
tree.heading("Quantity", text="Quantity", anchor=tk.W)
tree.heading("Time", text="Time", anchor=tk.W)
tree.pack()

# Labels, Entries, Submit and Delete button for GUI
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

# Runs the GUI
window.mainloop()
