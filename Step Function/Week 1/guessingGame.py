import random # Import the random module

number = random.randrange(1, 11) # Gets random number between [1 and 10)
guesses = 0
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    guesses += 1
    if guess > number:
        print(guess, "- Too Big.")
    elif guess < number:
        print(guess, "- Too Small.")
    guess = int(input("Try again: "))
print('\n')
print("Well Done! It took you ", guesses,  "guesses!")
