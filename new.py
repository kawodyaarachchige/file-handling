import json

# Read a JSON file and convert it to a Python dictionary
json_file_path = "example_1.json"
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)
    print(data, type(data))
