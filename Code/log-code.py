# study_timer.py

import pygame
import time
import csv
import os

# Dictionary to store subject information (expandable later)
subjects = {
    "Math": {},
    "Science": {},
    "History": {}
}

# CSV file name
csv_file = "tasks.csv"

# Ensure the CSV file exists with headers
def initialize_csv():
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Subject", "Start Time", "End Time", "Duration (seconds)"])

# Class to handle a study session
class StudySession:

    # function for study session, getting the subject, start and end time.
    def __init__(self, subject):
        self.subject = subject
        self.start_time = None
        self.end_time = None
    
    # Function to start the timer.
    def start(self):
        self.start_time = time.time()
    
    # function to end the timer.
    def end(self):
        self.end_time = time.time()
    
    # Function to get the data on how long the timer went on for
    def get_duration(self):
        if self.start_time and self.end_time:
            return round(self.end_time - self.start_time, 2)
        else:
            return 0

# Helper function to create a timed study session
def create_study_session():
    # This is the format for the timer.
    pygame.init()
    window_size = (400, 300)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Click to end session")
    white = (255, 255, 255)
    black = (0, 0, 0)
    window.fill(white)
    pygame.display.update()

    # Must input a subject before starting study session.

    # Your input is added to the csv file.
    subject = input("Enter the subject you are studying: ").strip()
    if subject not in subjects:
        print("Adding it to the list.")
        subjects[subject] = {}

    # Runs the class
    session = StudySession(subject)
    session.start()
    
    running = True

    # While loop for the timer in study session
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                session.end()
                running = False

    # Closes pygame when done, and returns session
    pygame.quit()
    return session

# Helper function to save session to CSV
def save_session_to_csv(session):
    # Opens the file in append mode.
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            session.subject,
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session.start_time)),
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session.end_time)),
            session.get_duration()
        ])

# Main menu for the program
def main_menu():
    initialize_csv()

    # While loop set true, for the main menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Create a timed study session")
        print("2. View past study sessions")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        # Choices, 1-3 for session menu, view session, and exit
        if choice == "1":
            session_menu()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            print("Goodbye!")
            break
        # Error message
        else:
            print("Invalid choice. Please try again.")

# Helper function: menu to create and optionally save a study session
def session_menu():
    # While loop set True
    while True:
        # Input to create a study session
        create_new = input("Would you like to create a timed study session? (yes/no): ").lower()
        if create_new == 'yes':
            # If yes, run create study session function
            session = create_study_session()

            # A message to ensure what they're doing is what they want
            keep = input("Is the study session you just had something you want to keep? (yes/no): ").lower()
            if keep == 'yes':
                # runs save session function(session)
                save_session_to_csv(session)
                print("Session saved successfully.")
            # Message if its no, doesnt save the study session
            else:
                print("Session discarded.")

            # Input for user to go back to main menu or keep making study sessions
            back_to_menu = input("Would you like to return to the main menu? (yes/no): ").lower()
            # If yes it takes them back to main menu
            if back_to_menu == 'yes':
                break
        # If no it goes to making a study session
        elif create_new == 'no':
            break
        # Error message 
        else:
            print("Please enter 'yes' or 'no'.")

# Helper function to view sessions from CSV
def view_sessions():
    # Checks if the csv file exists
    if not os.path.exists(csv_file):
        # Print message if there are no study sessions
        print("No study sessions found.")
        return

    # Opens the csv file in read mode
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        sessions = list(reader)
        
        # Tells the user with a print if there are no study sessions 
        if len(sessions) <= 1:
            print("No study sessions recorded yet.")
            return

        # Formatting
        print("\n--- Study Sessions ---")
        for row in sessions[1:]:
            print(f"Subject: {row[0]}, Start: {row[1]}, End: {row[2]}, Duration: {row[3]} seconds")

# Run the program
if __name__ == "__main__":
    main_menu()
