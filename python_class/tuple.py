#Q25. Write a program to create tuple (name,age,address,college) for atleast two members and concatenate the tuples and print the concatenated tuple 

"""a = ("Gulshan", 18, "kishanganj", "Geck")
b = ("mohit", 20, "patana", "BEU")

c = a + b #concatenate of a and b tuple.
print(c, type(c))"""

# Q26. write a program to return the top 'n' most frequently occunig chars and  their resppecitive counts. eg->(aaaabbbbccc, 2should return[(a5)(b4)])

'''from collections import Counter
n = "aaaaabbbbccc"
t = 2
f = Counter(n)
print(f)  # => ({'a':5, 'b': 'c':3})
most_common = f.most_common(t)

c = [(x) for x in most_common]
print(c)
print(tuple(c))'''

# write a program to count the number of vowel  in a String (No control flow allowed) 
'''s = input("Enter a string: ")
count = sum(map(s.lower().count, "aeiou"))
print("Number of vowels:", count)'''

# write a program that dispays which letters are present in both string. 

'''s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = set(s1) & set(s2)
print("Letters present in both strings:", ''.join(sorted(common)))'''

# write a program to sort given list of String in the order of Thair Vowel counts.
'''def vowel_count(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')

words = ["apple", "banana", "grape", "kiwi", "orange"]

sorted_words = sorted(words, key=vowel_count)
print("Sorted by vowel count:", sorted_words)'''

# Write a program to generate a dictionary that contains number(b/w 1 and n) in The From of (x, x*x).
'''n = int(input("Enter a number: "))
d = {x: x*x for x in range(1, n+1)}
print(d)'''

# Write a program to check if a given key exists in a dictonary or not. 
'''d = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter key to check: ")

if key in d:
    print("Key exists in dictionary.")
else:
    print("Key does not exist in dictionary.")'''

# write a program to add a new key-value pair to an exisling dictonary.  
"""d = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", d)

key = input("Enter new key: ")
value = input("Enter value: ")

d[key] = value
print("Updated dictionary:", d)

output hai
Enter new key: d
Enter value: 4
Original dictionary: {'a': 1, 'b': 2, 'c': 3}
Updated dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': '4'}"""

# Write a program to sum all items in a given dicitonary. 
'''d = {'a': 10, 'b': 20, 'c': 30}
total = sum(d.values())
print("Sum of all items:", total)'''

# write a program to sort words in a file and put them in another file. the output  file should have only lower case words so any upper case words from source must be lowerd .
# Read words from source file
"""with open("source.txt", "r") as f:
    words = f.read().split()

# Convert to lowercase and sort
words = [w.lower() for w in words]
words.sort()

# Write to destination file
with open("output.txt", "w") as f:
    f.write(" ".join(words))

print("Words have been sorted and written to output.txt")"""


# Write a program to find the most frequent worrd in text(read from a test file). 
from collections import Counter

# Read the file
with open("text.txt", "r") as f:
    words = f.read().lower().split()  # convert to lowercase and split into words

# Count frequency of each word
word_counts = Counter(words)

# Find the most common word
most_common_word, freq = word_counts.most_common(1)[0]

print(f"The most frequent word is '{most_common_word}' with {freq} occurrences.")
