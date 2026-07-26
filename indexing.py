#indexing = accessing elements of a sequence using [] (indexing operator)
#   [start : end : step]

credit_number = "123-424-234-2342"
#print(credit_number[0:5])
#print(credit_number[:5])
#print(credit_number[3:5])
#print(credit_number[3:])
#print(credit_number[-2])
#this will print every second character if we use step
#print(credit_number[::2])
#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

# -1 will start backwards with 1 step
credit_number = credit_number[::-1]
print(credit_number)