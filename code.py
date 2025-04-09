import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt

expenses = []

# Limit to 5 entries
MAX_ENTRIES = 5

categories = ["Food", "Travel", "Shopping", "Bills", "Others"]

def add_expense():
    if len(expenses) >= MAX_ENTRIES:
        messagebox.showinfo("Limit Reached", "You can only add 5 expenses.")
        return

    title = title_entry.get()
    amount = amount_entry.get()
    category = selected_category.get()

    if title == "" or amount == "" or category == "Select Category":
        messagebox.showwarning("Missing Data", "Please fill all fields.")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Invalid Amount", "Enter a valid number.")
        return

    expenses.append({"title": title, "amount": amount, "category": category, "date": datetime.now().strftime("%Y-%m-%d")})
    messagebox.showinfo("Success", f"Expense added! {MAX_ENTRIES - len(expenses)} entries left.")
    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    selected_category.set("Select Category")

def show_chart():
    if not expenses:
        messagebox.showwarning("No Data", "Add some expenses first.")
        return

    category_totals = {}
    for expense in expenses:
        cat = expense['category']
        category_totals[cat] = category_totals.get(cat, 0) + expense['amount']

    labels = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.axis('equal')
    plt.show()

# Tkinter Window
root = tk.Tk()
root.title("Simple Expense Tracker")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Title
tk.Label(root, text="Title:", bg="#f0f0f0").pack()
title_entry = tk.Entry(root, width=30)
title_entry.pack()

# Amount
tk.Label(root, text="Amount:", bg="#f0f0f0").pack()
amount_entry = tk.Entry(root, width=30)
amount_entry.pack()

# Category dropdown
tk.Label(root, text="Category:", bg="#f0f0f0").pack()
selected_category = tk.StringVar()
selected_category.set("Select Category")
category_menu = tk.OptionMenu(root, selected_category, *categories)
category_menu.pack()

# Buttons
tk.Button(root, text="Add Expense", command=add_expense, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Show Pie Chart", command=show_chart, bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()
