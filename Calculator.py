print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
print ("::: CALCULATOR :::")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print ("1 for addition")
print ("2 for sbtraction")
print ("3 for multiplication")
print ("4 for division")

choice = int(input("Choose from 1 to 4:"))

if choice == 1:
    print(num1 + num2 )
elif choice ==2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2) 
else:
    print ("INVALID INPUT !!!")
    

