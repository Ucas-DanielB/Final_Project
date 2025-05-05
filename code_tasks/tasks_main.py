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


def managing_tasks():

    while True:
        try:    
            main_tasks = int(input("""Welcome to your Task Manager, what would you like to do?
                           1. Make Tasks.
                           2. Delete Tasks.
                           3. Mark down Tasks.
                           4. Return back.
                           5. Exit program.\n"""))
            if main_tasks == 1:
                pass
            elif main_tasks == 2:
                pass
            elif main_tasks == 3:
                pass
            elif main_tasks == 4:
                print("Okay, see you later!")
                return
            elif main_tasks == 5:
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