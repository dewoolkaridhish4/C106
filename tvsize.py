import csv 
import numpy as np

def getdatasource(datapath):
    time=[]
    size=[]
    with open(datapath) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            time.append(float(row["Time"]))
            size.append(float(row["Size"]))
    return {"x":time,"y":size}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("CORRELATION BEETWEEN TIME AND SIZE = ",correlation[0,1])

def setup():
    datapath="Size of Tv.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup() 