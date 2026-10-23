A = int(input("Enter first number : "))
B = int(input("Enter second number : "))
C = int(input("Enter third number : "))

if A > B and C:
    print(A,"is a greater number")
elif B > A and C:
    print(B,"is a greater number")
elif C > B and A:
    print(C,"is a greater number")
else:
    print("invalid number")