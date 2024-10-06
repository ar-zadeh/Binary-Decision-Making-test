import matplotlib.pyplot as plt
import csv
import os
def Plotter(folder):
    # read the file and create the list
    results = []
    with open(f"C:/eyetrack/PyTribe/example/python_samples/{folder}/results.txt", "r") as f:
        for line in f:
            # print(line)
            if line.strip() == "Heads":
                results.append(1)
            else:
                results.append(0)
    # create blocks of 10 iterations
    block_size = 10
    block_count = len(results) // block_size
    ratios = []
    for i in range(block_count):
        block = results[i * block_size:(i + 1) * block_size]
        ratio = sum(block) / block_size
        ratios.append(ratio)
    with open('C:/eyetrack/PyTribe/example/headprop.csv', 'a') as file:
        writer = csv.writer(file)
        # Write the ratios as a new row in the csv file
        writer.writerow(ratios)



    # plot the ratio of heads in every 10 iterations
    plt.scatter(range(len(ratios)), ratios)
    plt.plot(range(len(ratios)), ratios)
    # plt.axhline(y=0.6, color='r', linestyle='-')
    plt.xlabel("Block Number")
    plt.ylabel("Ratio of Heads")
    plt.savefig(f"C:/eyetrack/PyTribe/example/python_samples/{folder}/Proportions.png")
    plt.close()
rootpath = r'C:\eyetrack\PyTribe\example\python_samples'
files_root = [file for file in os.listdir(rootpath)]
for folder in files_root:
    Plotter(folder)


