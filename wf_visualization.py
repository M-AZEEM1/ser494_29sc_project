

# Program file for computing basic stats, correlations, and visualization
#

# NOTICE:
# Using my code from hw3q2 as a base



__author__ = "???"
__date__ = "3.6.2026"



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
    Outputs mean, median, and mode of each quantitative feature of choice (see project_ecploration.md)
    from human_selected_dataset.csv

    """

    channel_counter = 0

    file = open('data_original/human_selected_dataset.csv', encoding="utf-8")

    # opens csv file and stores data into dictionary
    datafile = c.DictReader(file)

    code_sizes = list()
    cpu_times = list()
    memory_vals = list()


    for entry in datafile:
        code_sizes.append(float(entry.get('code_size')))
        cpu_times.append(float(entry.get('cpu_time')))
        memory_vals.append(float(entry.get('memory')))



    code_size_median = statistics.median(code_sizes)
    code_size_mode = statistics.mode(code_sizes)
    code_size_mean = statistics.mean(code_sizes)

    cpu_time_median = statistics.median(cpu_times)
    cpu_time_mode = statistics.mode(cpu_times)
    cpu_time_mean = statistics.mean(cpu_times)

    memory_val_median = statistics.median(memory_vals)
    memory_val_mode = statistics.mode(memory_vals)
    memory_val_mean = statistics.mean(memory_vals)

    __file__ = "data_processed\\summary.txt"

    outfile = open(__file__, "x")

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
    matrix = {
        "code_size": [],
        "cpu_time": [],
        "memory": []
    }

    df = pandas.DataFrame(matrix, index=["code_size", "cpu_time", "memory"])


    pass


if __name__ == '__main__':
    compute_stats()
