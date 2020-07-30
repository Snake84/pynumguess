import random
from datetime import datetime
number = random.randrange(1,20)
guess = int(input("Guess the number between 1 and 20: "))
attempts = 0
# highscore = open("highscore.txt", "w+")
# highscore.write("")

while guess != number:
    if guess < number:
        attempts +=1
        print("the random number is higher")
        guess = int(input("Guess the number between 1 and 20: "))

    elif guess> number:
        attempts +=1
        print("The random number is lower")
        guess = int(input(" Guess the number between 1 and 20: "))
print("congratulations, you guessed the number correctly, it took " + str(attempts) + " attempts")
# if attempts > highscore:
#     newscore = open(highscore.txt, "w")
#     newscore.write(attempts)

