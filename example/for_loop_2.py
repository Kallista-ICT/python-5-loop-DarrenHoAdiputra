#
if show_history == 'yes':
    print("History of your rolls:")
    roll_number = 1
    for roll in rolls:
        print(f"Roll {roll_number}: {roll}")
        roll_number += 1