from tkinter import *

application = Tk()
application.geometry("600x600")
application.title("To-Do List")

tasks = []
task_labels = []

# Functions
def createFunc():
    createWindow = Toplevel()
    createWindow.geometry("400x400")
    createWindow.title("Create a new Task")

    Label(createWindow, text="New Task", font=("Arial", 18)).pack(padx=10, pady=10)
    Label(createWindow, text="Name", font=("Arial", 15)).pack(padx=30, pady=30)

    namebox = Entry(createWindow)
    namebox.pack(padx=10, pady=10)

    def storeTask():
        task_name = namebox.get()
        if task_name.strip() == "":
            return  # Ignore empty tasks

        print("Task created:", task_name)
        createWindow.destroy()

        task_label = Label(application, text=task_name, font=("Arial", 18))
        task_label.pack(padx=10, pady=5)
        task_labels.append(task_label)
        tasks.append(task_name)

    Button(createWindow, text="Create", font=("Arial", 17), command=storeTask).pack(padx=40, pady=40)

def deleteFunc():
    deleteWindow = Toplevel()
    deleteWindow.geometry("400x400")
    deleteWindow.title("Delete A Task")

    def deleteTask(index):
        task_labels[index].destroy()
        del task_labels[index]
        del tasks[index]
        deleteWindow.destroy()

    for idx, task in enumerate(tasks):
        Button(deleteWindow, text=task, font=("Arial", 14),
               command=lambda i=idx: deleteTask(i)).pack(padx=10, pady=10)

Label(application, text="To-Do List", font=("Arial", 18)).pack(padx=10, pady=10)

Button(application, text="Create", font=("Arial", 18), command=createFunc).place(x=1, y=1)
Button(application, text="Delete", font=("Arial", 18), command=deleteFunc).place(x=100, y=1)

Label(application, text="Tasks", font=("Arial", 18)).pack(padx=30, pady=30)

application.mainloop()
