print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to the quiz game..")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

playing = input("DO YOU WANT TO PLAY? ")
if playing.lower() != "yes":
    quit()

print("Let's play the game")
score = 0
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("What is python in computer? ")
if answer.lower() == "language":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("Who created this program? ")
if answer.lower() == "prit":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("What is a phone? ")
if answer.lower() == "device":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("Who is the owner of the boat company? ")
if answer.lower() == "aman gupta":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("What is the full form of OS? ")
if answer.lower() == "operating system":
    print("Right Answer")
    score += 1
else:
    print("Wrong Answer")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("You got " + str(score) + " questions correct")