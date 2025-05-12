####
####
####
####
####
####
#Ethan Blanco
####
####
####
####
####
####

import csv

#Define file path
folder = "tasks"
file_name = "tasks.csv"
file_path = "code_tasks/tasks.csv"
try:
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"File not found: {file_path}")

    
def load_tasks():

    #Load tasks from file into the list.
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]
    
def save_tasks(tasks):
    #Save the list of tasks to the file.
    with open(file_path, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    #Add a task to the to-do list.
    task = input("Enter the new task: ")
    if task:
        tasks = load_tasks()
        tasks.append("[ ] " + task)  #Unmarked task
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Task can't be empty!\n")

def mark_down():
    #Mark a task as complete.
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks to mark as complete!\n")
        return
    
    view_task() #Lets the user review all current and available Tasks in the CSV file.
    try:
        task_num = int(input("Enter the number of the task to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            if tasks[task_num].startswith("[X]"):
                print("Task was already completed!\n")
            else:
                tasks[task_num] = "[X]" + tasks[task_num][3:]
                save_tasks(tasks)
                print("Task is complete!\n")
        else:
            print("Wrong task number!\n")
    except ValueError:
        print("This didn't work, please enter a number.\n")

def delete_task():
    #Delete a task from the to-do list.
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks to delete!\n")
        return
    
    view_task()
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            save_tasks(tasks)
            print("Task deleted.\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")


def view_task():

    #Display the Tasks list.
    tasks = load_tasks()
    if not tasks:
        print("\nTasks is empty!\n")
    else:
        print("\nTasks List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def main_managing_tasks(): #Main user interface.

    while True:
        try:    
            main_tasks = int(input("""Welcome to your Task Manager, what would you like to do?
                           1. Make Tasks.
                           2. Delete Tasks.
                           3. Mark down Tasks.
                           4. View all Tasks.
                           5. Return back.
                           6. Exit program.\n"""))
            if main_tasks == 1:
                print("Welcome! What would you like to Add?")
                add_task()
            elif main_tasks == 2:
                print("Welcome! What would you like to Remove?")
                delete_task()
            elif main_tasks == 3:
                print("Welcome! What Tasks would you like to Mark down?")
                mark_down()
            elif main_tasks == 4:
                print("Welcome! Here are all your tasks!")
                view_task()
            elif main_tasks == 5:
                print("Okay, see you later!")
                return
            elif main_tasks == 6:
                print("Okay, goodbye!")
                break
            else:
                print("This isn't available, maybe try something else?")
                continue
        except ValueError: #Error management.
            print("This doesn't work for whatever reason! Try using a correct response.")


####
####
####
####
####
####
####
####
####
####
####
####
####