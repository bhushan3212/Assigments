import cmath

A = float(input("Enter a :"))
B = float(input("Enter b :"))
C = float(input("Enter c :"))

D = B**2 - 4*A*C

root1 = (-B + cmath.sqrt(D)) / (2*A)
root2 = (-B - cmath.sqrt(D)) / (2*A)

print("Root 1 = ",root1)
print("Root 2 = ",root2)