# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has askeed us to complete the election audit of a recent local congressional election by performing the following tasks:

1. Calculate the total number of votes cast.
2. Get a complete list of votes each candidate received.
3. Calculate the percentage of votes each candidate won.
4. Determine the winner of the election based on popular vote.
5. Determine the voter turnout for each county
6. The percentage of votes from each county out of the count
7. The county with the highest turnout

## Resources
- Data Source: election_result.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1


## Election- Audit Results

The analysis of the election show that:

- There were 369.711 votes cast in the election
- The candidates were 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
    
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the total vote, 85,213 votes
    - Diana DeGette received 73.8% of the total vote, 272.892 votes
    - Raymon Anthony Doane received 3.1% of the total vote, 11,606 votes
       
The winner of the election was:

Diana DeGette was the winner of the election. She received 73.8% of the vote and 272.892 votes.

# Election-Audit Summary

This script can be reused to analyse any other election that determines the winner by popular vote. 
In order for the script to work correctly the source code needs to be in the same order as the csv file in this 
analysis. 

 - As an example you could use the script to analyse a local election for city commision.
   The data in the current county column would have to be replaced with the city's residential districts.
   All print statements that refer to "county" need to be modified, for example:
   
   - f"-------------------------\nLargest County Turnout: {winning_county}\n-------------------------\n"
  
    would need to be changed to:
  
   - f"-------------------------\nLargest residential district Turnout: {winning_county}\n-------------------------\n"
  
   Even though the script will run without modification of the variable names it would be good to change the names of these as well to reflect the new purpose. 
   
-  Another example would be to modify the script slighlty to pull data source files that are in a different format, for example an excel file or url.
   This part of the script that imports and reads the file would need to be adjusted:
  
    # Add our dependencies.
    import csv
    import os

    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
  
-  The script could also be used to predict the outcome of elections by using forecast numbers in the data source file. 

-  If additional data gets added to the source file the script can be used to analyse them by reusing the existing code as a template. 
   
    


