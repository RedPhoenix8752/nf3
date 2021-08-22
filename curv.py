import csv
import pandas as pd
import random
import plotly.figure_factory as ff

count = []
dice = []

for i in range(0, 100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1 + dice2)
    count.append(i)
print(count, dice)

fig = ff.create_distplot([dice], ["result"])
fig.show()