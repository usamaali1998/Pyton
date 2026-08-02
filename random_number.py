import random

#low = 1
#high = 100
#options = ("rock","paper","scissors")
#card = ["2","3","4","J","K","A"]

#number = random.randint(low,high)
#number = random.random()
#options = random.choice(options)
#random.shuffle(card)
#print(options)

#number guesssing game

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python Number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int (guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low ! try again")
        elif guess > answer:
            print("Too high ! try again")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")