import pandas as pd 
import plotly_express as px  
data=[1,2,3,4,5]
df=pd.read_csv("C:/Users/Murali/Desktop/Adhok/python/c 103.csv")
fig=px.bar(df,x="date",y="cases",color="country")
fig.show()


