'''import math
x = int(input("Enter the number:"))
print(f"sqare",math.sqrt(x))
'''
'''import math
x = int(input("Enter the number:"))
y = int(input("Enter the number:"))
print(f"sqare",math.pow(x,y))
'''

'''import math
a = float(input("Enter the number:"))
b = float(input("Enter the number:"))
c = float(input("Enter the number:"))

# calculate the disscriminat
D = b**2 - 4*a*c

print("Discrimimnat (D):", D)

# Check nature of roots
if D > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("Roots are real and distinct.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif D == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print("Roots are real and equal.")
    print("Root =", root)
else:
    # Complex roots
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(abs(D)) / (2 * a)
    print("Roots are complex and imaginary.")
    print("Root 1 =", complex(realPart, imaginaryPart))
    print("Root 2 =", complex(realPart, -imaginaryPart))'''


     
