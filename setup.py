import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    iceCream_sales =[]
    cooldrink_sales= []

    with open(data_path) as csv_file:
        reader=csv.DictReader(csv_file)
        for row in reader:
            iceCream_sales.append(float(row["Temperature"]))
            cooldrink_sales.append(float(row["Ice-cream Sales"]))

    return{'x':iceCream_sales,'y':cooldrink_sales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print('correlation between icecream vs temperatuer:: \n-->',correlation[0,1])

def setup():
    data_path='Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    dataSourc = getDataSource(data_path)
    findCorrelation(dataSourc)

setup()


