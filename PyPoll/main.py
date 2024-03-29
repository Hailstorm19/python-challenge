import os
import csv
import numpy as np

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    total = 0
    candidate = []    
    values = []
    
    csv_header = next(csv_file)
    
    for row in csv_reader:
        total = total + 1
        candidate.append(row[2])
        
    set_candidate = set(candidate)
    
    def most_frequent(List):
        return max(set(List), key = List.count)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print('-------------------------')
        
    for item in set_candidate:
        amount = candidate.count(item)
        percent_votes = (amount / total) * 100
        print(f'{item}: {round(percent_votes, 2)}% ({amount})')
        
    print('-------------------------')
    print(f"Winner: {most_frequent(candidate)} ")
    print('-------------------------') 
    
    with open ("output2.txt", "a") as f:
        print("Election Results", file = f)
        print("-------------------------", file = f)
        print(f"Total Votes: {total}", file = f)
        print('-------------------------', file = f)
        
        for item in set_candidate:
            amount = candidate.count(item)
            percent_votes = (amount / total) * 100
            print(f'{item}: {round(percent_votes, 2)}% ({amount})', file = f)
        
        print('-------------------------', file = f)
        print(f"Winner: {most_frequent(candidate)} ", file = f)
        print('-------------------------', file = f)