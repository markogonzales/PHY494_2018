number = 42   # secret number
correct = False

while not correct:
    guess = int(input("Guess the number: "))
    if guess < 42:
        print("guess again, too low bone head")
    elif guess > 42:
        print("guess again, too high smoke less")
    else:
        print("correct!")
        correct = True
