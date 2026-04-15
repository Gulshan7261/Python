Student = {"name": "john", "age":20, "grade": "A"}
print(f"Student distionary:{Student}")

# Accessing Value
print("\n2. ACCESSING VALUES")
print("_" * 30)

# using square brakets
print(f"Name:{Student['name']}")

# Using get() method (safer)
print(f"Age {Student.get('age')}")
print(f"city: {Student.get('city', 'Not specified')}")

# Adding and updating 
print(f"\n3. ADDING AND UPDATING")
print("_" * 30)

# Adding new key-value pair
Student["city"] = "New York"
print(f"After adding city :{Student}")

# Updating existing key 
Student["age"] = 21
print(f"After updating age: {Student}")

# Checking keys
print("\n4. CHECKING KEYS")
print("_" * 30)

print(f"'name' in student : {'name' in Student}")
print(f"")


# Using del 
del Student["grade"]
print(f"After deleting 'grade': {Student}")

# Using pop() - remove and return value 
age = Student.pop("age")
print(f"popped age:{age}")
print(f"After popping 'age': {Student}")

# Using pop() with defult value 
country = Student.pop("country", "De")

