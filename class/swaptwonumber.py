# wap to swap two numbers widthout using a tempoary variables
# method 1
'''a = 5
b = 10
a = a + b 
b = a - b
a = a - b
print(a,b)'''

# method 2
'''a = 6
b = 11
(a, b) = (b, a)
print(a, b)'''

# wap to define a function with multiple return Value
'''def calcuate(a, b):
    addition = a + b
    subtration = a - b
    multiplication = a * b
    return addition,subtration, multiplication

add,sub,mul = calcuate(6, 2)
print(f"add:{add},\nsub:{sub}\n,mul:{mul}")'''

# wap to find factorial of number using Recursion
# recursion = when a function call itself is called recursion 
'''def fact (n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))'''

# write a python script to print the current data

