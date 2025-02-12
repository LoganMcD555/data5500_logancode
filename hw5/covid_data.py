import requests
import json
import os
import time

# Define base API URL
BASE_URL = "https://api.covidtracking.com/v1/states/{}/daily.json"

# Get the current script directory
script_dir = os.path.dirname(__file__)

# Path to the states/territories file (created by create_states.py)
states_file_path = os.path.join(script_dir, "states_territories.txt")

# Ensure states_territories.txt exists
if not os.path.exists(states_file_path):
    print("Error: Missing states_territories.txt. Run create_states.py first.")
    exit(1)

# Read state codes
try:
    with open(states_file_path, "r") as file:
        state_codes = [line.strip() for line in file]
except IOError as e:
    print("Error reading states file:", e)
    exit(1)

# Fetch COVID data for each state and save as JSON
for state_code in state_codes:
    api_url = BASE_URL.format(state_code.lower())  # Ensure lowercase state codes
    print("Fetching data for: " + state_code + " from " + api_url)

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an error for failed requests
        data = response.json()

        # Save JSON response
        json_file_path = os.path.join(script_dir, state_code + ".json")
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Data saved for: " + state_code)

        # Avoid API rate limits
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print("Error fetching data for: " + state_code + " - " + str(e))
        continue  # Move to the next state even if one fails

