'''num = int(input("Enter the number"))
for i in range(2,num+1):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        print(i)'''


'''num  = int(input("Enter the number"))

factor = []
for i in range(1,num):
    if( num % i == 0):
        factor.append(i)
print(f"factor of {num} are: {factor}")

prime_factors = []
non_prime_factors = []
for i in factor:
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            non_prime_factors.append(i)
            break
    if is_prime:
        prime_factors.append(i)
print(f"Prime factors of {num} are: {prime_factors}")
print(f"Non-prime factors of {num} are: {non_prime_factors}")'''


"""num  = int(input("Enter the number"))
factor = []
for i in range(1,num):
    if( num % i == 0):
        factor.append(i)
print(factor)
list1 =[]
list2 =[]

for i in factor:
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if(i % j == 0):
            is_prime=False
            list2.append(i)
            break

    if is_prime:
        list1.append(i)
print(f"prime factors of {num} are: {list2})"""            


number = int(input("Enter the number:"))
factors = []
for i in range(1, number+1):
    if number % i  ==0:
        prime = True
        for j in range(2,i):
            if(i%j==0):
                prime= False
                break
        if(prime==True):
            continue
        factors.append(i)
print(f"the factors of {number} are: {factors}")

'''output:Enter the number:12
the factors of 12 are: [4, 6, 12]'''







