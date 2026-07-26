import math


radius = float(input("Enter the radius of a circle "))
circumference = 2 * math.pi * radius

radius2 = float(input("Enter the radius of a circle 1 "))
area = math.pi * pow(radius2,2)

#hyp of a triangle
a = pow(int(input("Enter teh vlaue of a")) ,2)
b = pow(int(input("Enter teh vlaue of b")),2)
c = math.sqrt(a+b)




print(f"The circumference of a circle is : {round(circumference)}")
print(f"The area of a circle is : {round(area,2)}")
print(round(c,2))


