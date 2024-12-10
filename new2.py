import csv

# Read a CSV file
# csv_file_path = "customers-100.csv"

# with open(csv_file_path,'r',newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(row,type(row))
#     print(csv_reader,type(csv_reader))

csv_file_path = "mycsv.csv"
data =[
    {
        "name":"Tharushi",
        "age":25,
        "city":"Kandy"
     
    },
     {
        "name":"Kusal",
        "age":20,
        "city":"Matara"
     
    }, {
        "name":"Ashi",
        "age":24,
        "city":"Galle"
     
    }
]
field_names = ["name","age","city"]
# Write a CSV file
with open ('mycsv.csv','w',newline='') as file:
    #create a csv writer object
 csv_writer = csv.DictWriter(file,fieldnames=field_names)
 #write the header (column names) to the file
 csv_writer.writeheader()
 for row in data:
     #write each row to the file
     csv_writer.writerow(row)

 


