import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(data)
    fig = ff.create_distplot([data],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)