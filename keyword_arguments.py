#keyword arguments = an argument proceded by an identifier
# helps with redability
# order of arguemnts doesnot matter
# 1. positional , 2. default , 3. keyword, 4. arbitrary


#def hello(greeting,title,first,last):
#    print(f"{greeting} {title} {first} {last}")
#hello("hello","Mr","Usama","Ali")
#positional arguments always first before keyword argument
#hello("hello","Mr",last = "Usama",first= "Ali")

#print("1","2","3","4","5",sep="-")

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1,area=123,first=456,last=222)
print(phone_num)