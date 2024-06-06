import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("800x600")
root.resizable(0,0)

completed_tasks = []
incomplete_tasks = []

def add_task():
    task = entry.get()
    if task:
        incomplete_tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Field!", "Task can't be empty")


def delete_task():
    incomplete_task_index = incomplete_tasks_listbox.curselection()
    completed_task_index = complete_tasks_listbox.curselection()
    if incomplete_task_index:
        incomplete_tasks.pop(incomplete_task_index[0])
        update_task_list()
    elif completed_task_index:
        completed_tasks.pop(completed_task_index[0])
        update_task_list()
    else:
        messagebox.showwarning("Selection Error!", "No task selected.")


def update_task():
    task_index = incomplete_tasks_listbox.curselection()
    updated_task = entry.get()
    if task_index and updated_task:
        incomplete_tasks[task_index[0]] = updated_task
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Selection/Input Error!", "No task selected or input given.")


def mark_as_done():
    task_index = incomplete_tasks_listbox.curselection()
    if task_index:
        task = incomplete_tasks.pop(task_index[0])
        completed_tasks.append(task)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error!", "No task selected.")



def update_task_list():
    complete_tasks_listbox.delete(0, tk.END)
    for task in completed_tasks:
        complete_tasks_listbox.insert(tk.END, task)

    incomplete_tasks_listbox.delete(0, tk.END)
    for task in incomplete_tasks:
        incomplete_tasks_listbox.insert(tk.END, task)


entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

entry_label = tk.Label(entry_frame, text="Task : ", font=('Times New Roman', 13))
entry_label.pack(side=tk.LEFT, padx=4)

entry = tk.Entry(entry_frame, width=20, font=('Times New Roman', 12), fg="red")
entry.pack(side=tk.LEFT, padx=5)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=20)

add_btn = tk.Button(buttons_frame, text="Add", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

update_btn = tk.Button(buttons_frame, text="Update", command=update_task)
update_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(buttons_frame, text="Delete", command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

mark_complete_btn = tk.Button(buttons_frame, text="Mark as done", command=mark_as_done)
mark_complete_btn.pack(side=tk.LEFT, padx=5)

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=20)

incomplete_tasks_frame = tk.Frame(listbox_frame)
incomplete_tasks_frame.pack(side=tk.LEFT, padx=10)

scrollbar_incomplete = tk.Scrollbar(incomplete_tasks_frame, orient=tk.VERTICAL, command=incomplete_tasks_frame)
scrollbar_incomplete.pack(side=tk.RIGHT, fill=tk.Y)

incomplete_tasks_listbox = tk.Listbox(incomplete_tasks_frame, height=18, width=37, yscrollcommand=scrollbar_incomplete.set, fg="orange")
incomplete_tasks_listbox.pack(side=tk.LEFT)

scrollbar_incomplete.config(command=incomplete_tasks_listbox.yview)

completed_tasks_frame = tk.Frame(listbox_frame)
completed_tasks_frame.pack(side=tk.LEFT, padx=10)

scrollbar_complete = tk.Scrollbar(completed_tasks_frame, orient=tk.VERTICAL, command=completed_tasks_frame)
scrollbar_complete.pack(side=tk.RIGHT, fill=tk.Y)

complete_tasks_listbox = tk.Listbox(completed_tasks_frame, height=18, width=37, yscrollcommand=scrollbar_complete.set, fg="green")
complete_tasks_listbox.pack(side=tk.LEFT)

scrollbar_complete.config(command=complete_tasks_listbox.yview)

root.mainloop()
