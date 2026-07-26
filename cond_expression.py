# conditional expression = A one line shortcut for if else statement (ternarny operator)
        # print or assign one of two values based on a condition
        # X if condition else Y

num = -5
a=6
b=7
age = 25
#print("positive" if num>0 else "negative")

#result = "Even" if num % 2 == 0 else "odd"
max_num = a if a > b else b
min_num = a if a < b else b

status = "adult" if age>= 18 else "Child"
#print(max_num)
#print(min_num)
print(status)