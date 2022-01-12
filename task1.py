#GUESSING THE 2 DIGIT NUMBER (TASK1)
import random
import math
#give your desired inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# to generating random number from your given bounds
x = random.randint(lower, upper)
print("\n\tYou have only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer,Akshitha\n")

# Initializing the number of guesses.
count = 0

# to calculate the minimum number of guesses based on the range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess the number:- "))

	# testing the conditions
	if x == guess:
		print("Congratulations Akshitha you guessed the number in ",
			count, "attempts")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed is too small!")
	elif x < guess:
		print("You Guessed is too high!")

# If Guessing is more than required guesses, show this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!,Akshitha")
exit(0)