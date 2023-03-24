import os

#Check current directory
print(os.getcwd())

employees_file = open("file_operations\employees.txt", "r") #r (read), w (write), a (append to file), r+ (all permissions)

print(employees_file.readable())
#read whole file
#print(employees_file.read())

#read line and move cursor to the next one, so when you call readline() next time, it will read the following line
#print(employees_file.readline())  

#Read line #2
#print(employees_file.readlines()[1])

for employee in employees_file.readlines():
    print("line:\t" + employee)

employees_file.close