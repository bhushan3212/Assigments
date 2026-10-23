a = int(input("Enter a number :"))

status = False

if a < 2 :
    status = False
else :
    status = True

for i in range(2,a):
    if a % i == 0:
        status = False
        break


if status :
    print(f'{a} is a prime number')
else:
    print(f'{a} is not a prime number')