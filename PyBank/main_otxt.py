import os
import csv

csvpath=os.path.join('Resources','budget_data.csv')

with open (csvpath, 'r') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')
    
    csv_header=next(csv_read)
    
    date=[]
    pl=[]
    plch=[]
    total_pl = 0.0
    total_plch = 0.0
    max_pld=[]
    min_pld=[]
    
    for budget_data in csv_read:
        date.append(budget_data[0])
        pl.append(budget_data[1])

    #The total number of months included in the dataset
    total_months = len(date)
        
    #The net total amount of "Profit/Losses" over the entire period
    for row in range(total_months):
        total_pl += float(pl[row])
    
    #The changes in "Profit/Losses" over the entire period, then find the average of those changes      
    for row1 in range(1, (total_months)):
        plch.append(float(pl[row1]) - float(pl[(row1-1)]))
        total_plch += float(plch[(row1-1)])
    #average
    #total_plch += float(plch[row1])
    ave_plch = total_plch / (total_months - 1)
        
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    max_pl = max(plch)
    min_pl = min(plch)

    date1=[]
    for r1 in range(1,len(plch)):
        date1.append(date[r1])
    maxpl_zip = zip(date1, plch)

    mz=list(maxpl_zip)
    
    for row2 in range(len(plch)):
        if plch[row2] == max_pl:
            max_pld = mz[row2] 
        elif plch[row2] == min_pl:
            min_pld = mz[row2]
   
    
    print("-----------------------------")
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${int(total_pl)}")
    print(f"Average Change: ${round(ave_plch,2)}")
    print("Greatest Increase in Profits: " + str(max_pld[0]) + " ($" + str(int(max_pld[1])) + ")")
    print("Greatest Decrease in Profits: " + str(min_pld[0]) + " ($" + str(int(min_pld[1])) + ")") 
    print("'''")

    output_path = os.path.join('Financial_Analysis.txt')
    
with open(output_path, 'w', newline='') as fao:    

    fao.write("----------------------------- \n")
    fao.write("Financial Analysis \n")
    fao.write("----------------------------- \n")
    fao.write(f"Total Months: {total_months} \n")
    fao.write(f"Total: ${int(total_pl)} \n")
    fao.write(f"Average Change: ${round(ave_plch,2)} \n")
    fao.write("Greatest Increase in Profits: " + str(max_pld[0]) + " ($" + str(int(max_pld[1])) + ") \n")
    fao.write("Greatest Decrease in Profits: " + str(min_pld[0]) + " ($" + str(int(min_pld[1])) + ") \n")