from random import randint

n=int(input("Enter no of trial : "))
for i in range(1,n+1,1):
    guessNumber = int(input("Enter your guessing number between 1 to 5 : "))
    randomNumber = randint(1, 5)
    if guessNumber==randomNumber:
        print("Wow,You have won")
    else:
        print("Sad! You have lossed")
        print("random number was ",randomNumber)