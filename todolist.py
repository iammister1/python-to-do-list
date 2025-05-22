from tkinter import *

application = Tk()
application.geometry("600x600")
application.title("To-Do List")

tasks = []

# Functions


def createFunc():
    createWindow = Toplevel()
    createWindow.geometry("400x400")
    createWindow.title("Create a new Task")

    newtasklabel = Label(createWindow, text="New Task", font=("Arial", 18))
    newtasklabel.pack(padx=10, pady=10)

    namelabel = Label(createWindow, text="Name", font=("Arial", 15))
    namelabel.pack(padx=30, pady=30)

    namebox = Entry(createWindow)
    namebox.pack(padx=10, pady=10)

    def storeTask():
        global tasks
        task_name = namebox.get()
        print("Task created:", task_name)

        createWindow.destroy()

        newtasklabel = Label(application, text=task_name, font=("Arial", 18))
        newtasklabel.pack(padx=10, pady=10)

        tasks.append(task_name)

    createButton = Button(createWindow, text="Create", font=("Arial", 17), command=storeTask)
    createButton.pack(padx=40, pady=40)

mainlabel = Label(application, text="To-Do List", font=("Arial", 18))
mainlabel.pack(padx=10, pady=10)

createbutton = Button(application, text="Create", font=("Arial", 18), command=createFunc)
createbutton.place(x=1, y=1)

tasksLabel = Label(application, text="Tasks", font=("Arial", 18))
tasksLabel.pack(padx=30, pady=30)



application.mainloop()
