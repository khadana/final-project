import tkinter as tk
from tkinter import simpledialog, messagebox

# Store entries in a list
entries = []

# Function to add an entry
def add_entry():
    title = simpledialog.askstring("Add Entry", "Enter the title of the entry:")
    if title:
        content = simpledialog.askstring("Add Entry", "Enter the content of the entry:")
        if content:
            entries.append({"title": title, "content": content})
            messagebox.showinfo("Success", "Entry added successfully!")
        else:
            messagebox.showwarning("Input Error", "Content cannot be empty.")
    else:
        messagebox.showwarning("Input Error", "Title cannot be empty.")

# Function to view entries
def view_entries():
    if not entries:
        messagebox.showinfo("View Entries", "No entries available.")
        return

    view_window = tk.Toplevel(root)
    view_window.title("View Entries")
    view_window.geometry("400x300")
    view_window.configure(bg="lightgray")  # Set background color

    for index, entry in enumerate(entries, start=1):
        tk.Label(view_window, text=f"{index}. {entry['title']}", font=("Arial", 12, "bold"), bg="lightgray").pack(anchor="w")
        tk.Label(view_window, text=entry['content'], font=("Arial", 10), wraplength=350, justify="left", bg="lightgray").pack(anchor="w")
        tk.Label(view_window, text="", bg="lightgray").pack()  # Add spacing

# Function to delete an entry
def delete_entry():
    if not entries:
        messagebox.showinfo("Delete Entry", "No entries available to delete.")
        return

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Entry")
    delete_window.geometry("300x200")
    delete_window.configure(bg="lightgray")  # Set background color

    tk.Label(delete_window, text="Select an entry to delete:", font=("Arial", 12), bg="lightgray").pack(pady=10)

    for index, entry in enumerate(entries, start=1):
        button = tk.Button(
            delete_window, 
            text=f"{index}. {entry['title']}", 
            command=lambda idx=index-1: confirm_delete(idx, delete_window)
        )
        button.pack(pady=2)

# Confirm deletion of an entry
def confirm_delete(index, window):
    result = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete '{entries[index]['title']}'?")
    if result:
        del entries[index]
        messagebox.showinfo("Success", "Entry deleted successfully!")
        window.destroy()

# Main application window
root = tk.Tk()
root.title("Personal Journal Application")
root.geometry("400x300")
root.configure(bg="lightgray")  # Set background color for main window

# Main title
tk.Label(root, text="Personal Journal Application", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=10)

# Add buttons
tk.Button(root, text="Add Entry", command=add_entry, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="View Entries", command=view_entries, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Delete Entry", command=delete_entry, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=5)

# Run the application
root.mainloop()
