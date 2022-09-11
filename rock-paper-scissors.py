
import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors) ")
    

    possible_actions =["rock","paper","scissors"]

    machine_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, machine chose {machine_action}.\n")

    if user_action == machine_action:
        print(f"Both players selected {user_action}.It's a tie!")

    elif user_action == "rock":
        if machine_action == "scissors":
            print("Rock smashes scissors! You win!!")
        else:
            print("Paper covers rock! You lose!!")

    elif user_action == "paper":
        if machine_action == "rock":
            print("Paper covers rock.You win!!")

        else:
            print("Scissors cut paper!You lose!!")

    elif user_action == "scissors":
        if machine_action == "paper":
            print("Scissors cut paper!You win!!")
        else:
            print("Rock smashes scissors! You lose!!")

    play_again = input("Wanna play again? (Enter 'q' to quit,enter go to continue): ")
    if play_again.lower()=='q':

        break
    elif play_again.lower() != 'go':
        break