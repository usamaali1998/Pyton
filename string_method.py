

phone_number = input("Enter your phone number")

#name = input("Enter the full name")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")

result = phone_number.replace("-","#")


#print(len(name))
# find is used to find the first occurence
# rfind is used to find the last or reverse occurence
#result = name.find("A")
#result1 = name.rfind("a")


print(result)
print(help(str))