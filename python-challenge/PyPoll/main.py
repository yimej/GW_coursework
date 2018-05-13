import csv

again = "y"

while again == "y":
    print("----------------------------------------------------------")
    
    file = input("Enter file name: ")

    with open(str(file), newline="") as csvfile:
        poll_list = list(csv.reader(csvfile, delimiter=","))
        print("--------------------------")
        print("Election Results " + "(" + file + ")")
        print("--------------------------")

        totalVotes = int(len(poll_list)) - 1
        print("Total Votes: " + str(totalVotes))
        print("--------------------------")

        candidateList, votesList, percentList = [], [], []
        votes, maxVotes, percent, winner = 0, 0, 0, 0

        for i in range(1, totalVotes):
            if str(poll_list[i][2]) not in candidateList:
                candidateList.append(str(poll_list[i][2]))

        totalCandidates = int(len(candidateList))

        for j in range(totalCandidates):
            for i in range(1, totalVotes):
                if str(poll_list[i][2]) == str(candidateList[j]):
                    votes = votes + 1
            votesList.append(str(votes))

            if votes > maxVotes:
                maxVotes = votes
                winner = j

            percent = round(((votes / totalVotes) * 100),2)
            percentList.append(str(percent))

            print(str(candidateList[j]) + ": " + str(percentList[j]) + "% (" + str(votesList[j]) + ")")
            
            votes, percent = 0, 0
        
        print("--------------------------")
        print("Winner: " + candidateList[int(winner)])
    
    output = open("results.txt","w+")
    output.write("Election Results " + "(" + file + ")\n")
    output.write("--------------------------\n")
    output.write("Total Votes: " + str(totalVotes) + "\n")
    output.write("--------------------------\n")
    for j in range(totalCandidates):
        output.write(str(candidateList[j]) + ": " + str(percentList[j]) + "% (" + str(votesList[j]) + ")\n")
    output.write("--------------------------\n")
    output.write("Winner: " + candidateList[int(winner)])
    output.close()
    again = input("Analyze another election: (y)es or (n)o? ")