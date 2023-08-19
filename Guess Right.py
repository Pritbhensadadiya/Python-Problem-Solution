print ("------------------------")
print ("    GUESS THE NUMBER    ")
print ("------------------------")

import random

computer = random.randint(1, 11)

for _ in range(5):      
    user = int(input("Enter number from 1 to 10:-- "))

    if computer > user:
        print("low guess")
    elif user > computer:
        print("High")
    else:
        print("Equal") 
        print("CONGRATS YOU WON!!")
        break
else:
    print("Out of guesses")