'''import random

def chocolate_distribution():
    chocolates = 0
    count = 0
    while chocolates < 20:
        given = random.randint(1, 10)
        chocolates += given
        count += 1
        print(f"Uncle gave {given}, Total chocolates = {chocolates}")

    print("\nChild got at leaste 20 chocolates!")
    print("Uncle had to give chocolates", count,"times")

chocolate_distribution()'''

# child ro raha hai jab tak uasse 20se jayada chokolate ho jata hai to rona band kar deta hai
'''import random

def chocolate_distribution():
    chocolates = 0
    count = 0
    crying = True
    while crying!=False:
        given = random.randint(1, 10)
        chocolates += given
        count += 1
        print(f"Uncle gave {given}, Total chocolates = {chocolates}")
        if chocolates >= 20:
            crying=False

    print("\nChild got at leaste 20 chocolates!")
    print("Uncle had to give chocolates", count,"times")

chocolate_distribution()'''

# chocolate kha leta hai 
'''import random

def chocolate_distribution():
    chocolates = 0
    count = 0
    crying = True
    while crying!=False:
        given = random.randint(1, 10)
        chocolates += given
        count += 1
        consume=random.randint(0, 5)
        chocolates -=consume
        print(f"Uncle gave {given}, Total chocolates = {chocolates}")
        if chocolates >= 20:
            crying=False

    print("\nChild got at leaste 20 chocolates!")
    print("Uncle had to give chocolates", count,"times")

chocolate_distribution()'''

""" Q. 21 two friends me divied kare 
f1 => 1, 2, 3, 4, 1 
f2 => 4, 3, 2, 1 |"""
'''import random
def chocolate_distribution():
    chocolates = 0
    count = 0
    crying = True
    while crying!=False:
        given = random.randint(1, 10)
        chocolates += given
        count += 1
        consume=random.randint(0, 5)
        chocolates -=consume
        print(f"Uncle gave {given}, Total chocolates = {chocolates}")
        if chocolates >= 20:
            crying=False

    print("\nChild got at leaste 20 chocolates!")
    print("Uncle had to give chocolates", count,"times")

chocolate_distribution()'''

'''def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add,sub,mul

x,y,z = calculate(10, 5)
print("Addition",x)
print("Addition",y)
print("Addition",z)'''


# user se input leke 
'''def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    sqr = a ** b
    divi = a / b
    return add,sub,mul,sqr,divi

# x,y,z = calculate(10, 5)
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

add,sub,mul,sqr,divi = calculate(a,b)

print("Addition", add)'''


def calculate(a, b):
    add = a + b
    return add
x = calculate(10, 5)
print(x)



