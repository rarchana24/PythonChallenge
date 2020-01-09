import os
import csv

# Files to load and output
inputFile = "Resources/budget_data.csv"

#Create variables
totalmonths =[]
totalprofits =[]
profitchange=[]

with open(inputFile,newline="") as revenue_data:
    
    #file contents in a variable
    csvread = csv.reader(revenue_data,delimiter=",")
    header = next(csvread)
    
    #iteration 
    for row in csvread:
        #Append the values
        totalmonths.append(row[0])
        totalprofits.append(int(row[1]))
    #iterate profit per month
    for i in range(len(totalprofits)-1):
        profitchange.append(totalprofits[i+1] - totalprofits[i])

# get min and max profits
maxprofitvalue = max(profitchange)
minprofitvalue = min(profitchange)

#Get max and min profit month
maxprofitmonth = profitchange.index(max(profitchange)) +1 
minprofitmonth = profitchange.index(min(profitchange)) + 1

#printing the statements 
## Display Results ##      
#The total number of months
print(f'Total Months : {len(totalmonths)}')
#The total net amount
print(f'Total: $ {sum(totalprofits)}')
#Increase in profit
print(f'Greatest Increase in Profits: {totalmonths[maxprofitmonth]} (${(str(maxprofitvalue))})')
#Decrease in profit
print(f'Greatest Decrease in Profits: {totalmonths[minprofitmonth]} (${(str(minprofitvalue))})')
#Average Profit 
print(f'Average Profit : {round(sum(profitchange)/len(profitchange),2)}')

outfile = ("Resources/ProfitLoss.txt")
with open(outfile,"w") as revenueresult:
    #printing the statements again
    revenueresult.write(f"Profit/Loss")
    revenueresult.write("\n")
    #The total number of months
    revenueresult.write(f'Total Months : {len(totalmonths)}')
    revenueresult.write("\n")
    revenueresult.write(f'Total: $ {sum(totalprofits)}')
    revenueresult.write("\n")
    revenueresult.write(f'Greatest Increase in Profits: {totalmonths[maxprofitmonth]} (${(str(maxprofitvalue))})')
    revenueresult.write("\n")
    revenueresult.write(f'Greatest Decrease in Profits: {totalmonths[minprofitmonth]} (${(str(minprofitvalue))})')
    revenueresult.write("\n")
    revenueresult.write(f'Average Profit : {round(sum(profitchange)/len(profitchange),2)}')       

    