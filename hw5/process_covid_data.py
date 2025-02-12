import json
import os
from collections import defaultdict

# Get the current script directory
script_dir = os.path.dirname(__file__)

# Get all JSON files (state data)
json_files = [f for f in os.listdir(script_dir) if f.endswith(".json")]

# Function to process each state's data
def process_state_data(state_code):
    json_file_path = os.path.join(script_dir, state_code + ".json")

    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)

        if not data:
            print("No data found for " + state_code + ", skipping.")
            return

        # Extract relevant statistics
        positive_increases = []
        highest_cases = 0
        highest_date = "N/A"
        zero_case_date = "N/A"
        monthly_cases = defaultdict(int)

        for entry in data:
            date = str(entry.get("date", "N/A"))
            new_cases = entry.get("positiveIncrease", 0)

            # Collect daily new cases
            positive_increases.append(new_cases)

            # Track highest new cases date
            if new_cases > highest_cases:
                highest_cases = new_cases
                highest_date = date

            # Track the most recent date with zero new cases
            if new_cases == 0:
                zero_case_date = date

            # Aggregate cases by month-year
            if len(date) == 8:
                month_year = date[:4] + "-" + date[4:6]
                monthly_cases[month_year] += new_cases

        # Compute final stats
        if len(positive_increases) > 0:
            avg_daily_cases = round(sum(positive_increases) / len(positive_increases), 2)
        else:
            avg_daily_cases = 0

        highest_month_year = max(monthly_cases, key=monthly_cases.get, default="N/A")
        lowest_month_year = min(monthly_cases, key=monthly_cases.get, default="N/A")

        # Print the results
        print("\nCOVID-19 Statistics for " + state_code + ":")
        print("  - Average Daily Cases: " + str(avg_daily_cases))
        print("  - Highest Cases on: " + highest_date + " (" + str(highest_cases) + " cases)")
        print("  - Most Recent Zero New Cases on: " + zero_case_date)
        print("  - Month with Highest Total Cases: " + highest_month_year + " (" + str(monthly_cases.get(highest_month_year, 0)) + " cases)")
        print("  - Month with Lowest Total Cases: " + lowest_month_year + " (" + str(monthly_cases.get(lowest_month_year, 0)) + " cases)")

    except IOError as e:
        print("Error reading " + state_code + " JSON file: " + str(e))
    except json.JSONDecodeError:
        print("Error parsing JSON for " + state_code + ", skipping.")

# Process each state
for json_file in json_files:
    state_code = json_file.replace(".json", "").upper()
    process_state_data(state_code)
