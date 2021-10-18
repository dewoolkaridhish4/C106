import pandas as pd
import plotly.express as px
import csv

with open("IceCream.csv") as csv_files:
    df=csv.DictReader(csv_files)
    fig=px.scatter(df,x="Temperature",y="Sale1")
    fig.show()