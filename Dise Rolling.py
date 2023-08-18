import random

again = True

while again:
    print(random.randint(1, 6))
    again = input("Want to roll the dice again? (y/n)")
    if again.lower() == "y":
        continue
    else:
        break
