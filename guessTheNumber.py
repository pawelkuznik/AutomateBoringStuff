# This is guess the number game.
import random
firstNbRange = 1
lastNbRange = 20
secretNumber = random.randint(firstNbRange, lastNbRange)
print('I am thinking of a number beetween', firstNbRange, 'and ', lastNbRange, '.')


# Ask player to guess 6 times.
maxAttempt = 7;
for guessTaken in range(1, maxAttempt):
    print('take a guess.')
    guess = int(input())


    if guess < secretNumber:
        print("Your guess is to low.")
    elif guess > secretNumber:
        print("Your guess is to high")
    else:
        break       #This condition is the correct guess!


if guess == secretNumber:
    print('Good joob! You guessed my numebr in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
