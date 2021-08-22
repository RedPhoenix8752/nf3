import random
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

count = []
dice = []

for i in range(0, 1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)
    count.append(i)

mean = sum(dice)/len(dice)
print("mean is: " + str(mean))

median = statistics.median(dice)
print("median is: " + str(median))

mode = statistics.mode(dice)
print("mode is: " + str(mode))

stdev = statistics.stdev(dice)
print("standard deviation is: " + str(stdev))

fig = ff.create_distplot([dice], ["result"], show_hist = False)
fig.show()
first_standard_deviation_start, first_standard_deviation_end = mean - stdev, mean + stdev
list_of_data_within_1_standard_deviation = [result for result in dice if result > first_standard_deviation_start and result < first_standard_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100/len(dice)))


second_standard_deviation_start, second_standard_deviation_end = mean - (2*stdev), mean + (2*stdev)
list_of_data_within_2_standard_deviation = [result for result in dice if result > second_standard_deviation_start and result < second_standard_deviation_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100/len(dice)))


third_standard_deviation_start, third_standard_deviation_end = mean - (3*stdev), mean + (3*stdev)
list_of_data_within_3_standard_deviation = [result for result in dice if result > third_standard_deviation_start and result < third_standard_deviation_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100/len(dice)))
