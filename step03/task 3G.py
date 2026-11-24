# Secret word

SECRET = "python"
guess = input("Guess the word: ")

if guess == SECRET:
    print("Correct!")
else:
    print("Wrong guess.")