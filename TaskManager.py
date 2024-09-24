import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Task Manager")
        self.root.geometry("600x400")

        # List to store tasks (each task is a tuple: (task, due date, completed status))
        self.tasks = []

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, height=15, width=60, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        # Add Task button
        self.add_task_button = tk.Button(self.buttons_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=10)

        # Delete Task button
        self.delete_task_button = tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=10)

        # Mark Complete button
        self.mark_complete_button = tk.Button(self.buttons_frame, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.grid(row=0, column=2, padx=10)

        # Mark Incomplete button
        self.mark_incomplete_button = tk.Button(self.buttons_frame, text="Mark Incomplete", command=self.mark_incomplete)
        self.mark_incomplete_button.grid(row=0, column=3, padx=10)

        self.update_task_list()

    def add_task(self):
        task = simpledialog.askstring("Task", "Enter the task:")
        due_date = simpledialog.askstring("Due Date", "Enter the due date:")
        if task and due_date:
            # Initially, tasks are not completed
            self.tasks.append((task, due_date, False))
            self.update_task_list()

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task, due_date, completed = self.tasks[selected_index]
            # Mark the task as completed
            self.tasks[selected_index] = (task, due_date, True)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

    def mark_incomplete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task, due_date, completed = self.tasks[selected_index]
            # Mark the task as not completed
            self.tasks[selected_index] = (task, due_date, False)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark incomplete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task, due_date, completed in self.tasks:
            completion_status = ("\u2705") if completed else ("\u274C")
            self.task_listbox.insert(tk.END, f"{task} - Due: {due_date} - {completion_status}")

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()

