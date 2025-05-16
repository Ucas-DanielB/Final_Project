from task_handling import *
from summary_handling import *
from study_handling import *

def main():
    while True:
        print("\nWelcome to the Study Session Planner!")
        print("1. Task Manager")
        print("2. Summary Dashboard")
        print("3. Study Session Planner")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            main_managing_tasks()
        elif choice == "2":
            summary_menu()
        elif choice == "3":
            main_menu()
        elif choice == "4":
            break
        else:
            print("Please select a number 1-4")

if __name__ == "__main__":
    main()
