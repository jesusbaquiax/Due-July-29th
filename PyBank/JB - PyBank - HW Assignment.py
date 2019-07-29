#Import Data
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

total_month = []
total_amount = []
average_change = []
greatest_increase = []
greatest_decrease = []

with open(csvpath,newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")










# Final Analysis
# Total Months: XX

# Total: $XX

# Average Change: $XX

# Greatest Increase in Profits:

# Greatest Decrease in Profits: XX/XX ($XX)