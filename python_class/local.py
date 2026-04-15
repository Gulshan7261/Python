x=20
def local_example():
    #local variable
    global x
    x+=2
    print("Inside function, x=", x)

local_example()
print("Outside function, x=", x)