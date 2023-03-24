import os

#Append information to file
employees_file = open("file_operations\employees.txt", "a") 
print(employees_file.writable())

employees_file.write("\nKelly - Customer Service")
employees_file.close()

#Overwrite existing file or create a new file
employees_file = open("file_operations\index.html", "w") 

employees_file.write("<p>This is HTML</p>")
employees_file.close()