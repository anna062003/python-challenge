import os
import csv

#Path to collect data from the Resources folder
electionData = r"C:\Github Repo\python-challenge\PyPoll\Resources\election_data.csv"

#Define the function and have it accept the "Election Data" as its sole paramenter
def pyPoll(election):
    
#the total number of votes cast
#Set the varaibale to totalVotesCast
#Count total row

    totalVotesCast = len(election)

#A complete list of candidates who received votes
#Make candidates to a dictionary
#loop through all the row in csvfile and locate candidate on column 3
#Add candidate and vote into the dictionary, if same candidate add up the vote
#if different candidate pop up then add the name into the dictionary
    candidates = {}
    for i in election:
        candidate = i[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    print("Electronin Results")
    print("------------------------------")
    print(f"Total Votes: {totalVotesCast}")
    print("------------------------------")
    

#The total number of votes each candidate won
#The precentage of votes each candidate won
#Use .item to display both key and value in the list of candidates
#Use formula to calculate percetage of Vote for each candidate
    for candidate, votes in candidates.items():
        percentageOfVotes = (votes / totalVotesCast) * 100
        percentageOfVotes = round(percentageOfVotes,3)

        print(f"{candidate}: {percentageOfVotes}% ({votes})")
    


#The winner of the election based on popular vote
#In the candidates dictionary, use .get methond to return the votes value for all candidates
#and use max method to find the person who got the most votes, then return the name of the candidates.
    winner = max(candidates, key=candidates.get)

    print("------------------------------")
    print(f"Winner: {winner}")
             
election = []
with open(electionData, encoding = "UTF-8") as csvfiles:
    csvReader = csv.reader(csvfiles, delimiter=",")
    csvHeader = next(csvReader)

    for row in csvReader:
        election.append(row)

pyPoll(election)
