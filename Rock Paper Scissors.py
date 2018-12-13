# Title: Rock, Paper, Scissors!
# Author: Zach Theilen
# This is a simple game where the user selects rock, paper, or scissors,
# the computer selects one, and the winner is announced

# import the random library
import random

play_again = "Yes"
choices = ["Rock" , "Paper" , "Scissors"]

# display title and instructions
title = """Welcome to Rock, Paper, Scissors!
You and the computer will both secretly select either Rock, Paper, or Scissors.
Then a winner will be chosen or a tie will be broken."""
print(title)

# start a while loop that gets player's and computer's random choices
while play_again == "Yes":
    print("Choose Rock, Paper, or Scissors:")
    player_choice = input("Enter your choice: ")
    computer_choice = choices[random.randint(0,2)]

    #display the choices and determine if tied or if a winner can be named
    print("Your choice is " + player_choice + ".")
    print("The computer's choice is " + computer_choice + ".")
    if player_choice == computer_choice:
        print("It's a tie")
    else:
        if ((player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Scissors" and computer_choice == "Paper") or
            (player_choice == "Paper" and computer_choice == "Rock")):
                print("!" * 80)
                print("You win!")
                print("!" * 80)
        else:
            print(":(" * 40)
            print("You lose!")
            print(":(" * 40)

    # play again?
    play_again = input("Do you want to play again [Yes/No]? ")
