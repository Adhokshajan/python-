import plotly_express as px
import csv


with open("C:/Users/Murali/Desktop/Adhok/python/cupsOfCoffeVsHoursOfSleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.bar(df,x="Coffee ", y="sleep ")
    fig.show()