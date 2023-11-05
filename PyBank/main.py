import os
import csv

#Path to collect data from the Resources folder
budgetDatapath = r"C:\Users\Iris2812052\Desktop\python-challenge\PyBank\Resources\budget_data.csv"

#Define the function and have it accept the "budget Data" as its sole paramenter
def pyBank(budgetData):


#total number of months included in the dataset
#Use len method to calculate the total row (Months)
    totalMonths = len(budgetData)
    
    
#Net total amount of "Profit/Losses" Over the entire period
#loop all the row in budgetData
#sum the row in column 2
#assign the the sum to a variable - totalProfitLoss
    totalProfitLoss = sum(int(row[1]) for row in budgetData)
    
 #Changes in "Profit/Losses" over the entire period, and then the average of those changes
 #set changes and datechage as list 
 #loop through the csv file, pull the value for current month and pervious month
 #Calculate the monthly change by subtracting current month from pervious month
 #add all the monthly change into changes list
 #add date into the dateChange list
 #Calculate the average of changes and round the result to 2 decimials

    changes = []
    dateChange = []

    for i in range(1,totalMonths):
        perviousProfitLoss = int(budgetData[i-1][1])
        currentProfitLoss = int(budgetData[i][1])
        monthlyChange = currentProfitLoss - perviousProfitLoss
        changes.append(int(monthlyChange))
        dateChange.append(budgetData[i][0])
    
    averageOfChanges = sum(changes) / len(changes)
    averageOfChanges = round(averageOfChanges,2)

#Pull The greatest increase in profits (Date and amount) over the entire period
#Use max methon to find the greatest increase
#return the month which associated with greatest increase

    greatestIncrease = max(changes)
    greatestIncreaseMonth = dateChange[changes.index(greatestIncrease)]
    
#Pull The greatest decrease in profits(date and amount) over the entire period
#Use max methon to find the greatest decrease
#return the month which associated with greatest decrease
    greatestDecrease = min(changes)
    greatestDecreaseMonth = dateChange[changes.index(greatestDecrease)] 

    
    print("Financial Analysis")
    print("-----------------------------------------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfitLoss}")
    print(f"Average Change: ${averageOfChanges}")
    print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")

budgetData = []
with open(budgetDatapath, encoding="UTF-8") as csvFiles:
    csvReader = csv.reader(csvFiles, delimiter=",")
    csvHeader = next(csvReader)
   
    for row in csvReader:
        budgetData.append(row)

pyBank(budgetData)


