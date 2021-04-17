import random
random_num = random.randint(0, 10)

def main():
	try:
		print("Guess the number from 0 to 10.\n")

		answer = (input("Enter a number: "))
		print("Your answer is " + answer)

		print("\nThe answer is " + str(random_num))

		int(answer)

		if str(random_num) in answer:
			print("\nCongratulations you won!")
		else:
			print("\nYou lost, try again later.")

	except ValueError:
		print("Invalid Input")

main()