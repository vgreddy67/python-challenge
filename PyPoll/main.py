import csv
import os

#storing the file path
election_csv = "election_data.csv"

#creating an output text file
output = open("election_output.txt",'w')

totalVotes = 0
votesPerCandidate = 0
candidatePresent = False

#List for total candidates
candidates = []

#Dictionary to store the candidates and their votes
candidateDictionary = {}
percentVotes = 0

#print("len(candidates):" + str(len(candidates)))
#opening the election_data.csv
with open(election_csv,newline ="") as poll:
    pollreader = csv.reader(poll,delimiter=",")

    #Read the header first
    poll_header = next(poll)

    #Reading through the csv file
    for row in pollreader:
        totalVotes = totalVotes + 1

        #Listing the candidates who received votes
        if len(candidates) > 0:
            for num in candidates:
                if num == row[2]:
                   candidatePresent = True
            if candidatePresent == False:
                candidates.append(row[2])
            else:
               candidatePresent = False
        else:
            candidates.append(row[2])

    #Calculating the total votes for each candidate
    for name in candidates:
        #Takes us to the begining of the file
        poll.seek(0,os.SEEK_SET) 

        #Read the header first
        poll_header = next(poll)

        for val in pollreader:
            if name == val[2]:
                votesPerCandidate = votesPerCandidate + 1
        
        #calculating percentage votes per candidate
        percentVotes = round((votesPerCandidate * 100)/totalVotes)
        #candidateDictionary[name] = votesPerCandidate
        #percentageVotes[name] = percentVotes
        candidateDictionary[name] = [percentVotes,votesPerCandidate]

        votesPerCandidate = 0

    #print(candidateDictionary)
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-----------------------------")
    print(candidateDictionary[name][1])
    for name,lst in candidateDictionary.items():
        print(name + ": " +str(float(lst[0]))+"%  ("+str(lst[1])+")")
    

    #Writing to the output file
    output.write("Election Results \n")
    output.write("-----------------------------\n")
    output.write("Total Votes: " + str(totalVotes) + "\n")
    output.write("-----------------------------\n")