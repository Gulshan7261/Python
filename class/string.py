# Q18.Write to find the length of the string without using any libray function 

def find_length(str):
    count = 0
    for i in str:
        count = count + 1
    return count
string = input("Enter the string=")
length = find_length(string)
print(length) 

# Enter the string=hello
# 5

#Q19. WAP to check if two string are anagrams or not
'''def check_anagrams(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    return(sorted(str1)==sorted(str2))
str1 = input("Enter first string:")
str2 = input("Enter first string:")
if check_anagrams(str1,str2):
    print("string are anagrams")
else:
    print("notanagrams")'''
'''output
Enter first string: listen
Enter second string: silent
Strings are anagrams

Enter first string: hello
Enter second string: world
Not anagrams'''

#Q20. WAP to check if the substring is present in a given string or not (use regular expression)

'''str1 = "hello"
str2 = "he"
print(str1 in str2)'''

'''import re
string = input("Enetr string:")
substring = input("Enetr substring:")
if re.search(substring,string):
    print("substring present in string")
else:
    print("substring not present in string")'''

'''Enetr string:Python is powerful
Enetr substring:power'''


