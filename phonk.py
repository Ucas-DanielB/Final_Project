----------------------------------------------------------------------------------------------------------------------
#aiden's code

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# File path varibles (may be changed depending on what others need) 
file1 = 'homework.csv'
file2 = 'study_sessions.csv'

# hel[per for reading the files using os
def read_homework_csv():
    if not os.path.exists(file1):
        return pd.DataFrame()
    return pd.read_csv(file1)

# helper function for plotting pie charts 
def plot_pie_chart(data, labels, title):
    plt.figure()
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
    return (data, labels, title)

# displaying the last made pie chart 
def show_last_chart(chart_data):
    if chart_data is None:
        print("No chart to display.")
        return
    data, labels, title = chart_data
    plot_pie_chart(data, labels, title)

# homework filtering based on user inputs 
def summarize_homework(
    detailed=False,
    sort_by='class',
    secondary_sort='points',
    filter_class=None,
    filter_complete=None,
    due_before=None,
    min_points=None
):
    df = read_homework_csv()
    if df.empty:
        print("No tasks to summarize.")
        return None
#sorting based on filter inputs 
    if filter_class:
        df = df[df['class'].str.lower() == filter_class.lower()]
    if filter_complete is not None:
        df = df[df['complete'] == filter_complete]
    if due_before:
        df['due_date'] = pd.to_datetime(df['due_date'], errors='coerce')
        df = df[df['due_date'] <= pd.to_datetime(due_before)]
    if min_points:
        df = df[df['points'] >= min_points]

    df = df.sort_values(by=[sort_by, secondary_sort], ascending=[True, False])
    if df.empty:
        print("No tasks match the applied filters.")
        return None
#data for chars 
    chart_data = None
    for cls in df['class'].unique():
        class_df = df[df['class'] == cls]
        complete = class_df[class_df['complete'] == True]
        total = len(class_df)
        complete_count = len(complete)
        incomplete_count = total - complete_count
        chart_data = plot_pie_chart(
            [complete_count, incomplete_count],
            ['complete', 'Incomplete'],
            f"Homework Completion for {cls}"
        )

    print("\nFiltered Homework List:")
    if detailed:
        print(df.to_string(index=False))
    else:
        print(df[['name', 'class', 'points', 'complete']].to_string(index=False))

    return chart_data

#function to summarize study session using info from daniels section 
def summarize_sessions():
    if not os.path.exists(file2):
        print("No study session data found.")
        return

    df = pd.read_csv(file2)
    df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
    df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')
    df['duration'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60  # minutes

    total_time = df['duration'].sum()
    average_time = df['duration'].mean()
    recent_sessions = df.sort_values(by='end_time', ascending=False).head(3)

    print(f"Total study time: {total_time:.2f} minutes")
    print(f"Average study session: {average_time:.2f} minutes")
    print("3 Most Recent Sessions:")
    print(recent_sessions[['start_time', 'end_time', 'duration']].to_string(index=False))

# summary based on classes 
def display_info():
    df = read_homework_csv()
    if df.empty:
        print("No class data found.")
        return

    for cls in df['class'].unique():
        class_df = df[df['class'] == cls]
        not_done = class_df[class_df['complete'] == False]
        complete = class_df[class_df['complete'] == True]
        plot_pie_chart(
            [len(complete), len(not_done)],
            ['complete', 'Not complete'],
            f"Work Completion for {cls}"
        )

        print(f"\nClass: {cls}")
        print("Pending Work:")
        if not not_done.empty:
            print(not_done[['name', 'due_date', 'points']].to_string(index=False))
        else:
            print("No pending work.")

def summary_menu():
    last_chart_data = None

    while True:
        print("\n--- Homework & Study Summary Menu ---")
        print("1. Summarize Homework")
        print("2. Summarize Study Sessions")
        print("3. Display Class Info")
        print("4. View Last Chart")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()
        #choice one which also takes inputs for the filter info 
        if choice == '1':
            detailed = input("Show detailed list? (y/n): ").strip().lower() == 'y'

            filter_class = input("Filter by class (press Enter to skip): ").strip()
            filter_class = filter_class if filter_class else None
            
            filter_completed = input("Filter by completed? (yes/no/skip): ").strip().lower()
            if filter_completed == 'yes':
                filter_completed = True
            elif filter_completed == 'no':
                filter_completed = False
            else:
                filter_completed = None

            due_before = input("Filter by due date before (YYYY-MM-DD or skip): ").strip() #Inistailly issue when testing 
            due_before = due_before if due_before else None

            try:
                min_points = input("Minimum points (or skip): ").strip()
                min_points = int(min_points) if min_points else None
            except ValueError:
                min_points = None

            last_chart_data = summarize_homework(
                detailed=detailed,
                filter_class=filter_class,
                filter_completed=filter_completed,
                due_before=due_before,
                min_points=min_points
            )

        elif choice == '2':
            summarize_study_sessions()

        elif choice == '3':
            display_class_info()

        elif choice == '4':
            show_last_chart(last_chart_data)

        elif choice == '5':
            break

        else:
            print("Please enter a number from 1 to 5.")
#code should be working but some changes may need to be made depending on others code


--------------------------------------------------------------------------------------------------------------------
