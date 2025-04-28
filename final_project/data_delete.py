import os

# Path to the data directory inside your final_project folder
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "data")

deleted_files = 0

# Loop through and remove all .txt files
for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(data_dir, filename)
        try:
            os.remove(file_path)
            deleted_files += 1
            print("Deleted:", filename)
        except Exception as e:
            print("Failed to delete", filename, ":", e)

print("Done. Deleted", deleted_files, "files.")
