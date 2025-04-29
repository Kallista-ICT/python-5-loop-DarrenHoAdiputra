# Rolls history (I was realised that this was needed for the code to know the history of the no. of rolls)
rolls = [4, 2, 6, 3, 5]

# Asks if the player wants to see the history of rolls
show_history = input("Do you want to see the history of your rolls? (Yes/No): ").strip().lower()

# Display the history if player asks for it
if show_history == 'yes':
    print("History of your rolls:")
    roll_number = 1
    for roll in rolls:
        print(f"Roll {roll_number}: {roll}")
        roll_number += 1
else:
    print("Thank you for playing!")
