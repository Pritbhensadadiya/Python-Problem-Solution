print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("         Rock-Paper-Scissors           ")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import random

options = ("rock", "paper", "scissors")

playing = True
while playing:
    player = None
    computer = random.choice(options)
    
    while player not in options: 
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"player: {player}")
    print(f"computer: {computer}")
    
    if player == computer:
        print("IT'S A TIE!!!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN!")
    else:
        print("YOU LOSE!!")
        
    if input("Play again? (y/n)").lower() != "y":
        playing = False
print("THANKS FOR PLAYING !!!")
