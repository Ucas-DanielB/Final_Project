
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Helper function to read homework CSV
def read_homework_csv(filename='homework.csv'):
    if not os.path.exists(filename):
        return pd.DataFrame()
    df = pd.read_csv(filename)

    expected_columns = {'name', 'class', 'points', 'completed', 'due_date'}
    if not expected_columns.issubset(df.columns):
        print(f"Missing required columns in {filename}")
        return pd.DataFrame()

    df['completed'] = df['completed'].astype(bool)
    return df

# General pie chart function
def plot_pie_chart(data, labels, title, filename=None):
    plt.figure()
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()

# Overall summary
def summarize_overall_progress(df):
    total = len(df)
    completed = len(df[df['completed'] == True])
    incomplete = total - completed
    print(f"\nOverall Completion: {completed}/{total} tasks completed ({completed / total:.1%})")

# Summarize homework tasks
def summarize_homework(filename='homework.csv', detailed=False, sort_by='class', secondary_sort='points'):
    df = read_homework_csv(filename)
    if df.empty:
        print("No tasks to be summarized")
        return

    df = df.sort_values(by=[sort_by, secondary_sort], ascending=[True, False])
    summarize_overall_progress(df)

    classes = df['class'].unique()
    for cls in classes:
        class_df = df[df['class'] == cls]
        completed = class_df[class_df['completed'] == True]
        total = len(class_df)
        completed_count = len(completed)
        incomplete_count = total - completed_count

        plot_pie_chart(
            [completed_count, incomplete_count],
            ['Completed', 'Incomplete'],
            f"Homework Completion for {cls}",
            filename=f"{cls}_homework_completion.png"
        )

    # Display list
    if detailed:
        print(df.to_string(index=False))
    else:
        print(df[['name', 'class', 'points', 'completed']].to_string(index=False))

# Summarize study sessions
def summarize_study_sessions(filename='study_sessions.csv'):
    if not os.path.exists(filename):
        print("No study session data found.")
        return

    df = pd.read_csv(filename)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])
    df['duration'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60  # minutes

    total_time = df['duration'].sum()
    average_time = df['duration'].mean()
    recent_sessions = df.sort_values(by='end_time', ascending=False).head(3)

    print(f"Total study time: {total_time:.2f} minutes")
    print(f"Average study session: {average_time:.2f} minutes")
    print("3 Most Recent Sessions:")
    print(recent_sessions[['start_time', 'end_time', 'duration']].to_string(index=False))

# Display class information
def display_class_info(homework_file='homework.csv'):
    df = read_homework_csv(homework_file)
    if df.empty:
        print("No class data found.")
        return

    classes = df['class'].unique()

    for cls in classes:
        class_df = df[df['class'] == cls]
        not_done = class_df[class_df['completed'] == False]
        completed = class_df[class_df['completed'] == True]

        plot_pie_chart(
            [len(completed), len(not_done)],
            ['Completed', 'Not Completed'],
            f"Work Completion for {cls}",
            filename=f"{cls}_work_completion.png"
        )

        print(f"\nClass: {cls}")
        print("Pending Work:")
        print(not_done[['name', 'due_date', 'points']].to_string(index=False)
#don't forget to add to mai nand create menu for selection instead of running all 

