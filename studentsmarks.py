import csv 
import numpy as np

def getdatasource(datapath):
    marks=[]
    days=[]
    with open(datapath) as csv_files:
        csv_reader=csv.DictReader(csv_files)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks,"y":days}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("CORRELATION BEETWEEN MARKS AND DAYS = ",correlation[0,1])

def setup():
    datapath="StudentsAndDays.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)

setup() 