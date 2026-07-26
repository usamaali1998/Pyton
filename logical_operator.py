
temp = -25
is_sunny = True

#is_raining = True
'''
if temp > 35 or temp < 0 or is_raining:
    print("The oudoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''
if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("is is cold outside")
elif 28>temp>0 and is_sunny:
    print("is is warm")
