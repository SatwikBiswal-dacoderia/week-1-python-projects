import random
n=random.randint(1,100)
c=int(input("Enter a number between 1-100 : "))
if c==n:
    print("You won !!!")
else:
    print("You guessed wrong the number was ",n)