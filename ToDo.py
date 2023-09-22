import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bg="lightgrey",
    bd=0,
    font=("Helvetica", 12)
)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    root,
    font=("Helvetica", 12)
)
entry.pack(pady=10)

add_button = tk.Button(
    root,
    text="Add Task",
    font=("Helvetica", 12),
    command=add_task
)
add_button.pack(padx=20, pady=5, fill=tk.BOTH)

delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Helvetica", 12),
    command=delete_task
)
delete_button.pack(padx=20, pady=5, fill=tk.BOTH)

root.mainloop()
