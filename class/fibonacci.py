'''num = int(input("enetr the number:"))
a=1
b=1
# sum=1
for i in range(1,num+1):
    sum=a+b
    a=b
    b=sum
    print(sum)'''



def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a


def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1]+fib_series[i-2])
        return fib_series[:n]
    
num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
n = int(input("Enter how many Fibonacci number you want:"))

# output
print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
print(f"fibonacci number are:{fibonacci(n)}")
