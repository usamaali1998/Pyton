#function = A block of reusable code
    # place () after the function too invoke it

def usama(name,age):
    print(f"Hello happy birthday {name}")
    print(f"you are {age} years old")
usama("Haseeb",20)
usama("haasn",20)
usama("fati",20)
usama("Huri",20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due: {due_date}")
display_invoice("Usama", 2000, "20 march")

def sum(a,b):
    c = a+b
    return c
print(sum(2,3))

def add(x,y):
    z = x+y
    return z
def sub(x,y):
    z = x-y
    return z
def mul(x,y):
    z = x*y
    return z
def div(x,y):
    z = x/y
    return z
print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("usama", "ali")
print(full_name)
