#class variables = shared among all instances of a class
#       define outside the constructer
#       allow you to share data among all objects created from that class
from tkinter.font import names


class Student:

    class_year = 2024
    num_students = 0
    def __init__(self,name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Usama", 27)
student2 = Student("hassi", 22)
student3 = Student("hassi", 22)
student4 = Student("hassi", 22)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students ")
print(Student.num_students)

#print(student1.name)
#print(student1.age)
#print(student1.class_year)
#print(Student.class_year)