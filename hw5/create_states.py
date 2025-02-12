import os

# List of 50 U.S. states + 5 territories
state_codes = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "AS", "GU", "MP", "PR", "VI"  # 5 U.S. territories
]

# Define file path
file_path = os.path.join(os.path.dirname(__file__), "states_territories.txt")

# Write state codes to file
try:
    with open(file_path, "w") as file:
        file.write("\n".join(state_codes) + "\n")
    print("File created: " + file_path)
except IOError as e:
    print("Error creating file:", e)
