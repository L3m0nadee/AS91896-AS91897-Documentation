import tkinter as tk

# Create the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x600")

MAX_NUMBER = 500
MIN_NUMBER = 1

# Labels for the input fields
name_label = tk.Label(window, text="Full Name:")
receipt_label = tk.Label(window, text="Receipt Number:")
items_label = tk.Label(window, text="Items Hired:")
quantity_label = tk.Label(window, text="Quantity:")

# Create the entry fields for the input data
name_entry = tk.Entry(window)
receipt_entry = tk.Entry(window)
items_entry = tk.Entry(window)
quantity_entry = tk.Entry(window)

# Create a button to submit the customer information
submit_button = tk.Button(window, text="Submit", command=lambda: submit_info())

# Create a text widget to display errors
error_text = tk.Text(window, height=5)

# Add the labels, entry fields, submit button, and error box to the GUI window
name_label.pack()
name_entry.pack()
receipt_label.pack()
receipt_entry.pack()
items_label.pack()
items_entry.pack()
quantity_label.pack()
quantity_entry.pack()
submit_button.pack()
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

    # Check if the name contains only letters
    if not name.isalpha():
        # Display error message in the error box
        error_text.insert(tk.END, "Invalid name.\n")
        # Clear the name entry field
        name_entry.delete(0, tk.END)
        return

    # Check if the quantity is within the limit
    if not quantity.isdigit() or int(quantity) < MIN_NUMBER or int(quantity) > MAX_NUMBER:
        # Display error message in the error box
        error_text.insert(tk.END, f"Invalid Quantity.\nPlease enter a number between {MIN_NUMBER}-{MAX_NUMBER}.\n")
        # Clear the quantity entry field
        quantity_entry.delete(0, tk.END)
        return

    # Print the customer information to the console
    print("Customer Name: " + name)
    print("Receipt Number: " + receipt)
    print("Items Hired: " + items)
    print("Quantity: " + quantity)

    # Clear the entry fields after submission
    name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    items_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Run the GUI window
window.mainloop()
