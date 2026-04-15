
def dob(a):
    year = a%10000
    month = (a//10000) % 100
    day = a//1000000
    print(f"your death of brith: {day},{month},{year}")

name = input("Enter the name:")
b = int(input("Enter Date of Birth in format DDMMYYYY:"))
print(name)
dob(b)

'''list = [4,4,6,3]
for i in range(len(list)) :
    # b = [i**2]
    list[i] *= list[i] 
print(list)'''



'''list1 = [4,4,6,3]
i = 0
while i < 4:
     list1[i] *= list1[i] 
     i += 1
print(list1)'''


