import json
import os
data_directory="/home/sierra/repository/assignment009/test_data"
combined_data = []
for filename in os.listdir(data_directory):
    if filename.endswith(".json"):
        with open(os.path.join(data_directory, filename), "r") as file:
            file_data = json.load(file)
            combined_data.extend(file_data)
sorted_data = sorted(combined_data, key=lambda x: x.get("name", ""))
with open("combined_data.json", "w") as combined_file:
    json.dump(combined_data, combined_file, indent=4)
with open("sorted_data.json", "w") as sorted_file:
    json.dump(sorted_data, sorted_file, indent=4)
