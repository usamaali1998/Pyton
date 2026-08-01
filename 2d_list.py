
'''

fruits =["apple", "orange" , "banana"]
vegetables =["celery", "carrots" , "potatoes"]
meats =["apple", "orange" , "banana"]

groceries = [fruits, vegetables, meats]
print(groceries[0][3])
'''

groceries = [["apple", "orange" , "banana"],["celery", "carrots" , "potatoes"],["apple", "orange" , "banana"]]
#groceries = [["apple", "orange" , "banana"],["celery", "carrots" , "potatoes"],["apple", "orange" , "banana"]]

for collection in groceries:
    for food in collection:
        print(food, end ="\n")
    print()


num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
