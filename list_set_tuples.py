# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicate OK
# set = {} unordered and immutable , but ADD/REmove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicated OK . Faster

fruits = ["Apple","orange","banana"]
#print(fruits[::-1])

'''
for fruit in fruits:
    print(fruit)
'''
print(dir(fruits))
print(len(fruits))

print("apple" in fruits)
print(fruits.count("banana"))