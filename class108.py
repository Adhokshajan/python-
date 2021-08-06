import pandas as pd 
import plotly.figure_factory as ff 
import csv 
df=pd.read_csv("C:/Users/Murali/Desktop/Adhok/python/c108.csv")
fig= ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"], show_hist=False)
fig.show()