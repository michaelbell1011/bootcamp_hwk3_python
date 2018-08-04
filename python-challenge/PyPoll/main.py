# poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate.

#  analyze the votes and calculate, and output to cmd line and txt file:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# Dependencies
import os
import csv
import operator

# Variables
vote_results = {}
total_votes = 0

# Read in csv
csvpath = os.path.join('election_data.csv')
with open(csvpath, 'r', newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # # print first 4 rows of data like pandas head() function
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    
# Caluculations
    # Read each row of data after the header 
    for row in csvreader:
        
        # count total votes
        total_votes += 1
        
        # tally votes for each candidate within a dictionary
        # for each row read Candidate Name as the key for the 'voting results' dictionary
        key = row[2]
        #If candidate name is in the votes dictionary then increment that candidate's vote count by 1 using the += assignment operator. 
        #If candidate name is not already in the votes dictionary then set the candidate's vote count to 1 as their first vote.
        if key in vote_results:
            vote_results[key] += 1
        else:
            vote_results[key] = 1

# function to calculate cadidate % of vote-- args: candidate vote count (from dictionary), and total_votes
def percent_vote(prop, tot):
    percent = (prop / tot) * 100
    return(str(round(percent,3)) + '%')
            # obsolete-- variables not needed because of for loop used below:
            # K_percent = percent_vote(vote_results['Khan'],total_votes)
            # L_percent = percent_vote(vote_results['Li'],total_votes)
            # C_percent = percent_vote(vote_results['Correy'],total_votes)
            # O_percent = percent_vote(vote_results["O'Tooley"],total_votes)


# OUTPUT TABLE TO CMD LINE
print('''
Election Results
=====================================''')

# # The total number of votes in the dataset
print(f'Total number of votes: {total_votes}')
print("=====================================")

# candidate results from  vote results dictionary
            # obsolete:
            # print(f'Khan earned {K_percent} of vote ({vote_results["Khan"]})')
            # print(f'Li earned {L_percent} of vote ({vote_results["Li"]})')
            # print(f'Correy earned {C_percent} of vote ({vote_results["Correy"]})')
            # print(f'''O'Tooley earned {O_percent} of vote ({vote_results["O'Tooley"]})''')
            # print("=====================================")
# using a loop insead of 1 off print statements:
for k, v in vote_results.items():
    print(f'{k} earned ' + percent_vote(v, total_votes) + ' of the vote with')
    print(str(v) + ' votes.')
print("=====================================")

# winning candidate statement
# thx google
print(max(vote_results.items(), key=operator.itemgetter(1))[0] + ' is the winner.')


# OUTPUT TABLE TO TXT FILE-- opens in current directory
file = open('Vote_Results.txt', 'w')
file.write('''
Election Results
=====================================''')
file.write('\n' + f'Total number of votes: {total_votes}')
file.write('\n' + "=====================================")
for k, v in vote_results.items():
    file.write('\n' + f'{k} earned ' + percent_vote(v, total_votes) + ' of the vote with ')
    file.write(str(v) + ' votes.')
file.write('\n' + "=====================================")
file.write('\n' + max(vote_results.items(), key=operator.itemgetter(1))[0] + ' is the winner.')
file.close()