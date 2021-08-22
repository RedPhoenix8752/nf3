import random
import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("hw.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

heightmean = statistics.mean(height_list)
weightmean = statistics.mean(weight_list)

heightmedian = statistics.median(height_list)
weightmedian = statistics.median(weight_list)

heightmode = statistics.mode(height_list)
weightmode = statistics.mode(weight_list)

heightstdev = statistics.stdev(height_list)
weightstdev = statistics.stdev(weight_list)

print("mean, median, mode of height: {}, {}, {}".format(heightmean, heightmedian, heightmode))
print("mean, median, mode of weight: {}, {}, {}".format(weightmean, weightmedian, weightmode))

height_first_standard_deviation_start, height_first_standard_deviation_end = heightmean - heightstdev, heightmean + heightstdev
list_of_data_within_1_standard_deviation = [result for result in height_list if result > height_first_standard_deviation_start and result < height_first_standard_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100/len(df)))


height_second_standard_deviation_start, height_second_standard_deviation_end = heightmean - (2*heightstdev), heightmean + (2*heightstdev)
list_of_data_within_2_standard_deviation = [result for result in height_list if result > height_second_standard_deviation_start and result < height_second_standard_deviation_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100/len(df)))


height_third_standard_deviation_start, height_third_standard_deviation_end = heightmean - (3*heightstdev), heightmean + (3*heightstdev)
list_of_data_within_3_standard_deviation = [result for result in height_list if result > height_third_standard_deviation_start and result < height_third_standard_deviation_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100/len(df)))

weight_first_standard_deviation_start, weight_first_standard_deviation_end = weightmean - weightstdev, weightmean + weightstdev
list_of_data_within_1_standard_deviation = [result for result in weight_list if result > weight_first_standard_deviation_start and result < weight_first_standard_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100/len(df)))


weight_second_standard_deviation_start, weight_second_standard_deviation_end = weightmean - (2*weightstdev), weightmean + (2*weightstdev)
list_of_data_within_2_standard_deviation = [result for result in weight_list if result > weight_second_standard_deviation_start and result < weight_second_standard_deviation_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100/len(df)))


weight_third_standard_deviation_start, weight_third_standard_deviation_end = weightmean - (3*weightstdev), weightmean + (3*weightstdev)
list_of_data_within_3_standard_deviation = [result for result in weight_list if result > weight_third_standard_deviation_start and result < weight_third_standard_deviation_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100/len(df)))

