#This program counts the amount of white pixels in an image, as well as the percent of pixels that are white.
#Specifically made to determine the amount of snow that has melted from the Sierra Nevada range from 2011 - 2014.

import numpy as np
import matplotlib.pyplot as plt

file_name = input("Enter file name: ")
file_threshold = float(input("Enter threshold: "))

cali = plt.imread(file_name)
snowCount = 0
t = file_threshold
percentage = 0

for i in range(cali.shape[0]):
    for j in range(cali.shape[1]):
        if (cali[i,j,0] > t) and (cali[i,j,1] > t) and (cali[i,j,2] > t):
            snowCount = snowCount + 1

for i in range(cali.shape[0]):
    for j in range(cali.shape[1]):
        percentage = percentage + 1

print("number of white pixels is" ,snowCount)
print("percentage of white pixels is", float(round((snowCount/percentage)*100,2)),"%")