#Typecasting is a process of converting a variable from one data type to another data type
#   str(), int(), float(), bool()

name =  ""
age = 25
gpa = 3.2
is_student = True

print(type(name))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = str(age)
age += "1"
print(age)

name = bool(name)
print(name)