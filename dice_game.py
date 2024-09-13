import random

while True:
    user_input = input("Roll the dice? (y/n): ")
    if user_input.lower() == "y":
        dice_number_1, dice_number_2 = random.randint(1,6) ,random.randint(1,6)
        print(f'({dice_number_1}, {dice_number_2})')
    elif user_input.lower() != "y" and user_input.lower() != "n": 
        print("Invalid Input, Try Again")
    else :
        print("Thanks for playing .....")
        break 