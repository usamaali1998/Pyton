#for loop = execute a block of a code fixed number of times.
    #you can iterate over a range , string sequence etc
    # we can also add steps in addition to range

'''
for x in reversed(range(1,19, 2)):
    print(x)
print("hello world")
'''

'''
credit_card = "1234-2345-6789-5433"
for x in credit_card:
    print(x)
'''

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)