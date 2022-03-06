from ast import Expression
import plotly.express as px
import csv

with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
    reader =csv.DictReader(csv_file)
    plot = px.scatter(reader, x="Temperature", y="Ice-cream Sales")
    plot.show()
