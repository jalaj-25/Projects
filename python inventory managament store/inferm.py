import tkinter as tk
from tkinter import ttk, messagebox
from product_manager import display_data, purchase_product

def create_gui():
    """Create and launch the GUI application."""
    root = tk.Tk()
    root.title("Inventory Management System")

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=("ID", "Name", "Price", "Category", "Quantity", "Date"), show="headings")
    tree.heading("ID", text="ID", anchor=tk.CENTER)
    tree.heading("Name", text="Name", anchor=tk.CENTER)
    tree.heading("Price", text="Price", anchor=tk.CENTER)
    tree.heading("Category", text="Category", anchor=tk.CENTER)
    tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
    tree.heading("Date", text="Date", anchor=tk.CENTER)
    tree.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

    # Display initial data in Treeview
    from product_manager import available_products
    display_data(tree, available_products)

    product_id_label = ttk.Label(frame, text="Product ID:", anchor=tk.CENTER)
    product_id_label.grid(row=1, column=0, padx=5)
    product_id_entry = ttk.Entry(frame)
    product_id_entry.grid(row=1, column=1, padx=5)

    name_label = ttk.Label(frame, text="Name:", anchor=tk.CENTER)
    name_label.grid(row=2, column=0, padx=5)
    name_entry = ttk.Entry(frame)
    name_entry.grid(row=2, column=1, padx=5)

    contact_label = ttk.Label(frame, text="Contact Number:", anchor=tk.CENTER)
    contact_label.grid(row=3, column=0, padx=5)
    contact_entry = ttk.Entry(frame)
    contact_entry.grid(row=3, column=1, padx=5)

    quantity_label = ttk.Label(frame, text="Quantity:", anchor=tk.CENTER)
    quantity_label.grid(row=4, column=0, padx=5)
    quantity_entry = ttk.Entry(frame)
    quantity_entry.grid(row=4, column=1, padx=5)

    def purchase_button_click():
        """Handle the Purchase button click event."""
        try:
            product_id = int(product_id_entry.get())
            quantity = int(quantity_entry.get())
            name = name_entry.get()
            contact = contact_entry.get()

            success = purchase_product(product_id, quantity, name, contact, tree)

            if success:
                # Clear the entries after a successful purchase
                product_id_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
                name_entry.delete(0, tk.END)
                contact_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Product ID and Quantity.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process purchase: {e}")

    purchase_button = ttk.Button(frame, text="Purchase", command=purchase_button_click)
    purchase_button.grid(row=5, column=1, pady=10)

    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
