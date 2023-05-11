import tkinter as tk

# Create the GUI window
window = tk.Tk()
window.title("Julies Party Hiring Store")
window.geometry("1024x600")

MAX_NUMBER = 500
MIN_NUMBER = 1

# Create the labels for the input fields
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

# Add the labels and entry fields to the GUI window
name_label.pack()
name_entry.pack()
receipt_label.pack()
receipt_entry.pack()
items_label.pack()
items_entry.pack()
quantity_label.pack()
quantity_entry.pack()
submit_button.pack()

# Function to handle the submission of the customer information
def submit_info():
    # Get the input data from the entry fields
    name = name_entry.get()
    receipt = receipt_entry.get()
    items = items_entry.get()
    quantity = quantity_entry.get()

    # Check if the receipt number is within the limit
    if int(receipt) < MIN_NUMBER or int(receipt) > MAX_NUMBER:
        # Display error message in a pop-up window
        error_window = tk.Toplevel(window)
        error_window.title("Error")
        error_window.geometry("200x100")
        error_label = tk.Label(error_window, text="Invalid number.\nPlease select a number between 1-500")
        error_label.pack(pady=10)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=10)
        # Clear the receipt number entry field
        receipt_entry.delete(0, tk.END)
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