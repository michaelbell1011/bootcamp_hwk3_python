# Your task is to create a Python script that calculates the following:

    # The total number of months included in the dataset
    # The total net amount of "Profit/Losses" over the entire period
    # The average change in "Profit/Losses" between months over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# Dependencies
import os
import csv

# lists for storing parsed csv data
months = []
profits = []

# read in csv
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#     prints the csv object-- not needed here
#     print(csvreader)

#     # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header and compile data into separate lists
    for row in csvreader:
#         print(row)
        months.append(row[0])
        profits.append(int(row[1]))
#         profits_delta.append(int(row[1]) - profits_delta[-1])


# CALCULATIONS 
# # caluculating The average CHANGE in "Profit/Losses" between months over the entire period
# Average Profits Delta
        # # NOT average profits:
        # avg_profits = Net_Profits / len(profits)
        # print(f"Total Average Profits: ${avg_profits}")
prev_prof = 0
profits_delta_list = []

for n in profits:
    profits_delta_list.append(n - prev_prof)
    prev_prof = n
avg_profits_delta = round(sum(profits_delta_list)/(len(profits_delta_list)))
# print(f"Average change in Profits between Months: ${avg_profits_delta}")

# # identifying The greatest increase in profits (date and amount) over the entire period
greatest_delta = max(profits_delta_list)
# print(greatest_delta)
greatest_delta_ndx = profits_delta_list.index(max(profits_delta_list))
greatest_delta_mo = months[greatest_delta_ndx]
# print(f"Greatest increase in Profits between Months was: {greatest_delta_mo} (${greatest_delta})")

# # identifying The greatest decrease in losses (date and amount) over the entire period
smallest_delta = min(profits_delta_list)
# print(smallest_delta)
smallest_delta_ndx = profits_delta_list.index(min(profits_delta_list))
smallest_delta_mo = months[smallest_delta_ndx]
# print(f"Greatest descrease in Profits between Months was: {smallest_delta_mo} (${smallest_delta})")



# OUTPUT TABLE TO CMD LINE
print('''
Financial Analysis
=====================================
''')
# # The total number of months included in the dataset
# count of month entries
print("Total number of Month entries:" + str(len(months)))

# # The total net amount of "Profit/Losses" over the entire period
# net profits
Net_Profits = sum(profits)
print(f"Total Net Profits: ${Net_Profits}")

# # The average CHANGE in "Profit/Losses" between months over the entire period
# Average Profits Delta
print(f"Average change in Profits between Months: ${avg_profits_delta}")

# # The greatest increase in profits (date and amount) over the entire period
print(f"Greatest increase in Profits: {greatest_delta_mo} (${greatest_delta})")

# # The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest descrease in Profits: {smallest_delta_mo} (${smallest_delta})")


# OUTPUT TABLE TO TXT FILE-- opens in current directory
file = open('Financial_Analysis.txt', 'w')

file.write('''
Financial Analysis
=====================================
''')
file.write("Total number of Month entries:" + str(len(months)))
file.write('\n' + f"Total Net Profits: ${Net_Profits}")
file.write('\n' + f"Average change in Profits between Months: ${avg_profits_delta}")
file.write('\n' + f"Greatest increase in Profits: {greatest_delta_mo} (${greatest_delta})")
file.write('\n' + f"Greatest descrease in Profits: {smallest_delta_mo} (${smallest_delta})")

file.close()
