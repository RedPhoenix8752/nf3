import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
mean = statistics.mean(data)
st_dev = statistics.stdev(data)
#population_mean = statistics.mean(data)
print("mean is: ", mean)
print("standard deviation is: ", st_dev)
fig = ff.create_distplot([data],["temp"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1], mode = "lines", name = "mean"))
fig.show()