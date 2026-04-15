# set {1,2,3,4,5,6,7,8,9} -> {} collection of unique data 

#Q27 write a program to count the number of vowels in a string (No control flow allowed).

'''a = "apple"
x = len(set(x for x in a if x in "aeiouAEIOU"))
print(x)

b = "mango"
y = {ch for ch in b if ch in "aeiouAEIOU"}
print(len(y))
# print(y)'''

#Q28 write a program that displays which letters are present in both string 
a = "Gulshan"
b = "Govind"
x = set(a)
y = set(b)
z = z = x & y 
c = z = x.intersection(y)
print(c)
print(z)

# lambda 
'''add = lambda x,y:x+y
x = add(3, 4)
print(x)'''

#Q29 WAp to sort given list of string in the order of their vowels counts.
x = ["apple", "banana", "kiwi", "pineapple"]
y = sorted(x, key = lambda  s: len(set(c for c in s if c in "aeiou")))
print(y)



