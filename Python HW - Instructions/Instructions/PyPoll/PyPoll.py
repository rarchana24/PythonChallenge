import os
import csv

# Files to load and output
inputFile = "Resources/election_data.csv"

#Declare variables
totalvotes=0
khanvotes =0
correyvotes =0
livotes=0
tooleyvotes=0

with open(inputFile,newline="") as election_data:
    
    #file contents in a variable
    csvread = csv.reader(election_data,delimiter=",")
    header = next(csvread)
    #iteration 
    for row in csvread:
        #count the unique votes
        totalvotes+=1
        if row[2] == "Khan":
            khanvotes +=1
        elif row[2] == "Correy":
            correyvotes +=1
        elif row[2] == "Li":
            livotes +=1
        elif row[2] == "O'Tooley":
            tooleyvotes +=1

#Create a dictionary for the candidates and votes
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khanvotes, correyvotes,livotes,tooleyvotes]

dictionary = dict(zip(candidates,votes))
keyvalues = max(dictionary,key=dictionary.get)

#Get percentage 
khanpercent = (khanvotes/totalvotes) * 100
correypercent = (correyvotes/totalvotes) * 100
lipercent = (livotes/totalvotes) * 100
tooleypercent = (tooleyvotes/totalvotes) * 100


# Print the values
print(f"Election Data")
print(f"Total Votes: {totalvotes}")
print(f"Khan: {khanpercent:.2f}% ({khanvotes})")
print(f"Correy: {correypercent:.2f}% ({correyvotes})")
print(f"Li: {lipercent:.2f}% ({livotes})")
print(f"O'Tooley: {tooleypercent:.2f}% ({tooleyvotes})")
print(f"Winner: {keyvalues}")

outfile = ("Resources/Electiondata.txt")
with open(outfile,"w") as election_result:
    #printing the statements again
    election_result.write(f"Election Data")
    election_result.write("\n")
    election_result.write(f"Total Votes: {totalvotes}")
    election_result.write("\n")
    election_result.write(f"Khan: {khanpercent:.2f}% ({khanvotes})")
    election_result.write("\n")
    election_result.write(f"Correy: {correypercent:.2f}% ({correyvotes})")
    election_result.write("\n")
    election_result.write(f"Li: {lipercent:.2f}% ({livotes})")
    election_result.write("\n")
    election_result.write(f"O'Tooley: {tooleypercent:.2f}% ({tooleyvotes})")
    election_result.write("\n")
    election_result.write(f"Winner: {keyvalues}")    
    
