import os
import csv

csvpath2=os.path.join("Resources","election_data.csv")

with open(csvpath2, 'r') as election_file:
    election_read=csv.reader(election_file, delimiter=',')
    
    election_header=next(election_read)
    
    voter=[]
    county=[]
    candidate=[]
    candidates=[]
    election_reader=[]
    count_candidate=[]
    vote_percent=[]
    total_votes = 0
    correct_count = 0
    c_c1=[]

    for row in election_read:
        voter.append(row[0])
        county.append(row[1]) 
        candidate.append(row[2])
    
    #The total number of votes cast    
    total_votes = len(voter)
    
    #A complete list of candidates who received votes
    candidate_sorted = sorted(candidate)
    for r1 in range(1,total_votes):
        if candidate_sorted[r1] != candidate_sorted[(r1-1)] and r1 < total_votes - 1:
            candidates.append(candidate_sorted[(r1-1)])
            count_candidate.append(r1)
        elif r1 == total_votes-1:
            candidates.append(candidate_sorted[(r1-1)])
            count_candidate.append(r1)

    candidates_len=len(candidates)
    
    #The percentage of votes each candidate won   
    #The total number of votes each candidate won
    for r2 in range(candidates_len):
        if r2 == 0:
            c_c1.append(count_candidate[0]) 
            vote_percent.append(100 * c_c1[r2] / total_votes)
        elif r2 < candidates_len:
            c_c1.append(count_candidate[r2] - count_candidate[(r2-1)])
            vote_percent.append(100 * c_c1[r2] / total_votes) 
    
    won_zip = list(zip(vote_percent, c_c1, candidates))
    won_zip.sort(reverse = True)



  #The winner of the election based on popular vote.
    popular_vote = max(c_c1) 
    for r3 in range(candidates_len):
        if c_c1[r3] == popular_vote:
            winner = candidates[r3]

    
    #Results={"candidates" : candidates, "percentage of votes" : vote_percent, "number of votes" : c_c1} }
    
    print("---------------------")
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    for r4 in range(candidates_len):
        print(f"{won_zip[r4][2]}: {format(won_zip[r4][0], '.3f')}% ({won_zip[r4][1]})")
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")
    print("---")

output_path = os.path.join("Election_Results.txt")
with open(output_path, 'w', newline = '') as ero:

    ero.write("--------------------- \n")
    ero.write("Election Results \n")
    ero.write("--------------------- \n")
    ero.write(f"Total Votes: {total_votes} \n")
    ero.write("--------------------- \n")
    for r4 in range(candidates_len):
        ero.write(f"{won_zip[r4][2]}: {format(won_zip[r4][0], '.3f')}% ({won_zip[r4][1]}) \n")
        
    ero.write("--------------------- \n")
    ero.write(f"Winner: {winner} \n")
    ero.write("--------------------- \n")
    ero.write("--- \n")   