#open file
#file_1 = open("myfile.txt")
#read file (by default read the whole file)
# file_content = file_1.read()
#file_content = file_1.readline()#read a single line
#file_content = file_1.readlines()#read all lines
#print(file_content,type(file_content))

#close file
#file_1.close()

#with statement
# with open("myfile2.txt","a") as file_2:
#     #write file
#     writeList = ["Hello World \n" ,"This is our python class and we are learning python baalla"]
#     file_2.writelines(writeList)
   
# #append file
# with open("myfile2.txt","a") as file_2:
#     #write file
#     writeList = ["\nTharushi"]
#     file_2.writelines(writeList)
 
# #read file
# with open("myfile2.txt","r") as file_2:
#     file_content = file_2.readlines()
#     print(file_content,type(file_content))   

# with open ("myfile3.txt","w") as file_3:
#     writeList = ["My name is Tharushi and i am 25 years old"]
#     file_3.writelines(writeList)

#implmet  a simple contact manager
#create a programe that stores and manage contact in a file name contacts.txt each contacat entry should name ,phone number and email
#features of the program
#append a concat to the file
#add a  new contact
#view all contacts(read and display all concat in the file)
#exit program

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    with open("contacts.txt","a") as file_1:
        writeList = [name + "," + phone + "," + email + ","]
        file_1.writelines(writeList)
    print("Contact added successfully.")

def view_contacts():
    with open("contacts.txt","r") as file_1:
        contacts = file_1.readlines()
        for contact in contacts:
            print(contact)
       
while True:
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        break
    
    
      
    
    
        



    
