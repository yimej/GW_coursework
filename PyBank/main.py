import csv

again = "y"

while again == "y":
    print("----------------------------------------------------------")

    file = input("Enter file name: ")

    with open(str(file), newline="") as csvfile:
        budget_df = csv.reader(csvfile, delimiter=",")
        budget_list = list(csv.reader(csvfile, delimiter=","))
        
        numOfMonths = len(budget_list)
        revenue = 0
        revChange = 0
        totalRevChange = 0
        aveRevChange = 0
        lastChange = 0
        maxChange = 0
        minChange = 0
        maxDate = ""
        minDate = ""

        for i in range(1,(numOfMonths - 1)):
            revenue = revenue + int(budget_list[i][1])

            lastChange = revChange
            revChange = int(budget_list[i+1][1]) - int(budget_list[i][1])
            totalRevChange = totalRevChange + revChange
            aveRevChange = totalRevChange / numOfMonths

            if revChange > lastChange:
                maxChange = revChange
                maxDate = budget_list[i+1][0]

            if revChange < lastChange:
                minChange = revChange
                minDate = budget_list[i+1][0]

    print("----------------------------------------------------------")
    print("Financial Analysis: " + file)
    print("Total Months: " + str(numOfMonths))
    print("Total Revenue: " + str(revenue))
    print("Average Revenue Change: $" + str(aveRevChange))
    print("Greatest Increase in Revenue: " + str(maxDate) + " ($" + str(maxChange) + ")")
    print("Greatest Decrease in Revenue: " + str(minDate) + " ($" + str(minChange) + ")")
    print("----------------------------------------------------------")

    output = open("results.txt","a+")
    output.write("Financial Analysis: " + file)
    output.write("\nTotal Months: " + str(numOfMonths))
    output.write("\nTotal Revenue: " + str(revenue))
    output.write("\nAverage Revenue Change: $" + str(aveRevChange))
    output.write("\nGreatest Increase in Revenue: " + str(maxDate) + " ($" + str(maxChange) + ")")
    output.write("\nGreatest Decrease in Revenue: " + str(minDate) + " ($" + str(minChange) + ")")
    output.close()
    again = input("Analyze another file: (y)es or (n)o? ")