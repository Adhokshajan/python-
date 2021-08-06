from c110 import standard_deviation
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv 

df = pd. read_csv("studentMarksc111.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
fig.show()

mean = statistics.mean(data)
standarddeviation = statistics.stdev(data)
print(mean , standarddeviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)



std_deviation = statistics.stdev(mean_list)
print(std_deviation)






fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()


first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)







fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show()










df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3) 
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()







df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample2:- ",mean_of_sample2) 
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT EXTRA CLASEsS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()













df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("mean of sample1:- ",mean_of_sample1) 
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT TABS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 




fig.show()






















zscore = (mean_of_sample3 - mean)/std_deviation
print( "zscore = " + zscore)