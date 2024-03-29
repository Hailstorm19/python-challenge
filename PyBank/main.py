import os
import csv
import numpy as np

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    total = 0
    total_spend = 0
    dates = []
    values = []
    
    csv_header = next(csv_file)
    
    for row in csv_reader:
        total = total + 1
        total_spend = total_spend + int(row[1])
        dates.append(row[0])
        values.append(int(row[1]))
        
    average_change = sum(np.diff(values))/len(values)
    max_index = values.index(max(values))
    min_index = values.index(min(values))
    
    max_date = dates[max_index]
    min_date = dates[min_index]
    max_profit = values[max_index]
    min_profit = values[min_index]
    
    print("Financial Analysis") 
    print("----------------------------")  
    print("Total Months:", total)
    print(f"Total: ${total_spend}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest increase in Profits: {max_date} (${max_profit})")
    print(f"Greatest decrease in Profits: {min_date} (${min_profit})")
    
    with open ("output.txt", "a") as f:
        print("Financial Analysis", file = f) 
        print("----------------------------", file = f)  
        print("Total Months:", total, file = f)
        print(f"Total: ${total_spend}", file = f)
        print(f"Average Change: ${round(average_change, 2)}", file = f)
        print(f"Greatest increase in Profits: {max_date} (${max_profit})", file = f)
        print(f"Greatest decrease in Profits: {min_date} (${min_profit})", file = f)        