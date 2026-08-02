# list comprehension = A consise way to create lists in python
#       compact and easier to read than traditional loop
#           [expression for value in iterable if condition]


double = []
for x in range(1,11):
    double.append(x*2)
print(double)

doubles = [x*2 for x in range(1,11)]
triple = [x*2 for x in range(1,11)]
square = [z* z for z in range(1,11)]

#fruits = ["apple", "orange", "coconut"]
#fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit.upper() for fruit in ["apple", "orange", "coconut"]]

numbers = [1,2,-3,-6]
positive_num= [num for num in numbers if num >=0]
negative_num= [num for num in numbers if num <0]
print(negative_num)
