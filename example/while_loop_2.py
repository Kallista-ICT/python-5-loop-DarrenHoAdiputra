import random

# variables consisting of score & rolls value
score = 0
rolls = []

# welcome message
print("Welcome!")
print("Instructions: ")

# scoring systems
while score < 50:
    input("To roll the dice, enter values from 1-6")
    die = random.randint(1,6)
    score +- die
    rolls.append(die)

    print(f"")
    print(f)

# congratulation message, result of totoal score, roll result
