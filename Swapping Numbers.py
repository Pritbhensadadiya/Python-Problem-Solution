x=int(input("Enter value of x:"))
Y=int(input("enter value of Y:"))
temp=x
x=Y
Y=temp
print("Swapping x :",(x))
print("swapping Y :",(Y))


x=5
Y=10
x,Y=Y,x
print("x= ", x)
print("Y =", Y)