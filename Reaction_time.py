# import matplotlib.pyplot as plt
# import csv
# import time
# def reaction():
#     # Extract the timestamps of clicks from the log file
#     timestamps = []
#     with open("mouse_log.txt") as file:
#         for line in file:
#             # print(line)
#             if line.split()[2] == "C":
#                 timestamp = line[:19]
#                 timestamps.append(time.strptime(timestamp, '%Y-%m-%d %H:%M:%S'))
#
#     # Calculate the time between clicks
#     time_diff = []
#     for i in range(1, len(timestamps)):
#         time_diff.append(time.mktime(timestamps[i]) - time.mktime(timestamps[i-1]))
#
#     # Plot the averages of every 10 clicks
#     averages = []
#     for i in range(0, len(time_diff), 10):
#         averages.append(sum(time_diff[i:i+10])/10)
#
#     plt.plot(averages)
#     plt.savefig("time_between_clicks.png")
#     with open('C:\eyetrack\PyTribe\example\reaction_results.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(averages)
import os
import re
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import time
rootpath = r'C:\eyetrack\PyTribe\example\python_samples'
files_root = [file for file in os.listdir(rootpath)]
for folder in files_root:
    # Define the folder path
    folder_path = f'C:/eyetrack/PyTribe/example/python_samples/{folder}/Screenshots'
    # Get all the png files in the folder
    files = [file for file in os.listdir(folder_path) if file.endswith('.png')]

    # Extract the timestamps from the file names
    timestamps = []
    for file in files:
        match = re.search(r'file_(\d+?).\d+.png', file)
        if match:
            timestamp = int(match.group(1))
            timestamps.append(timestamp)

    # Sort the timestamps
    timestamps.sort()

    # Convert the timestamps to datetime objects
    datetimes = [datetime.fromtimestamp(ts) for ts in timestamps]

    # Create a list with the time differences between two consecutive datetime objects in seconds
    time_differences = [(datetimes[i+1] - datetimes[i]).total_seconds() for i in range(len(datetimes)-1)]
    # Plot the averages of every 10 clicks
    averages = []
    for i in range(0, len(time_differences), 10):
        averages.append(sum(time_differences[i:i+10])/10)

    plt.plot(averages)
    plt.savefig(f"C:/eyetrack/PyTribe/example/python_samples/{folder}/time_between_clicks.png")
    plt.close()
    with open(r'C:/eyetrack/PyTribe/example/reaction_results.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(averages)
