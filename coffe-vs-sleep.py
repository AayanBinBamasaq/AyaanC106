from ast import Expression
import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv") as csv_file:
    reader =csv.DictReader(csv_file)
    plot = px.scatter(reader, x="Coffee_in_ml", y="sleep_in_hours")
    plot.show()
