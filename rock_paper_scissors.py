import random
import emoji

game_dict = {
    'r' : "Rock",
    'p' : "Paper",
    's' : 'Scissors'
}

def get_choie():
    try :
        user_input = input("Rock,paper or scissors? (r/p/s) : ").lower()
        if user_input  in list(game_dict.keys()) :
            game_options = ["Rock", "Paper", "Scissors"]
            computer_choice = random.choice(game_options).lower()
            user_choice = game_dict[user_input].lower()
            print(f"You chose {user_choice}")
            print(f"Computer Chose {computer_choice}")
            return user_choice, computer_choice 
        else:
            print("Invalid input")
            return None, None
    except:
         print("Invalid input") 
    return None, None


def determine_winner(user_choice, computer_choice):
    if user_choice == None:
        print(' ')
    elif user_choice == computer_choice and user_choice :
        print("It's a draw game")
    elif (
        (user_choice == "rock" and computer_choice == "paper") or 
        (user_choice == "scissors"  and computer_choice == "rock") or 
        (user_choice == "paper"  and computer_choice == "scissors")):
        print("Computer Won")
    else :
        print("You won")
            
def play_game():
    while True:
        user_choice, computer_choice = get_choie()
        determine_winner(user_choice, computer_choice)   
        continue_option = input("Continue? (y/n) : ").lower()
        if continue_option == "n":
            print("Thanks for playing")
            break
   

play_game()