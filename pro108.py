from os import name
import pandas as pd 
import plotly_express as px
import plotly.figure_factory as ff 
import csv 
name = ["Mobile Brand"]

df=pd.read_csv("C:/Users/Murali/Desktop/Adhok/python/pro108.csv")
name.append("Mobile Brand")

fig= ff.create_distplot([df["Avg Rating"].tolist()],["Samsung"], show_hist= False)
fig.show()