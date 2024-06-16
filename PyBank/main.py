import os
import csv

# Define the path to the CSV file
budget_data = "Resources/budget_data.csv"

# Initialize variables
row_count = 0
total = 0
previous_profit = 0
profit_changes = []
greatest_increase = {"amount": 0, "date": ""}
greatest_decrease = {"amount": 0, "date": ""}

try:
    # Open the CSV file
    with open(budget_data, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        # Skip header row
        next(reader)

        # Process each row
        for row in reader:
            row_count += 1
            current_profit = int(row[1])
            total += current_profit

            if row_count > 1:
                yearly_change = current_profit - previous_profit
                profit_changes.append(yearly_change)

                # Find greatest increase
                if yearly_change > greatest_increase["amount"]:
                    greatest_increase["amount"] = yearly_change
                    greatest_increase["date"] = row[0]

                # Find greatest decrease
                if yearly_change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = yearly_change
                    greatest_decrease["date"] = row[0]

            # Update previous profit
            previous_profit = current_profit

    # Calculate average change
    avg_change = sum(profit_changes) / len(profit_changes) if profit_changes else 0

    # Print the analysis results
    print("Financial Analysis")
    print("_________________________________")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    # Export analysis to text file
    with open("analysis/financial_analysis.txt", "w") as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("_________________________________\n")
        output_file.write(f"Total Months: {row_count}\n")
        output_file.write(f"Total: ${total}\n")
        output_file.write(f"Average Change: ${avg_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
        output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    # Print confirmation message
    print("Analysis results exported to financial_analysis.txt")

except FileNotFoundError:
    print(f"Error: The file {budget_data} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

