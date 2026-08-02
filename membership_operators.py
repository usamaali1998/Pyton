# Membership operator = used to test ehether a value or variable is found in a sequence
#   (strings, list, tuple, set, or dictionary)
#           1. in
#           2. not in

word = "Apple"

letter = input("Guess a letter in secret word")
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

if letter not in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")