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


#code should be working but some changes may need to be made depending on others code


--------------------------------------------------------------------------------------------------------------------
