'''name = input("Enter your name:")
print(type(name))

age = int(input("Enter your age:"))
print(type(age))

weight= float(input("Enter your weight:"))
print(type(weight))'''


'''a= map(int, input("name,age,weight:").split())
print(type(a))'''

'''weight = float(input("Enter the value"))
Hight = float(input("Enter the value"))
a = weight/(Hight*Hight)
print(a)'''

'''name = "Gulshan"
print("Hello" + name)'''

'''print("2025","07","30",sep="-")
print("Hello",end="soni")'''

'''name = "gulshan"
age = 18
print(f"My name is {name} and i am {age} years old.")'''

'''x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x == y,type(x == y))
print(x is y)
print(z is y)
print(x is z)
print(x is y)'''

def calculate_bmi():
    try:
        height_cm = float(input("Enter your height in cm: "))
        weight_kg = float(input("Enter your weight in kg: "))

        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight_kg / (height_m ** 2)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError:
        print("Please enter valid numbers for height and weight.")

# Run the function
calculate_bmi()




