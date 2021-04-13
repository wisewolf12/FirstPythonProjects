import random


your_range = int(input("Choose a range between 10,20,30,40 or 50: "))
the_number = random.randint(1,your_range)
guess = int(input("Guess a number between 1 and the range you asked "))
print("enter 2 to quit")
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high.Try again.")
    if guess < the_number:
        print(guess, "was too low.Try again.")
    guess = int(input("Guess again:"))
    if guess == 2:
        quit(2)

print(guess, "was the number! You win!")


