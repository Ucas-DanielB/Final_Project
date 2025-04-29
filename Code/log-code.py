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
csv_file = "study_sessions.csv"

# Ensure the CSV file exists with headers
def initialize_csv():
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Subject", "Start Time", "End Time", "Duration (seconds)"])

# Class to handle a study session (Bonus points for OOP)
class StudySession:
    def __init__(self, subject):
        self.subject = subject
        self.start_time = None
        self.end_time = None
    
    def start(self):
        self.start_time = time.time()
    
    def end(self):
        self.end_time = time.time()
    
    def get_duration(self):
        if self.start_time and self.end_time:
            return round(self.end_time - self.start_time, 2)
        else:
            return 0

# Helper function to create a timed study session
def create_study_session():
    pygame.init()
    window_size = (400, 300)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Click to end session")
    white = (255, 255, 255)
    black = (0, 0, 0)
    window.fill(white)
    pygame.display.update()

    subject = input("Enter the subject you are studying: ").strip()
    if subject not in subjects:
        print("Subject not found. Adding it to the list.")
        subjects[subject] = {}

    session = StudySession(subject)
    session.start()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                session.end()
                running = False

    pygame.quit()
    return session

# Helper function to save session to CSV
def save_session_to_csv(session):
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
    while True:
        print("\n--- Main Menu ---")
        print("1. Create a timed study session")
        print("2. View past study sessions")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            session_menu()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Helper function: menu to create and optionally save a study session
def session_menu():
    while True:
        create_new = input("Would you like to create a timed study session? (yes/no): ").lower()
        if create_new == 'yes':
            session = create_study_session()

            keep = input("Is the study session you just had something you want to keep? (yes/no): ").lower()
            if keep == 'yes':
                save_session_to_csv(session)
                print("Session saved successfully.")
            else:
                print("Session discarded.")

            back_to_menu = input("This is it. Nothing else to do. Would you like to return to the main menu? (yes/no): ").lower()
            if back_to_menu == 'yes':
                break
        elif create_new == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Helper function to view sessions from CSV
def view_sessions():
    if not os.path.exists(csv_file):
        print("No study sessions found.")
        return

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        sessions = list(reader)
        
        if len(sessions) <= 1:
            print("No study sessions recorded yet.")
            return

        print("\n--- Study Sessions ---")
        for row in sessions[1:]:
            print(f"Subject: {row[0]}, Start: {row[1]}, End: {row[2]}, Duration: {row[3]} seconds")

# Run the program
if __name__ == "__main__":
    main_menu()
