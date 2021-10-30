# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election by performing the following tasks:

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
    
-The candidate results were:
    - Charles Casper Stockham received 23.0% of the total vote, 85,213 votes
    - Diana DeGette received 73.8% of the total vote, 272.892 votes
    - Raymon Anthony Doane received 3.1% of the total vote, 11,606 votes
       
The winner of the election was:

Diana DeGette was the winner of the election. She received 73.8% of the vote and 272.892 votes.

# Election-Audit Summary

This script can be reused to analyse any other election that determines the winner by popular vote. 

 - In order for the script to work correctly the source code needs to be in the same order as the csv file in this 
   analysis. 

 - As an example you could use the script to analyse a local election for city commision.
   The data in the current county column would have to be replaced with the city residential districts.
 
- Another example would be to modify the script slighlty to pull data source files that are in a different format, for eexample a url or an excel file.
  This part of the script that imports and reads the file would need to be adjusted:
  
    # Add our dependencies.
    import csv
    import os

    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
  
  
  

    


