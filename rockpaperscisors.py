import random

def get_user_input():
    valid_user_choice = ['rock','paper','scissors']
    choice= input(" Enter your choice(rock/paper/scissors) or type 'quit' to exit ")
    while choice not in valid_user_choice +['quit']:
        print("Invalid choice! please enter rock,paper,scissors")
    return choice
def get_computer_choices():
    choices = ['rock','paper','scissors']
    return random.choice(choices)    

def play_game():
    print("Welcome to the rock-paper-scissors game")
    while True:
        user_choice = get_user_input()
        if user_choice == "quit":
            print("Thanks for playing ")
            break
        computer_choice = get_computer_choices()
        print(f"\n You chose {user_choice}. The computer choose {computer_choice}")


        if user_choice == computer_choice:
            print(" It's Tie")

        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer win!")
            else:
                print("You win!")

        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer win!")
            else:
                print("You win") 

        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("computer wins!")
            else:
                print("you win")                           
play_game()