import json
# Read a JSON file and convert it to a Python dictionary
# json_file_path = "example_1.json"
# with open(json_file_path, "r") as json_file:
#     data = json.load(json_file)
#     print(data, type(data))

# Write a Python dictionary to a JSON file
# data ={
#     "name":"Tharushi",
#     "age":25,
#     "city":"Colombo",
#     "hobbies":["cricket","reading","coding"]
# }

# json_file_path = "test.json"
# with open(json_file_path, "w") as json_file:
#     data = json.dumps(data, indent=4) #indent=4 is used to format the json file
#     print(data, type(data))

#you are given json file name  students .json which contains information about students and their grades 
#your task is to
#read the json file
#Display the name of all the students who score aboved 75
#save the update data back to the json file

data =[]

with open("student.json","r") as file:
    data = json.load(file)
    for student in data:
        if student["grade"] > 75:
            print(student["name"])

add_student = {
    "name": "Tharushi",
    "grade": 90
}

data.append(add_student)
with open("student.json","w") as file:
    new_data = json.dumps(data,indent=4)
    file.write(new_data)







