# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
previous_profit = None
net_change_list = []
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Define functions
def process_row(row):
    global total_months, net_total, previous_profit, net_change_list, greatest_increase, greatest_decrease

    # Update total months and net total
    total_months += 1
    net_total += int(row[1])

    if previous_profit is not None:
        # Calculate the net change
        net_change = int(row[1]) - previous_profit
        net_change_list.append(net_change)

        # Update greatest increase and decrease
        if net_change > greatest_increase[1]:
            greatest_increase = (row[0], net_change)
        if net_change < greatest_decrease[1]:
            greatest_decrease = (row[0], net_change)

    # Update previous profit
    previous_profit = int(row[1])

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    next(reader)

    # Process each row of data
    for row in reader:
        process_row(row)

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

