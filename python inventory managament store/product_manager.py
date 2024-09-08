import openpyxl
from tkinter import messagebox

# Sample available products dictionary
available_products = {
    1001: {"name": "Fruits", "price": 230, "category": "grocery", "quantity": 10, "date": "15/01/2024"},
    1002: {"name": "Lotion", "price": 250, "category": "beauty & personal", "quantity": 100, "date": "15/01/2024"},
    1003: {"name": "Combiflame", "price": 500, "category": "health", "quantity": 200, "date": "15/01/2024"},
    1004: {"name": "Chilli Sauce", "price": 20, "category": "grocery", "quantity": 50, "date": "15/01/2024"},
    1005: {"name": "Toothbrush", "price": 700, "category": "beauty & personal", "quantity": 100, "date": "15/01/2024"},
    1006: {"name": "Ice Creams", "price": 33, "category": "grocery", "quantity": 56, "date": "15/01/2024"},
    1007: {"name": "Nail Polish", "price": 765, "category": "beauty & personal", "quantity": 70, "date": "15/01/2024"},
    1008: {"name": "Vegetables", "price": 764, "category": "grocery", "quantity": 90, "date": "15/01/2024"},
    1009: {"name": "Face Wash", "price": 87, "category": "beauty & personal", "quantity": 50, "date": "15/01/2024"},
    1010: {"name": "Chocolate Bars", "price": 30, "category": "grocery", "quantity": 60, "date": "15/01/2024"}
}

def display_data(tree, data):
    """Clear and display product data in Treeview."""
    for tree_entry in tree.get_children():
        tree.delete(tree_entry)

    for id, product in data.items():
        tree.insert("", "end", values=(id, product['name'], product['price'], product['category'], product['quantity'], product['date']))

def purchase_product(product_id, quantity, customer_name, contact_number, tree):
    """Handle product purchase logic."""
    if product_id in available_products:
        if available_products[product_id]['quantity'] >= quantity:
            available_products[product_id]['quantity'] -= quantity
            display_data(tree, available_products)  # Update tree after purchase
            save_purchase_to_excel(product_id, quantity, customer_name, contact_number)
            messagebox.showinfo("Success", "Purchase successful!")
            return True
        else:
            messagebox.showerror("Error", "Insufficient quantity!")
    else:
        messagebox.showerror("Error", "Invalid Product ID!")
    return False

def save_purchase_to_excel(product_id, quantity, customer_name, contact_number):
    """Save purchase data to Excel."""
    try:
        wb = openpyxl.load_workbook("purchase_data.xlsx")
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Product ID", "Name", "Price", "Category", "Quantity", "Date", "Customer Name", "Contact Number"])
    else:
        ws = wb.active

    product = available_products[product_id]
    ws.append([product_id, product['name'], product['price'], product['category'], quantity, product['date'], customer_name, contact_number])
    wb.save("purchase_data.xlsx")
    messagebox.showinfo("Success", "Purchase data saved to Excel file.")
