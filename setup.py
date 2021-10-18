import csv 
import plotly.express as px
import numpy as np

def plotfigure(datapath):
    with open(datapath) as csv_files:
        df=csv.DictReader(csv_files)
        fig=px.scatter(df,x="Temperature",y="Sale1")
        fig.show()

def getdatasource(datapath):
    icecreame=[]
    colddrink=[]
    with open(datapath) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            icecreame.append(float(row["Temperature"]))
            colddrink.append(float(row["Sale1"]))
    return {"x":icecreame,"y":colddrink}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("CORRELATION BEETWEEN ICE CREAM AND COLD DRINK = ",correlation[0,1])

def setup():
    datapath="IceCream.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)
    plotfigure(datapath)

setup() 