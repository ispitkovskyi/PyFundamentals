# "from" refers to a file name, and "import" refers to a class name
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
print(student1.name, student1.gpa, student1.is_on_probation)

student2 = Student("Pam", "Art", 2.5, True)
print(student2.name, student2.gpa, student2.is_on_probation)