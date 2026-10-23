# single line comment program

A = float(input("Enter first number: ")) # take input as a 1st number from user.
B = float(input("Enter seconnd number: ")) # take input number as a 2nd number from user.
C = input("Enter operators: (+,-,*,/,//,%)") # take operator from user for operation on operand.

if C == '+':
    print(A + B)
elif C == '-':
    print(A - B)
elif C == '*':
    print(A * B)
elif C == '/':
    print(A / B)
elif C == '//':
    print(A // B)
elif C == '%':
    print(A % B)
elif C == '**':
    print(A ** B)
else:
    print("Invalid Operation")