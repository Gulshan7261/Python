# write a python script that print prime number less then 20

def prime ():
    for i in range(20):
        if i > 1:
            for j in range (2, i):
                if i % j == 0:
                    break
            else:
                print(i)

prime()

'''num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")
'''