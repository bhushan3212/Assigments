A = int(input("Enter year"))

if A % 400 == 0 or A % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")