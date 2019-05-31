import csv
import os

#Storing the file path
budget_csv  = "budget_data.csv"

#opening file stream for reading csv file
with open (budget_csv,newline = "") as budget:
    budgetreader = csv.reader(budget,delimiter=",")

    #read the header first
    budget_header = next(budget)

    #prev_row = next(budget)
    #print(f"Previous row data : {prev_row}")

    count = 0
    totalAmount = 0
    prevRow = 0
    changeTotal = 0
    avg = 0

    #reading through the budget file
    for row in budgetreader:
        #print(f"current row data : {row}")
        #Number of months
        count = count + 1

        #Net total amount of profit/losses
        totalAmount = totalAmount + int(row[1])

        #change Total calculation
        if (prevRow == 0):
           changeTotal = 0
        else:
            changeTotal = changeTotal + (int(row[1]) - int(prevRow))

        prevRow = row[1]
        #print(f"previous row value is : {prevRow}")
        #print(f"change value is : {changeTotal}")

        
    #Average change
    avg = changeTotal / (count - 1) #change will be one less than total months

    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(totalAmount))
    #Formatting to restrict the decimal places to 2
    print("Average Change: {0}{1:.2f}".format("$",avg))

