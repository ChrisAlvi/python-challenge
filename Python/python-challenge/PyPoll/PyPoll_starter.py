# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Define a function to process votes
def process_votes(file_path):
    global total_votes, candidate_votes

    with open(file_path) as election_data:
        reader = csv.reader(election_data)
        next(reader)  # Skip header

        # Process each row
        for row in reader:
            total_votes += 1
            candidate_name = row[2]

            # Update candidate vote counts
            candidate_votes[candidate_name] = candidate_votes.get(candidate_name, 0) + 1

# Function to calculate and generate results
def generate_results(vote_counts, total, output_path):
    # Prepare output
    lines = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total}",
        "-------------------------",
    ]

    # Track the winner
    winner = ""
    max_votes = 0

    # Calculate percentages and find the winner
    for candidate, votes in vote_counts.items():
        percentage = (votes / total) * 100
        lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
        if votes > max_votes:
            winner = candidate
            max_votes = votes

    # Append the winner
    lines.extend([
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------",
    ])

    # Print results
    for line in lines:
        print(line)

    # Write to file
    with open(output_path, "w") as txt_file:
        txt_file.write("\n".join(lines))

# Process the data
process_votes(file_to_load)

# Generate and save the results
generate_results(candidate_votes, total_votes, file_to_output)

