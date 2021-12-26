import random

number = random.randint(1,9)

chances = 0


while chances<5:

    guess = int(input("Enter Guess:"))

    if(guess==number):
        print("YOU WIN CONGRATS")

    elif(guess<number):
        print("Your guess was to low, guess a number higher than", guess)

    else:
        print("Your Number Is To High Guess a number lower than", guess)

        chances += 1

if not chances < 5:
    print("You Lose the number was", number)
