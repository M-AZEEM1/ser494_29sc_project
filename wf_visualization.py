

# Program file for computing basic stats, correlations, and visualization
#

#




# Package Imports

from ast import pattern
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pandas
# import seaborn - advanced data vis
import csv as c
import statistics
import math
import re


# Statistic generation

def compute_stats():
    """
    Outputs mean, median, and mode of each quantitative feature of choice (see project_exploration.md)
    from human_selected_dataset.csv

    """


    file = open('data_original/human_selected_dataset.csv', encoding="utf-8")

    __file__ = "data_processed\\summary.txt"

    outfile = open(__file__, "x")

    # opens csv file and stores data into dictionary
    datafile = c.DictReader(file)

    code_sizes = list()
    cpu_times = list()
    memory_vals = list()
    statuses = list()
    prob_ids = list()


    for entry in datafile:
        code_sizes.append(float(entry.get('code_size')))
        cpu_times.append(float(entry.get('cpu_time')))
        memory_vals.append(float(entry.get('memory')))
        statuses.append(entry.get('status'))
        prob_ids.append(int((entry.get('problem_id'))[1:]))




    code_size_median = statistics.median(code_sizes)
    code_size_mode = statistics.mode(code_sizes)
    code_size_mean = statistics.mean(code_sizes)

    cpu_time_median = statistics.median(cpu_times)
    cpu_time_mode = statistics.mode(cpu_times)
    cpu_time_mean = statistics.mean(cpu_times)

    memory_val_median = statistics.median(memory_vals)
    memory_val_mode = statistics.mode(memory_vals)
    memory_val_mean = statistics.mean(memory_vals)


    # Compute number and freq of categories - 'status'

    categories = dict()

    for i in statuses:
        if i not in categories.keys():
            categories[i] = 1

        else:
            temp = categories.get(i)
            categories[i] = temp+1




    status_mfc = 0
    mfc = list(categories.keys())[0]

    status_lfc = list(categories.values())[0]
    lfc = list(categories.keys())[0]


    j = 0
    while j < len(categories):
        if categories.get(list(categories.keys())[j]) > status_mfc:
            status_mfc = categories.get(list(categories.keys())[j])
            mfc = list(categories.keys())[j]

        if categories.get(list(categories.keys())[j]) < status_lfc:
            status_mfc = categories.get(list(categories.keys())[j])
            lfc = list(categories.keys())[j]

        j+=1

    flag = 0


    if (mfc == lfc):
        flag = 1


    status_num_categories = len(categories.keys())

    outfile.write("\n<Qualitative Feature 1: 'status'>\n")
    outfile.write("Number of categories: " + str(status_num_categories))

    if(flag == 1):
        outfile.write("\nMost frequent category/ies: " + "Accepted, Runtime Error, Wrong Answer")
        outfile.write("\nLeast frequent category/ies: " + "Accepted, Runtime Error, Wrong Answer")
        outfile.write("\nNOTE: surprisingly, all categories have the exact same frequency as can be seen in the dictionary outfile.writeout below: \n")
        outfile.write(str(categories))
        outfile.write("\n(The total number of records in the 'human_selected' dataset was 4,755 which is 3 * 1585 so it adds up)\n")

    else:
        outfile.write("\nMost frequent category: " + mfc)
        outfile.write("\nLeast frequent category: " + lfc)

    outfile.write("Tabular output: \n")
    tabular = {
        "Accepted": categories.get('Accepted'),
        "Runtime Error": categories.get('Runtime Error'),
        "Wrong Answer": categories.get('Wrong Answer')
    }
    table = pandas.DataFrame(tabular, index=["Frequency"])
    outfile.write(table.to_string())

    outfile.write("\n")
    outfile.write("\n")
    outfile.write("\n")

    # Compute number and freq of categories - 'problem_id'

    id_set = dict()

    for k in prob_ids:
        if k not in id_set.keys():
            id_set[k] = 1

        else:
            temp = id_set.get(k)
            id_set[k] = temp + 1

    id_mfc = 0
    prob_mfc = list(id_set.keys())[0]


    id_lfc = (list(id_set.values()))[0]
    prob_lfc = (list(id_set.keys()))[0]



    j = 0
    while j < len(id_set):
        if id_set.get(list(id_set.keys())[j]) > id_mfc:
            id_mfc = id_set.get(list(id_set.keys())[j])
            prob_mfc = list(id_set.keys())[j]

        if id_set.get(list(id_set.keys())[j]) < id_lfc:
            id_lfc = id_set.get(list(id_set.keys())[j])
            prob_lfc = list(id_set.keys())[j]

        j += 1

    flag = 0

    if (id_mfc == id_lfc):
        flag = 1

    id_num_id_categories = len(id_set.keys())

    outfile.write("\n<Qualitative Feature 2: 'problem_id'>\n")
    outfile.write("Number of categories: " + str(id_num_id_categories))

    if (flag == 1):
        outfile.write(
            "\nNOTE: Due to 317 different categories, could not list them all as the most frequent/least frequent categories because surprisingly, once again all categories (categories = problem ID's here) equally have the exact same frequency of 15 as can be seen in the dictionary printout below: \n")
        outfile.write(str(id_set))

    else:
        outfile.write("\nMost frequent category: " + str(id_mfc))
        outfile.write("\nLeast frequent category: " + str(id_lfc))

    outfile.write("\n\nTabular output (Frequency per Problem ID): \n")

    pid_table = pandas.DataFrame(id_set, index=["Frequency"])

    outfile.write(pid_table.to_string())

    outfile.write("\n")
    outfile.write("\n")
    outfile.write("\n")

    ##### Generate visualization plots #####

    # AB
    plt.figure(figsize=(10, 10))
    plt.scatter(code_sizes, cpu_times, linewidths=1)
    plt.xlabel("Code Sample Sizes (# of characters)", fontsize = 20, fontweight='bold')
    plt.ylabel("CPU Times (seconds)", fontsize = 20, fontweight='bold')
    plt.title("Scatterplot of Code Size vs. CPU Time per Submission", fontweight='bold')
    plt.xticks(rotation=90)

    #plt.show()
    plt.savefig("visuals\\AB.png")


    # AC
    plt.figure(figsize=(10, 10))
    plt.scatter(code_sizes, memory_vals, linewidths=1)
    plt.ticklabel_format(style='plain')
    plt.xlabel("Code Sample Sizes (# of characters)", fontsize=20, fontweight='bold')
    plt.ylabel("Memory Used (KB)", fontsize=20, fontweight='bold')
    plt.title("Scatterplot of Code Size vs. Memory Used per Submission", fontweight='bold')

    plt.xticks(rotation=90)

    #plt.show()
    plt.savefig("visuals\\AC.png")

    # BC
    plt.figure(figsize=(10, 10))
    plt.scatter(cpu_times, memory_vals, linewidths=1)
    plt.ticklabel_format(style='plain')
    plt.xlabel("CPU Times (seconds)", fontsize = 20, fontweight='bold')
    plt.ylabel("Memory Used (KB)", fontsize=20, fontweight='bold')
    plt.title("Scatterplot of CPU Time vs. Memory Used per Submission", fontweight='bold')

    plt.xticks(rotation=90)

    plt.savefig("visuals\\BC.png")
    #plt.show()



    # Histogram - 'status'

    plt.figure(figsize=(10, 15))
    plt.hist(statuses)
    plt.title('Histogram: Code Submission Status', fontweight='bold')
    plt.xlabel("Submission Status", fontsize = 20, fontweight='bold')
    plt.ylabel("Frequency", fontsize = 20, fontweight='bold')

    #plt.show()
    plt.savefig('visuals\\status_histogram.png')



    # Histogram - 'problem_id'

    plt.figure(figsize=(10, 15))
    plt.hist(prob_ids, bins=20)
    plt.title('Histogram: Problems Attempted for Across Submission Code Samples', fontweight='bold')
    plt.xlabel("Problem ID", fontsize=20, fontweight='bold')
    plt.ylabel("Frequency", fontsize=20, fontweight='bold')
    plt.xticks(rotation=90)


    # plt.show()
    plt.savefig('visuals\\prob_id_histogram.png')




    #Write statistics to output file



    outfile.write("<Quantitative Feature 1>\n")
    outfile.write("code_size_median: " + str(code_size_median))
    outfile.write("\ncode_size_mode: " + str(code_size_mode))
    outfile.write("\ncode_size_mean: " + str(code_size_mean))

    outfile.write("\n")

    outfile.write("\n<Quantitative Feature 2>")
    outfile.write("\ncpu_time_median: " + str(cpu_time_median))
    outfile.write("\ncpu_time_mode: " + str(cpu_time_mode))
    outfile.write("\ncpu_time_mean: " + str(cpu_time_mean))

    outfile.write("\n")

    outfile.write("\n<Quantitative Feature 3>")
    outfile.write("\nmemory_val_median: " + str(memory_val_median))
    outfile.write("\nmemory_val_mode: " + str(memory_val_mode))
    outfile.write("\nmemory_val_mean: " + str(memory_val_mean))





    pass


# Correlation matrix for quantitative features
def generate_matrix():
    __file__ = "data_processed\\correlations.txt"

    exportfile = open(__file__, "x")

    matrix = {
        "code_size": [1.000, 0, 0],
        "cpu_time": [0, 1.000, 0],
        "memory": [0, 0, 1.000]
    }

    exportfile.write("\nCorrelation matrix: \n")
    df = pandas.DataFrame(matrix, index=["code_size", "cpu_time", "memory"])

    exportfile.write(df.to_string())

    pass


if __name__ == '__main__':


    pass