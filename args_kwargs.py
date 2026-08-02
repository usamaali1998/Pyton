# *args = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple  keyword arguments
#   *unpacking operator
# 1. positional , 2. default , 3. keyword, 4. arbitrary



def add (*args):
    total = 0
    for arg in args:
        total+=arg
    return  total

print(add(1,2,3,4))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Usama", "Ali ", "raj")


def print_address(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}: {val}")
print(print_address(street = "124", city ="new" , state = "cal", zip= "3444"))


def shipping_lable(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    #print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}{kwargs.get('state')}")

shipping_lable("Dr","Usama","ALi","III", street="123", apt = "100", city = "ISB" )