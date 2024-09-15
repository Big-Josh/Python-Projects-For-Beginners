import random


random_number = random.randint(1,100)
while True:
    try:
        user_input = int(input("Enter a number between 1 and 100: "))
        if user_input not in range(1,101):
            print("Enter a valid number")
        elif user_input < random_number:
            print("Too low")
        elif user_input > random_number:
            print("Too high")
        else:
            print("Congratulations you guessed right")
            break
    except:
        print("Enter a valid number")