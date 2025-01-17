import random

words = open('dictionary.txt').readlines()
word = random.choice(words)

print("WORDLE:")
print("Welcome to WORDLE. You have 6 tries to guess the 5 letter word.")

guessed = False

for i in range(6):
	guess = input(f"Guess {i+1} : ")

	for j in range(5):
		if guess[j].lower() == word[j].lower():
			print(guess[j].upper(), end="")
		else:
			for k in range(5):
				if guess[j].lower() == word[k].lower():
					print(guess[j].lower(), end="")
					break
			else:
				print("#",end="")
	print("\n\n")

	for i in range(5):
	if word[i].lower() == guess[i].lower:
		guessed = True
	else:
		guessed = False
		break

if guessed:
	print(f"WORDLE!! The word was {word}!")
else:
	print(f"Failed. The word was {word}.")