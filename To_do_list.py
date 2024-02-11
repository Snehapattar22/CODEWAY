import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.config(bg="#e5b7e5")

tasks = tk.Listbox(root, width=60, height=22)
tasks.pack(pady=20)

entry = tk.Entry(root, width=40, bg="white", fg="#545454", borderwidth=3)
entry.pack(pady=20)

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    selected_task = tasks.curselection()
    if selected_task:
        tasks.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete")

add_button = tk.Button(root, text="Add Task", command=add_task, bg="white", fg="#545454")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#DC143C", fg="white")
delete_button.pack(pady=5)

root.mainloop()
