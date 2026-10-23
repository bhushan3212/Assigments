A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
C = int(input("Enter third number : "))

if A > B and A > C:
    print(A,"is a greater number")
elif B > A and B > C:
    print(B,"is a greater number")
elif C > A and C > B:
    print(C,"is a greater number")
else:
    print("Two or more numbers are equal")