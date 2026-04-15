def outer():
    y = 30 #enclosed variable

    def inner():
        # nonlocal y
        y = 5
        print("Inside inner, y =", y)

    inner()
    print("Inside outer after inner call, y=", y)

outer()

# parameter local variable 