import tkinter as tk
from tkinter import messagebox
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Profissional")
        self.root.geometry("400x450")
        self.filename = "tarefas.txt"

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Remover", command=self.delete_task, fg="red")
        self.delete_button.pack()

        self.load_tasks() # Carrega as tarefas ao iniciar

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

    def save_tasks(self):
        with open(self.filename, "w") as f:
            tasks = self.task_listbox.get(0, tk.END)
            for task in tasks:
                f.write(task + "\n")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks() # Salva após adicionar

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.save_tasks() # Salva após remover
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()