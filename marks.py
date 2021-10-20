import csv
import numpy as np
import plotly_express as px
def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()
def getDataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_present}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks and days:\n--->",correlation[0,1])
def setup():
    data_path="marks.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path) 
setup()