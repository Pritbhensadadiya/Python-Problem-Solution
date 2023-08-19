print ("----------------------------")
print ("  :: SNAKE WATER GUN ::     ")
print ("----------------------------")
import random

def check(comp, player):
    if comp == player:
        return 0
    if (comp == 1 and player == 2) or (comp == 2 and player == 3) or (comp == 3 and player == 1):
        return -1
    return 1

while True:
    comp = random.randint(1, 3)
    player = int(input("Enter 1 for SNAKE, 2 for WATER, 3 for GUN:> "))

    score = check(comp, player)
    print("You:", player)
    print("Computer:", comp)
    
    if score == 0:
        print("It's a draw")
    elif score == 1:
        print("You won")
    else:
        print("You lose")
    
    again = input("Do you want to play again? (y/n): ")

    if again.lower() != "y":

        break 
   