import time

#using sleep function will sleep the program for some time
my_time = int(input("Enter the time in second"))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("times up")