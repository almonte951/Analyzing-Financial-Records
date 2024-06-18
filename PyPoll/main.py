import csv

# Define the path to the CSV file and initialize variables
votes_data = "Resources/election_data.csv"
total_votes = 0
candidate_votes = {}

# open the CSV file
with open(votes_data, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(reader)

    # run through each row in the CSV 
    for row in reader:
        total_votes += 1 
        candidate = row[2] 

        # if the candidate is already in the dictionary, add vote
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        # if the candidate is not in the dictionary, add them with one vote
        else:
            candidate_votes[candidate] = 1

# print the total number of votes
print("Election Results")
print("_________________________________")
print(f"Total Votes: {total_votes}")
print("_________________________________")

# print each candidate's vote count and percentage
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
print("_________________________________")

# the winner based on the highest vote
winner = max(candidate_votes, key=candidate_votes.get)
print("Winner:", winner)
print("_________________________________")

# export the results to a txt file
with open("analysis/vote_analysis.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("_________________________________\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("_________________________________\n")
    for candidate, votes in candidate_votes.items():
        percentage = round((votes / total_votes) * 100, 3)
        output_file.write(f"{candidate}: {percentage}% ({votes})\n")
    output_file.write("_________________________________\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("_________________________________\n")

# confirm that the results were exported
print("Vote analysis result exported to text file successfully")
