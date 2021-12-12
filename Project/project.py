import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv("Project/medium_data.csv")
data = df["reading_time"].tolist()

pop_mean = statistics.mean(data)
pop_std_dev = statistics.stdev(data)
print("Mean of population:", pop_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.5], mode="lines", name="Mean"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution:",mean )

setup()