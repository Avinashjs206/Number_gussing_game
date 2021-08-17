import random
import math

# Taking Lower inputs
lower = int(input("Enter a Lower number:- "))

# Taking Upper Inputs
upper = int(input("Enter a upper number:- "))

# generating random number between the lower and the upper
x = random.randint(lower, upper)
print("\n\tyou have only", round(math.log(upper - lower +1, 2)), "chances the guess the integer!")

# Inirilizing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower +1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Entere your guess:- "))

    # Condition testing
    if x == guess:
        print("Congratulation you did in", count, "try!" )

        # Once guessed, loop will break
        break
    elif guess > x:
        print("Your guess is to high!")
    elif guess < x:
        print("Your guess is to low!")
        
# If Guessing is more than required guess,
# Show this output
if count >= math.log(upper - lower +1, 2):
    print("\nThe number is %d" %x)
    print("\tBetter Luck next time!")
