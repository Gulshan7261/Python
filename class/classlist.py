# Wap to perform the given poeration an list 
# a = [2,5,6,7,8]
'''a.append(9)
print(a)

a = a + [9]
print(a)'''

'''a.insert(1, 3333)
print(a)''' 

'''a.extend(a)
print(a)'''

'''b = a[1:3:1]  #slicing
print(b)'''

'''print(a[2:4:1])
print(a[::-1]) 
print(a[::1])'''

"""a = ["Hello", "hi", "world"]
print(a[2][-1])"""

# WAP to perform any 5 bulit in function by taking any list[max,min,sorted,sum,len()].
'''a = [2, 1, 7, 3, 5]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))
print(type(a))'''

# WAP to get a list of the even number from a given list of number,
a = [1,2,3,4,5,6,7,8,9,10]
p = []
for i in a:
    if i%2==0:
        p.append(i)
        i+=1
print(p)

# WAP to get a list of the even number from a given list of number (using only comprehension)
a = [1,2,3,4,5,6,7,8,9,10]

b = [num for num in a if num%2==0]
print(b)


