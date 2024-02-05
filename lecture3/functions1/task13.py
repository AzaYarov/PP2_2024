import random

def guess(y):
    x = random.randint(1, 5)
    count = 1
    while y != x:
        print("Your guess is too low.\nTake a guess") 
        y = int(input())
        count += 1
    print("Good job, KBTU! You guessed my number in", count, "guesses!")

number = int(input())

guess(number)

