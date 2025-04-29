import random

# variables consisting of score & rolls value
score = 0
rolls = []

# welcome message
print("Welcome!")
print("Instructions: Roll the dice until your total score reaches 50.\n")

# scoring systems
while score < 50:
    input("To roll the dice, enter a value from 1-6")
    die = random.randint(1,6)
    score += die
    rolls.append(die)

    print(f"You rolled a {die}")
    print(f"Current total score: {score}.\n")

# congratulation message, result of total score, roll result
print("Congratulations! You have finished the game.")
print(f"Your total score: {score}")
print(f"Your dice rolls: {rolls}")