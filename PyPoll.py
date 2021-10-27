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
# Open the election results and read the file
with open (file_to_load,"r") as election_data:
# Close the file - not necessary if using with statement
#election_data.close()
#To do: perform analysis


#Read the file with the reader function.
    file_reader = csv.reader(election_data)
#Print each row in the CVS file
    #for row in file_reader:
      #Print the header row 
#Read and print the header row    
    headers = next(file_reader)        
    print(headers)
    
 #   print(election_data)
