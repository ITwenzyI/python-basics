from random import randint
zahl = randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == zahl:
        print("You guessed right!")
        break
    elif guess < zahl:
        print("Too low!")
    elif guess > zahl:
        print("Too high!")
    else:
        print("You guessed wrong.")