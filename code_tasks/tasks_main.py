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

#Define file path, to_do_list.py\to_do_list.txt
folder = "tasks"
file_name = "tasks.csv"
file_path = csv.path.join(folder, file_name)

#Ensure the folder and file exist
if not csv.path.exists(folder):
    csv.makedirs(folder)

if not csv.path.exists(file_path):
    with open(file_path, "w") as f:
        pass  #Create an empty file

def managing_tasks():

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
            elif main_tasks == 2:
                print("Welcome! What would you like to Remove?")
            elif main_tasks == 3:
                print("Welcome! What Tasks would you like to Mark down?")
            elif main_tasks == 4:
                print("Welcome! Here are all your tasks!")
                
            elif main_tasks == 5:
                print("Okay, see you later!")
                return
            elif main_tasks == 6:
                print("Okay, goodbye!")
                break
        except ValueError:
            print("This doesn't work for whatever reason! Try using a correct response.")




####
####
####
####
####
####
#Remember to callback all functions and stuff :)
####
####
####
####
####
####