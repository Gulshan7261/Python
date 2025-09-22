# using third variable
'''x = int(input("enter the value:"))
y = int(input("enter the value:"))

temp = x
x = y
y = temp

print("the value",x)
print("the value",y)'''

# without using third variable
x = int(input("enter the value:"))
y = int(input("enter the value:"))

x , y = y, x
print("the value of x",x)
print("the value of x",y)
