import random

computer_choice= random.choice(["rock", "paper", "scissors"])

user_choice= input("Rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("DRAW")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("WIN")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("WIN")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("WIN")
else:
    print("Computers WIN :)")