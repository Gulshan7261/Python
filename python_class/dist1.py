student = {"name": "john", "age": 21, "city": "new york"}
print(f"Keys: {list(student.keys())}")
print(f"values: {list(student.values())}")
print(f"items: {list(student.items())}")

print("\n7. MERGING DICTIONARIES")
print("_" * 30)

additional_info = {"hobby":"reading", "country": "USA"}
student.update(additional_info)


print("\n8. COPING DICTIONARIES")
print("_" * 30)

student_copy = student.copy()
print(f"Original: {student}")
print(f"Copy: {student_copy}")


city = student.setdefault("city", "Boston")
print(f"setdefult('city','Boston'): {city}")

temp_dict = {"a": 1, "b": 2}
print(f"Before clear: {temp_dict}")
temp_dict.clear()
print(f"After clear : {temp_dict}")

print("\n10. COPING DICTIONARIES")
print("_" * 30)

print()