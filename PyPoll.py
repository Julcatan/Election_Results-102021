# The data we need to retrieve
# count total number of votes cast
# Create complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote


# Import the datetime class from the datetime module.
#import datetime as dt
#from os import read
# Use the now attribute on the datetime class to get the present time. 
#now = dt.datetime.now()
#print the present time.
#print("The time right now is ",now)

# Import CSV file
# Assign a variable for the file to load and the path
#file_to_load = "Resources/election_results.csv"
# Open the election results and read the file
#election_data = open(file_to_load, read)
# Close the file
#election_data.close()
#Open the election results and  read the file
#with open(file_to_load) as election_data:
#To do: perform analysis
 #   print(election_data)


'''# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)'''

"""# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis",'election_analysis.txt')

#Using the with statement open the file as a text file.
open(file_to_save, "w")"""


"""# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open (file_to_save,"w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World\n")

    txt_file.write("Arapahoe,\n Denver,\n Jefferson")"""


# Import CSV file
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join ("Resources", "election_results.csv")
file_to_save = os.path.join ("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
#Candidate Options - declare list lisa of unique candidates?
candidate_options = []
#Candidate_Votes - declare dictionary
candidate_votes ={}
# Winning Candidate and Winning Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file
with open (file_to_load) as election_data:

#To do: perform analysis
#Read the file with the reader function.
    file_reader = csv.reader(election_data)
#Print each row in the CVS file
    
#Read and print the header row    
    headers = next(file_reader)        
#for row in file_reader:
    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2] 
    #If the candidate is not in the candidate list already
        if candidate_name not in candidate_options:
        # Add it to the list of candidates
            candidate_options.append (candidate_name) 
        # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    #4. Print the candidate name and percentage of votes
   
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning count and candidate
    #1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage> winning_percentage):
        #2. It true then set winning_count = votes and winning percentage = # voter percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
#print out the winnning candidate, vote count and percentage to terminal
winning_candidate_summary = (f"------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage: .1f}%\n"
f"------------------\n")

print(winning_candidate_summary)


#print total votes
#print(total_votes)
#print the canditate list
#print(candidate_votes)


