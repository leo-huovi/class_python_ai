import numpy as np
import csv
import matplotlib.pyplot as plt

#Let's first explore the csv file by parsing the header:

with open('weight-height.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    
print(header, "\n------")
#> ['Gender', 'Height', 'Weight']

#Height is located as the second column, weight as the third

#Let's parse the CSV as numpy array by slicing the column by index, while including all rows

csv_data = np.genfromtxt("weight-height.csv",delimiter=",",skip_header=1)

height = csv_data[:, 1]
weight = csv_data[:, 2]

#Let's define and map numpy conversion functions on every height and weight element

def inch_to_cm(inch):
    cm = inch * 2.54
    return cm

def pound_to_kg(pound):
    kg = pound * 0.4536
    return kg

height_cm = np.array(list(map(inch_to_cm, height)))
weight_kg = np.array(list(map(pound_to_kg, weight)))

#Mean, median, standard deviation, variance:

print("Height (cm):")
print("Mean:", np.mean(height_cm))
print("Median:", np.median(height_cm))
print("Standard deviation:", np.std(height_cm))
print("Variance:", np.var(height_cm), "\n----")

print("Weight (kg):")
print("Mean:", np.mean(weight_kg))
print("Median:", np.median(weight_kg))
print("Standard deviation:", np.std(weight_kg))
print("Variance:", np.var(weight_kg), "\n----")

#Histogram

plt.hist(height_cm, 16)
