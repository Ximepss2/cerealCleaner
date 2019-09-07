#import modules
import os
import csv

#open csv
cerealCSV = os.path.join(".","resources","cereal.csv")

with open(cerealCSV,"r", encoding="UTF-8") as csvfile:
    #create CSV reader
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvHeader=next(csvreader)
    print(csvHeader)
    #iterate rows (for loop)
    for row in csvreader:
        #if statement (if cereal contains 5 or more grams of fiber, print)
        if float(row[7])>=5:
            #print if condition meets
            print(row)

