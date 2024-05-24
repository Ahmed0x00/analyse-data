import json
from scrape_data import get_data, datascience, robotics, multimedia
from analyze_departments import analyze_departments
from analyze_subjects import analyze_marks, analyze_students

# Scrape the data and save the files for analysis
get_data(231051001, 231051369, "C", datascience, "datascience.json")
get_data(231052001, 231052233, "B", robotics, "robotics.json")
get_data(231053001, 231053108, "A", multimedia, "multimedia.json")

# Combine the departments file into one file (Faculty of CS) to analyze it
def combine_json_files(files, combined_file):
    combined_data = []

    # Read data from each JSON file and append to combined_data
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
            combined_data += data  # Append data from each file to combined_data

    # Write combined_data to a new JSON file
    with open(combined_file, "w") as f:
        json.dump(combined_data, f, indent=2)

# List of JSON files to combine
json_files = ["datascience.json", "robotics.json", "multimedia.json"]
combined_json_file = "Faculty of CS.json"

combine_json_files(json_files, combined_json_file)


# Analyze the departments
analyze_departments()

# Analyze the subjects
analyze_marks()

# Analyze the students
analyze_students()