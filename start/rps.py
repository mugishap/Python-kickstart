
from random import randint, random

name = input("Enter your name here please: ")

computer_wins = 0
player_wins = 0

choices = ['rock', 'paper', 'scissors']

while True:
    choice = input("Enter Rock/Paper/Scissors or r/p/s or q to quit: ")
    if choice == "q":
        break
    elif choice == "r" or choice == "Rock":
        computer_choice = choices[randint(0, 2)]
        if computer_choice == "rock":
            print("Computer chose rock")
            print("Tie")
        elif computer_choice == "paper":
            print("Computer chose paper")
            print("Computer wins")
            computer_wins += 1
        else:
            print("Computer chose scissors")
            print(f"{name} wins")
            player_wins += 1

    elif choice == "p" or choice == "Paper":
        computer_choice = choices[randint(0, 2)]
        if computer_choice == "paper":
            print("Computer chose paper")
            print("Tie")
        elif computer_choice == "rock":
            print("Computer chose rock")
            print(f"{name} wins")
            player_wins += 1
        else:
            print("Computer chose scissors")
            print("Computer wins")
            computer_wins += 1

    elif choice == "s" or choice == "Scissors":
        computer_choice = choices[randint(0, 2)]
        if computer_choice == "scissors":
            print("Computer chose scissors")
            print("Tie")
        elif computer_choice == "rock":
            print("Computer chose rock")
            print("Computer wins")
            computer_wins += 1
        else:
            print("Computer chose paper")
            print(f"{name} wins")
            player_wins += 1

    else:
        print("Invalid choice")



print(f"{name} has {player_wins} wins")
print(f"Computer has {computer_wins} wins")
